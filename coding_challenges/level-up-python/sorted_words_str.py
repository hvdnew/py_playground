

class Solution:

    def sortStrWords(self, str: str):

        words = str.split(' ')

        bloated_list = [word.lower() + word for word in words]

        bloated_list.sort()

        cleaned_up_list = [appended_word[len(appended_word)//2:] for appended_word in bloated_list]

        return " ".join(cleaned_up_list)

if __name__ == "__main__":
    sol = Solution()
    print(f'{sol.sortStrWords("banana ORANGE apple")}')