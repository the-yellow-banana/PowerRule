equ = (input("enter your equation to find the derivative:")).lower()
p=[]
s=""
def find_derivative (equ):
    terms = list(equ.split("+"))
    for term in terms:
        if "x" in term:
            if "^" in term:
                poop = term.split("^")
                power = poop[1]
                new_power = int(power)-1
                coef = poop[0].split("x", -1)[0]
                coef = int(s.join(coef))
                coef = coef*(int(power))
                print(str(coef) + "x^" + str(new_power))
            elif "^" not in term:
                print(term.split("x",1)[0])


        #print(str(coef) + "x^" + str(new_power))
find_derivative(equ)
