import os
from zipfile import ZipFile

class ZipIt:

    def create_zip(self, path, extensions, op_file_name):
        with ZipFile(op_file_name, 'w') as output_zip:
            for root, _, files in os.walk(path):
                rel_path = os.path.relpath(root, path)
                for file in files:
                    _, ext = os.path.splitext(file)
                    if ext.lower() in extensions:
                        output_zip.write(os.path.join(root, file),
                                         arcname=os.path.join(rel_path, file))
        

if __name__ == '__main__':
    zip = ZipIt()
    zip.create_zip('files', ('.py', '.csv'), 'files.zip')