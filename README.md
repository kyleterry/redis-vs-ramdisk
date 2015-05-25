# Setup

Make a ramdisk:

```bash
mkdir ~/ramdisk
sudo mount -t tmpfs -o size=10G,mode=0755 tmpfs ~/ramdisk
```

Populate the ramdisk:

```bash
python populate.py ramdisk
```

Populate redis with the same data:

```bash
python populate.py redis
```

## How to test

Run the tests:

```bash
python run_tests.py
```

## Results

### No compression; raw access from python; no persistence

```
Running setup
Iterations set to 100000

Testing ramdisk
That took 1.549776s

Testing redis
That took 5.170801s
```

### Compression; raw access from python; no persistence

TODO
