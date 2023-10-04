def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        # Create a list to store whether each number is prime or not.
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime.

        # Mark multiples of each prime as not prime.
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False

        return [i for i in range(2, n + 1) if is_prime[i]]

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Create a dictionary to memoize game results.
    memo = {}

    def can_win(n):
        # If n is in the list of prime numbers, the current player can win immediately.
        if n in primes:
            return True
        # If we have memoized the result for n, return it.
        if n in memo:
            return memo[n]
        # Otherwise, check if the current player can force a win.
        for prime in primes:
            if prime > n:
                break
            if not can_win(n - prime):
                memo[n] = True
                return True
        # If the current player cannot force a win, memoize the result and return False.
        memo[n] = False
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
