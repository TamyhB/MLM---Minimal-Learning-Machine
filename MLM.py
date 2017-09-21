import numpy as np
import sklearn.datasets as database
class MLM():

    def __init__(self, numero_pontos_referencia = 10):
        '''
            :param numero_pontos_de_referencia: Unico hiperparametro do Minimal Learning Machine
        '''
        self.numero_pontos_referencia = numero_pontos_referencia

    def calcula_distancia(self, matrizA, matrizY):
        pontos_referencia = self.random_pontos_referencias(matrizA.shape[0])

        dX = []
        dY = []

    def random_pontos_referencias(self, tamanho):
        random_pontos = []
        for i in range(tamanho):
            ponto = np.random.randint(tamanho)
            if ponto in random_pontos == False:
                random_pontos.append(ponto)

        return random_pontos

#x = database.load_iris()
#xd = x.data
#print xd