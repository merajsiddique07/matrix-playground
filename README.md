# 🎯 Matrix Playground

An interactive Python program to create and perform various matrix operations using **NumPy**.  
Easily create matrices (manually or randomly) and apply addition, subtraction, multiplication, division, transpose, and determinant operations — all from the terminal.

---

## 📌 Features

- Create matrices of **any size** (e.g., `3*3`, `5*2`, `10*10`)
- Two creation modes:
  - **Random integers** (0–99)
  - **Manual input**
- Supported operations:
  1. Addition of two matrices
  2. Subtraction of two matrices
  3. **Proper** matrix multiplication (`np.matmul`)
  4. Element-wise division
  5. Transpose
  6. Determinant (square matrices only)
- Keeps running until you choose to exit

---

## 🛠 Requirements

- Python 3.10+ (because the program uses `match-case` syntax)
- NumPy

Install dependencies:

```bash
pip install numpy

********Welcome to Matrix Playground!********
Choose an option:
1. Add Matrices
2. Subtract Matrices
3. Multiply Matrices
4. Divide Matrices
5. Transpose Matrix
6. Find Determinant
7. Exit

Enter choice: 1
Enter Order of Matrix (as 3*3 or 2*4): 2*2
1. Create random value matrix:
2. Create manually: 1
Matrix A = [[34  7]
 [12 88]]

Enter Order of Matrix (as 3*3 or 2*4): 2*2
1. Create random value matrix:
2. Create manually: 1
Matrix B = [[65 42]
 [ 5 17]]

Sum of Matrices:
 [[ 99  49]
 [ 17 105 ]]
```
