equ = (input("enter your equation to find the derivative:")).lower()
s=""
d=[]
def find_derivative (equ):
    terms = list(equ.split("+"))
    for term in terms:
        if "x" in term:
            if "^" in term:
                stuff_in_term = term.split("^")
                power = stuff_in_term[1]
                new_power = float(power)-1
                coef = stuff_in_term[0].split("x", -1)[0]
                coef = float(s.join(coef))
                coef = coef*(float(power))
                d.append(str(coef) + "x^" + str(new_power))
            elif "^" not in term:
                d.append(term.split("x", 1)[0])
    print(d)

find_derivative(equ)
