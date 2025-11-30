# 🚀 QUICK START GUIDE

## Get Started in 3 Steps!

### Step 1: Install Dependencies
Open PowerShell in this directory and run:
```powershell
pip install -r requirements.txt
```

### Step 2: Start the Server
```powershell
python main.py
```

### Step 3: Open Your Browser
Go to: **http://localhost:8000**

---

## 📋 What You Can Do

### 1. Jacobi Method
- Solve systems of linear equations
- Input: Matrix A and vector b (JSON format)
- Output: Solution vector with iterations

### 2. Regula-Falsi Method  
- Find roots of equations
- Input: Function and interval [a, b]
- Output: Approximate root

### 3. Forward Finite Difference
- Calculate derivatives using forward points
- Input: Function or data points
- Output: 1st or 2nd derivative

### 4. Backward Finite Difference
- Calculate derivatives using backward points
- Input: Function or data points
- Output: 1st or 2nd derivative

### 5. Center Finite Difference
- Calculate derivatives using central points (most accurate)
- Input: Function or data points
- Output: 1st or 2nd derivative

---

## 🧪 Run Tests (Optional)

To verify everything works:
```powershell
pytest test_numerical_methods.py -v
```

Expected: All tests pass ✓

---

## 💡 Quick Examples

### Example 1: Solve Linear System (Jacobi)
```
Matrix A: [[4, -1, 0], [-1, 4, -1], [0, -1, 4]]
Vector b: [5, 0, 6]
```

### Example 2: Find Square Root of 4 (Regula-Falsi)
```
Function: x**2 - 4
Interval: [0, 3]
Result: x ≈ 2.0
```

### Example 3: Find Derivative (Central Difference)
```
Function: x**2
X value: [2.0]
Step size: 0.01
Result: f'(2) ≈ 4.0
```

---

## ❓ Troubleshooting

**Problem**: Dependencies won't install
**Solution**: Make sure Python 3.8+ is installed

**Problem**: Port 8000 in use
**Solution**: Use a different port:
```powershell
uvicorn main:app --reload --port 8080
```

**Problem**: Templates not found
**Solution**: Make sure you're in the correct directory

---

## 📚 More Information

See **README.md** for detailed documentation
See **PROJECT_SUMMARY.md** for complete project details

---

**Ready to start? Run `python main.py` now!** 🎉
