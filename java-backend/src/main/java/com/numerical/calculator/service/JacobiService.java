package com.numerical.calculator.service;

import com.numerical.calculator.model.JacobiRequest;
import com.numerical.calculator.model.NumericalResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class JacobiService {
    
    @Value("${numerical.jacobi.max-iterations:100}")
    private int defaultMaxIterations;
    
    @Value("${numerical.jacobi.tolerance:0.000001}")
    private double defaultTolerance;

    public NumericalResponse solve(JacobiRequest request) {
        try {
            List<List<Double>> A = request.getMatrixA();
            List<Double> b = request.getVectorB();
            int maxIter = request.getMaxIterations() != null ? request.getMaxIterations() : defaultMaxIterations;
            double tol = request.getTolerance() != null ? request.getTolerance() : defaultTolerance;

            // Validate input
            int n = b.size();
            if (A.size() != n) {
                return NumericalResponse.error("Matrix A must be square");
            }
            
            for (List<Double> row : A) {
                if (row.size() != n) {
                    return NumericalResponse.error("Matrix A must be square");
                }
            }

            // Check for zero diagonal elements
            for (int i = 0; i < n; i++) {
                if (Math.abs(A.get(i).get(i)) < 1e-10) {
                    return NumericalResponse.error("Matrix has zero diagonal elements");
                }
            }

            // Initialize solution vector
            double[] x = new double[n];
            if (request.getInitialGuess() != null && request.getInitialGuess().size() == n) {
                for (int i = 0; i < n; i++) {
                    x[i] = request.getInitialGuess().get(i);
                }
            }

            List<Map<String, Object>> iterationLog = new ArrayList<>();
            double error = 0.0;
            int iteration;

            // Jacobi iteration
            for (iteration = 0; iteration < maxIter; iteration++) {
                double[] xNew = new double[n];

                // Compute new values
                for (int i = 0; i < n; i++) {
                    double sum = 0.0;
                    for (int j = 0; j < n; j++) {
                        if (i != j) {
                            sum += A.get(i).get(j) * x[j];
                        }
                    }
                    xNew[i] = (b.get(i) - sum) / A.get(i).get(i);
                }

                // Calculate error (infinity norm)
                error = 0.0;
                for (int i = 0; i < n; i++) {
                    error = Math.max(error, Math.abs(xNew[i] - x[i]));
                }

                // Log iteration
                Map<String, Object> log = new HashMap<>();
                log.put("iteration", iteration + 1);
                log.put("solution", Arrays.stream(xNew).boxed().toList());
                log.put("error", error);
                iterationLog.add(log);

                // Update x
                System.arraycopy(xNew, 0, x, 0, n);

                // Check convergence
                if (error < tol) {
                    NumericalResponse response = NumericalResponse.success(
                        Arrays.stream(x).boxed().toList(),
                        "Converged after " + (iteration + 1) + " iterations"
                    );
                    response.setIterations(iteration + 1);
                    response.setError(error);
                    response.setIterationLog(iterationLog);
                    return response;
                }
            }

            // Did not converge
            NumericalResponse response = NumericalResponse.success(
                Arrays.stream(x).boxed().toList(),
                "Maximum iterations reached without convergence"
            );
            response.setIterations(maxIter);
            response.setError(error);
            response.setIterationLog(iterationLog);
            return response;

        } catch (Exception e) {
            return NumericalResponse.error("Error in Jacobi method: " + e.getMessage());
        }
    }
}
