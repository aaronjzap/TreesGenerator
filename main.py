from arbol import Tree, Measure_calculation
from  correlations import Correlations
from  permutations import Differentes_same_grades


if __name__ == "__main__":
    n= 15
    Tree(n-2)
    Differentes_same_grades(n)
    Measure_calculation(n)
    
    Correlations(n)



