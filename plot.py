from cl import a,months
import sys
import pandas as pd


instance = None
option = {}
functions_with_no_arguments = ['annual_total_incomes','monthly_total_incomes_for_each_year']

class month_exception(Exception):
    pass

def dec(func):

     def inner(*args):
        while True:
            try:
                if not args:
                    
                    return func()
                else:
                    return func(args[0],args[1])
            except ValueError:
                print('You must give a number')
            except month_exception:
                print('You must give a Month and the first letter must be upper')
     return inner



def excecute_class_func(class_instance:a,option:int,options_dict:dict,number_of_arguments,*args):

    if (options_dict[option] == 'incomes'):
     print(class_instance.incomes)   
    
    if number_of_arguments == 2:
   
        attribute = options_dict[option]
        func = getattr(class_instance,attribute)
        func(args[0],args[1])
        input('press enter to continue')
        print()
    elif number_of_arguments == 4:
       

        attribute = options_dict[option]
        func = getattr(class_instance,attribute)
        func(args[0],args[1],args[2],args[3])
        input('press enter to continue')
        print()
    elif number_of_arguments == 0: 
        attribute = options_dict[option]
        func = getattr(class_instance,attribute)
        func()
        input('press enter to continue')
        print()
    elif  number_of_arguments == 1:   
        attribute = options_dict[option]
        func = getattr(class_instance,attribute)
        func(args[0])
        input('press enter to continue')
        print()

@dec
def gamhsou():
            global options,instance
            years = int(input('Give a number of years for your income: '))
            instance = a(years)
            options = {index-25:func  for index,func in enumerate(dir(instance)) if not func.startswith('__') and not func.startswith('years')  and not func.startswith('w_')}  

            return instance

@dec
def Input(message:str,flag:int)-> int:
    if flag == 0:
        value = int(input(f'{message}'))
    else:
        
        value = input(f'{message}')
        if value not in months:
            raise month_exception()
    return value

def excecute_option(option,u,**kwargs):
    
    lista = []
    for key,value in kwargs.items():
        key = key.replace('_',' ')
        value = Input(key,value)
        lista.append(value)

    if len(lista) == 2:    
        excecute_class_func(instance,option,options,u,lista[0],lista[1])    
    if len(lista) == 4:
        excecute_class_func(instance,option,options,u,lista[0],lista[1],lista[2],lista[3])    
    if len(lista) == 1:
                columns = []
                number_of_months = Input('Give the number of months you want to see: ',0)
                for index,_ in enumerate([i for i in range(0,number_of_months)]):
                    columns.append(Input(f'Give month {index+1}: ',1))
                excecute_class_func(instance,option,options,1,columns)    


def main():
    
    instance = gamhsou() 
    s = pd.Series(options)


    while True:

        print('These are you option!!!\n')
        print(s)

        try:
            option = int(input('Select a number of your options: '))
            
            if options[option] == 'compares_annual_incomes':
                excecute_option(option,2,Give_first_year_= 0,Give_second_year_= 0)
            elif options[option] == 'specific_month_income_for_specific_year': 
                excecute_option(option,2,Give_the_year_= 0,Give_the_month_= 1)
            elif options[option] == 'compare_incomes_two_specific_months':
                excecute_option(option,4,Give_first_year_=0,Give_first_month_=1,Give_second_year_=0,Give_second_month_=1)
            elif options[option] in functions_with_no_arguments: 
                select_option(instance,option,options,0,None)
            elif options[option] == 'month_total_income_for_all_year':
                columns = []
                number_of_months = Input('Give the number of months you want to see: ',0)
                for index,_ in enumerate([i for i in range(0,number_of_months)]):
                    columns.append(Input(f'Give month {index+1}: ',1))
                excecute_class_func(instance,option,options,1,columns)    
            elif options[option] == 'incomes_specific_months_specific_years':
                year_counter = 1
                month_counter = 1
                columns = []
                raws = []
                number_of_months = Input('how many month',0)
                number_of_years = Input('how many years',0)
                for _ in range(0,number_of_years):
                    raws.append(Input(f'Give {year_counter} year',0))
                    year_counter += 1
                for _ in range(0,number_of_months):
                    columns.append(Input(f'Give {month_counter} month',1))
                    month_counter += 1
                select_option(instance,option,options,2,raws,columns)    
        except ValueError:
            print('ffffff')
            print('You must give a number')





if __name__=='__main__':
    main()

   
    
    
   
    
