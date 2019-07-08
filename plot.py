from cl import a,months
import sys
import pandas as pd

menu = None
years = None
instance = None
options = {}
functions_with_no_arguments = ['annual_total_incomes','monthly_total_incomes_for_each_year']

class month_exception(Exception):
    pass

class years_exception(Exception):
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
            except years_exception:
                print('sfdafads')
     return inner



@dec
def initial_incomes():
            global options,instance,years
            years = int(input('Give a number of years for your income: '))
            instance = a(years)
            options = {index-25:func  for index,func in enumerate(dir(instance)) if not func.startswith('__') and not func.startswith('years')  and not func.startswith('w_')}  


@dec
def Input(message:str,flag:int)-> int:
    if flag == 0:
        value = int(input(f'{message}'))
    elif flag == 1:
        value = input(f'{message}')
        if value not in months:
            raise month_exception()
    elif flag == 2:
        value = int(input(f'{message}'))
        if value > years:
            raise years_exception()
    return value






def exce(kwargs):
    args = []
    for key,value in kwargs.items():
        key = key.replace('_',' ')
        value = Input(key,value)
        args.append(value)
    return args


def select_raws_columns(option,dica,a):
    raws = []
    if a != 0:
        print('aaaa')
        number_of_years = Input('Give the number of years you want to see: ',2)
        for index,_ in enumerate([i for i in range(0,number_of_years)]):
            raws.append(Input(f'Give year {index+1}: ',2))
    columns = []
    number_of_months = Input('Give the number of months you want to see: ',0)
    for index,_ in enumerate([i for i in range(0,number_of_months)]):
        columns.append(Input(f'Give month {index+1}: ',1))
    if raws:
        dica[options[option]](raws,columns) 
        input('press enter to continue')
        print()
    else:
        dica[options[option]](columns)
        input('press enter to continue')
        print()

def excecute_option(instance_methods,option,**kwargs):
    args = exce(kwargs)
    instance_methods[options[option]]([argument for argument in args])
    input('press enter to continue')
    print()
        


@dec
def main(instance_methods,a):
    while True:
            print('These are you option!!!\n')
            print(menou)
            option = int(input('Select a number of your options: '))
                         
            if options[option] == 'compares_annual_incomes':
                excecute_option(instance_methods,option,Give_first_year_= 2,Give_second_year_= 2)
            elif options[option] == 'specific_month_income_for_specific_year': 
                excecute_option(instance_methods,option,Give_the_year_= 2,Give_the_month_= 1)
            elif options[option] == 'compare_incomes_two_specific_months':
                excecute_option(instance_methods,option,Give_first_year_=2,Give_first_month_=1,Give_second_year_=2,Give_second_month_=1)
            elif options[option] in functions_with_no_arguments: 
                instance_methods[options[option]]() 
                input('press enter to continue')
                print()
            elif options[option] == 'month_total_income_for_all_year':
                select_raws_columns(option,instance_methods,0)
            elif options[option] == 'incomes_specific_months_specific_years':
                select_raws_columns(option,instance_methods,1)





if __name__=='__main__':
    
    initial_incomes()
    menou = pd.Series(options)
    instance_methods = instance.class_methods()
    main(instance_methods,None)

   
    
    
   
    
