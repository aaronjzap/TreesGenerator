
def permutations(x):
    s = list(set(x))
    if len(s)==1:
        return x
    con = [x.count(i) for i in s]
    y = dict(zip(s, con))
    
    
    f = open ('permutaciones.txt','w')
    f.close()
    f = open ('permutaciones.txt','a')
    
    
    
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
             print(sequence)
       
    
    val = list(y.keys())
    print(val)
    for i in val[:-1]:
        yy=y.copy()
        yy[i]-=1
        sequence = str(i)
        sub_fun(yy, sequence)
        
    
    f.close()







def Measure_calculation():
    
    f = open ('permutaciones.txt','r')

    L = []
    for linea in f:        
        divided = linea.split("\t")
        divided =list( map(int, divided))
        print(divided)
        L.append(divided)
        
        
    f.close()
    return L
    
    
def Duplicate(L):
    Bool= []
    for i,l in enumerate(L):
        if  not( L[i][::-1] in L[i:]):
            Bool.append(i)
    return Bool
    
    for i in Bool:
        l= L[i]
        l= list(map(str, l))
        print('\t'.join(l))    

if __name__ == "__main__":

    x= [1,1,1,4]
    permutations(x)
    L= Measure_calculation()
    print(len(L))
    Duplicate(L)
