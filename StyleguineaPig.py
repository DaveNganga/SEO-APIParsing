# A simple function, mainly to test the style and Unittest functionality

def print_factors(x):
    # print("The factors of", x, "are:")
    for i in range(1, x+1):
        if x % i == 0:
            prime_list = []
            prime_list.append(i)
            return prime_list
