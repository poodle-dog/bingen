# bingen

Rhymes with "engine". 

Quick and dirty Python script to generate raw binary files. 

We have this cool AI generated logo, so you know it must be good.

![please help I've been stuck in Vim for weeks](bingen_logo.png)

# Quickstart

Need to generate a file of `0x5a` to fill a 256 byte EEPROM? `bingen` can do that:

```bash
$ python3 bingen.py 0x5a 256
00000000: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000010: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000020: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000030: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000040: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000050: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000060: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000070: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000080: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000090: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
000000a0: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
000000b0: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
000000c0: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
000000d0: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
000000e0: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
000000f0: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
```

Oh shit, was that acutally a 512 byte EEPROM, and you confused `0x100` and `0x200`? Not to worry - you can just feed raw hex to `bingen`, and leave messing up binary conversions to the co-ops:

```bash
$ python3 bingen.py 0x5a 0x200
00000000: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000010: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
```

Uh oh, is your EEPROM write pooping out somewhere? Need to figure out which 32 byte stride of writes is failing? `bingen` can make files of incremented blocks using the `--chunk` argument, so you can examine your memory to see which one is missing:

```bash
$ python3 bingen.py 0x5a 0x200 -c 32
00000000: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000010: 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a 5a5a
00000020: 5b5b 5b5b 5b5b 5b5b 5b5b 5b5b 5b5b 5b5b
00000030: 5b5b 5b5b 5b5b 5b5b 5b5b 5b5b 5b5b 5b5b
00000040: 5c5c 5c5c 5c5c 5c5c 5c5c 5c5c 5c5c 5c5c
00000050: 5c5c 5c5c 5c5c 5c5c 5c5c 5c5c 5c5c 5c5c
00000060: 5d5d 5d5d 5d5d 5d5d 5d5d 5d5d 5d5d 5d5d
00000070: 5d5d 5d5d 5d5d 5d5d 5d5d 5d5d 5d5d 5d5d
00000080: 5e5e 5e5e 5e5e 5e5e 5e5e 5e5e 5e5e 5e5e
00000090: 5e5e 5e5e 5e5e 5e5e 5e5e 5e5e 5e5e 5e5e
000000a0: 5f5f 5f5f 5f5f 5f5f 5f5f 5f5f 5f5f 5f5f
000000b0: 5f5f 5f5f 5f5f 5f5f 5f5f 5f5f 5f5f 5f5f
000000c0: 6060 6060 6060 6060 6060 6060 6060 6060
000000d0: 6060 6060 6060 6060 6060 6060 6060 6060
000000e0: 6161 6161 6161 6161 6161 6161 6161 6161
000000f0: 6161 6161 6161 6161 6161 6161 6161 6161
```

# Usage 

```bash
usage: bingen.py [-h] [--chunk CHUNK] [--filename FILENAME] [--verbose]
                 value length

positional arguments:
  value                 Hex value to fill file with. Used for whole file if
                        chunk is None.
  length                length of file to generate, in bytes

optional arguments:
  -h, --help            show this help message and exit
  --chunk CHUNK, -c CHUNK
                        Size of chunk to generate, in bytes. Successive chunk
                        values inc'ed from first.
  --filename FILENAME, -f FILENAME
                        Name of file to write output to. (default: stdout)
  --verbose, -v         Prints debug outputs.
```
