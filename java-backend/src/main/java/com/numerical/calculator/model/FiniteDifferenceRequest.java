package com.numerical.calculator.model;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.util.List;

public class FiniteDifferenceRequest {
    
    @NotBlank(message = "Function is required")
    private String function;
    
    @NotNull(message = "X values are required")
    private List<Double> xValues;
    
    @NotNull(message = "Order is required (1 or 2)")
    private Integer order;
    
    private Double stepSize;

    // Constructors
    public FiniteDifferenceRequest() {}

    public FiniteDifferenceRequest(String function, List<Double> xValues, Integer order) {
        this.function = function;
        this.xValues = xValues;
        this.order = order;
    }

    // Getters and Setters
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public List<Double> getXValues() {
        return xValues;
    }

    public void setXValues(List<Double> xValues) {
        this.xValues = xValues;
    }

    public Integer getOrder() {
        return order;
    }

    public void setOrder(Integer order) {
        this.order = order;
    }

    public Double getStepSize() {
        return stepSize;
    }

    public void setStepSize(Double stepSize) {
        this.stepSize = stepSize;
    }
}
