import math
#Opening screen to feature the following
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

#User to select one of Investment or Bond to proceed
investment_calculation = input("Enter either Investment or Bond from the menu above to proceed:")

#One of the three format to be used for investment to be calculated
if investment_calculation == "Investment" or  investment_calculation == "INVESTMENT" or investment_calculation == "investment":
    P = int(input("Deposit:"))
    r = int(input("Interest rate:"))
    t = int(input("Number of years:"))
    interest = input("Simple or Compound Interest:") #User to select to calculate one of the two options
    if interest == "Simple":
        interest_simple = print(P*(1 + ((r/100)*t)))
    elif interest == "Compound":
        interest_compound = print((P*(1 + (r/100)),t))

#One of the three formats to be used for bond repayments to be calculated
elif investment_calculation == "Bond" or investment_calculation == "BOND" or investment_calculation == "bond":
    P = int(input("Present Value:"))
    i = int(input("Interest rate:"))
    n = int(input("Number of months:"))
    bond_repayment = print((((i/100)/12) * P)/(1 - (1 + (i/100)/12)**(-n)))

else:
    print("Sorry! Please enter correct option from above menu:")