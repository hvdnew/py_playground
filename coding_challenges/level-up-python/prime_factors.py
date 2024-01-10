

class Solution:

    def primeFactors(self, input_int):

        factors = []
        divisor = 2

        while divisor <= input_int:
            if input_int % divisor == 0:
                factors.append(divisor)
                input_int = input_int // divisor
            else:
                divisor += 1

        return factors


if __name__ == "__main__":
    sol = Solution()
    print(f'{sol.primeFactors(60)}')