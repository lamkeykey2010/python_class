#1
print("python")

#3
var = "Ernie"
print(var)

#5
q5 = "python"
print(q5[4])

#7
print(q5[-3])

#9
print(q5[0:3])

#11
print(q5[:2])

#13
print(q5[-3:-2])

#15
print(q5[2:-2])

#17
print(q5[:])

#19
print(q5.find("tho"))

#21
print(q5.find("oh"))

#23
q23 = "whippersnapper"
print(q23.rfind("pp"))

#25
q25 = "mississippi"
print(q25.find("ss"))

#27
q27 = "colonel"
print(q27.find("k"))

#31
q31 = "8 ball"
print(q31.lower())

#33
print(q31.upper())

#35
print(q5[3:len("python")])

#37
q37 = "the artist"
print(q37.title())

#39
q39 = "Grand Hotel"
print(len(q39[:6].rstrip()))

#41
q41 = "let it go"
print(q41.title().find('G'))

#43
q43 = "Amazon"
print(q43.lower().count('a'))

#45
q45 = "King Kong"
print(q45.title())

#47
a = 4
b = 6
c = "Municipality"
d = "pal"
print(len(c))
print(c.upper())
print(c[a:b] + c[b + 4:])
print(c.find(d))

#49
print("f" + "lute")

#51
print("your age is " + str(21) + ".")

#53
r = "A ROSE"
b = " IS "
print(r + b + r + b +r)

#55
var = "WALLA"
var += var
print(var)

#57
str1 = "good"
str1 += "bye"
print(str1)

#59
print('M' + ('m' * 6) + '.')

#61
print('a' + ( " " * 5 + 'b'))

#63
s = "trombones"
n = 76
print(n, s)

#65
num = input("Enter an integer: ")
print('1' + str(num))

#67
num = float(input("Enter a number: "))
print(1 + num)

#69
film = "the great gatsby".title()[:10].rstrip()
print(film, len(film))

#71
q71 = "Hello"
print(q71[:-1])

#73
q73 = "ABCDERTY"
print(q73[-8])

#75 # False

#77 # False

#79
phoneNumber = "234-5678" # Missing " " for the number
print("My phone number is " + phoneNumber)

#81
fore = "happily ever after" # for is a commend line which cannot be variable
print("They lived " + fore)

#83
print("Say it ain't so") # ain't " <--

#85
print("Python".upper()) ##upper need to be all small case

#87
age = "19"
print("Age: " + age) #must be str not int

#89
num = "1234" # need find in str not int
print(num.find('2'))

#91
language = "Python678" # python does not have 8 characters
print(language[8])

#97
n = float(input("Lightning and thunder = ")) #second per mile
stormDistance = n / 5
print(round(stormDistance, 2))

#100
Wattage = float(input("Enter wattage: "))
NumOfHoursUsed = float(input("Enter number of hours used: "))
PricePerkWhInCents = float(input("Enter price per kWh in cents: "))
costOfElectricity = (Wattage * NumOfHoursUsed) / (1000 * PricePerkWhInCents)
print("$", (round(costOfElectricity, 2)))

#102
ERS = float(input("Enter earning per share: "))
PPS = float(input("Enter price per share: "))
PPE = PPS / ERS
print("Price-to-Earning ratio: ", PPE)

#107
taxBracket = float(input("Enter tax bracket(as decimal): "))
MBIR = float(input("Enter municipal bond interest rate (as %): "))
CDIR = MBIR / (1 - taxBracket)
print("Equivalent CD interest rate:", round(CDIR, 3), "%")

#110
Sentence = input("Enter a sentence: ")
WTR = input("Enter word to replace: ")
Replacement = input("Enter replacement word: ")
print(Sentence.replace(WTR, Replacement))

#111
NOI = float(input("Enter Number of Inches"))
print






