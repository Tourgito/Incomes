from cl import a,months
import sys
import pandas as pd



option = {}

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



def select_option(class_instance:a,option:int,options_dict:dict):

    if (options_dict[option] == 'incomes'):
     print(class_instance.incomes)   
    else: 
        attribute = options_dict[option]
        func = getattr(class_instance,attribute)
        func()
        input('press enter to continue')
        print()


@dec
def gamhsou():
            global options
            years = int(input('Give a number of years for your income: '))
            instance = a(years)
            options = {index-25:func  for index,func in enumerate(dir(instance)) if not func.startswith('__') and not func.startswith('years')  and not func.startswith('w_')}  
            return instance

@dec
def Input(message:str,flag:int)-> int:
    if flag == 0:
        value = int(input(f'{message}'))
    else:
        print(type(months))
        value = input(f'{message}')
        if value not in months:
            raise month_exception()
    return value



def main():
    
    instance = gamhsou() 
    s = pd.Series(options)


    while True:

        print('These are you option!!!\n')
        print(s)

        try:
            option = int(input('Select a number of your options: '))
            
            if options[option] == 'compares_annual_incomes':
                first_year = Input('Give first year: ',0) 
                second_year = Input('Give second year: ',0)
                instance.compares_annual_incomes(first_year,second_year)
            elif options[option] == 'compare_incomes_two_specific_months':
                first_year = Input('Give first year: ',0) 
                first_month = Input('Give first month: ',1)
                second_year = Input('Give second year: ',0)
                second_month = Input('Give second month: ',1)
                #prpei na dinei mhna p.x 'January'
                instance.compare_incomes_two_specific_months(first_year,first_month,second_year,second_month)
            else: 
                select_option(instance,option,options)
            
        except ValueError:
            print('ffffff')
            print('You must give a number')

    
if __name__=='__main__':
 
    main()

   
    
    
   
    
