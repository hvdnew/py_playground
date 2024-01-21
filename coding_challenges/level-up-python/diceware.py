import csv
from secrets import randbelow

class Diceware:
    
    _diceware_file = './files/diceware_words.txt'

    def load_diceware(self):
        word_dict = {}
        with open(self._diceware_file, 'r') as file:
            csv_reader = csv.reader(file, delimiter='\t')
            for row in csv_reader:
                word_dict[row[0]] = row[1]

        return word_dict



    def generate_random_diceware_pwd(self, number_of_rolls):

        word_dict = self.load_diceware();

        words = []

        for num in range(number_of_rolls):
            words.append(word_dict[''.join([str(randbelow(idx)+1) for idx in range(1, 6)])])
            
        return words

if __name__ == '__main__':
    diceware = Diceware()
    print(f'{diceware.generate_random_diceware_pwd(5)}')
