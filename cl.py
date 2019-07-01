import random
import matplotlib.pyplot as plt
import pandas as pd
plt.close('all')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class a(object):

    def __init__(self,years:int):
       
        self.years = years
        self.incomes = pd.DataFrame(self.incomes_gen(), columns = [*months])

    
    def incomes_gen(self):
      
        for _ in range(0,self.years):
            yield from self.annual_income()

    def annual_income(self): 

         lista = [] 
         for i in range(1,13):
            
             if i == 6 or i == 7 or i == 8:
                 lista.append(random.randint(3000,4000))
             else:
                 lista.append(random.randint(2000,3000))
         yield lista



    def annual_total_incomes(self)-> 'emfanizei ta ethsia eisodhmata':
      
        p = pd.DataFrame(self.incomes.sum(axis=1),columns=['ethsio eisodhma'])
        print(p)



    def compares_annnual_incomes(self,year_first:int,year_second:int)-> 'sugrinei ta sunolika eisodhmata duo sugekrimenwn etwn':
        
        difference =  self.incomes.iloc[year_first].sum() - self.incomes.iloc[year_second].sum()
        if difference < 0:
            print(f'{year_second} more {difference}')
        elif difference > 0:
           print(f'{year_first} more {difference}')
        else:
            print('equal') 


    def monthly_total_incomes_for_each_month(self)-> 'emfanizei ta athroistika eisodhmata olwn twn mhnwn gia ola ta eth':

       a = pd.DataFrame(self.incomes.sum(), columns=['athroisthko eisodhma kathe mhna gia ola ta eth'])
       print(a)



    def specific_month_income_for_specifc_year(self,year:int,month:str)-> 'emfanizei to eisodhma enos sugekrimenou mhna gia sugekrimeno etos':
        print(self.incomes.at[year,month])


    def month_total_income_for_all_year(self,*col)-> 'emfanizei to eisodhma enos sugekrimenou mhna gia ola ta eth':
     
        new = pd.DataFrame(self.incomes.loc[:, [i for i in col]].sum(), columns={'Atrhoisma eisodhmatwn olwn twn etwn'})
        print(new)
        
        



    def compare_incomes_two_specific_months(self,year_first:int,month_first:str,year_second:int,month_second:str)-> 'sugrinei sugekrimena eisodhmata 2 mhnwn':
       
        difference =  self.incomes.at[year_first,month_first] - self.incomes.at[year_second,month_second]
       
        if difference < 0:
            print(f'{year_second}:{month_second} more {difference}')
        elif difference > 0:
           print(f'{year_first}:{month_first} more {difference}')
        else:
            print('equal')



    def incomes_specific_mothns_speific_years(self,*columns_raws:tuple)-> 'emfanizei eisodhmata sugekrimenwn mhnwn gia sugekrimena eth':
      
        print(self.incomes.loc[[i for i in columns_raws[0]], [i for i in columns_raws[1]]])
        
       
       
    
    def gr(self):
        a = self.incomes.cumsum()
        plt.figure()
        a.plot()

    def plot_etos(self,etos):
        ts = self.incomes.iloc[etos]
        
        ts.plot()

        
