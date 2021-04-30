import os

final = 10000 #excleusive

the_list = []

for i in range (2,final+1):
    print(i)
    k = True
    for n in range (2,i):
        if i % n == 0:
            k = False
            break

    if k:
        the_list.append(i)

list_code = """prime_list = {}
""".format(the_list)

with open(r"C:\Utilities\Scripts\math_utilities\4d_primes.py", 'w', encoding="utf-8") as f:
    f.write(list_code)
input("DONE")