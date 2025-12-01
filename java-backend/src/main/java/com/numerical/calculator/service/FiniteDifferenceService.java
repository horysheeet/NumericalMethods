package com.numerical.calculator.service;

import com.numerical.calculator.model.FiniteDifferenceRequest;
import com.numerical.calculator.model.NumericalResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import java.util.*;

@Service
public class FiniteDifferenceService {
    
    @Value("${numerical.finite-difference.default-step:0.01}")
    private double defaultStepSize;
    
    private final ScriptEngine engine;
    
    public FiniteDifferenceService() {
        ScriptEngineManager manager = new ScriptEngineManager();
        this.engine = manager.getEngineByName("JavaScript");
    }

    public NumericalResponse forwardDifference(FiniteDifferenceRequest request) {
        try {
            String funcStr = request.getFunction();
            List<Double> xValues = request.getXValues();
            int order = request.getOrder() != null ? request.getOrder() : 1;
            double h = request.getStepSize() != null ? request.getStepSize() : defaultStepSize;

            if (order != 1 && order != 2) {
                return NumericalResponse.error("Order must be 1 or 2");
            }

            List<Map<String, Object>> results = new ArrayList<>();

            for (double x : xValues) {
                double derivative;
                
                if (order == 1) {
                    // First order: f'(x) ≈ (f(x+h) - f(x)) / h
                    double fx = evaluateFunction(funcStr, x);
                    double fxh = evaluateFunction(funcStr, x + h);
                    derivative = (fxh - fx) / h;
                } else {
                    // Second order: f''(x) ≈ (f(x+2h) - 2f(x+h) + f(x)) / h²
                    double fx = evaluateFunction(funcStr, x);
                    double fxh = evaluateFunction(funcStr, x + h);
                    double fx2h = evaluateFunction(funcStr, x + 2 * h);
                    derivative = (fx2h - 2 * fxh + fx) / (h * h);
                }

                Map<String, Object> result = new HashMap<>();
                result.put("x", x);
                result.put("derivative", derivative);
                result.put("order", order);
                results.add(result);
            }

            return NumericalResponse.success(
                results,
                "Forward difference computed for " + xValues.size() + " point(s)"
            );

        } catch (Exception e) {
            return NumericalResponse.error("Error in forward difference: " + e.getMessage());
        }
    }

    public NumericalResponse backwardDifference(FiniteDifferenceRequest request) {
        try {
            String funcStr = request.getFunction();
            List<Double> xValues = request.getXValues();
            int order = request.getOrder() != null ? request.getOrder() : 1;
            double h = request.getStepSize() != null ? request.getStepSize() : defaultStepSize;

            if (order != 1 && order != 2) {
                return NumericalResponse.error("Order must be 1 or 2");
            }

            List<Map<String, Object>> results = new ArrayList<>();

            for (double x : xValues) {
                double derivative;
                
                if (order == 1) {
                    // First order: f'(x) ≈ (f(x) - f(x-h)) / h
                    double fx = evaluateFunction(funcStr, x);
                    double fxh = evaluateFunction(funcStr, x - h);
                    derivative = (fx - fxh) / h;
                } else {
                    // Second order: f''(x) ≈ (f(x) - 2f(x-h) + f(x-2h)) / h²
                    double fx = evaluateFunction(funcStr, x);
                    double fxh = evaluateFunction(funcStr, x - h);
                    double fx2h = evaluateFunction(funcStr, x - 2 * h);
                    derivative = (fx - 2 * fxh + fx2h) / (h * h);
                }

                Map<String, Object> result = new HashMap<>();
                result.put("x", x);
                result.put("derivative", derivative);
                result.put("order", order);
                results.add(result);
            }

            return NumericalResponse.success(
                results,
                "Backward difference computed for " + xValues.size() + " point(s)"
            );

        } catch (Exception e) {
            return NumericalResponse.error("Error in backward difference: " + e.getMessage());
        }
    }

    public NumericalResponse centralDifference(FiniteDifferenceRequest request) {
        try {
            String funcStr = request.getFunction();
            List<Double> xValues = request.getXValues();
            int order = request.getOrder() != null ? request.getOrder() : 1;
            double h = request.getStepSize() != null ? request.getStepSize() : defaultStepSize;

            if (order != 1 && order != 2) {
                return NumericalResponse.error("Order must be 1 or 2");
            }

            List<Map<String, Object>> results = new ArrayList<>();

            for (double x : xValues) {
                double derivative;
                
                if (order == 1) {
                    // First order: f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
                    double fxh_plus = evaluateFunction(funcStr, x + h);
                    double fxh_minus = evaluateFunction(funcStr, x - h);
                    derivative = (fxh_plus - fxh_minus) / (2 * h);
                } else {
                    // Second order: f''(x) ≈ (f(x+h) - 2f(x) + f(x-h)) / h²
                    double fx = evaluateFunction(funcStr, x);
                    double fxh_plus = evaluateFunction(funcStr, x + h);
                    double fxh_minus = evaluateFunction(funcStr, x - h);
                    derivative = (fxh_plus - 2 * fx + fxh_minus) / (h * h);
                }

                Map<String, Object> result = new HashMap<>();
                result.put("x", x);
                result.put("derivative", derivative);
                result.put("order", order);
                results.add(result);
            }

            return NumericalResponse.success(
                results,
                "Central difference computed for " + xValues.size() + " point(s)"
            );

        } catch (Exception e) {
            return NumericalResponse.error("Error in central difference: " + e.getMessage());
        }
    }

    private double evaluateFunction(String funcStr, double x) throws ScriptException {
        // Replace x with actual value and handle common math functions
        String expression = funcStr
            .replace("x", String.valueOf(x))
            .replace("^", "**")
            .replace("Math.sqrt", "sqrt")
            .replace("Math.sin", "sin")
            .replace("Math.cos", "cos")
            .replace("Math.tan", "tan")
            .replace("Math.exp", "exp")
            .replace("Math.log", "log");
        
        // Add Math methods back for JavaScript engine
        expression = expression
            .replace("sqrt", "Math.sqrt")
            .replace("sin", "Math.sin")
            .replace("cos", "Math.cos")
            .replace("tan", "Math.tan")
            .replace("exp", "Math.exp")
            .replace("log", "Math.log");
        
        Object result = engine.eval(expression);
        return ((Number) result).doubleValue();
    }
}
