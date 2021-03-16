import sys
script = sys.argv[0]

def print_usage():
        sys.exit(f'Usage: python {script} pattern [FILE]')

def main(argv):
        if len(argv) < 2:
                print_usage()

        lines = open(argv[1])

        pattern = argv[0]
        for line in lines:
                if pattern in line:
                        print(line.strip())

if __name__ == '__main__':
        main(sys.argv[1:])
