package com.numerical.calculator.model;

import jakarta.validation.constraints.NotNull;
import java.util.List;

public class JacobiRequest {
    
    @NotNull(message = "Matrix A is required")
    private List<List<Double>> matrixA;
    
    @NotNull(message = "Vector b is required")
    private List<Double> vectorB;
    
    private List<Double> initialGuess;
    
    private Integer maxIterations;
    
    private Double tolerance;

    // Constructors
    public JacobiRequest() {}

    public JacobiRequest(List<List<Double>> matrixA, List<Double> vectorB) {
        this.matrixA = matrixA;
        this.vectorB = vectorB;
    }

    // Getters and Setters
    public List<List<Double>> getMatrixA() {
        return matrixA;
    }

    public void setMatrixA(List<List<Double>> matrixA) {
        this.matrixA = matrixA;
    }

    public List<Double> getVectorB() {
        return vectorB;
    }

    public void setVectorB(List<Double> vectorB) {
        this.vectorB = vectorB;
    }

    public List<Double> getInitialGuess() {
        return initialGuess;
    }

    public void setInitialGuess(List<Double> initialGuess) {
        this.initialGuess = initialGuess;
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
