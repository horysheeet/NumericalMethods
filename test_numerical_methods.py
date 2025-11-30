"""Comprehensive test suite for all numerical methods."""
import pytest
import numpy as np
from jacobi import jacobi_method, check_diagonal_dominance
from regula_falsi import regula_falsi_method
from forward_fd import forward_finite_difference
from backward_fd import backward_finite_difference
from center_fd import center_finite_difference


# ============================================================================
# JACOBI METHOD TESTS
# ============================================================================

class TestJacobiMethod:
    """Tests for Jacobi iterative method."""
    
    def test_jacobi_simple_system(self):
        """Test Jacobi method with a simple 3x3 system."""
        A = [[4, -1, 0], [-1, 4, -1], [0, -1, 4]]
        b = [5, 0, 6]
        
        result = jacobi_method(A, b, max_iterations=100, tolerance=1e-6)
        
        assert result["success"] == True
        assert result["solution"] is not None
        assert len(result["solution"]) == 3
        assert result["iterations"] > 0
        
        # Verify solution
        x = np.array(result["solution"])
        A_np = np.array(A)
        b_np = np.array(b)
        residual = np.linalg.norm(A_np @ x - b_np)
        assert residual < 1e-4
    
    def test_jacobi_diagonal_dominant(self):
        """Test Jacobi with diagonally dominant matrix."""
        A = [[10, 1, 1], [1, 10, 1], [1, 1, 10]]
        b = [12, 12, 12]
        
        result = jacobi_method(A, b, max_iterations=50, tolerance=1e-6)
        
        assert result["success"] == True
        assert result["iterations"] < 50
    
    def test_jacobi_with_initial_guess(self):
        """Test Jacobi with custom initial guess."""
        A = [[4, -1, 0], [-1, 4, -1], [0, -1, 4]]
        b = [5, 0, 6]
        x0 = [1, 1, 1]
        
        result = jacobi_method(A, b, x0=x0, max_iterations=100, tolerance=1e-6)
        
        assert result["success"] == True
        assert result["solution"] is not None
    
    def test_jacobi_invalid_dimensions(self):
        """Test Jacobi with mismatched dimensions."""
        A = [[4, -1], [-1, 4]]
        b = [5, 0, 6]
        
        result = jacobi_method(A, b)
        
        assert result["success"] == False
        assert "Dimensions" in result["message"]
    
    def test_jacobi_non_square_matrix(self):
        """Test Jacobi with non-square matrix."""
        A = [[4, -1, 0], [-1, 4, -1]]
        b = [5, 0]
        
        result = jacobi_method(A, b)
        
        assert result["success"] == False
        assert "square" in result["message"]
    
    def test_jacobi_zero_diagonal(self):
        """Test Jacobi with zero diagonal element."""
        A = [[0, -1, 0], [-1, 4, -1], [0, -1, 4]]
        b = [5, 0, 6]
        
        result = jacobi_method(A, b)
        
        assert result["success"] == False
        assert "diagonal" in result["message"]
    
    def test_check_diagonal_dominance(self):
        """Test diagonal dominance checker."""
        A_dominant = [[10, 1, 1], [1, 10, 1], [1, 1, 10]]
        A_not_dominant = [[1, 10, 1], [1, 1, 10], [10, 1, 1]]
        
        is_dominant, msg = check_diagonal_dominance(A_dominant)
        assert is_dominant == True
        
        is_dominant, msg = check_diagonal_dominance(A_not_dominant)
        assert is_dominant == False


# ============================================================================
# REGULA-FALSI METHOD TESTS
# ============================================================================

class TestRegulaFalsiMethod:
    """Tests for Regula-Falsi method."""
    
    def test_regula_falsi_quadratic(self):
        """Test Regula-Falsi with quadratic function."""
        func = "x**2 - 4"
        a = 0
        b = 3
        
        result = regula_falsi_method(func, a, b, max_iterations=100, tolerance=1e-6)
        
        assert result["success"] == True
        assert abs(result["root"] - 2.0) < 1e-4
    
    def test_regula_falsi_transcendental(self):
        """Test Regula-Falsi with transcendental function."""
        func = "x - cos(x)"
        a = 0
        b = 1
        
        result = regula_falsi_method(func, a, b, max_iterations=100, tolerance=1e-6)
        
        assert result["success"] == True
        assert abs(result["root"] - 0.739085) < 1e-4
    
    def test_regula_falsi_exponential(self):
        """Test Regula-Falsi with exponential function."""
        func = "exp(x) - 2"
        a = 0
        b = 1
        
        result = regula_falsi_method(func, a, b, max_iterations=100, tolerance=1e-6)
        
        assert result["success"] == True
        assert abs(result["root"] - np.log(2)) < 1e-4
    
    def test_regula_falsi_same_sign(self):
        """Test Regula-Falsi with same sign at endpoints."""
        func = "x**2 + 1"
        a = 0
        b = 3
        
        result = regula_falsi_method(func, a, b)
        
        assert result["success"] == False
        assert "same sign" in result["message"]
    
    def test_regula_falsi_exact_root_at_a(self):
        """Test Regula-Falsi when a is exact root."""
        func = "x**2 - 4"
        a = 2.0
        b = 3.0
        
        result = regula_falsi_method(func, a, b, tolerance=1e-6)
        
        assert result["success"] == True
        assert abs(result["root"] - 2.0) < 1e-5
    
    def test_regula_falsi_exact_root_at_b(self):
        """Test Regula-Falsi when b is exact root."""
        func = "x**2 - 9"
        a = 2.0
        b = 3.0
        
        result = regula_falsi_method(func, a, b, tolerance=1e-6)
        
        assert result["success"] == True
        assert abs(result["root"] - 3.0) < 1e-5


# ============================================================================
# FORWARD FINITE DIFFERENCE TESTS
# ============================================================================

class TestForwardFiniteDifference:
    """Tests for forward finite difference."""
    
    def test_forward_fd_first_order_quadratic(self):
        """Test first order forward difference with x^2."""
        func = "x**2"
        x_vals = [2.0]
        h = 0.01
        
        result = forward_finite_difference(func, x_vals, order=1, h=h)
        
        assert result["success"] == True
        # Derivative of x^2 at x=2 is 4
        assert abs(result["points"][0]["derivative"] - 4.0) < 0.1
    
    def test_forward_fd_second_order_quadratic(self):
        """Test second order forward difference with x^2."""
        func = "x**2"
        x_vals = [2.0]
        h = 0.01
        
        result = forward_finite_difference(func, x_vals, order=2, h=h)
        
        assert result["success"] == True
        # Second derivative of x^2 is 2
        assert abs(result["points"][0]["derivative"] - 2.0) < 0.1
    
    def test_forward_fd_with_y_values(self):
        """Test forward difference with provided y values."""
        x_vals = [0, 1, 2, 3]
        y_vals = [0, 1, 4, 9]  # x^2 values
        h = 1.0
        
        result = forward_finite_difference("", x_vals, y_vals, order=1, h=h)
        
        assert result["success"] == True
        assert len(result["points"]) == 4
    
    def test_forward_fd_sine_function(self):
        """Test forward difference with sine function."""
        func = "sin(x)"
        x_vals = [0.0]
        h = 0.01
        
        result = forward_finite_difference(func, x_vals, order=1, h=h)
        
        assert result["success"] == True
        # Derivative of sin(x) at x=0 is cos(0) = 1
        assert abs(result["points"][0]["derivative"] - 1.0) < 0.01
    
    def test_forward_fd_invalid_order(self):
        """Test forward difference with invalid order."""
        func = "x**2"
        x_vals = [2.0]
        
        result = forward_finite_difference(func, x_vals, order=3, h=0.01)
        
        assert result["success"] == False
        assert "Order must be 1 or 2" in result["message"]


# ============================================================================
# BACKWARD FINITE DIFFERENCE TESTS
# ============================================================================

class TestBackwardFiniteDifference:
    """Tests for backward finite difference."""
    
    def test_backward_fd_first_order_quadratic(self):
        """Test first order backward difference with x^2."""
        func = "x**2"
        x_vals = [2.0]
        h = 0.01
        
        result = backward_finite_difference(func, x_vals, order=1, h=h)
        
        assert result["success"] == True
        # Derivative of x^2 at x=2 is 4
        assert abs(result["points"][0]["derivative"] - 4.0) < 0.1
    
    def test_backward_fd_second_order_quadratic(self):
        """Test second order backward difference with x^2."""
        func = "x**2"
        x_vals = [2.0]
        h = 0.01
        
        result = backward_finite_difference(func, x_vals, order=2, h=h)
        
        assert result["success"] == True
        # Second derivative of x^2 is 2
        assert abs(result["points"][0]["derivative"] - 2.0) < 0.1
    
    def test_backward_fd_with_y_values(self):
        """Test backward difference with provided y values."""
        x_vals = [0, 1, 2, 3]
        y_vals = [0, 1, 4, 9]  # x^2 values
        h = 1.0
        
        result = backward_finite_difference("", x_vals, y_vals, order=1, h=h)
        
        assert result["success"] == True
        assert len(result["points"]) == 4
    
    def test_backward_fd_exponential(self):
        """Test backward difference with exponential function."""
        func = "exp(x)"
        x_vals = [1.0]
        h = 0.01
        
        result = backward_finite_difference(func, x_vals, order=1, h=h)
        
        assert result["success"] == True
        # Derivative of exp(x) at x=1 is exp(1)
        assert abs(result["points"][0]["derivative"] - np.exp(1)) < 0.01


# ============================================================================
# CENTER FINITE DIFFERENCE TESTS
# ============================================================================

class TestCenterFiniteDifference:
    """Tests for center finite difference."""
    
    def test_center_fd_first_order_quadratic(self):
        """Test first order center difference with x^2."""
        func = "x**2"
        x_vals = [2.0]
        h = 0.01
        
        result = center_finite_difference(func, x_vals, order=1, h=h)
        
        assert result["success"] == True
        # Derivative of x^2 at x=2 is 4
        assert abs(result["points"][0]["derivative"] - 4.0) < 0.001
    
    def test_center_fd_second_order_quadratic(self):
        """Test second order center difference with x^2."""
        func = "x**2"
        x_vals = [2.0]
        h = 0.01
        
        result = center_finite_difference(func, x_vals, order=2, h=h)
        
        assert result["success"] == True
        # Second derivative of x^2 is 2
        assert abs(result["points"][0]["derivative"] - 2.0) < 0.001
    
    def test_center_fd_cubic(self):
        """Test center difference with cubic function."""
        func = "x**3"
        x_vals = [1.0]
        h = 0.01
        
        result = center_finite_difference(func, x_vals, order=1, h=h)
        
        assert result["success"] == True
        # Derivative of x^3 at x=1 is 3
        assert abs(result["points"][0]["derivative"] - 3.0) < 0.01
    
    def test_center_fd_with_y_values(self):
        """Test center difference with provided y values."""
        x_vals = [0, 1, 2, 3, 4]
        y_vals = [0, 1, 4, 9, 16]  # x^2 values
        h = 1.0
        
        result = center_finite_difference("", x_vals, y_vals, order=1, h=h)
        
        assert result["success"] == True
        assert len(result["points"]) == 5
    
    def test_center_fd_accuracy_comparison(self):
        """Test that center difference is more accurate than forward/backward."""
        func = "sin(x)"
        x_vals = [1.0]
        h = 0.1
        
        # Exact derivative: cos(1) ≈ 0.5403023
        exact = np.cos(1.0)
        
        forward = forward_finite_difference(func, x_vals, order=1, h=h)
        backward = backward_finite_difference(func, x_vals, order=1, h=h)
        center = center_finite_difference(func, x_vals, order=1, h=h)
        
        forward_error = abs(forward["points"][0]["derivative"] - exact)
        backward_error = abs(backward["points"][0]["derivative"] - exact)
        center_error = abs(center["points"][0]["derivative"] - exact)
        
        # Center difference should be more accurate
        assert center_error < forward_error
        assert center_error < backward_error


# ============================================================================
# INTEGRATION TESTS
# ============================================================================

class TestIntegration:
    """Integration tests for the complete system."""
    
    def test_all_methods_available(self):
        """Test that all methods can be imported and called."""
        # Jacobi
        result = jacobi_method([[4, -1], [-1, 4]], [5, 0])
        assert "success" in result
        
        # Regula-Falsi
        result = regula_falsi_method("x**2 - 4", 0, 3)
        assert "success" in result
        
        # Forward FD
        result = forward_finite_difference("x**2", [2.0], order=1)
        assert "success" in result
        
        # Backward FD
        result = backward_finite_difference("x**2", [2.0], order=1)
        assert "success" in result
        
        # Center FD
        result = center_finite_difference("x**2", [2.0], order=1)
        assert "success" in result
    
    def test_config_integration(self):
        """Test that config values are used correctly."""
        from config_loader import config
        
        # Test that config loads
        max_iter = config.get("jacobi.max_iterations", 100)
        assert isinstance(max_iter, int)
        assert max_iter > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
