import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**3 + x**2 - 3*x - 3  # Contoh fungsi

def bolzano(a, b, tol):
    if function(a) * function(b) >= 0:
        raise ValueError("f(a) dan f(b) harus beda tanda")
    
    iterasi = []
    while (b - a) / 2 > tol: # a = 1, b =2 , c = 1,5
        c = (a + b) / 2
        iterasi.append((a, b, c))
        
        if function(c) == 0: 
            break
        elif function(c) * function(a) < 0: # f(a) = -4, f(b) = 3, f(c) = -1,875 
            b = c
        else:
            a = c # a = -1,875
    
    return c, iterasi

# Parameter
a = 1
b = 2
toleransi = 1e-6

# Menjalankan metode Bolzano
root, iters = bolzano(a, b, toleransi)
print(f"Akar: {root}")
print("Hasil Iterasi:")
for i, (x1, x2, x3) in enumerate(iters, 1):
    print(f"Iterasi {i}: x1 = {x1:.5f}, f(x1) = {function(x1):.5f}, x2 = {x2:.5f}, f(x2) = {function(x2):.5f}, x3 = {x3:.5f}, f(x3) = {function(x3):.5f}")

# Menampilkan grafik
x = np.linspace(a, b, 400)
y = function(x) 

plt.plot(x, y, label='f(x)') 
plt.axhline(0, color='black', lw=0.5) 
plt.axvline(root, color='r', linestyle='--', label=f'Akar ≈ {root:.5f}')
plt.scatter([x3 for _, _, x3 in iters], [0]*len(iters), color='green', zorder=5, label='Iterasi')

plt.title('Grafik Fungsi Iterasi Metode Bolzano')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
