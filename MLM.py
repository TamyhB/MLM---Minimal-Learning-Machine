import numpy as np
import sklearn.datasets as database
import math
class MLM():

    def __init__(self, numero_pontos_referencia = 10):
        '''
            :param numero_pontos_de_referencia: Unico hiperparametro do Minimal Learning Machine
        '''
        self.numero_pontos_referencia = numero_pontos_referencia

    def calcula_distancia(self, X, Y):
        '''

        :param X:
        :param Y:
        :return:
        '''

        auxA = self.random_pontos_referencias(X.shape[0])
        pontos_referenciaX, pontos_referenciaY = self.random_pontos_referencias(Y.shape[0], X, Y)
        dX = []
        dY = []
        #Faca a distancia dos dois pontos = raiz2((dp - dx)ˆ2)
        for i in range(X.shape[0]):
            for j in range(len(pontos_referenciaX)-1):
                for t in range(X.shape[1]):
                    dX = math.sqrt((pontos_referenciaX[i][j] - X[i][j]) ** 2)

        for i in range(Y.shape[0]):
            for j in range(len(pontos_referenciaY)-1):
                for t in range(X.shape[1]):
                    dY = math.sqrt((pontos_referenciaY[i][j] - Y[i][j])**2)

        B_hat = np.linalg.solve(dX,dY)

        return B_hat, pontos_referenciaX, pontos_referenciaY



    def random_pontos_referencias(self, tamanho, A, Y):
        random_indices = []
        random_pontosA = []
        random_pontosY = []
        for i in range(tamanho):
            ponto = np.random.randint(tamanho)
            if ponto in random_indices == False:
                random_indices.append(ponto)
                random_pontosA.append(A[ponto])
                random_pontosY.append(Y[ponto])


        return random_pontosA, random_pontosY

#x = database.load_iris()
#xd = x.data
#print xd