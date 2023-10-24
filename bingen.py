import argparse

def generate_chunk(value,length):
    return [ value ] * length 

def write_binfile(list_data, filename):
    with open(filename, 'wb') as f:
        for a in list_data:
            f.write(a.to_bytes(1, 'little'))

def print_like_xxd(list_data):
    # Prints all lines  
    for idx, a in enumerate(zip(*(iter(list_data),) * 16)):
        printlist = [ f'{a[i]:02x}{a[i+1]:02x}' for i in range(0, len(a)-1, 2) if i+1 < len(a)]
        print(f'{(idx*16):08x}:', ' '.join(printlist))

    modulus = len(list_data) % 16
    if modulus:
        start = len(list_data) - modulus
        printlist = []
        for i in range(modulus):
            printlist.append(f'{list_data[start+i]:02x}')
            if (i % 2) == 1:
                printlist.append(' ')

        print(f'{(start*16):08x}:', ''.join(printlist))


def main(args):
    # Dumps all the input args 
    if args.verbose:
        print(args)

    # Populates list_data with either incremented chunks, or all one value
    list_data = []
    if args.chunk:
        chunkval  = args.value
        len_file  = args.length
        len_chunk = args.chunk

        for a in range(args.length // args.chunk):
            list_data += generate_chunk(chunkval,args.chunk)
            chunkval += 1
            chunkval &= 0xff

        modulus = args.length % args.chunk
        if modulus:
            list_data += generate_chunk(chunkval,modulus)

    else: 
        list_data = generate_chunk(args.value, args.length)

    # Writes binary file out, or dumps to stdout in xxd format
    if args.filename:
        write_binfile(list_data, args.filename)
        if args.verbose:
            print(f'Data written to {args.filename}')
    else:
        print_like_xxd(list_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'value',
        help='Hex value to fill file with. Used for whole file if chunk is None.',
        type=lambda x: int(x,0) # https://stackoverflow.com/a/48950906
    )

    parser.add_argument(
        'length',
        help='length of file to generate, in bytes',
        type=lambda x: int(x,0) # https://stackoverflow.com/a/48950906
    )

    parser.add_argument(
        '--chunk',
        '-c',
        help='Size of chunk to generate, in bytes. Successive chunk values inc\'ed from first.',
        type=lambda x: int(x,0) # https://stackoverflow.com/a/48950906
    )

    parser.add_argument(
        '--filename',
        '-f',
        help='Name of file to write output to. (default: stdout)',
        type=str
    )

    parser.add_argument(
        '--verbose',
        '-v',
        help='Prints debug outputs.',
        action='store_true'
    )

    args = parser.parse_args()

    main(args)
