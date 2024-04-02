import preguntas as p
import random


def shuffle_alt(pregunta):
    """    Mezcla las alternativas de una pregunta.

    Args:
        pregunta (dict): Diccionario que contiene el enunciado y las alternativas de la pregunta.

    Returns:
        list: Lista de alternativas mezcladas.
    """

    #mezclar alternativas
    #######################################################################
    alternativas=pregunta['alternativas']
    random.shuffle(alternativas)
    
    
    
    #######################################################################
    
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]