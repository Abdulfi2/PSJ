import sys
script = sys.argv[0]

def print_usage():
        sys.exit(f'Usage: python {script} pattern [FILE]')

def main(argv):
        if len(argv) < 2:
                print_usage()

        lines = sys.stdin
        pattern = argv[0]
        
        if(len(argv) > 1):
            try:
                lines = open(argv[1])
            except:
                sys.exit("File not found")
        for line in lines:
                if pattern in line:
                        print(line.strip())

if __name__ == '__main__':
        main(sys.argv[1:])
