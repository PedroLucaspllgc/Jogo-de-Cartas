from collections import namedtuple
from itertools import product

Carta = namedtuple('Carta', ['face', 'naipe'])

faces = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
naipes = {'O', 'P', 'C', 'E'}

baralho = [Carta(face, naipe) for face, naipe in product(faces, naipes)]

print('Seu baralho possui', len(baralho), 'cartas')
