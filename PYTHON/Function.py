from math import sqrt
def say_hello(name):
    #print("Hello, {}!".format(name))
    result = "Hello, {}!".format(name)
    return result

'''pirmskaitlis ir skaitlis, kas dalās ar 1 un pats ar sevi un kuram ir tieši divi dalītāji:
2, 3, 4, 7, 11, 13, 17, 19, 23, 29, 31, 37'''

def check_if_prime(number):
    if number <= 1:
        return False
    is_prime = True
    for i in range(2, int(sqrt(number)) +1):
        if number % 1 == 0:
            is_prime = False
            break
    return is_prime