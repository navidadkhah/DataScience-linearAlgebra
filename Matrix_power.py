# Matrix power using special value and special vector

p = np.array([[2, 2], [1+np.sqrt(5), 1-np.sqrt(5)]])
p_inverse = np.linalg.inv(p)

a = (1 + np.sqrt(5)) / 2
b = (1 - np.sqrt(5)) / 2

D = np.array([[a, 0], [0, b]])   
   
javab = np.matmul(np.matmul(p, np.linalg.matrix_power(D, 10)), p_inverse)

print(javab)