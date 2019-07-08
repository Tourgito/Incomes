import random
import matplotlib.pyplot as plt
import pandas as pd
plt.close('all')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


class a(object):

    def __init__(self,years:int):
       
        self.years = [i+1 for i in range(0,years)]
        self.incomes = pd.DataFrame(self.w_incomes_gen(), columns = [*months], index=[*self.years])

   
    
    def w_incomes_gen(self):
      
        for _ in self.years:
            yield from self.w_annual_income()

    def w_annual_income(self): 

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


    def compares_annual_incomes(self,args:list)-> 'sugrinei ta sunolika eisodhmata duo sugekrimenwn etwn':
        print(self.incomes.loc[[args[0],args[1]]])
        difference =  self.incomes.iloc[args[0]].sum() - self.incomes.iloc[args[1]].sum()
        if difference < 0:
            difference = abs(difference) 
            print(f'\nThe income of year {args[1]}  is bigger  by {difference}')
        elif difference > 0:
           print(f'\nThe income of year {args[1]}  is bigger by {difference}')
        else:
            print('\nThe incomes of both years are equal') 


    def monthly_total_incomes_for_each_year(self)-> 'emfanizei ta athroistika eisodhmata olwn twn mhnwn gia ola ta eth':

       a = pd.DataFrame(self.incomes.sum(), columns=['athroisthko eisodhma kathe mhna gia ola ta eth'])
       print(a)



    def specific_month_income_for_specific_year(self,args:list)-> 'emfanizei to eisodhma enos sugekrimenou mhna gia sugekrimeno etos':
        print(pd.Series(self.incomes.at[args[0],args[1]], index=[args[1]]))


    def month_total_income_for_all_year(self,col:list)-> 'emfanizei to eisodhma enos sugekrimenou mhna gia ola ta eth':

        new = pd.DataFrame(self.incomes.loc[:, [i for i in col]].sum(), columns={'Atrhoisma eisodhmatwn olwn twn etwn'})
        print(new)
        
        



    def compare_incomes_two_specific_months(self,args:list)-> 'sugrinei sugekrimena eisodhmata 2 mhnwn':
       
        difference =  self.incomes.at[args[0],args[1]] - self.incomes.at[args[2],args[3]]
        lista = [self.incomes.at[args[0],args[1]],self.incomes.at[args[2],args[3]]]
        serie = pd.Series(lista, index = [args[1],args[3]])
        print(f'{serie}\n')
       
        if difference < 0:
            difference = abs(difference)
            print(f'{args[2]}:{args[3]} more {difference}')
        elif difference > 0:
           print(f'{args[0]}:{args[1]} more {difference}')
        else:
            print('equal')



    def incomes_specific_months_specific_years(self,raws:list,columns:list)-> 'emfanizei eisodhmata sugekrimenwn mhnwn gia sugekrimena eth':

        print(self.incomes.loc[[i for i in raws], [i for i in columns]])
        
       
       
    
    def gr(self):
        a = self.incomes.cumsum()
        plt.figure()
        a.plot()

    def plot_etos(self,etos):
        ts = self.incomes.iloc[etos]
        
        ts.plot()

    def class_methods(self):
        lista = {
                'incomes_specific_months_specific_years' : self.incomes_specific_months_specific_years,
                'annual_total_incomes': self.annual_total_incomes,
                'compare_incomes_two_specific_months' : self.compare_incomes_two_specific_months ,

                'month_total_income_for_all_year' : self.month_total_income_for_all_year,

                'specific_month_income_for_specific_year' : self.specific_month_income_for_specific_year,
                'compares_annual_incomes' : self.compares_annual_incomes,
                'monthly_total_incomes_for_each_year': self.monthly_total_incomes_for_each_year
                }

        return lista
