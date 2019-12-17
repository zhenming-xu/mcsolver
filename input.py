import numpy as np
import Lattice as lat
import mcMain as mc
import matplotlib.pyplot as plt
## magnetic crystal part
LMatrix=[[1,0,0],
         [0,1,0],
         [0,0,1]]
# magnetic orbitals in fractional coordinates
pos=[[0,0,0]] 
# couplings   #source #target #edge  #J(meV) negative for FM coupling
bond1=lat.Bond(0,0,np.array([1,0,0]),-4.2,-3.8,-3.8, True)
bond2=lat.Bond(0,0,np.array([0,1,0]),-4.2,-3.8,-3.8, True)
bondList=[bond1,bond2]

mcslave=mc.MC(0,LMatrix,pos,[1.],bondList,T=1.0,Lx=128,Ly=128,Lz=1)
mcslave.mainLoopViaCLib_On(nsweep=8000,nthermal=4000,algo='Metroplis',flunc=0.0)
'''
TList=np.linspace(2.2,2.3,10)
U4_list=[]
for L in [16,32]:
    U4_L=[]
    for T in TList:
        mcslave=mc.MC(0,LMatrix,pos,bondList,T,L,L,1)
        mData, eData=np.array(mcslave.mainLoopViaCLib(nsweep=40000,nthermal=20000,algo='Wolff'))
        U4_L.append(np.mean(mData*mData)**2/np.mean(mData**4))
    U4_list.append(U4_L)
    
plt.plot(TList,U4_list[0])
plt.plot(TList,U4_list[1])
plt.show()
'''