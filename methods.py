import plot

@plot.dec
def compares_incomes_two_specific_months():
                first_year = Input('Give first year: ',0) 
                first_month = Input('Give first month: ',1)
                second_year = Input('Give second year: ',0)
                second_month = Input('Give second month: ',1) 
                return first_year,first_month,second_year,second_month


 
dict_methods = {
                'compare_incomes_two_specific_months':compares_incomes_two_specific_months
                }               