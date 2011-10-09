"""
Lyle Scott III
lyle@digitalfoo.net
http://www.digitalfoo.net
"""

import re
import sys


PC1 = [[57,  49,  41,  33,  25,  17,   9],
       [ 1,  58,  50,  42,  34,  26,  18],
       [10,   2,  59,  51,  43,  35,  27],
       [19,  11,   3,  60,  52,  44,  36],
       [63,  55,  47,  39,  31,  23,  15],
       [ 7,  62,  54,  46,  38,  30,  22],
       [14,   6,  61,  53,  45,  37,  29],
       [21,  13,   5,  28,  20,  12,   4]]

PC2 = [[14,  17,  11,  24,   1,   5],
       [3,   28,  15,   6,  21,  10],
       [23,  19,  12,   4,  26,   8],
       [16,   7,  27,  20,  13,   2],
       [41,  52,  31,  37,  47,  55],
       [30,  40,  51,  45,  33,  48],
       [44,  49,  39,  56,  34,  53],
       [46,  42,  50,  36,  29,  32]]

IP = [[58,   50,  42,  34,  26,  18,  10,   2],
      [60,   52,  44,  36,  28,  20,  12,   4],
      [62,   54,  46,  38,  30,  22,  14,   6],
      [64,   56,  48,  40,  32,  24,  16,   8],
      [57,   49,  41,  33,  25,  17,   9,   1],
      [59,   51,  43,  35,  27,  19,  11,   3],
      [61,   53,  45,  37,  29,  21,  13,   5],
      [63,   55,  47,  39,  31,  23,  15,   7]]

EBIT= [[32,   1,   2,   3,   4,   5],
       [ 4,   5,   6,   7,   8,   9],
       [ 8,   9,  10,  11,  12,  13],
       [12,  13,  14,  15,  16,  17],
       [16,  17,  18,  19,  20,  21],
       [20,  21,  22,  23,  24,  25],
       [24,  25,  26,  27,  28,  29],
       [28,  29,  30,  31,  32,   1]]

S1 = [[14,   4,  13,   1,   2,  15,  11,   8,   3,  10,   6,  12,   5,   9,   0,   7],
      [ 0,  15,   7,   4,  14,   2,  13,   1,  10,   6,  12,  11,   9,   5,   3,   8],
      [ 4,   1,  14,   8,  13,   6,   2,  11,  15,  12,   9,   7,   3,  10,   5,   0],
      [15,  12,   8,   2,   4,   9,   1,   7,   5,  11,   3,  14,  10,   0,   6,  13]]

S2 = [[15,   1,   8,  14,   6,  11,   3,   4,   9,   7,   2,  13,  12,   0,   5,  10],
      [ 3,  13,   4,   7,  15,   2,   8,  14,  12,   0,   1,  10,   6,   9,  11,   5],
      [ 0,  14,   7,  11,  10,   4,  13,   1,   5,   8,  12,   6,   9,   3,   2,  15],
      [13,   8,  10,   1,   3,  15,   4,   2,  11,   6,   7,  12,   0,   5,  14,   9]]

"""
S3 = [[10,   0,   9,  14,   6,   3,  15,   5,   1,  13,  12,   7  11  4   2  8
      [13,   7,   0,   9,   3,   4,   6,  10,   2,   8,   5,  14  12 11  15  1
      [13,   6,   4,   9,   8,  15,   3,   0,  11,   1,   2,  12   5 10  14  7
      [ 1,  10,  13,   0,   6,   9,   8,   7,   4,  15,  14,   3  11  5   2 12

S4 = [[ 7,  13,  14,   3,   0,   6,   9,  10,   1,   2,   8,   5  11 12   4 15
      [13,   8,  11,   5,   6,  15,   0,   3,   4,   7,   2,  12   1 10  14  9
      [10,   6,   9,   0,  12,  11,   7,  13,  15,   1,   3,  14   5  2   8  4
      [ 3,  15,   0,   6,  10,   1,  13,   8,   9,   4,   5,  11  12  7   2 14

S5 = [[ 2,  12,   4,   1,   7,  10,  11,   6,   8,   5,   3,  15  13  0  14  9
      [14,  11,   2,  12,   4,   7,  13,   1,   5,   0,  15,  10   3  9   8  6
      [ 4,   2,   1,  11,  10,  13,   7,   8,  15,   9,  12,   5   6  3   0 14
      [11,   8,  12,   7,   1,  14,   2,  13,   6,  15,   0,   9  10  4   5  3

S6 = [[12,   1,  10,  15,   9,   2,   6,   8,   0,  13,   3,   4  14  7   5 11
      [10,  15,   4,   2,   7,  12,   9,   5,   6,   1,  13,  14   0 11   3  8
      [ 9,  14,  15,   5,   2,   8,  12,   3,   7,   0,   4,  10   1 13  11  6
      [ 4,   3,   2,  12,   9,   5,  15,  10,  11,  14,   1,   7   6  0   8 13
 
S7 = [[ 4,  11,   2,  14,  15,   0,   8,  13,   3,  12,   9,   7   5 10   6  1
      [13,   0,  11,   7,   4,   9,   1,  10,  14,   3,   5,  12   2 15   8  6
      [ 1,   4,  11,  13,  12,   3,   7,  14,  10,  15,   6,   8   0  5   9  2
      [ 6,  11,  13,   8,   1,   4,  10,   7,   9,   5,   0,  15  14  2   3 12

S8 = [[13,   2,   8,   4    6,  15,  11,   1,  10,   9,   3,  14   5  0  12  7
      [ 1,  15,  13,   8,  10,   3,   7,   4,  12,   5,   6,  11   0 14   9  2
      [ 7,  11,   4,   1,   9,  12,  14,   2,   0,   6,  10,  13  15  3   5  8
      [ 2,   1,  14,   7,   4,  10,   8,  13,  15,  12,   9,   0   3  5   6 11
"""


LSHIFT_MAP = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2,  2, 2, 2, 1]

###############################################################################

def hex_to_64binary(hex):
    print_broken_str('hex', hex)
    
    int64 = long(hex, 16)
    print_broken_str('int64', int64)
    
    bin64 = str(bin(int64))[2:].rjust(64, '0')
    print_broken_str('bin64', bin64)
    
    return bin64


def print_broken_str(label, input, breakAt=None):
    if breakAt != None:
        s = ''
        for i in xrange(0, len(input), breakAt):
            for ii in xrange(breakAt):
                s += str(input[i+ii])
            s += ' '
    else:
        s = input
    print '%s: %s\n' % (label.ljust(10), s),

    
def subkey(key64):
    """map a 64bit key to a 57bit key"""
    key56 = [-1]*56
    
    """
    8*0 - 0-1
    8*1 - 1-1
    8*2 - 2-1
    .........
    8*N - N-1
    """
    
    for row_i in xrange(len(PC1)):
        r = (8*row_i)-(row_i-1)
        for col_i in xrange(len(PC1[row_i])):
            key64_index = PC1[row_i][col_i] - 1
            key56[r+col_i-1] = key64[key64_index]
            
    return ''.join(map(str, key56))

###############################################################################

def subkey2(key56):
    key48 = [-1]*48
    
    """
    7*0 - 0-0 = 1
    7*1 - 1-1 =
    7*2 - 2-1 = 
    """
    
    for row_i in xrange(len(PC2)):
        r = (7*row_i)-(row_i-1)
        for col_i in xrange(len(PC2[row_i])):
            key56_index = PC2[row_i][col_i] - 1
            key48[r+col_i-1] = key56[key56_index]
            
    return ''.join(map(str, key48))

        
def do_rounds1(key56):
    middle = len(key56) / 2
    c = key56[:middle]
    d = key56[middle:]
    
    print_broken_str('C0', c)
    print_broken_str('D0', d)
    
    key48s = []
    
    for i in range(16):
        c,d = _do_round1(c, d, i)
        substring_key = '%s%s' % (c, d)
        k = subkey2(substring_key)
        print_broken_str('C%d' % (i+1), c)
        print_broken_str('D%d' % (i+1), d)
        print_broken_str('K%d' % (i+1), k, 6)
        
    return k
        
    
def _do_round1(c, d, iteration):
    c_lst = [n for n in c]
    d_lst = [n for n in d]
        
    for i in xrange(LSHIFT_MAP[iteration]):
        c_lst.append(c_lst.pop(0))
        d_lst.append(d_lst.pop(0))
    
    return (''.join(c_lst), ''.join(d_lst))

###############################################################################
        
def m2ip(m):
    key64 = [-1]*64
    
    for row_i in xrange(len(IP)):
        r = (9*row_i)-(row_i-1)
        for col_i in xrange(len(IP[row_i])):
            m_index = IP[row_i][col_i] - 1
            key64[r+col_i-1] = m[m_index]
            
    return ''.join(map(str, key64))

###############################################################################

def do_round2(ip, key48):
    middle = len(ip) / 2
    l_prev = ip[:middle]
    r_prev = ip[middle:]

    print_broken_str('L0', l_prev)
    print_broken_str('R0', r_prev)    
    
    for i in xrange(16):
        l = r_prev
        
        f = _f(r_prev, key48)
        r = l_prev + f
        
        print_broken_str('L%d' % (i+1), l)
        print_broken_str('R%d' % (i+1), r)
        

def _do_round2():
    pass


def _f(r32, key48):
    """XOR addition"""
    
    print_broken_str('key48:', key48)
    
    e = _e(r32)
    print_broken_str('E(Rn-1):', e)
    
    tmp = []
    
    for i in xrange(len(e)):
        #print e[i], key48[i], '=', _xor(e[i], key48[i])
        tmp.append(_xor(r32, key48[i]))
    return ''.join(map(str, tmp))


def _e(r32):
    key48 = [-1]*48
    
    for row_i in xrange(len(EBIT)):
        r = (7*row_i)-(row_i-1)
        for col_i in xrange(len(EBIT[row_i])):
            r32_index = EBIT[row_i][col_i] - 1
            key48[r+col_i-1] = r32[r32_index]
            
    return ''.join(map(str, key48))

def _xor(s1, s2):
    s1 = int(s1)
    s2 = int(s2)
    return int(bool(s1) ^ bool(s2))

###############################################################################

def main():
    m = hex_to_64binary('0123456789ABCDEF')
    print_broken_str('M', m, 4)
    print '-'*80
    
    k = hex_to_64binary('133457799BBCDFF1')
    print_broken_str('K', k, 8)
    print '-'*80
    
    kp = subkey(k)
    print_broken_str('K+', kp, 8)
    print '-'*80
    
    key48 = do_rounds1(kp)
    print '-'*80    
    
    ip = m2ip(m)
    print_broken_str('IP', ip, 8)
    print '-'*80
    
    do_round2(ip, key48)
    
###############################################################################
    
if __name__ == '__main__':
    main()