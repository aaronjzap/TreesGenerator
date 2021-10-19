
def permutations(x):
    
    f = open ('aux.txt','w')
    f.close()
    f = open ('aux.txt','a')
    s = list(set(x))
    if len(s)==1:
        x= list(map(str, x))
        f.write('\t'.join(x) +'\n')
        return 0
    con = [x.count(i) for i in s]
    y = dict(zip(s, con))
    
    
    
    def sub_fun(y, sequence):
        I= True
        for i in y:
            if y[i]>0:
                yy=y.copy()
                yy[i]-=1
                sequence2 = sequence +'\t'+str(i) 
                sub_fun(yy, sequence2)
                I=False
            
        if I == True:
             f.write(sequence +'\n')
             #print(sequence)
       
    
    val = list(y.keys())
    for i in val:
        yy=y.copy()
        yy[i]-=1
        sequence = str(i)
        sub_fun(yy, sequence)
        
    
    f.close()








def ToList():
    f = open ('aux.txt','r')
    L = []
    for linea in f:        
        divided = linea.split("\t")
        divided =list( map(int, divided))
        L.append(divided)
    f.close()
    
    
    return L
    
    
    
    
def Duplicate(L):
    new= []
    #print("-"*10)
    #print(L)
    for i,l in enumerate(L):
        if  not( L[i][::-1] in L[i+1:]):
            new.append(L[i])
    return new
    
    
    
    
    
def Write(trees, w):
    for l in trees:
        l= list(map(str, l))
        s= '\t'.join(l)  
        w.write(s +'\n')
        
        
        




def Differentes_same_grades(n):
    f = open ("Trees_"+str(n)+'.txt','r')
    
    W = open ('Distint_Tree_'+str(n)+'.txt','w')
    
    g= 0
    t=0
    for linea in f:        
        divided = linea.split("\t")
        divided =list( map(int, divided[:-1]))
        
        permutations(divided)
        L = ToList()
        L = Duplicate(L)
        Write(L, W)
        g+=1
        t+=len(L)
    print("Distribuciones grado:\t",g,"Total: \t", t)
    f.close()
    W.close()
    

    
    
    

"""
if __name__ == "__main__":

    x= [1,1,1,4]
    permutations(x)
    L= ToList()

    Duplicate(L)
"""

