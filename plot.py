from cl import a
import sys
import pandas as pd

option = {}

def select_option(class_instance:a,option:int,options_dict:dict):
   
    attribute = options_dict[option]
    func = getattr(class_instance,attribute)
    func()
    input('press enter to continue')
    print()


    
def main():
    while True:
        try:
            global options
            years = int(input('Give a number of years for your income: '))
            instance = a(years)
            options = {index-25:func  for index,func in enumerate(dir(instance)) if not func.startswith('__') and not func.startswith('years')}  
            #print(options) 
            break 
        except ValueError:
            print('You must give a number')
    
   
    s = pd.Series(options)
    while True:

        print('These are you option!!!\n')
        print(s)

        try:
            option = int(input('Select a number of your options: '))
            select_option(instance,option,options)
            
        except ValueError:
            print('You must give a number')

    


if __name__=='__main__':
    main()

   
    
    
   
    
