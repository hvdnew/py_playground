from collections import Counter

class Solution:

    def cound_words(self, file_path):

        with open(file_path, 'r') as file:
            the_file_content = file.read()

        words = the_file_content.split()
        counts = Counter()

        for word in words:
            counts[word] += 1

        print(f'Total words: {len(words)}')

        print(f'\nTop 5 words:')

        most_common = counts.most_common(5)

        for tuple in most_common:
            print(f'{tuple[0]}: {tuple[1]}')


if __name__ == '__main__':
    sol = Solution()
    sol.cound_words('./waiting_game.py')