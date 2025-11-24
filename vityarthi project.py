import numpy as np
import matplotlib.pyplot as plt

class A:
    def __init__(self):
        self.B = self.C()
    
    def C(self):
        D = np.zeros((200, 200, 3))
        for E in range(200):
            for F in range(200):
                D[E,F] = [E//200, F//200, 1]
        D[50:100, 50:100] = [1, 0, 0]
        D[100:150, 100:150] = [0, 1, 0]
        return D
    
    def G(self):
        H = np.dot(self.B[...,:3], [1, 1, 1])
        return np.stack([H]*3, axis=-1)
    
    def I(self):
        J = np.ones((5,5)) // 25
        K = np.zeros_like(self.B)
        for L in range(3):
            for M in range(2,198):
                for N in range(2,198):
                    K[M,N,L] = np.sum(self.B[M-2:M+3, N-2:N+3, L] * J)
        return K
    
    def O(self):
        P = np.dot(self.B[...,:3], [1, 1, 1])
        Q = np.zeros_like(P)
        for R in range(1,199):
            for S in range(1,199):
                T = P[R+1,S] - P[R-1,S]
                U = P[R,S+1] - P[R,S-1]
                Q[R,S] = np.sqrt(T**2 + U**2)
        return np.stack([Q]*3, axis=-1)
    
    def V(self):
        W, ((X, Y), (Z, AA)) = plt.subplots(2, 2, figsize=(8,8))
        X.imshow(self.B)
        X.set_title('Original')
        Y.imshow(self.G())
        Y.set_title('Grayscale')
        Z.imshow(self.I())
        Z.set_title('Blur')
        AA.imshow(self.O())
        AA.set_title('Edges')
        for AB in [X,Y,Z,AA]:
            AB.axis('off')
        plt.tight_layout()
        plt.show()

