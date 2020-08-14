##import needed libraries
import numpy as np
import matplotlib.pyplot as plt

#empty string and list used to be added to further into the program
s=""
d=[]
##derivative function only usefull for polynomials to de derived
def find_derivative ():
    ##get user input
    global equ
    equ = (input("enter your equation to find the derivative:")).lower()
    terms = list(equ.split("+"))
    ##logic for power rule
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
    derivative = ('+'.join(d))
    print("the derivative is " + derivative)



def graph_equations():
    ##make input equations graphable
    new_d = [w.replace('^', '**') for w in d]
    new_d = [w.replace('x', '*x') for w in new_d]
    new_d = ("+".join(new_d))

    new_equ = [w.replace('^', '**') for w in equ]
    new_equ = [w.replace('x', '*x') for w in new_equ]
    new_equ = ("".join(new_equ))

    # plot the derivative

    x = np.linspace(-5, 5, 100)
    y = eval(new_d)

    old_y = eval(new_equ)

    #plot jargin to make it look pretty
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    if 'x' not in new_d:
        plt.plot(x, old_y, 'b', label=' Original Equation')
        plt.grid()
        plt.hlines(new_d, -50, 50,'r', label= 'Derivative')
        plt.legend(loc='upper left')
        plt.show()
        return

    else:
        plt.grid()

        plt.plot(x, y, 'r', label='Derivative')
        plt.plot(x, old_y, 'b', label=' Original Equation')
        plt.legend(loc='upper left')
        plt.show()
        return

if __name__ == "__main__":
    find_derivative()
    graph_equations()
