import math

def suma(a1, b1, a2, b2):
    return f"Result: {a1 + a2} + {b1 + b2}i"

def resta(a1, b1, a2, b2):
    return f"Result: {a1 - a2} + {b1 - b2}i"

def multi(a1, b1, a2, b2):
    return f"{a1*a2 - b1*b2} + {a1*b2 + a2*b1}i"

def div(a1, b1, a2, b2):
    return f"{(a1*a2 + b1*b2)/(a2**2 + b2**2)} + {(a2*b1 - a1*b2)/(a2**2 + b2**2)}i"

def arg(a1, b1):

    if a1 == 0 and b1 == 0:
        return -1

    elif b1 == 0:
        if a1 > 0:
            return 0
        else:
            return math.pi

    elif a1 == 0:
        if b1 > 0:
            return math.pi/2
        else:
            return -math.pi/2

    elif a1 > 0:
        return (math.atan(b1/a1))

    elif b1 > 0:
        return (math.pi + math.atan(b1/a1))
    else:
        return (-(math.pi) + math.atan(b1/a1))


def modulo(a1, b1):
    return (((a1**2) + (b1**2))**(1/2))

def raiz(a1, b1):
    raiz = int(input("Which root do you want? "))
    mod = modulo(a1, b1)
    argu = arg(a1, b1)
    r = mod**(1/raiz)
    for k in range(0, raiz):
        teta = (argu + (2*k*math.pi))/raiz
        b = r*math.sin(teta)
        a = r*math.cos(teta)
        print(f"{a} + {b}i")

def potencia(a1, b1):
    potencia = int(input("What power do you want? "))
    mod = modulo(a1, b1)
    argu = arg(a1, b1)
    r = mod**potencia
    teta = (argu*mod + argu*mod)
    a = r*(math.cos(teta))
    b = r*(math.sin(teta))
    return f"{a} + {b}i"

def inverso(a1, b1):
    return f"{a1/(a1**2 + b1**2)} - {b1/(a1**2 + b1**2)}i"


operacion = input("What operation would you like? (+,-,*,/,modulus,argument,root,power,inverse) ")

a1 = float(input("Enter the real part 1: "))
b1 = float(input("Enter the imaginary part 1: "))
print(f"Your complex number is {a1} + {b1}i\n")

if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/":
    a2 = float(input("Enter the real part 2: "))
    b2 = float(input("Enter the imaginary part 2: "))
    print(f"Your second complex number is {a2} + {b2}i\n")
    if operacion == "+":
        print(suma(a1, b1, a2, b2))
    elif operacion == "-":
        print(resta(a1, b1, a2, b2))
    elif operacion == "*":
        print(multi(a1, b1, a2, b2))
    elif operacion == "/":
        print(div(a1, b1, a2, b2))

elif operacion == "argument":
    print(arg(a1, b1))
elif operacion == "modulus":
    print(modulo(a1, b1))
elif operacion == "power":
    print(potencia(a1, b1))
elif operacion == "root":
    raiz(a1, b1)
elif operacion == "inverse":
    print(inverso(a1, b1))
else:
    print("Error")

