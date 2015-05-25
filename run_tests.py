from datetime import datetime
import random

import os

import redis

ITERATIONS = 100000
RAMDISK_PATH = os.environ['HOME'] + '/ramdisk'

REDIS_KEY_PREFIX = 'speed-test'

def main():
    print('Running setup')
    with open('./some.html', 'r') as f:
        compare_string = f.read()

    print('Iterations set to {}'.format(ITERATIONS))

    print('')

    print('Testing ramdisk')
    start = datetime.now()
    for i in range(ITERATIONS):
        key = random.randint(0, 99999)
        with open('{}/{}'.format(RAMDISK_PATH, key), 'r') as f:
            contents = f.read()
        if contents != compare_string:
            print('CONTENT MISMATCH WHILE READING {}'.format(key))
    end = datetime.now()

    delta = end - start
    print('That took {}s'.format(delta.total_seconds()))

    print('')

    print('Testing redis')
    r = redis.Redis()
    start = datetime.now()
    for i in range(ITERATIONS):
        key = random.randint(0, 99999)
        contents = r.get('{}:{}'.format(REDIS_KEY_PREFIX, key))
        if contents != compare_string:
            print('CONTENT MISMATCH WHILE READING {}'.format(key))
    end = datetime.now()

    delta = end - start
    print('That took {}s'.format(delta.total_seconds()))


if __name__ == '__main__':
    main()
