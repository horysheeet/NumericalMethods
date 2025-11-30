"""Main FastAPI application for Numerical Methods project."""
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Optional
import json

# Import numerical methods
from jacobi import jacobi_method, check_diagonal_dominance
from regula_falsi import regula_falsi_method
from forward_fd import forward_finite_difference
from backward_fd import backward_finite_difference
from center_fd import center_finite_difference
from config_loader import config

# Create FastAPI app
app = FastAPI(title="Numerical Methods Calculator", version="1.0.0")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Setup static files
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    pass  # Directory may not exist yet


# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with links to all methods."""
    return templates.TemplateResponse("home.html", {
        "request": request,
        "title": "Numerical Methods Calculator"
    })


# ============================================================================
# JACOBI METHOD
# ============================================================================

@app.get("/jacobi", response_class=HTMLResponse)
async def jacobi_page(request: Request):
    """Jacobi method page."""
    return templates.TemplateResponse("jacobi.html", {
        "request": request,
        "title": "Jacobi Method",
        "result": None
    })


@app.post("/jacobi", response_class=HTMLResponse)
async def jacobi_compute(
    request: Request,
    matrix_a: str = Form(...),
    vector_b: str = Form(...),
    initial_guess: str = Form(""),
    max_iterations: Optional[int] = Form(None),
    tolerance: Optional[float] = Form(None)
):
    """Compute Jacobi method."""
    try:
        # Parse input
        A = json.loads(matrix_a)
        b = json.loads(vector_b)
        x0 = json.loads(initial_guess) if initial_guess else None
        
        # Compute
        result = jacobi_method(A, b, x0, max_iterations, tolerance)
        
        # Check diagonal dominance
        dominance_check = check_diagonal_dominance(A)
        result["diagonal_dominance"] = {
            "is_dominant": dominance_check[0],
            "message": dominance_check[1]
        }
        
        return templates.TemplateResponse("jacobi.html", {
            "request": request,
            "title": "Jacobi Method",
            "result": result,
            "input_data": {
                "matrix_a": matrix_a,
                "vector_b": vector_b,
                "initial_guess": initial_guess,
                "max_iterations": max_iterations,
                "tolerance": tolerance
            }
        })
    
    except json.JSONDecodeError as e:
        return templates.TemplateResponse("jacobi.html", {
            "request": request,
            "title": "Jacobi Method",
            "result": {
                "success": False,
                "message": f"Invalid JSON input: {str(e)}"
            }
        })
    except Exception as e:
        return templates.TemplateResponse("jacobi.html", {
            "request": request,
            "title": "Jacobi Method",
            "result": {
                "success": False,
                "message": f"Error: {str(e)}"
            }
        })


@app.post("/api/jacobi")
async def jacobi_api(
    matrix_a: List[List[float]],
    vector_b: List[float],
    initial_guess: Optional[List[float]] = None,
    max_iterations: Optional[int] = None,
    tolerance: Optional[float] = None
):
    """Jacobi method API endpoint."""
    result = jacobi_method(matrix_a, vector_b, initial_guess, max_iterations, tolerance)
    dominance_check = check_diagonal_dominance(matrix_a)
    result["diagonal_dominance"] = {
        "is_dominant": dominance_check[0],
        "message": dominance_check[1]
    }
    return result


# ============================================================================
# REGULA-FALSI METHOD
# ============================================================================

@app.get("/regula-falsi", response_class=HTMLResponse)
async def regula_falsi_page(request: Request):
    """Regula-Falsi method page."""
    return templates.TemplateResponse("regula_falsi.html", {
        "request": request,
        "title": "Regula-Falsi Method",
        "result": None
    })


@app.post("/regula-falsi", response_class=HTMLResponse)
async def regula_falsi_compute(
    request: Request,
    function: str = Form(...),
    a: float = Form(...),
    b: float = Form(...),
    max_iterations: Optional[int] = Form(None),
    tolerance: Optional[float] = Form(None)
):
    """Compute Regula-Falsi method."""
    try:
        result = regula_falsi_method(function, a, b, max_iterations, tolerance)
        
        return templates.TemplateResponse("regula_falsi.html", {
            "request": request,
            "title": "Regula-Falsi Method",
            "result": result,
            "input_data": {
                "function": function,
                "a": a,
                "b": b,
                "max_iterations": max_iterations,
                "tolerance": tolerance
            }
        })
    
    except Exception as e:
        return templates.TemplateResponse("regula_falsi.html", {
            "request": request,
            "title": "Regula-Falsi Method",
            "result": {
                "success": False,
                "message": f"Error: {str(e)}"
            }
        })


@app.post("/api/regula-falsi")
async def regula_falsi_api(
    function: str,
    a: float,
    b: float,
    max_iterations: Optional[int] = None,
    tolerance: Optional[float] = None
):
    """Regula-Falsi method API endpoint."""
    return regula_falsi_method(function, a, b, max_iterations, tolerance)


# ============================================================================
# FORWARD FINITE DIFFERENCE
# ============================================================================

@app.get("/forward-fd", response_class=HTMLResponse)
async def forward_fd_page(request: Request):
    """Forward finite difference page."""
    return templates.TemplateResponse("forward_fd.html", {
        "request": request,
        "title": "Forward Finite Difference",
        "result": None
    })


@app.post("/forward-fd", response_class=HTMLResponse)
async def forward_fd_compute(
    request: Request,
    function: str = Form(""),
    x_values: str = Form(...),
    y_values: str = Form(""),
    order: int = Form(1),
    h: Optional[float] = Form(None)
):
    """Compute forward finite difference."""
    try:
        x_vals = json.loads(x_values)
        y_vals = json.loads(y_values) if y_values else None
        
        result = forward_finite_difference(function, x_vals, y_vals, order, h)
        
        return templates.TemplateResponse("forward_fd.html", {
            "request": request,
            "title": "Forward Finite Difference",
            "result": result,
            "input_data": {
                "function": function,
                "x_values": x_values,
                "y_values": y_values,
                "order": order,
                "h": h
            }
        })
    
    except json.JSONDecodeError as e:
        return templates.TemplateResponse("forward_fd.html", {
            "request": request,
            "title": "Forward Finite Difference",
            "result": {
                "success": False,
                "message": f"Invalid JSON input: {str(e)}"
            }
        })
    except Exception as e:
        return templates.TemplateResponse("forward_fd.html", {
            "request": request,
            "title": "Forward Finite Difference",
            "result": {
                "success": False,
                "message": f"Error: {str(e)}"
            }
        })


@app.post("/api/forward-fd")
async def forward_fd_api(
    function: str = "",
    x_values: List[float] = None,
    y_values: Optional[List[float]] = None,
    order: int = 1,
    h: Optional[float] = None
):
    """Forward finite difference API endpoint."""
    return forward_finite_difference(function, x_values, y_values, order, h)


# ============================================================================
# BACKWARD FINITE DIFFERENCE
# ============================================================================

@app.get("/backward-fd", response_class=HTMLResponse)
async def backward_fd_page(request: Request):
    """Backward finite difference page."""
    return templates.TemplateResponse("backward_fd.html", {
        "request": request,
        "title": "Backward Finite Difference",
        "result": None
    })


@app.post("/backward-fd", response_class=HTMLResponse)
async def backward_fd_compute(
    request: Request,
    function: str = Form(""),
    x_values: str = Form(...),
    y_values: str = Form(""),
    order: int = Form(1),
    h: Optional[float] = Form(None)
):
    """Compute backward finite difference."""
    try:
        x_vals = json.loads(x_values)
        y_vals = json.loads(y_values) if y_values else None
        
        result = backward_finite_difference(function, x_vals, y_vals, order, h)
        
        return templates.TemplateResponse("backward_fd.html", {
            "request": request,
            "title": "Backward Finite Difference",
            "result": result,
            "input_data": {
                "function": function,
                "x_values": x_values,
                "y_values": y_values,
                "order": order,
                "h": h
            }
        })
    
    except json.JSONDecodeError as e:
        return templates.TemplateResponse("backward_fd.html", {
            "request": request,
            "title": "Backward Finite Difference",
            "result": {
                "success": False,
                "message": f"Invalid JSON input: {str(e)}"
            }
        })
    except Exception as e:
        return templates.TemplateResponse("backward_fd.html", {
            "request": request,
            "title": "Backward Finite Difference",
            "result": {
                "success": False,
                "message": f"Error: {str(e)}"
            }
        })


@app.post("/api/backward-fd")
async def backward_fd_api(
    function: str = "",
    x_values: List[float] = None,
    y_values: Optional[List[float]] = None,
    order: int = 1,
    h: Optional[float] = None
):
    """Backward finite difference API endpoint."""
    return backward_finite_difference(function, x_values, y_values, order, h)


# ============================================================================
# CENTER FINITE DIFFERENCE
# ============================================================================

@app.get("/center-fd", response_class=HTMLResponse)
async def center_fd_page(request: Request):
    """Center finite difference page."""
    return templates.TemplateResponse("center_fd.html", {
        "request": request,
        "title": "Center Finite Difference",
        "result": None
    })


@app.post("/center-fd", response_class=HTMLResponse)
async def center_fd_compute(
    request: Request,
    function: str = Form(""),
    x_values: str = Form(...),
    y_values: str = Form(""),
    order: int = Form(1),
    h: Optional[float] = Form(None)
):
    """Compute center finite difference."""
    try:
        x_vals = json.loads(x_values)
        y_vals = json.loads(y_values) if y_values else None
        
        result = center_finite_difference(function, x_vals, y_vals, order, h)
        
        return templates.TemplateResponse("center_fd.html", {
            "request": request,
            "title": "Center Finite Difference",
            "result": result,
            "input_data": {
                "function": function,
                "x_values": x_values,
                "y_values": y_values,
                "order": order,
                "h": h
            }
        })
    
    except json.JSONDecodeError as e:
        return templates.TemplateResponse("center_fd.html", {
            "request": request,
            "title": "Center Finite Difference",
            "result": {
                "success": False,
                "message": f"Invalid JSON input: {str(e)}"
            }
        })
    except Exception as e:
        return templates.TemplateResponse("center_fd.html", {
            "request": request,
            "title": "Center Finite Difference",
            "result": {
                "success": False,
                "message": f"Error: {str(e)}"
            }
        })


@app.post("/api/center-fd")
async def center_fd_api(
    function: str = "",
    x_values: List[float] = None,
    y_values: Optional[List[float]] = None,
    order: int = 1,
    h: Optional[float] = None
):
    """Center finite difference API endpoint."""
    return center_finite_difference(function, x_values, y_values, order, h)


# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
