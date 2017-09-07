#get numeric expression without the pc, and use python check the answer#
q1 = 3 *4
print(q1)

q3 = 1 / (2 ** 3)
print(q3)

q5 = (5 - 3) * 4
print(q5)

q7 = 7 // 3
print(q7)

q9 = 7 % 3
print(q9)

q11 = 5 // 5
print(q11)

#determine whether the name is a valid variable name#

##q13 sales.2008  #not valid since it has.2008#

#q15  fOrM_1040# # valid#
fOrM_1040 = 5
print(fOrM_1040)

#q17 expenses? # not valid because it has ? at the end

# q19-23  set a=2, b=3, c=4 and evaluate those formula
a = 2
b = 3
c = 4
q19 = (a * b) + c
print(q19)

q21 = (1 + b) * c
print(q21)

q23 = b ** (c - a)
print(q23)

#write lines of code to calculate and display value

q25 = 7 * 8 +5
print(q25)

q27 = 20 * 0.055
print(q27)

q29 = 17 * (3 + 162)
print(q29)

#Q31 complete the table
x = 2
print("x=", x)
y = 3 * x
print("x=", x, "y=", y)
x = y + 5
print("x=", x, "y=", y)
print("x=", x + 4, "y=", y)
y = y + 1
print("x=", x,"y=", y)

#Q33-38 determine the output displayed by the lines of code
#q33
a = 4
b = 5 * a
print("Q33 = ", a + b)

#q35
num =5
num *= 2
print("num=", num)

#q37
totalMinutes = 135
hours = totalMinutes // 60
minutes = totalMinutes % 60
print("hours=", hours, "minutes=", minutes)

#39-41 identify the errors
a = 2
b = 3
c = a + b  #errors was a + b = c, the varible should put at first place
print(b)

interest = 0.05 #book shows 0.05 = interest, error same as q39
balance = 800
print(interest * balance)

#fuind the value of function
q43 = int(10.75)
print("q43=", q43)

q45 = abs(3 - 10)
print("q45=", q45)

q47 = round(3.1279, 3)
print("q47=", q47)

#find the value of function where a = 5, b = 3
a = 5
b = 3
print("q49=", int(-a / 2))
print("q51=", abs(a - 5))
print("q53=", round(a + .5))

#rewrite the statement using augmented assignment operation
#q55. cost = cost + 5
#cost += 5

#q57, cost = cost / 6
#cost /= 6

#q59, sum = sum % 2
#sum %= 2

#61
revenue = 98456
costs = 45000
profit = revenue - costs
print("q61.profit = ", profit)

#63
price = 19.95
discountPercent = 30
markdown = 1 - (discountPercent / 100)
price = price * markdown
print("q63.price=", round(price, 2))

#64
fixedCost = 5000
pricePerUnit = 8
costPerUnit = 6
breakEvenPoint = fixedCost / (pricePerUnit - costPerUnit)
print("BreakEvenPoint = ", breakEvenPoint)

#68
purchasePrice = 10
sellingPirce = 15
percentProfit = (100 * (sellingPirce - purchasePrice)/ purchasePrice)
print("percentProfit = ", percentProfit, "%")

#72 find the MPG
GasMileage = 23695 - 23352
filledGas = 14
MPG = GasMileage / filledGas
print("MPG = ", MPG)

#73
waterUsage = 1600 #in gallon
USPopulation = 315000000
yearWaterUsage = ((USPopulation * waterUsage) * 365)
print("yearlyWaterUsage=", yearWaterUsage)

#77
USNationalDebt = 1.68 * (10 ** 13)
USPopulation = 3.1588 * (10 ** 8)
PerCapitalUSNationalDebt = round(USNationalDebt / USPopulation, 0)
print("PerCapitalUSNationalDebt= ", PerCapitalUSNationalDebt)

#78
caloriePerCubicfoot = 48600
feetToMile = 5280
oneCubicMileIceCream = caloriePerCubicfoot * feetToMile * feetToMile * feetToMile
print("oneCubicMileIceCream = ", oneCubicMileIceCream)









