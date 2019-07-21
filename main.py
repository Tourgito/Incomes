from cl import revenue,months,not_show_in_menu
import sys
import pandas as pd
from Exceptions import month_exception,years_exception 
from decorators import Exception_Decorator

menu = None
years = None
instance = None
options = {}
functions_with_no_arguments = ['annual_total_incomes','monthly_total_incomes_for_each_year']




#create user income 
@Exception_Decorator
def initial_incomes():
            global options,instance,years
            years = int(input('Give a number of years for your income: '))
            instance = revenue(years)
            options = [func for func in (dir(instance)) if not func.startswith('__') and func not in not_show_in_menu] # a list with user choices 



#validate user input
@Exception_Decorator
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





#create the arguments for user choice 
def validate_sys_input(kwargs:dict)->list:
    args = []
    for key,value in kwargs.items():
        key = key.replace('_',' ')
        validated_input = Input(key,value)
        args.append(validated_input)
    return args


#excecute a range of users available choices and show the results
def select_raws_columns(option:int,instance_methods:list,selector:int):
    raws = []
    if selector != 0:
        number_of_years = Input('Give the number of years you want to see: ',2)
        for index,_ in enumerate([i for i in range(0,number_of_years)]):
            raws.append(Input(f'Give year {index+1}: ',2))
    columns = []
    number_of_months = Input('Give the number of months you want to see: ',0)
    for index,_ in enumerate([i for i in range(0,number_of_months)]):
        columns.append(Input(f'Give month {index+1}: ',1))
    if raws:
        instance_method[options[option]](raws,columns) 
        input('press enter to continue')
        print()
    else:
        instanece_method[options[option]](columns)
        input('press enter to continue')
        print()



#excecute a range of users available choices and show the results
def excecute_option(instance_methods:list,option:int,**kwargs:dict):
    args = validate_sys_input(kwargs) 
    instance_methods[options[option]]([argument for argument in args]) #excecute user choice
    input('press enter to continue')
    print()
        




#takes users choice and run the appropriate function
@Exception_Decorator
def select_option(instance_methods:list,none:None):
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
    instance_methods = instance.class_methods() # a list with excecutable function from revenue object 
    select_option(instance_methods,None)

   
    
    
   
    
