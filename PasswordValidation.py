def ValidatePassword(Pass):
    NextChar = chr
    LC = int
    UC = int
    Num = int
    SC = int

    LC = 0
    UC = 0
    Num = 0
    SC = 0

    for NextChar in (Pass):
        if (NextChar >="a") and (NextChar <="z"):
            LC = LC + 1
        elif(NextChar >="A") and (NextChar <="Z"):
            UC = UC + 1
        elif(NextChar >="0") and (NextChar <="9"):
            Num = Num + 1
        else:
            SC = SC + 1

    if (LC >=2) and (UC >=2) and (Num >=3) and (SC==0):
        return True
    else:
        return False
    

Pass = str
valid = bool

Pass = (input("Enter your password: "))

Valid = ValidatePassword(Pass)

if (Valid == True):
    print ("Your Password is Valid")
else:
    print ("Your Password is Invalid")
