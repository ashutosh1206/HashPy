#!/usr/bin/env python2.7

def string2bin(input_str):
    # To convert ASCII string to binary string
    binary_str = ''.join(map((lambda x: bin(ord(x))[2:].zfill(8)), [i for i in input_str]))
    return binary_str

def bin2string(input_str):
    return None

def padding(data):
    # SHA-1 has a block size of 512 bits (64 bytes)
    # `data` : ASCII string
    data_bin = string2bin(data)
    # 64 bit representation of length of `data_bin`
    l = bin(len(data_bin))[2:].zfill(64)
    # 512 bits per chunk which includes a 64 bit representation of length of `data_bin`
    # Therefore, padding takes place in such a way that len(data_bin) = 0 mod 448
    padlen = 448 - (len(data_bin) % 448)
    data_bin += '1' + (padlen-1)*'0' + l
    assert len(data_bin) % 512 == 0
    return data_bin

def div_padded_msg(msg):
    # Divide message into chunks of size 512 bits
    div_msg = [msg[i:i+512] for i in range(0,len(msg),512)]
    return div_msg
