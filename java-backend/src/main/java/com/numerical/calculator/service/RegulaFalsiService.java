package com.numerical.calculator.service;

import com.numerical.calculator.model.RegulaFalsiRequest;
import com.numerical.calculator.model.NumericalResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import java.util.*;

@Service
public class RegulaFalsiService {
    
    @Value("${numerical.regula-falsi.max-iterations:100}")
    private int defaultMaxIterations;
    
    @Value("${numerical.regula-falsi.tolerance:0.000001}")
    private double defaultTolerance;
    
    private final ScriptEngine engine;
    
    public RegulaFalsiService() {
        ScriptEngineManager manager = new ScriptEngineManager();
        this.engine = manager.getEngineByName("JavaScript");
    }

    public NumericalResponse findRoot(RegulaFalsiRequest request) {
        try {
            String funcStr = request.getFunction();
            double a = request.getA();
            double b = request.getB();
            int maxIter = request.getMaxIterations() != null ? request.getMaxIterations() : defaultMaxIterations;
            double tol = request.getTolerance() != null ? request.getTolerance() : defaultTolerance;

            // Evaluate function at endpoints
            double fa = evaluateFunction(funcStr, a);
            double fb = evaluateFunction(funcStr, b);

            // Check if root exists in interval
            if (fa * fb > 0) {
                return NumericalResponse.error(
                    String.format("Function has same sign at both endpoints: f(%.6f) = %.6f, f(%.6f) = %.6f", 
                    a, fa, b, fb)
                );
            }

            // Check if endpoints are roots
            if (Math.abs(fa) < tol) {
                return NumericalResponse.success(a, "Initial point a = " + a + " is a root");
            }
            if (Math.abs(fb) < tol) {
                return NumericalResponse.success(b, "Initial point b = " + b + " is a root");
            }

            List<Map<String, Object>> iterationLog = new ArrayList<>();
            double c = a;
            double fc = fa;
            int iteration;

            // Regula-Falsi iteration
            for (iteration = 0; iteration < maxIter; iteration++) {
                // Calculate new point using linear interpolation
                c = (a * fb - b * fa) / (fb - fa);
                fc = evaluateFunction(funcStr, c);

                // Log iteration
                Map<String, Object> log = new HashMap<>();
                log.put("iteration", iteration + 1);
                log.put("a", a);
                log.put("b", b);
                log.put("c", c);
                log.put("f_c", fc);
                iterationLog.add(log);

                // Check convergence
                if (Math.abs(fc) < tol) {
                    NumericalResponse response = NumericalResponse.success(
                        c,
                        "Converged after " + (iteration + 1) + " iterations"
                    );
                    response.setIterations(iteration + 1);
                    response.setError(Math.abs(fc));
                    response.setIterationLog(iterationLog);
                    return response;
                }

                // Update interval
                if (fa * fc < 0) {
                    b = c;
                    fb = fc;
                } else {
                    a = c;
                    fa = fc;
                }
            }

            // Maximum iterations reached
            NumericalResponse response = NumericalResponse.success(
                c,
                "Maximum iterations reached. Root approximation: " + c
            );
            response.setIterations(maxIter);
            response.setError(Math.abs(fc));
            response.setIterationLog(iterationLog);
            return response;

        } catch (Exception e) {
            return NumericalResponse.error("Error in Regula-Falsi method: " + e.getMessage());
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
