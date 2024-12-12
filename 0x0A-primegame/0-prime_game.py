#!/usr/bin/python3
# Script to determine the winner of a prime game

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Determine the maximum number in nums
    max_num = max(nums)

    # Precompute primes up to max_num using a sieve
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False

    # Precompute the cumulative count of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
