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
    if isinstance(principal, int) or isinstance(principal, float):
        return (str)(False)
    elif isinstance(interest_rate, float) or isinstance(interest_rate, int):
        return (str)(False)
    elif isinstance(years, int) or isinstance(years, float):
        return (str)(False)
    while i <= years:
        value = value + principal * (1 + interest_rate)
        i+=1
    return value

