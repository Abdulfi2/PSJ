import sys
argv_len = len(sys.argv[1:])
if not argv_len == 2:
    sys.exit(f'invalid number of arguments (expected 2, given:{argv_len})')
print('two arguments are:', sys.argv[1:])
