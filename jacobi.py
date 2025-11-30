"""Jacobi iterative method for solving systems of linear equations."""
import numpy as np
from typing import List, Dict, Tuple, Optional
from config_loader import config


def jacobi_method(
    A: List[List[float]], 
    b: List[float], 
    x0: Optional[List[float]] = None,
    max_iterations: Optional[int] = None,
    tolerance: Optional[float] = None
) -> Dict:
    """Solve a system of linear equations using the Jacobi iterative method.
    
    The Jacobi method solves Ax = b by iterating:
    x_i^(k+1) = (b_i - sum(A_ij * x_j^(k) for j != i)) / A_ii
    
    Args:
        A: Coefficient matrix (n x n)
        b: Right-hand side vector (n)
        x0: Initial guess (if None, uses zero vector)
        max_iterations: Maximum number of iterations
        tolerance: Convergence tolerance
        
    Returns:
        Dictionary containing:
            - success: Whether the method converged
            - solution: Final solution vector
            - iterations: Number of iterations performed
            - error: Final error
            - iteration_log: List of iteration details
            - message: Status message
    """
    # Load configuration
    if max_iterations is None:
        max_iterations = config.get('jacobi.max_iterations', 100)
    if tolerance is None:
        tolerance = config.get('jacobi.tolerance', 1e-6)
    
    try:
        # Convert to numpy arrays
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)
        n = len(b)
        
        # Validate input
        if A.shape[0] != A.shape[1]:
            return {
                "success": False,
                "solution": None,
                "iterations": 0,
                "error": None,
                "iteration_log": [],
                "message": "Matrix A must be square"
            }
        
        if A.shape[0] != n:
            return {
                "success": False,
                "solution": None,
                "iterations": 0,
                "error": None,
                "iteration_log": [],
                "message": "Dimensions of A and b don't match"
            }
        
        # Check for zero diagonal elements
        if np.any(np.diag(A) == 0):
            return {
                "success": False,
                "solution": None,
                "iterations": 0,
                "error": None,
                "iteration_log": [],
                "message": "Matrix has zero diagonal elements"
            }
        
        # Initialize solution vector
        if x0 is None:
            x = np.zeros(n)
        else:
            x = np.array(x0, dtype=float)
        
        iteration_log = []
        
        for iteration in range(max_iterations):
            x_new = np.zeros(n)
            
            # Jacobi iteration
            for i in range(n):
                sum_val = 0.0
                for j in range(n):
                    if i != j:
                        sum_val += A[i, j] * x[j]
                x_new[i] = (b[i] - sum_val) / A[i, i]
            
            # Calculate error
            error = np.linalg.norm(x_new - x, ord=np.inf)
            
            # Log iteration
            iteration_log.append({
                "iteration": iteration + 1,
                "solution": x_new.tolist(),
                "error": float(error)
            })
            
            # Check convergence
            if error < tolerance:
                return {
                    "success": True,
                    "solution": x_new.tolist(),
                    "iterations": iteration + 1,
                    "error": float(error),
                    "iteration_log": iteration_log,
                    "message": f"Converged after {iteration + 1} iterations"
                }
            
            x = x_new
        
        # Did not converge
        return {
            "success": False,
            "solution": x.tolist(),
            "iterations": max_iterations,
            "error": float(error),
            "iteration_log": iteration_log,
            "message": f"Did not converge after {max_iterations} iterations"
        }
    
    except Exception as e:
        return {
            "success": False,
            "solution": None,
            "iterations": 0,
            "error": None,
            "iteration_log": [],
            "message": f"Error: {str(e)}"
        }


def check_diagonal_dominance(A: List[List[float]]) -> Tuple[bool, str]:
    """Check if matrix is diagonally dominant.
    
    A matrix is strictly diagonally dominant if:
    |A_ii| > sum(|A_ij| for j != i) for all i
    
    Args:
        A: Coefficient matrix
        
    Returns:
        Tuple of (is_dominant, message)
    """
    try:
        A = np.array(A, dtype=float)
        n = A.shape[0]
        
        for i in range(n):
            diagonal = abs(A[i, i])
            row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
            
            if diagonal <= row_sum:
                return False, f"Row {i+1} fails diagonal dominance: |{A[i,i]}| <= {row_sum}"
        
        return True, "Matrix is strictly diagonally dominant"
    
    except Exception as e:
        return False, f"Error checking diagonal dominance: {str(e)}"
