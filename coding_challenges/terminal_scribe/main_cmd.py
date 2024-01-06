import argparse
import json
from canvas import Canvas

def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--filename"
    )

    args = parser.parse_args()

    if args.filename:
        with open(args.filename, 'r') as input_file:
            file_content = input_file.read()

        canvas = Canvas.fromDict(json.loads(file_content))

        canvas.go()



    pass

if __name__ == "__main__":
    print('Welcome to Terminal Scribe')
    main()