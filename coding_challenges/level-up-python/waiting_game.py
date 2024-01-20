import time
import random


class Solution:
    
    def waiting_game(self):
        num_of_seconds_to_wait = random.randint(2, 4)
        print(f'Your target wait time is {num_of_seconds_to_wait} seconds')

        input('-- Press ENTER to begin --')
        start = time.perf_counter()

        input('-- Press ENTER agan after {num_of_seconds_to_wait} seconds--')
        elapsed = time.perf_counter() - start

        print(f'elapsed time {elapsed :.3f} seconds')


if __name__ == "__main__":
    sol = Solution()
    sol.waiting_game()