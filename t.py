def calcula_norma(n, x, v):
    normaNum = 0
    normaDem = 0
    for i in range(n):
        t = abs(v[i] - x[i])
        if t > normaNum:
            normaNum = t
        if abs(v[i]) > normaDem:
            normaDen = abs(v[i])
        # vetor x e atualizado com vetor v
        x[i] = v[i]
    norma = normaNum / normaDen
    return norma

def gauss_seidel(n, A, b, e, iterMax):
    # construcao da matriz e do vetor de interacoes
    x = [1.0, 1.0, 1.0, 1.0, 1.0]
    v = [0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(n):
         r = 1 / A[i][i]
         for j in range(n):
                if i != j:
                    A[i][j] *= r
         b[i] *= r
         x[i] = b[i]
    k = 0
    while(True):
        k += 1
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma += (A[i][j] * x[j])
            v[i] = x[i]
            x[i] = b[i] - soma
        norma = calcula_norma(n, v, x)
        print (k, x, norma)
        if norma <= e or k >= iterMax:
            break
    return (x, k)
	
A = [ [6.0, 0.0, -3.0, 0.0, 0.0],[3.0, -3.0, 0.0, 0.0, 0.0],[0.0, -1.0, 9.0, 0.0, 0.0],[0.0, 1.0, 8.0, -11.0, 2.0],[3.0, 1.0, 0.0, 0.0, -4.0]]
b = [50.0, 0.0, 160.0, 0.0, 0.0]


gauss_seidel(5, A, b, 0.001, 500)
