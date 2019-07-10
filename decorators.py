
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
