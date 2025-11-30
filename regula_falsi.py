"""Regula-Falsi (False Position) method for finding roots of equations."""
import numpy as np
from typing import Callable, Dict, Optional
from config_loader import config


def regula_falsi_method(
    func_str: str,
    a: float,
    b: float,
    max_iterations: Optional[int] = None,
    tolerance: Optional[float] = None
) -> Dict:
    """Find root of equation using Regula-Falsi (False Position) method.
    
    The method finds the root by:
    1. Check that f(a) and f(b) have opposite signs
    2. Find intersection point: c = (a*f(b) - b*f(a)) / (f(b) - f(a))
    3. Replace a or b with c based on sign of f(c)
    4. Repeat until convergence
    
    Args:
        func_str: Function as string (e.g., "x**2 - 4")
        a: Left endpoint
        b: Right endpoint
        max_iterations: Maximum number of iterations
        tolerance: Convergence tolerance
        
    Returns:
        Dictionary containing:
            - success: Whether the method converged
            - root: Approximate root
            - iterations: Number of iterations performed
            - error: Final error estimate
            - iteration_log: List of iteration details
            - message: Status message
    """
    # Load configuration
    if max_iterations is None:
        max_iterations = config.get('regula_falsi.max_iterations', 100)
    if tolerance is None:
        tolerance = config.get('regula_falsi.tolerance', 1e-6)
    
    try:
        # Create function from string
        def f(x):
            # Safe evaluation with numpy functions available
            allowed_names = {
                'x': x,
                'np': np,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'exp': np.exp,
                'log': np.log,
                'sqrt': np.sqrt,
                'abs': np.abs,
                'pi': np.pi,
                'e': np.e
            }
            return eval(func_str, {"__builtins__": {}}, allowed_names)
        
        # Evaluate function at endpoints
        fa = f(a)
        fb = f(b)
        
        # Check if root exists in interval
        if fa * fb > 0:
            return {
                "success": False,
                "root": None,
                "iterations": 0,
                "error": None,
                "iteration_log": [],
                "message": f"Function has same sign at both endpoints: f({a}) = {fa}, f({b}) = {fb}"
            }
        
        # Check if a or b is already a root
        if abs(fa) < tolerance:
            return {
                "success": True,
                "root": a,
                "iterations": 0,
                "error": 0.0,
                "iteration_log": [],
                "message": f"Initial point a = {a} is a root"
            }
        
        if abs(fb) < tolerance:
            return {
                "success": True,
                "root": b,
                "iterations": 0,
                "error": 0.0,
                "iteration_log": [],
                "message": f"Initial point b = {b} is a root"
            }
        
        iteration_log = []
        c_old = a
        
        for iteration in range(max_iterations):
            # Regula-Falsi formula
            c = (a * fb - b * fa) / (fb - fa)
            fc = f(c)
            
            # Calculate error
            error = abs(c - c_old) if iteration > 0 else abs(b - a)
            
            # Log iteration
            iteration_log.append({
                "iteration": iteration + 1,
                "a": float(a),
                "b": float(b),
                "c": float(c),
                "f(c)": float(fc),
                "error": float(error)
            })
            
            # Check convergence
            if abs(fc) < tolerance or error < tolerance:
                return {
                    "success": True,
                    "root": float(c),
                    "iterations": iteration + 1,
                    "error": float(error),
                    "iteration_log": iteration_log,
                    "message": f"Converged after {iteration + 1} iterations"
                }
            
            # Update interval
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
            
            c_old = c
        
        # Did not converge
        return {
            "success": False,
            "root": float(c),
            "iterations": max_iterations,
            "error": float(error),
            "iteration_log": iteration_log,
            "message": f"Did not converge after {max_iterations} iterations"
        }
    
    except ZeroDivisionError:
        return {
            "success": False,
            "root": None,
            "iterations": 0,
            "error": None,
            "iteration_log": [],
            "message": "Division by zero - function may be constant"
        }
    
    except Exception as e:
        return {
            "success": False,
            "root": None,
            "iterations": 0,
            "error": None,
            "iteration_log": [],
            "message": f"Error: {str(e)}"
        }
