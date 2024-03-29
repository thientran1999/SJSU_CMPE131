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
    if years == 0:
        return principal
    elif not principal:
        return False
    elif not interest_rate or interest_rate < 0:
        return False
    elif not years:
        return False
    while i<=years:
        value = value + principal*(1+interest_rate)
        i+=1
    return value

