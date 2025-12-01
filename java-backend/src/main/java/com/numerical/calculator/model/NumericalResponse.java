package com.numerical.calculator.model;

import java.util.List;
import java.util.Map;

public class NumericalResponse {
    
    private boolean success;
    private Object result;
    private String message;
    private Integer iterations;
    private Double error;
    private List<Map<String, Object>> iterationLog;

    // Constructors
    public NumericalResponse() {}

    public NumericalResponse(boolean success, Object result, String message) {
        this.success = success;
        this.result = result;
        this.message = message;
    }

    // Static factory methods
    public static NumericalResponse success(Object result, String message) {
        return new NumericalResponse(true, result, message);
    }

    public static NumericalResponse error(String message) {
        return new NumericalResponse(false, null, message);
    }

    // Getters and Setters
    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public Object getResult() {
        return result;
    }

    public void setResult(Object result) {
        this.result = result;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public Integer getIterations() {
        return iterations;
    }

    public void setIterations(Integer iterations) {
        this.iterations = iterations;
    }

    public Double getError() {
        return error;
    }

    public void setError(Double error) {
        this.error = error;
    }

    public List<Map<String, Object>> getIterationLog() {
        return iterationLog;
    }

    public void setIterationLog(List<Map<String, Object>> iterationLog) {
        this.iterationLog = iterationLog;
    }
}
