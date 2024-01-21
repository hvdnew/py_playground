import csv

class MergeCSV:

    def write_csv(self, data, keys, filename):

        with open(filename, 'w') as file:
            dict_writer = csv.DictWriter(f=file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
            


    def read_csv_dict(self, file):

        data = []
        with open(file, 'r') as ip:
            dict_reader = csv.DictReader(ip)
            [data.append(row) for row in dict_reader]

        return data

    def merge(self, ip_file1, ip_file2, op_file):

        file1_content = self.read_csv_dict(ip_file1)
        file2_content = self.read_csv_dict(ip_file2)

        output_content = []

        [output_content.append(dict) for dict in file1_content]
        [output_content.append(dict) for dict in file2_content]

        keys = []

        for dict in output_content:
            for key, val in dict.items():
                if key not in keys:
                    keys.append(key)


        self.write_csv(output_content, keys, op_file)
        

if __name__ == '__main__':
    sol = MergeCSV()
    #print(sol.read_csv_dict("./files/csv1.csv"))
    print(f'{sol.merge("./files/csv1.csv", "./files/csv2.csv", "./files/merged.csv")}')