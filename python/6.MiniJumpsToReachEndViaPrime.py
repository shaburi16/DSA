from collections import deque, defaultdict
import math

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False

            limit = int(math.sqrt(x)) + 1
            for i in range(3, limit, 2):
                if x % i == 0:
                    return False
            return True

        divisible_map = defaultdict(list)

        primes_in_nums = set(x for x in nums if is_prime(x))

        for p in primes_in_nums:
            for i, val in enumerate(nums):
                if val % p == 0:
                    divisible_map[p].append(i)

    
        q = deque([(0, 0)])   
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            for nxt in [i - 1, i + 1]:
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, steps + 1))

           
            val = nums[i]

            if is_prime(val) and val not in used_prime:
                for nxt in divisible_map[val]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append((nxt, steps + 1))

                used_prime.add(val)

        return -1