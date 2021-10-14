# Fichero de la clase Aspectos, clase que encuentra y modela los aspectos positivos y negativos de un local en base a sus reseñas

import resenia


class Aspectos:
    '''Clase para analizar un conjunto de reseñas y extraer sus aspectos positivos y negativos.
    
    Atributos:
    resenias (List[resenia.Resenia]): Conjunto de reseñas.
    local (string): Local sobre el que se analizan las reseñas.
    aspectos_positivos (Array[string]): Lista de los aspectos positivos del local.
    aspectos_negativos (Array[string]): Lista de los aspectos negativos del local.
    '''


    def __init__(self, resenias, local):
        '''Inicializador de la clase.
        
        Argumentos:
        arg1 (Array[Resenias]): conjunto de Resenias.
        arg2 (string): local al que pertenecen las Resenias.
        '''
        
        self.resenias = resenias 
        self.local = local 
        self.aspectos_positivos = [] 
        self.aspectos_negativos = [] 

    
    def extraer_aspectos_positivos(self):
        '''Método para extraer los aspectos positivos.'''
        pass

    def extraer_aspectos_negativos(self):
        '''Método para extraer los aspectos negativos.'''
        pass
