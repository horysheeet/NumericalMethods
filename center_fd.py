"""Central Finite Divided Difference method for numerical differentiation."""
import numpy as np
from typing import List, Dict, Optional
from config_loader import config


def center_finite_difference(
    func_str: str,
    x_values: List[float],
    y_values: Optional[List[float]] = None,
    order: int = 1,
    h: Optional[float] = None
) -> Dict:
    """Compute central finite divided differences.
    
    Central difference formulas (more accurate than forward/backward):
    First order: f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
    Second order: f''(x) ≈ (f(x+h) - 2f(x) + f(x-h)) / h²
    
    Args:
        func_str: Function as string (e.g., "x**2") or empty if y_values provided
        x_values: List of x values (can be single value or list)
        y_values: List of corresponding y values (optional, computed from func_str if not provided)
        order: Order of derivative (1 or 2)
        h: Step size (optional, uses config default)
        
    Returns:
        Dictionary containing:
            - success: Whether computation succeeded
            - derivative: Computed derivative value(s)
            - order: Order of derivative
            - h: Step size used
            - points: Points used in computation
            - message: Status message
    """
    # Load configuration
    if h is None:
        h = config.get('finite_difference.default_h', 0.01)
    
    try:
        # Validate step size
        min_h = config.get('finite_difference.min_h', 1e-10)
        max_h = config.get('finite_difference.max_h', 1.0)
        
        if h < min_h or h > max_h:
            return {
                "success": False,
                "derivative": None,
                "order": order,
                "h": h,
                "points": [],
                "message": f"Step size h must be between {min_h} and {max_h}"
            }
        
        # Ensure x_values is a list
        if not isinstance(x_values, list):
            x_values = [x_values]
        
        # If y_values not provided, compute from function
        if y_values is None and func_str:
            def f(x):
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
            
            y_values = [f(x) for x in x_values]
        
        if y_values is None:
            return {
                "success": False,
                "derivative": None,
                "order": order,
                "h": h,
                "points": [],
                "message": "Either func_str or y_values must be provided"
            }
        
        results = []
        
        # Compute derivatives for each point
        for i, x in enumerate(x_values):
            if order == 1:
                # First order central difference
                if func_str:
                    def f(x):
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
                    
                    fx_h = f(x + h)
                    fx_neg_h = f(x - h)
                    derivative = (fx_h - fx_neg_h) / (2 * h)
                    
                    results.append({
                        "x": float(x),
                        "derivative": float(derivative),
                        "points_used": [
                            {"x": float(x - h), "f(x)": float(fx_neg_h)},
                            {"x": float(x + h), "f(x)": float(fx_h)}
                        ]
                    })
                else:
                    # Use provided y_values
                    if i > 0 and i + 1 < len(y_values):
                        derivative = (y_values[i + 1] - y_values[i - 1]) / (2 * h)
                        results.append({
                            "x": float(x),
                            "derivative": float(derivative),
                            "points_used": [
                                {"x": float(x - h), "f(x)": float(y_values[i - 1])},
                                {"x": float(x + h), "f(x)": float(y_values[i + 1])}
                            ]
                        })
                    else:
                        results.append({
                            "x": float(x),
                            "derivative": None,
                            "error": "Not enough points for central difference"
                        })
            
            elif order == 2:
                # Second order central difference
                if func_str:
                    def f(x):
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
                    
                    fx = f(x)
                    fx_h = f(x + h)
                    fx_neg_h = f(x - h)
                    derivative = (fx_h - 2*fx + fx_neg_h) / (h**2)
                    
                    results.append({
                        "x": float(x),
                        "derivative": float(derivative),
                        "points_used": [
                            {"x": float(x - h), "f(x)": float(fx_neg_h)},
                            {"x": float(x), "f(x)": float(fx)},
                            {"x": float(x + h), "f(x)": float(fx_h)}
                        ]
                    })
                else:
                    # Use provided y_values
                    if i > 0 and i + 1 < len(y_values):
                        derivative = (y_values[i + 1] - 2*y_values[i] + y_values[i - 1]) / (h**2)
                        results.append({
                            "x": float(x),
                            "derivative": float(derivative),
                            "points_used": [
                                {"x": float(x - h), "f(x)": float(y_values[i - 1])},
                                {"x": float(x), "f(x)": float(y_values[i])},
                                {"x": float(x + h), "f(x)": float(y_values[i + 1])}
                            ]
                        })
                    else:
                        results.append({
                            "x": float(x),
                            "derivative": None,
                            "error": "Not enough points for second order central difference"
                        })
            else:
                return {
                    "success": False,
                    "derivative": None,
                    "order": order,
                    "h": h,
                    "points": [],
                    "message": "Order must be 1 or 2"
                }
        
        return {
            "success": True,
            "derivative": results,
            "order": order,
            "h": float(h),
            "points": results,
            "message": f"Successfully computed {order}-order central finite differences"
        }
    
    except Exception as e:
        return {
            "success": False,
            "derivative": None,
            "order": order,
            "h": h if h else 0,
            "points": [],
            "message": f"Error: {str(e)}"
        }
