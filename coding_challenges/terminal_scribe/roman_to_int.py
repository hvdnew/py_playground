
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000



# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution(object):

    def __init__(self) -> None:
        self.prefix_info = {'I': ('V', 'X'),
                            'V': (),
                            'X': ('L', 'C'),
                            'L': (),
                            'C': ('D', 'M'),
                            'D': (),
                            'M': ()}

    def romanIntVal(self, roman):
        val = 0;
        match roman:
            case 'I':
                val = 1;
            case 'V':
                val = 5;
            case 'X':
                val = 10
            case 'L':
                val = 50
            case 'C':
                val = 100
            case 'D':
                val = 500
            case 'M':
                val = 1000
            case 'IV':
                val = 4
            case 'IX':
                val = 9
            case 'XL':
                val = 40
            case 'XC':
                val = 90
            case 'CD':
                val = 400
            case 'CM':
                val = 900
            case _:
                raise ValueError(f'Invalid roman char {roman}')
        
        return val

    def doAttach(self, eval_char, next_char):
        idx = -1
        try:
            next_chars = self.prefix_info[eval_char]
            idx = next_chars.index(next_char) if len(next_chars) > 0 else -1
        except:
            print(f'Error evaulating {eval_char} {next_char}')
            return False

        return idx != -1
        


    def romanToInt(self, input_str):

        if len(input_str) == 0:
           return 0;
    
        # TODO validate
    
        if len(input_str) == 1:
            return self.romanIntVal(input_str)

        # if the string has more than 1 chars, get calculating 

        char_list = list(input_str.upper())

        num = 0;
        idx = 0;

        while idx < len(char_list):
            eval_char = char_list[idx]

            if idx < len(char_list) -1 and self.doAttach(eval_char, char_list[idx+1]):
                eval_char = eval_char + char_list[idx+1]
                num = num + self.romanIntVal(eval_char)
                idx += 2
            else:
                num = num + self.romanIntVal(eval_char)
                idx += 1


        return num


def main():
    sol = Solution()
    print(sol.romanToInt('LVIII'))
    pass

if __name__ == '__main__':
    main()