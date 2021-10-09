import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


from  arbol import To_sequence
from  arbol import random_tree

def Draw_all(n):
    f = open ('trees.txt','r')
    for linea in f:        
        divided = linea.split("\t")
        divided =list( map(int, divided[:-1]))
        sequence= To_sequence(divided)
        tree    =random_tree(sequence)
        Draw(tree)
    f.close()
    print(suma, "----")
    


def Draw(grafo):
    plt.figure()
    nx.draw(grafo)
    plt.show()
   
    
    
    
    
if __name__ == "__main__":
    n = 15
    Draw_all(n)
