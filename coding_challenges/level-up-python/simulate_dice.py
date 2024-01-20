from random import randint
from collections import Counter

class Solution:
    '''There are X dices user will pass, we need to calculate probability using a method called Monte Carlo method
    In this method, we will sum up all the dice's output and find out how many time that combination (sum) can occur when we simulate
    '''

    def simmulate_dice(self, *dice, num_of_trails=1_000_000):
        counts = Counter();
        for _ in range(num_of_trails):
            counts[sum((randint(1, sides) for sides in dice))] += 1
        
        for outcome in range(len(dice), sum(dice)+1):
            print(f'{outcome} \t {counts[outcome] * 100 / num_of_trails :0.2f} %')

if __name__ == "__main__":
    sol = Solution()
    sol.simmulate_dice(4, 6, 6, 30)