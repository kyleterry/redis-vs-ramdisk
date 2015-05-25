import sys
import os

import redis

def main():
    if sys.argv[1] == 'redis':
        pass
    elif sys.argv[1] == 'ramdisk':
        pass
    else:
        print("dunno what that is bro?")
        sys.exit(1)

if __name__ == '__main__':
    main()
