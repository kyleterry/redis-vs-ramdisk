import sys
import os

import redis

RAMDISK_PATH = os.environ['HOME'] + '/ramdisk'
ITERATIONS = 100000

REDIS = None
REDIS_KEY_PREFIX = 'speed-test'


def get_redis_conn():
    global REDIS
    if not REDIS:
        REDIS = redis.Redis()
    return REDIS


def store_object(where, key, value):
    if where == 'ramdisk':
        with open('{}/{}'.format(RAMDISK_PATH, str(key)), 'w') as f:
            f.write(value)
    elif where == 'redis':
        r = get_redis_conn()
        r.set('{}:{}'.format(REDIS_KEY_PREFIX, key), value)
    else:
        print 'boom'


def main():
    with open('./some.html', 'r') as f:
        html_to_store = f.read()

    if sys.argv[1] not in ['redis', 'ramdisk']:
        print("dunno what that is bro?")
        sys.exit(1)

    where = sys.argv[1]

    print('Populating {}'.format(where))

    if where == 'ramdisk':
        print('ramdisk path: {}'.format(RAMDISK_PATH))

    for i in range(ITERATIONS):
        if i % 5000 == 0:
            print('Adding {}'.format(i))
        store_object(sys.argv[1], i, html_to_store)

if __name__ == '__main__':
    main()
