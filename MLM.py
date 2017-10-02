import numpy as np
import sklearn.datasets as database
import math
from sklearn.metrics.pairwise import euclidean_distances
import random
from sklearn.model_selection import train_test_split



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
        self.pontos_referenciaX, self.pontos_referenciaY = self.random_pontos_referencias(X.shape[0],X, Y)
        #print self.pontos_referenciaX
        #print X
        #matrizes de distancias
        dX = euclidean_distances(X, self.pontos_referenciaX)
        dY = euclidean_distances(Y, self.pontos_referenciaY)
        #Faca a distancia dos dois pontos = raiz2((dp - dx)^2)

        B_hat = np.linalg.solve(dX.T.dot(dX), dX.T).dot(dY)
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
        random_pontosX = []
        random_pontosY = []
        for i in range(self.numero_pontos_referencia):
            ponto = np.random.randint(tamanho)
            if (ponto in random_indices) == False:
                random_indices.append(ponto)
                random_pontosX.append(X[ponto])
                random_pontosY.append(Y[ponto])
        #print random_pontosX
        #print "\n"
        #print random_pontosY
        return random_pontosX, random_pontosY


    def predict(self, amostrasTeste):
        '''

        :param amostrasTeste: amostras de teste para serem classificadas
        :return: predicao da amostras (Vimos o seu futuro, ele diz que vc eh Versicolor Mwahhahaha)
        '''

        #Array que vai guardar a distancia

        dAmostraTX = euclidean_distances(amostrasTeste, self.pontos_referenciaX)
        dY = dAmostraTX.dot(self.B_hat)

        '''
        for para armazenar a classificacao da matriz de novas amostras
        '''
        pred_hat = []
        for indice in range(len(amostrasTeste)):
            pred_hat.append(self.pontos_referenciaY[np.argmin(dY[indice])])

        return pred_hat



    def binarizar(self, y):
        bin_ = np.zeros((y.shape[0], np.amax(y) + 1))
        for i in range(len(y)):
            bin_[i][y[i]] = 1
        return bin_

    def uniqueValues (self, X, y):
        Xn = [X[0]]
        yn = [y[0]]
        for i in range(len(X)):
            if not np.any(np.equal(Xn, X[i]).all(1)):
                Xn.append(X[i])
                yn.append(y[i])

        return np.array(Xn), np.array(yn)





mlmT = MLM(40)
iris = database.load_iris()
Xload = iris.data
yload = mlmT.binarizar(iris.target)
X, y = mlmT.uniqueValues(Xload,yload)
acertosInteracoes = []



for i in range(30):
    Xl, Xt, yl, yt = train_test_split(X, y, test_size=0.2)
    mlmT.treinamento(Xl, yl)
    predictXt = mlmT.predict(Xt)
    acertos = 0
    for j in range(len(yt)):
        acertos += int(np.array_equal(yt[j],predictXt[j]))
    acertosInteracoes.append(acertos)

print acertos