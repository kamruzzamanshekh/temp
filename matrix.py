import numpy as np
import pandas as pd

# Create two matrices using NumPy
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

# Convert NumPy arrays to Pandas DataFrames
df_A = pd.DataFrame(A, columns=['Col1', 'Col2', 'Col3'])
df_B = pd.DataFrame(B, columns=['Col1', 'Col2', 'Col3'])

# Sum the DataFrames (element-wise)
df_sum = df_A + df_B

print("Matrix A:")
print(df_A)
print("\nMatrix B:")
print(df_B)
print("\nSum of Matrices:")
print(df_sum)

# Optional: sum all elements using NumPy
total_sum = np.sum(df_sum.values)
print("\nSum of all elements:", total_sum)