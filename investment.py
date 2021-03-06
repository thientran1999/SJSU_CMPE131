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
    value = 0.0
    for i in range(years+1):
        value += principal(1+interest_rate)
    if isinstance(value, float):
        print(value)
    else:
        print("False")

