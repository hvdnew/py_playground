import json
import pickle

class Solution:

    def save_to_file(self, dict, output_file_name):

        with open(output_file_name, 'wb') as op_file:
            pickle.dump(dict, op_file)
            #op_file.write(json.dumps(dict))
            

    def read_from_file(self, input_file):

        with open(input_file, 'rb') as ip_file:
            #dict = json.loads(ip_file.read())
            dict = pickle.load(ip_file)

        return dict
    
if __name__ == "__main__":
    sol = Solution()
    
    a_dict = {"a": "Apple", "b": "Boy", 1: 1.3};

    sol.save_to_file(a_dict, './save_a_dict.binary')

    from_file = sol.read_from_file('./save_a_dict.binary')

    print(f'{from_file} -- {from_file["a"]}')
