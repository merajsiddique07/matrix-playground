import numpy as np
print(np.char.center("Welcome to Matrix Playground!",41,"*"))
print("Choose an option:")
def create(w):
  if w==None or w=='A':
    w='A'
  else:
    w="B"
  order=input("Enter Order of Matrix (as 3*3 or 2*4):" )
  row, col = map(int, order.split('*'))
  while True:
    c=int(input("1. Create random value matrix:\n2. Create manually:"))
    if c==1:
      mat1=np.random.randint(0, 100, size=(row, col))
      print(f'Matrix, {w}=',mat1)
      break
    elif c==2:
      list=[]
      l1=[]
      for i in range(row):
        for j in range(col):
          l1.append(int(input('Enter matrix values:')))
        list.append(l1.copy())
        l1.clear()
      mat1=np.array(list)
      print(mat1)
      break
    else:
      print("Please Choose correct option.")
  return mat1

def addMatrix(matrix1,matrix2):
  return matrix1+matrix2

def subMatrix(matrix1,matrix2):
  return matrix1-matrix2

def mulMatrix(matrix1,matrix2):
  if matrix1.shape[1] != matrix2.shape[0]:
    print("Error: For multiplication, columns of Matrix A must equal rows of Matrix B.")
  mul=np.matmul(matrix1, matrix2)
  return mul

def divMatrix(matrix1,matrix2):
  if np.any(matrix2 == 0):
    print("Error: Division by zero in matrix elements.")
  return matrix1/matrix2

def transpose():
  at=create(None).T
  return at

def deter():
  d=np.linalg.det(create(None))
  return d
  
while(True):
  choice=int(input("1. Add Matrices:\n2. Subtract Matrices\n3. Multiply Matrices:\n4. Divide Matrices:\n5. Transpose Matrix:\n6. Find Determinant:\n7. Exit:"))
  match choice:
    case 1:
      matrix1=create('A')
      matrix2=create('B')
      try:
        print("\nSum of Matrices:\n",addMatrix(matrix1,matrix2),"\n")
      except ValueError:
        print("Order mismatched! Enter same order of matrices.")
    case 2:
      matrix1=create('A')
      matrix2=create('B')
      try:
        print("\nSubtraction of Matrices:\n",subMatrix(matrix1,matrix2),"\n")
      except ValueError:
        print("Order mismatched! Enter same order of matrices.")
    case 3:
      matrix1=create('A')
      matrix2=create('B')
      try:
        print("\nMultiplication of Matrices:\n",mulMatrix(matrix1,matrix2),"\n")
      except ValueError:
        print("Order mismatched! Enter same order of matrices.")
    case 4:
      matrix1=create('A')
      matrix2=create('B')
      try:
        print("\nDivision of Matrices:\n",divMatrix(matrix1,matrix2),"\n")
      except ValueError:
        print("Order mismatched! Enter same order of matrices.")
      
    case 5:
      print("\nTranspose of Matrix:\n",transpose(),"\n")
      
    case 6:
      print("\nDeterminant of Matrix:\n",deter(),"\n")
      
    case 7:
      print(np.char.center("Thanku for visiting.",30,"*"))
      break
    case _:
        print("Wrong entry! Please try again.")