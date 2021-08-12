# Script to find the prime factorizaiton of a natural number
# Author: Collin Broderick
# Based on https://byjus.com/maths/prime-factorization/

# gives the prime factorization of integer num
def prime_factorization(num):
    if (num < 2): return None # zero or one not allowed
    num = abs(num) # gets rid of any negative
    factors = [] # list of factors
    while (num > 1):
        lpf = least_prime_factor(num)
        factors.append(int(lpf))
        num /= lpf

    return factors

# finds the smallest prime factor of integer num
def least_prime_factor(num):
    lpf = 2 # start with 2 as a candidate for the least prime factor
    while(num%lpf != 0):
        if (lpf >= num/2):
            return num # if lpf is at least half as big as num, there is no need to continue becuase there is no prime factor less than 2
        lpf+=1 # continue to increment lpf until it is evenly divisible into num
    return lpf

def main():
    num = input("Enter a natural number: ")
    result = prime_factorization(int(num))
    if (result == None):
        print("No prime factorization")
    else:
        print(result, sep=", ")
    

if __name__ == "__main__":
    main()