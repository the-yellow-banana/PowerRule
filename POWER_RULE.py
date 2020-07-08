equ = (input("enter your equation to find the derivative:")).lower()
s=""
def find_derivative (equ):
    terms = list(equ.split("+"))
    for term in terms:
        if "x" in term:
            if "^" in term:
                poop = term.split("^")
                power = poop[1]
                new_power = float(power)-1
                coef = poop[0].split("x", -1)[0]
                coef = float(s.join(coef))
                coef = coef*(float(power))
                print(str(coef) + "x^" + str(new_power))
            elif "^" not in term:
                print(term.split("x",1)[0])


find_derivative(equ)
