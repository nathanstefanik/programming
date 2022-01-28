'''
Probabilistic primality test using Miller-Rabin algorithm
:param n: An odd integer greater than 1 to be tested for primality
:return: True if prime, False otherwise
'''
n = input("Enter number to test for primality: ")
# Below are "star witnesses" for n < 3,317,044,064,679,887,385,961,981
witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

# Miller-Rabin algorithm
## Getting the correct form for n

for witness in witnesses:
    x = (witness**
