import os
import re
import urllib.parse
import urllib.request

class DownloadSequentialFiles:

    def get_em_all(self, first_file_link, output_directory):
        if not os.path.isdir(output_directory):
            os.mkdir(output_directory)
        url_head, url_tail = os.path.split(first_file_link)
        first_index = re.findall(r'[0-9]+', url_tail)[-1]
        index_count, error_count = 0, 0
        while error_count < 5:
            next_index = str(int(first_index) + index_count)
            if first_index[0] == '0': # zero padded
                next_index = '0' * (len(first_index) - len(next_index)) + next_index
            next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))
            try:
                output_file = os.path.join(output_directory, os.path.basename(next_url))
                urllib.request.urlretrieve(next_url, output_file)
                print(f'Successfully downloaded {output_file}')
                index_count += 1
            except IOError:
                print(f'Could not download {next_url}')
                error_count += 1


if __name__ == '__main__':
    go = DownloadSequentialFiles()
    go.get_em_all('http://699340.youcanlearnit.net/image001.jpg', 'images_from_the_web')
