import random
import matplotlib.pyplot as plt
import pandas as pd
plt.close('all')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
not_show_in_menu = ['plot_etos','gr', 'annual_income', 'incomes_gen', 'years', 'class_methods']

class revenue(object):

    def __init__(self,years:int):
       
        self.years = [i+1 for i in range(0,years)]
        self.incomes = pd.DataFrame(self.incomes_gen(), columns = [*months], index=[*self.years])

   
    
    def incomes_gen(self)->list:
      
        for _ in self.years:
            yield from self.annual_income()

    def annual_income(self)->list: 

         lista = [] 
         for i in range(1,13):
            
             if i == 6 or i == 7 or i == 8:
                 lista.append(random.randint(3000,4000))
             else:
                 lista.append(random.randint(2000,3000))
         yield lista


    #Shows annual revenue for each year
    def annual_total_incomes(self):
      
        Years_revenues = pd.DataFrame(self.incomes.sum(axis=1),columns=['Year revenue'])
        print(Years_revenues)



    #Compares revenues of two specific years
    #args[0] is the first year and args[1] the second
    def compares_annual_incomes(self,args:list):

        print()
        print(f' The annual income for year {args[0]} is {self.incomes.loc[args[0]].sum()}')
        print(f' The annual income for year {args[1]} is {self.incomes.loc[args[1]].sum()}')
        difference =  self.incomes.loc[args[0]].sum() - self.incomes.loc[args[1]].sum()
        if difference < 0:
            difference = abs(difference) 
            print(f'\nThe income of year {args[1]}  is bigger  by {difference}')
        elif difference > 0:
           print(f'\nThe income of year {args[1]}  is bigger by {difference}')
        else:
            print('\nThe incomes of both years are equal') 


    
    #Show annual revenue for all months for all years
    def monthly_total_incomes_for_each_year(self):

       Months_revenue = pd.DataFrame(self.incomes.sum(), columns=['Month revenue'])
       print(Months_revenue)


    #Show revenue for specific month and year
    #args[0] is the year and args[1] the month
    def specific_month_income_for_specific_year(self,args:list):

        print(pd.Series(self.incomes.at[args[0],args[1]], index=[args[1]]))


    #Show the revenue for specific months for all years
    #col:list has the months
    def month_total_income_for_all_year(self,col:list):

        Months_revenue = pd.DataFrame(self.incomes.loc[:, [i for i in col]].sum(), columns={'Month revenue'})
        print(Months_revenue)
        
        


    #Compare revenue of two specific months each for specific year
    #args[0] is the year of first revenue, args[1] is the month of first revenue
    #args[2] is the year of second revenue, args[3] is the month of second revenue
    def compare_incomes_two_specific_months(self,args:list):
       
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
    

    #return a list with excecutable function of the class
    def class_methods(self)->list:

        excecutable_lista = {
                'incomes_specific_months_specific_years' : self.incomes_specific_months_specific_years,
                'annual_total_incomes': self.annual_total_incomes,
                'compare_incomes_two_specific_months' : self.compare_incomes_two_specific_months ,

                'month_total_income_for_all_year' : self.month_total_income_for_all_year,

                'specific_month_income_for_specific_year' : self.specific_month_income_for_specific_year,
                'compares_annual_incomes' : self.compares_annual_incomes,
                'monthly_total_incomes_for_each_year': self.monthly_total_incomes_for_each_year,
                'incomes' : self.incomes
                }

        return excecutable_lista
