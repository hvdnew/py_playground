
## needs further improvement, parking right now to focus on others
class Solution:

    def isPalindrom(self, str):
        return str == str[::-1]

    def longestPalindrome(self, str: str) -> str:
        
        if not str:
            return None;

        if len(str) == 1:
            return str
        
        # start from 0 and calculate longest-pal length for that index
        longest_palindrome_substr = ''
        palindromes = []
        palendromic_length_for_idx = [-1 for idx in list(str)]
        idx_cntr = 0

        while idx_cntr < len(str):

            left_pointer = idx_cntr
            right_pointer = idx_cntr
            idx_palin_length = 1
            do_left_extend = True
            do_right_extend = False
            found_palin_inner = False

            #print(f'Test for idx {idx_cntr} -->')
            while left_pointer >=0 and right_pointer < len(str):
                sub_str = str[left_pointer:right_pointer+1]
                print(f'{left_pointer}, {right_pointer} ')
                if not sub_str in palindromes and self.isPalindrom(sub_str):
                    palindromes.append(sub_str)
                    idx_palin_length = len(sub_str)
                    found_palin_inner = True

                    # keep expending if left, right char are same 
                    potential_left_pointer = left_pointer - 1
                    potential_right_pointer = right_pointer + 1
                    while potential_left_pointer >=0 and potential_right_pointer < len(str) and str[potential_left_pointer] == str [potential_right_pointer]:
                        left_pointer = potential_left_pointer
                        right_pointer = potential_right_pointer
                        potential_left_pointer -= 1
                        potential_right_pointer += 1
                        smart_matching = True
                        sub_str = str[left_pointer:right_pointer]
                        idx_palin_length = len(sub_str)


                    if len(sub_str) > len(longest_palindrome_substr):
                        longest_palindrome_substr = sub_str
                

                # break if breached
                if left_pointer == 0 and right_pointer == len(str) -1:
                    break

                # widen left and right one after another
                # widen left bound
                if do_left_extend and left_pointer > 0 or right_pointer < len(str):
                    left_pointer -= 1
                    do_left_extend = False if not found_palin_inner else True
                    do_right_extend = True
                    continue;
                # widen right bound
                if not do_right_extend and right_pointer < len(str) or left_pointer > 0:
                    right_pointer += 1
                    do_left_extend = True
                    do_right_extend = False if not found_palin_inner else True

                

            palendromic_length_for_idx[idx_cntr] = idx_palin_length
            idx_cntr += 1

        print(f'==> palendromic_length_for_idx {palendromic_length_for_idx}, {longest_palindrome_substr}')

        return longest_palindrome_substr

    def longestPalindromeOn2(self, str: str) -> str:
        
        if not str:
            return None;

        if len(str) == 1:
            return str

        idx = 0
        longest_palindrome = ''
        palindromes = []

        while idx < len(str):

            inner_idx = idx

            while inner_idx < len(str):
                sub_str = str[idx:inner_idx+1]

                if not sub_str in palindromes and self.isPalindrom(sub_str):
                    palindromes.append(sub_str)
                    if len(sub_str) > len(longest_palindrome):
                        longest_palindrome = sub_str

                inner_idx += 1

            idx += 1

        print(f'==> {palindromes} longest_palindrome {longest_palindrome}')

        return longest_palindrome

if __name__ == '__main__':
    sol = Solution()
    #print(sol.longestPalindrome('cbbd'))
    #print(sol.longestPalindrome("jkexvzsqshsxyytjmmhauoyrbxlgvdovlhzivkeixnoboqlfemfzytbolixqzwkfvnpacemgpotjtqokrqtnwjpjdiidduxdprngvitnzgyjgreyjmijmfbwsowbxtqkfeasjnujnrzlxmlcmmbdbgryknraasfgusapjcootlklirtilujjbatpazeihmhaprdxoucjkynqxbggruleopvdrukicpuleumbrgofpsmwopvhdbkkfncnvqamttwyvezqzswmwyhsontvioaakowannmgwjwpehcbtlzmntbmbkkxsrtzvfeggkzisxqkzmwjtbfjjxndmsjpdgimpznzojwfivgjdymtffmwtvzzkmeclquqnzngazmcfvbqfyudpyxlbvbcgyyweaakchxggflbgjplcftssmkssfinffnifsskmsstfclpjgblfggxhckaaewyygcbvblxypduyfqbvfcmzagnznquqlcemkzzvtwmfftmydjgvifwjoznzpmigdpjsmdnxjjfbtjwmzkqxsizkggefvztrsxkkbmbtnmzltbchepwjwgmnnawokaaoivtnoshywmwszqzevywttmaqvncnfkkbdhvpowmspfogrbmuelupcikurdvpoelurggbxqnykjcuoxdrpahmhiezaptabjjulitrilkltoocjpasugfsaarnkyrgbdbmmclmxlzrnjunjsaefkqtxbwoswbfmjimjyergjygzntivgnrpdxuddiidjpjwntqrkoqtjtopgmecapnvfkwzqxilobtyzfmeflqobonxiekvizhlvodvglxbryouahmmjtyyxshsqszvxekj"))
    print(sol.longestPalindrome("jkexvzsqshsxyytjmmhauoyrbxlgvdovlhzivkeixnoboqlfemfzytbolixqzwkfvnpacemgpotjtqokrqtnwjpjdiidduxdprngvitnzgyjgreyjmijmfbwsowbxtqkfeasjnujnrzlxmlcmmbdbgryknraasfgusapjcootlklirtilujjbatpazeihmhaprdxoucjkynqxbggruleopvdrukicpuleumbrgofpsmwopvhdbkkfncnvqamttwyvezqzswmwyhsontvioaakowannmgwjwpehcbtlzmntbmbkkxsrtzvfeggkzisxqkzmwjtbfjjxndmsjpdgimpznzojwfivgjdymtffmwtvzzkmeclquqnzngazmcfvbqfyudpyxlbvbcgyyweaakchxggflbgjplcftssmkssfinffnifsskmsstfclpjgblfggxhckaaewyygcbvblxypduyfqbvfcmzagnznquqlcemkzzvtwmfftmydjgvifwjoznzpmigdpjsmdnxjjfbtjwmzkqxsizkggefvztrsxkkbmbtnmzltbchepwjwgmnnawokaaoivtnoshywmwszqzevywttmaqvncnfkkbdhvpowmspfogrbmuelupcikurdvpoelurggbxqnykjcuoxdrpahmhiezaptabjjulitrilkltoocjpasugfsaarnkyrgbdbmmclmxlzrnjunjsaefkqtxbwoswbfmjimjyergjygzntivgnrpdxuddiidjpjwntqrkoqtjtopgmecapnvfkwzqxilobtyzfmeflqobonxiekvizhlvodvglxbryouahmmjtyyxshsqszvxekj"))