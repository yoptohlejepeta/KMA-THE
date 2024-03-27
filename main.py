import streamlit as st
import numpy as np
import nashpy as nash


st.title('Nash Equilibrium Calculator')

st.header("Matrix A")
# input matrix
num_rows = st.number_input('Number of rows', min_value=2, max_value=10, value=2)
num_cols = st.number_input('Number of columns', min_value=2, max_value=10, value=2)

matrix_A = np.zeros((num_rows, num_cols))

cols = st.columns(num_cols)

for i in range(num_rows):
    for j in range(num_cols):
        matrix_A[i][j] = cols[j].number_input(f'Enter value for cell ({i+1}, {j+1})', value=0.0, step=0.1, key=f'A{i}{j}')
        
st.write(matrix_A)

st.header("Matrix B")

cols = st.columns(num_cols)

matrix_B = np.zeros((num_rows, num_cols))

for i in range(num_rows):
    for j in range(num_cols):
        matrix_B[i][j] = cols[j].number_input(f'Enter value for cell ({i+1}, {j+1})', value=0.0, step=0.1, key=f'B{i}{j}')
        
st.write(matrix_B)


game = nash.Game(matrix_A, matrix_B)
equilibria = game.support_enumeration()

st.header("Nash Equilibria")

for eq in equilibria:
    st.write("Player 1 strategy: ", eq[0])
    st.write("Player 2 strategy: ", eq[1])