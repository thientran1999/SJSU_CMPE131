"""
Calculate the money can earn on an investment
Parameter
principal: int
	the amount of money to starting invest
interest_rate: float
	the rate per year
years: int
	the times that money put in invest
Return
value: float
	the total money after the years that put in invest 
"""
def calculate_apr(principal, interest_rate, years):
    i = 1
    value = 0.0
    while i <= years:
        value = value + principal * (1 + interest_rate)
        i+=1
    principal =(str)(principal)
    interest_rate = (str)(interest_rate)
    years = (str)(years)
    if principal.isdigit()== False:
        return (str)(False)
    elif interest_rate.isdigit()== False: 
        return (str)(False)
    elif year.isdigit() == False: 
        return (str)(False)
    else:
        return (float)(value)

