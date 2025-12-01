package com.numerical.calculator.controller;

import com.numerical.calculator.model.RegulaFalsiRequest;
import com.numerical.calculator.model.NumericalResponse;
import com.numerical.calculator.service.RegulaFalsiService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/regula-falsi")
@CrossOrigin(origins = "*")
public class RegulaFalsiController {

    @Autowired
    private RegulaFalsiService regulaFalsiService;

    @PostMapping
    public ResponseEntity<NumericalResponse> findRoot(@Valid @RequestBody RegulaFalsiRequest request) {
        try {
            NumericalResponse response = regulaFalsiService.findRoot(request);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.badRequest()
                .body(NumericalResponse.error("Error processing Regula-Falsi request: " + e.getMessage()));
        }
    }

    @GetMapping("/health")
    public ResponseEntity<String> healthCheck() {
        return ResponseEntity.ok("Regula-Falsi service is running");
    }
}
