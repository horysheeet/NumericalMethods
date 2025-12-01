package com.numerical.calculator.controller;

import com.numerical.calculator.model.JacobiRequest;
import com.numerical.calculator.model.NumericalResponse;
import com.numerical.calculator.service.JacobiService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/jacobi")
@CrossOrigin(origins = "*")
public class JacobiController {

    @Autowired
    private JacobiService jacobiService;

    @PostMapping
    public ResponseEntity<NumericalResponse> solveJacobi(@Valid @RequestBody JacobiRequest request) {
        try {
            NumericalResponse response = jacobiService.solve(request);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.badRequest()
                .body(NumericalResponse.error("Error processing Jacobi request: " + e.getMessage()));
        }
    }

    @GetMapping("/health")
    public ResponseEntity<String> healthCheck() {
        return ResponseEntity.ok("Jacobi service is running");
    }
}
