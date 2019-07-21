from Exceptions import month_exception,years_exception

#raise errors when user input is wrong
def Exception_Decorator(func):

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
                print('You must give a number equal or less than the numbers of year for your income that you gave at the beginning')
     return inner
