

#54ms Beats 45.53% of users with Python3
class Solution(object):

    def romanIntVal(self, roman):
        val = -1;
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
                val = -1
        
        return val
        


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

            if idx < (len(char_list)) -1 and self.romanIntVal(eval_char + char_list[idx+1]) != -1:
                eval_char = eval_char + char_list[idx+1]
                num = num + self.romanIntVal(eval_char)
                idx += 2
            else:
                num = num + self.romanIntVal(eval_char)
                idx += 1


        return num


def main():
    sol = Solution()
    print(sol.romanToInt('MCMXCIV'))
    pass

if __name__ == '__main__':
    main()