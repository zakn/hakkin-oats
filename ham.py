from matasano_0 import ascii_bits, un64

def hamming_ascii(str1, str2):
    bits1 = ascii_bits(str1)
    bits2 = ascii_bits(str2)
    count = 0

    for i in range(len(bits1)):
        if (bits1[i] != bits2[i]):
            count = count+1

    return count



def hamming(str1, str2):
    bits1 = un64(str1)
    bits2 = un64(str2)
    count = 0

    for i in range(len(bits1)):
        if (bits1[i] != bits2[i]):
            count = count+1

    return count






##testn##
'''
x = 'this is a test'
y = 'wokka wokka!!!'

print(hamming(x, y))
'''
