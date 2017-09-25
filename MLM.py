import numpy as np
import sklearn.datasets as database
import math
class MLM():

    def __init__(self, numero_pontos_referencia = 10):
        '''
            :param numero_pontos_de_referencia: Unico hiperparametro do Minimal Learning Machine
        '''
        self.numero_pontos_referencia = numero_pontos_referencia
        self.B_hat = []
        pontos_referenciaX = []
        pontos_referenciaY = []


    def treinamento(self, X, Y):
        '''

        :param X: matriz X
        :param Y: matriz Y
        :return: B_hat, pontos de refencias X e Y
        '''

        self.pontos_referenciaX, self.pontos_referenciaY = self.random_pontos_referencias(Y.shape[0], X, Y)
        #matrizes de distancias
        dX = np.zeros(shape=(self.numero_pontos_referencia, X.shape[1]))
        dY = np.zeros(shape=(self.numero_pontos_referencia, Y.shape[1]))

        #Faca a distancia dos dois pontos = raiz2((dp - dx)^2)

        '''
            for para calcular a distancia. Acho que ta errado esse for, conserto depois :v
        '''
        for i in range(X.shape[0]):
            for j in range(len(self.pontos_referenciaX)-1):
                for t in range(X.shape[1]):
                    dX[i][j] = (math.sqrt((self.pontos_referenciaX[i][j] - X[i][j]) ** 2))

        for i in range(Y.shape[0]):
            for j in range(len(self.pontos_referenciaY)-1):
                for t in range(X.shape[1]):
                    dX[i][j] = (math.sqrt((self.pontos_referenciaY[i][j] - Y[i][j])**2))

        B_hat = np.linalg.solve(dX,dY)
        self.B_hat = B_hat
        return B_hat, self.pontos_referenciaX, self.pontos_referenciaY



    def random_pontos_referencias(self, tamanho, X, Y):
        '''
        :param tamanho: para saber o random.int usado
        :param X: Matriz de amostras
        :param Y: Matriz de rotulos de amostras
        :return: pontos de referencias
        '''
        random_indices = []
        random_pontosA = []
        random_pontosY = []
        for i in range(self.numero_pontos_referencia):
            ponto = np.random.randint(tamanho)
            if ponto in random_indices == False:
                random_indices.append(ponto)
                random_pontosA.append(X[ponto])
                random_pontosY.append(Y[ponto])


        return random_pontosA, random_pontosY


    def predict(self, amostraT):
        '''

        :param amostraT: amostra de treinamento, ou seja, vc manda uma amostra por vez
        :return: predicao da amostra (Vimos o seu futuro, ele diz que vc eh Versiculor Mwahhahaha)
        '''

        #Array que vai guardar a distancia
        DamostraT = []


        '''
        for para calcular a distancia da amostra. Acho que ta errado esse for, conserto depois :v
        '''
        for i in range(amostraT.shape[0]):
            for j in range(len(self.pontos_referenciaX) - 1):
                DamostraT.append(math.sqrt((amostraT[i][j] - amostraT[i][j]) ** 2))

        pred_hat = np.dot(amostraT, self.B_hat)
        min_pred_hat = min(pred_hat)

        predicaoIndice = np.where(self.pontos_referenciaX == min_pred_hat)[0]
        return self.pontos_referenciaY[predicaoIndice]



#x = database.load_iris()
#xd = x.data
#print xd