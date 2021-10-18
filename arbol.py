import numpy as np




    
#----------------------



import csv
def Grados_sele(lista):
    return [l[1] for l in lista]

def Gram_smidt(vectors):
    basis = []
    vectors=np.array(vectors)
    for v in vectors:
        v=np.array(v)
        w = v - np.sum( np.dot(v,b)*b for b in basis )
        basis.append(w/np.linalg.norm(w))
    return np.array(basis)







def Energia(matriz):
    matriz=np.array(matriz)
    x, v = np.linalg.eig(matriz)
    e=np.sum(np.abs(x))
    return e,Energia_vertice(x,v)



def Crear_matriz(n,ws):
    matriz=np.zeros((n,n))
    edges=ws.edges()
    for e in edges:
        matriz[e[0]][e[1]]=1
        matriz[e[1]][e[0]]=1
    return matriz


def Energia_vertice(valores,vectores):
    vectores, w= np.linalg.qr(vectores)
    e_v=[]
    if len(valores)==1:
        for entrada in vectores:
            suma=Decimal(entrada*abs(valores))
    else:
        suma_total=0
        for i in range(0,len(valores)):
            suma=0
            for j in range (0,len(valores)):
                suma+=vectores[i,j]*vectores[i,j]*abs(valores[j])
            e_v.append(suma)
            suma_total+=suma
       
    return  np.real(e_v)
    #return  [round(e,15) for e in np.real(e_v)]




#--------------------------------------------------------
def Tree(n):
    f = open ('trees.txt','w')
    f.close()
    f = open ('trees.txt','a')
    
    def List_nodes(Sum, j, num2):
        #print(Sum, j)
        if Sum==n:
            #f.write(str(k)+'\n')
            f.write(str(k)+ '\t'+num2 +'\n')
            return 0;
        
        for i in range(1, j+1):
            c= Sum+i
            if c<=n:
              num= num2+ str(i)+ '\t'
              #f.write(str(i)+ '\t')
              List_nodes(c, i, num)
    
            else:
                continue
            
    for k in range(1,n):
        #print(k, "----")
        List_nodes(k,k, '')
    f.write(str(n)+ '\t'+'\n')
    f.close()






    
    
def Verification(L):
    for l in L:
        print(sum(l))
    print(len(L))
    
    
def  To_sequence(Lis):
    L= []
    for i, l in  enumerate(Lis):
        L= L+[i]*l
    return L
    
    
    



import networkx as nx
def random_tree(sequence, seed=None, create_using=None):
    utree = nx.from_prufer_sequence(sequence)
    tree = nx.empty_graph(0, create_using)
    edges = utree.edges()    
    tree.add_nodes_from(utree.nodes)  
    tree.add_edges_from(edges)
   
    return tree






def Rename_files(n):
    def xx(name):
        f = open (name,'w')
        f.close()
        
    EnergyT ='EnergiaT_'+str(n)+'.csv'
    EnergyV ='EnergiaV_'+str(n)+'.csv'
    Degree  ='Grados_'+str(n)+'.csv'
    Close   ='Cercania_'+str(n)+'.csv'
    Bet     ='Entre_'+str(n)+'.csv'
    Eigen   ='Eigen_'+str(n)+'.csv'
    xx(EnergyT), xx(EnergyV), xx(Degree), xx(Close), xx(Bet), xx(Eigen)
    f = open ('trees.txt','a')
    return EnergyT, EnergyV,  Degree, Close, Bet, Eigen 
    

    
    
    

def Measures(grafo, n, EnergyT, EnergyV,  Degree, Close, Bet, Eigen):
    ET,EV=Energia(Crear_matriz(n,grafo))
    Add_csv([ET], EnergyT )
    Add_csv(EV, EnergyV)
    Add_csv(Grados_sele(grafo.degree), Degree)           
    Add_csv(list(nx.closeness_centrality(grafo).values()), Close)
    #Add_csv(list(nx.betweenness_centrality(grafo).values()), Bet)
    Add_csv(list(nx.eigenvector_centrality_numpy(grafo).values()), Eigen)

      
  

def Add_csv(data, name):
    with open(name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)




def Measure_calculation(n):
    
    f = open ('trees.txt','r')
    EnergyT, EnergyV,  Degree, Close, Bet, Eigen = Rename_files(n)
    suma=0
    for linea in f:        
        divided = linea.split("\t")
        divided =list( map(int, divided[:-1]))
        #print(sum(divided))
        suma+=1
        sequence= To_sequence(divided)
        tree    =random_tree(sequence)
        Measures(tree, n, EnergyT, EnergyV,  Degree, Close, Bet, Eigen)
        
    f.close()
    print(suma, "----")
    
    
    
    
    
    
    
    

    
if __name__ == "__main__":
    n= 6
    import time 
    start= time.time()
    Tree(n-2)
    #end= time.time()
    #print(end- start)
    #Measure_calculation(n)
    #Verification(n)
  
    
    
    
    
