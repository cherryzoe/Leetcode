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
        prime = [True] * n
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for j in range(i**2, n, i):
                    prime[j] = False
        return sum(prime[2:n])
        
