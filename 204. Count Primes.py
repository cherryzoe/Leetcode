# Description:

# Count the number of prime numbers less than a non-negative number, n.



# solution - sieve of eratosthenes: 
# reference: 
# http://www.tangjikai.com/algorithms/leetcode-count-primes
# http://bookshadow.com/weblog/2015/04/27/leetcode-count-primes/

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # assume a list of all prime numbers
        prime = [True] * n  
        # in the [2, n^0.5+1) range, set all their multiple to be False. 
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for j in range(i**2, n, i):
                    prime[j] = False
                # Count the number of Trues 
                return sum(prime[2:n])
        
