import random
def win(pcguess,userguess):
    return pcguess==userguess
def randomm_number(x,y):
    m=random.randint(x,y)
    return m
X=int(input("WRITE NUMBER FOR MIN-imum OF YOUR DOMAIN:"))
Y=int(input("WRITE NUMBER FOR MAX-imum OF YOUR DOMAIN:"))
usernumber=int(input(f"please write a number between {X} AND {Y} :"))
compguees=randomm_number(X,Y)
count=0
while (not win(compguees,usernumber)):
    if compguees > usernumber:
        Y=compguees
    else:
        X=compguees    
    count+=1
    compguees=randomm_number(X,Y)
print(f"i found your number in {count} and it is {compguees}")