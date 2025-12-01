package com.numerical.calculator.model;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public class RegulaFalsiRequest {
    
    @NotBlank(message = "Function is required")
    private String function;
    
    @NotNull(message = "Left endpoint 'a' is required")
    private Double a;
    
    @NotNull(message = "Right endpoint 'b' is required")
    private Double b;
    
    private Integer maxIterations;
    
    private Double tolerance;

    // Constructors
    public RegulaFalsiRequest() {}

    public RegulaFalsiRequest(String function, Double a, Double b) {
        this.function = function;
        this.a = a;
        this.b = b;
    }

    // Getters and Setters
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public Double getA() {
        return a;
    }

    public void setA(Double a) {
        this.a = a;
    }

    public Double getB() {
        return b;
    }

    public void setB(Double b) {
        this.b = b;
    }

    public Integer getMaxIterations() {
        return maxIterations;
    }

    public void setMaxIterations(Integer maxIterations) {
        this.maxIterations = maxIterations;
    }

    public Double getTolerance() {
        return tolerance;
    }

    public void setTolerance(Double tolerance) {
        this.tolerance = tolerance;
    }
}
