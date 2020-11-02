#calc running average
usernumber=1
usernumber2=1
while usernumber != '0':
    usernumber2 = usernumber
    usernumber = int(input('new number? '))
    print((usernumber + usernumber2)/2)