
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




def Rename_files(n):
    EnergyT ='EnergiaT_'+str(n)+'.csv'
    EnergyV ='EnergiaV_'+str(n)+'.csv'
    Degree  ='Grados_'+str(n)+'.csv'
    Close   ='Cercania_'+str(n)+'.csv'
    Bet     ='Entre_'+str(n)+'.csv'
    Eigen   ='Eigen_'+str(n)+'.csv'
    return EnergyT, EnergyV,  Degree, Close, Bet, Eigen 
    
    

def Correlations(n):
    def Read(name):
        data = pd.read_csv(name, header=0)
        #data= pd.to_numeric(data, downcast='integer')
        data.astype(float)
        return data
    def One_one(name_X, name_Y):
        X= Read(name_X)
        Y= Read(name_Y)
        X = X.to_numpy()
        Y = Y.to_numpy()
        return [np.corrcoef(x,y)[0][1] for x, y in zip(X,Y)]
            
        
    EnergyT, EnergyV,  Degree, Close, Bet, Eigen = Rename_files(n)  
    EV_Deg =One_one(EnergyV, Degree)
    EV_Cl  =One_one(EnergyV, Close)
    EV_Be  =One_one(EnergyV, Bet)
    EV_Ei  =One_one(EnergyV, Eigen)
    
    Draw_correlations([EV_Deg,EV_Cl, EV_Be, EV_Ei ], n)
    ET= Read(EnergyT)
    ET = ET.to_numpy()
    Order_by(ET)
   
def Order_by(Val):
    import itertools
    print(Val)
    Val= list(itertools.chain(*Val))
    V= list(zip(Val, range(0,len(Val))))
    c =list(np.array(V)[:,1])
    return c[::-1]
    
def Draw_correlations(Lista, n):
    plt.grid(color='silver', linestyle='-', linewidth=1)
    X=list(range(len(Lista[0])))
    print(len(X),Lista[0])
    plt.plot(X, Lista[0], label="$\delta$", linewidth=8)
    plt.plot(X, Lista[1],label= "$C_{clo}$", linewidth=8)
    plt.plot(X, Lista[2], label="$C_{bet}$", linewidth=8)
    plt.plot(X,Lista[3], label="$C_{eig}$", linewidth=8)

    plt.rc('legend',fontsize=25)
    plt.xlabel("Number of vertices ($n$)",size=25)
    plt.ylabel("Correlation",size=25)
    plt.legend()
    plt.show()
    
    
    
    
if __name__ == "__main__":

    n = 15
    Correlations(n)
