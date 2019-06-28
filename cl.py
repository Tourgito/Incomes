import random
import matplotlib.pyplot as plt
import pandas as pd
plt.close('all')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class a(object):

    def __init__(self,xronia:int):
        self.xronia = xronia
        self.eisodhmata = pd.DataFrame(self.eisodhmata_gen(), columns = [*months])

    
    def eisodhmata_gen(self):
      
        for _ in range(0,self.xronia):
            yield from self.ethsio_eisodhma()

    def ethsio_eisodhma(self): 

         lista = [] 
         for i in range(1,13):
            
             if i == 6 or i == 7 or i == 8:
                 lista.append(random.randint(3000,4000))
             else:
                 lista.append(random.randint(2000,3000))
         yield lista

    def sunoliko_ethsio_eisodhma(self):
      
        p = pd.DataFrame(self.eisodhmata.sum(axis=1),columns=['ethsio eisodhma'])
        print(p)


    def minhaia_eisodhmata(self):

       a = pd.DataFrame(self.eisodhmata.sum(), columns=['athroisthko eisodhma kathe mhna gia ola ta eth'])
       print(a)

    
    def gr(self):
        a = self.eisodhmata.cumsum()
        plt.figure()
        a.plot()

    def plot_etos(self,etos):
        ts = self.eisodhmata.iloc[etos]
        
        ts.plot()

        
