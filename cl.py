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



    def sunolika_ethsia_eisodhmata(self)-> 'emfanizei ta ethsia eisodhmata':
      
        p = pd.DataFrame(self.eisodhmata.sum(axis=1),columns=['ethsio eisodhma'])
        print(p)



    def sugrisei_ethsiwn_eisodhmatwn(self,year_first:int,year_second:int)-> 'sugrinei ta sunolika eisodhmata duo sugekrimenwn etwn':
        
        difference =  self.eisodhmata.iloc[year_first].sum() - self.eisodhmata.iloc[year_second].sum()
        if difference < 0:
            print(f'{year_second} more {difference}')
        elif difference > 0:
           print(f'{year_first} more {difference}')
        else:
            print('equal') 


    def minhaia_eisodhmata(self)-> 'emfanizei ta athroistika eisodhmata olwn twn mhnwn gia ola ta eth':

       a = pd.DataFrame(self.eisodhmata.sum(), columns=['athroisthko eisodhma kathe mhna gia ola ta eth'])
       print(a)



    def emfanisei_sugekrimenou_mhna_gia_ena_etos(self,etos:int,mhnas:str)-> 'emfanizei to eisodhma enos sugekrimenou mhna gia sugekrimeno etos':
        print(self.eisodhmata.at[etos,mhnas])


    def emfanisei_sugekrimenou_mhna_gia_ola_eth(self,*col)-> 'emfanizei to eisodhma enos sugekrimenou mhna gia ola ta eth':
     
        new = pd.DataFrame(self.eisodhmata.loc[:, [i for i in col]].sum(), columns={'Atrhoisma eisodhmatwn olwn twn etwn'})
        print(new)
        
        



    def sugrisei_mhnwn(self,year_first:int,month_first:str,year_second:int,month_second:str)-> 'sugrinei sugekrimena eisodhmata 2 mhnwn':
       
        difference =  self.eisodhmata.at[year_first,month_first] - self.eisodhmata.at[year_second,month_second]
       
        if difference < 0:
            print(f'{year_second}:{month_second} more {difference}')
        elif difference > 0:
           print(f'{year_first}:{month_first} more {difference}')
        else:
            print('equal')



    def emfanisei_sugekrimenwn_mhnwn_etwn(self,*columns_raws:tuple)-> 'emfanizei eisodhmata sugekrimenwn mhnwn gia sugekrimena eth':
      
        print(self.eisodhmata.loc[[i for i in columns_raws[0]], [i for i in columns_raws[1]]])
        
       
       
    
    def gr(self):
        a = self.eisodhmata.cumsum()
        plt.figure()
        a.plot()

    def plot_etos(self,etos):
        ts = self.eisodhmata.iloc[etos]
        
        ts.plot()

        
