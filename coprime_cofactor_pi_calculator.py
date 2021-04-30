#Coprime pi calculator thingy
# x = coprime / total
# x = 6/pi^2
#hence pi = sqrt(6/x)

#And you can just use np.gcd() and not have to write it yourself lol.

#Best version has a +1.75% error for some weird reason. (Probably my range)
#Update: -0.2% error
import math
import os
import random

prime_list = [2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,
        41,  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97,
       101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
       167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
       239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
       313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
       397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
       467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
       569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
       643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727,
       733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821,
       823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
       911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997] 
       #Copied from the usual place, also adding 1 gets a 40%error

iter_calc = 2000000
global x, n_coprime, n_iter, exp_pi
x, n_coprime, n_iter, exp_pi = 0,0,0,0


def common_factor_checker(a,b):
    common_factor = False
    for i in prime_list:
        if a % i == 0 and b % i == 0:
            common_factor = True
            break
            #print(a,b,"yes",i)

    return common_factor



while n_iter < iter_calc:
    coprime = False

    def random_int():
        return random.randint(0,1000)
    a = random_int()
    b = random_int()
    #print(a,b)
    if a in prime_list or b in prime_list:
        n_coprime += 1
        coprime = True
        #print(a,b,"yes")
    else:
        if common_factor_checker(a,b) == True:
            coprime = False
            #print(a,b,"no")
        else:
            n_coprime += 1
            coprime = True
            #print(a,b,"yes")
            
    n_iter += 1

    x = n_coprime / n_iter
    #print(x)
    if x > 0:
        #print(x)
        exp_pi = math.sqrt(6/x)
        #print(exp_pi)

    pi_error = abs((math.pi - exp_pi )/ math.pi) * 100
    main_msg = """Iteration: {}
Total coprimes: {}
Current value of pi: {}
Percentage deviation from pi: {}%
""".format(n_iter, n_coprime, exp_pi, pi_error)
    print(main_msg)

input()