import math
import random
import re

"""
basically 3 types of eqns

normal
Implicit (just do with y)
Parametric (just do with t, usually simpler than normal)


THINGS I CAN THINK ABOUT
fractions with complicated numerators, denominators can be easier - top part can be of 2 factors 

"""

def weighted_int_list(max, min = 1):
    integer_list = []
    for i in range(min, max + 1):
        integer_list += [i] * i

    return integer_list

def weighted_int_list_square(max, min = 1):
    integer_list = []
    for i in range(min, max + 1):
        integer_list += [i] * i * i

    return integer_list

def chance_list(element, percentageChance = 10):
    percentageChance = int(percentageChance)
    return [element] * percentageChance + [''] * ( 100 - percentageChance )

def fix(tofix):
    return (
        fix_spacing(
        fix_duplicatesums(
        tofix
        ))
    )

def fix_duplicatesums(tofix):
    while True:
        if re.search(r'- -|\+ -|- \+', tofix) == None:
            break

        tofix = re.sub(r'- -|\+ -|- \+', r'-', tofix)

    while True:
        if re.search(r'\+ \+', tofix) == None:
            break

        tofix = re.sub(r'\+ \+', r'\+', tofix)

    return tofix

def fix_spacing(tofix):
    while True:
        if re.search(r' [-\+]\S', tofix) == None:
            break

        tofix = re.sub(r' ([-\+])(?=\S)', r' \1 ', tofix)

    return tofix

def create_polynomial(maxIndex, randomLength = False, maxInteger = 5, elementNumber = 0, variable = "x", pi = False):

    def element_in_polynomial(constant, index, variable = "x"):
        if type(constant) == "str":
            constant = re.sub(r'1((?=\w))',r'\1',constant) #replaces 1pi with pi etc

        if constant == "1":
            constant = ""
        elif constant == "-1":
            constant = "-"

        if index == 0:
            return "{}".format(constant)
        elif index == 1:
            return "{}{}".format(constant, variable)
        elif index > 1:
            return "{}{}^{}".format(constant, variable, index)
        else:
            return ""

    if elementNumber == 0 and randomLength == True:
        elementNumber = random.choice(weighted_int_list_square(maxIndex + 1))
    elif elementNumber == 0 and randomLength == False :
        elementNumber = maxIndex + 1
    
    elems, polynomial = [], ""

    for n in range(1, elementNumber + 1):
        index = maxIndex - n + 1
        if pi:
            if random.choice(chance_list("pi",5)) == "pi":
                constant = str(random.randint(-maxInteger, maxInteger + 1)) + "pi"
            else:
                constant = random.randint(-maxInteger, maxInteger + 1)
        else:
            constant = random.randint(-maxInteger, maxInteger + 1)
        
        if str(constant) == '0':
            constant += random.choice([-1,1])
        elems.append((constant, index)) ## pref tuple, can do shit later

    for count, elem in enumerate(elems):
        if count == 0:
            polynomial += element_in_polynomial(elem[0], elem[1])
        else:
            polynomial += " + " + element_in_polynomial(elem[0], elem[1])

    return polynomial


for i in range(50):
    print(fix(create_polynomial(maxIndex=3, maxInteger=4, variable="A", randomLength=True, pi = True)))

input()