package com.numerical.calculator.controller;

import com.numerical.calculator.model.FiniteDifferenceRequest;
import com.numerical.calculator.model.NumericalResponse;
import com.numerical.calculator.service.FiniteDifferenceService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/finite-difference")
@CrossOrigin(origins = "*")
public class FiniteDifferenceController {

    @Autowired
    private FiniteDifferenceService finiteDifferenceService;

    @PostMapping("/forward")
    public ResponseEntity<NumericalResponse> forwardDifference(@Valid @RequestBody FiniteDifferenceRequest request) {
        try {
            NumericalResponse response = finiteDifferenceService.forwardDifference(request);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.badRequest()
                .body(NumericalResponse.error("Error processing forward difference: " + e.getMessage()));
        }
    }

    @PostMapping("/backward")
    public ResponseEntity<NumericalResponse> backwardDifference(@Valid @RequestBody FiniteDifferenceRequest request) {
        try {
            NumericalResponse response = finiteDifferenceService.backwardDifference(request);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.badRequest()
                .body(NumericalResponse.error("Error processing backward difference: " + e.getMessage()));
        }
    }

    @PostMapping("/central")
    public ResponseEntity<NumericalResponse> centralDifference(@Valid @RequestBody FiniteDifferenceRequest request) {
        try {
            NumericalResponse response = finiteDifferenceService.centralDifference(request);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.badRequest()
                .body(NumericalResponse.error("Error processing central difference: " + e.getMessage()));
        }
    }

    @GetMapping("/health")
    public ResponseEntity<String> healthCheck() {
        return ResponseEntity.ok("Finite Difference service is running");
    }
}
