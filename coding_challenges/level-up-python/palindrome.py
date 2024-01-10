import re

class Solution:

    def isPalin(self, str: str):

        # non alpha numeric
        rx = re.compile('\W+')
        res = rx.sub('', str).lower().strip()

        return res == "".join(list(res)[::-1])

if __name__ == "__main__":
    sol = Solution()
    print(f'{sol.isPalin(" Go hang a Salami - Im a lasagna hog! ")}')