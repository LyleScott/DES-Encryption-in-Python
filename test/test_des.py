"""
Lyle Scott III
lyle@digitalfoo.net
http://www.digitalfoo.net
"""
import des
import unittest


class TestDes(unittest.TestCase):
    """Test the DES script."""

    def setUp(self):
        """Initialize fixture."""
        self.key = '133457799BBCDFF1'

    def test_hex_to_64binary(self):
        """Test that a hex string can be converted to a 64 bit binary number.
        """
        hexstr = 'ABC'
        binstr = '0000000000000000000000000000000000000000000000000000101010111100'
        self.assertEquals(des.hex_to_64binary(hexstr), binstr)

        hexstr = '1234567890ABCDEF'
        binstr = '0001001000110100010101100111100010010000101010111100110111101111'
        self.assertEquals(des.hex_to_64binary(hexstr), binstr)

    def test_hex_to_64binary_blankstr(self):
        """Test that the TB is handled properly for input that is not
        able to transform into base16.
        """
        self.assertRaises(ValueError, des.hex_to_64binary, '')

    def test_binary_to_hex(self):
        """Test that a binary binstr can be properly converted to hex."""
        binstr = '0000000000000000000000000000000000000000000000000000101010111100'
        hexstr = '0000000000000ABC'
        self.assertEquals(des.binary_to_hex(binstr), hexstr)

        binstr = '0001001000110100010101100111100010010000101010111100110111101111'
        hexstr = '1234567890ABCDEF'
        self.assertEquals(des.binary_to_hex(binstr), hexstr)

    def test_binary_to_hex_blankstr(self):
        """Test that a binstr can be properly be converted to hex."""
        binstr = ''
        hexstr = ''
        self.assertEquals(des.binary_to_hex(binstr), hexstr)

    def test_string_chunker(self):
        """Test that the a string can properly be broken up at break_at
        intervals.
        """
        s = des.string_chunker('my label', '110011001100')
        expected = 'my label  : 110011001100'
        self.assertEquals(s, expected)

        s = des.string_chunker('my label', '110011001100', 2)
        expected = 'my label  : 11 00 11 00 11 00'
        self.assertEquals(s, expected)

        s = des.string_chunker('my label', '110011001100', 4)
        expected = 'my label  : 1100 1100 1100'
        self.assertEquals(s, expected)

        s = des.string_chunker('my label', '110011001100', 12)
        expected = 'my label  : 110011001100'
        self.assertEquals(s, expected)

    def test_lshift(self):
       """Test that a sequence/string can have its bits left shifted. The
       number of shifts is derived from the iteration count representing an
       index in the LSHIFT_MAP list.
       """
       c = 'abcde'
       d = 'mnopq'

       self.assertEquals(des.lshift(c, d, 0), ('bcdea', 'nopqm'))
       self.assertEquals(des.lshift(c, d, 1), ('bcdea', 'nopqm'))
       self.assertEquals(des.lshift(c, d, 2), ('cdeab', 'opqmn'))
       self.assertEquals(des.lshift(c, d, 8), ('bcdea', 'nopqm'))
       self.assertEquals(des.lshift(c, d, 15), ('bcdea', 'nopqm'))

    def test_permutate(self):
        """Test that a permutation gets mapped correctly."""
        permutation = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
        in_bits = '11011010111111000111101010010000'
        out_bits_wide = 32
        self.assertEquals(des.permutate(permutation, in_bits, out_bits_wide),
                          '01110110101011011001000111000111')

        permutation = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
        in_bits = '1111101000101000111000001000100110110010001011100100011101110111'
        out_bits_wide = 64
        self.assertEquals(des.permutate(permutation, in_bits, out_bits_wide),
                          '0000101111101010001010100111000111000010111101100100111011000101')

    def test_xor(self):
        """Test that two bit strings are correctly xor'ed."""
        a = '110010110011110110001011000011100001011111110101'
        b = '110110100100000101011100001000001110101110101111'
        c = '000100010111110011010111001011101111110001011010'
        self.assertEquals(des.xor(a, b), c)

        a = '10001100100001010111000101001110'
        b = '01110110101011011001000111000111'
        c = '11111010001010001110000010001001'
        self.assertEquals(des.xor(a, b), c)

    def test_message_to_hex(self):
        """Test that an ASCII string is converted to uppercase hex."""
        a = 'abc123'
        hex = '616263313233'
        self.assertEquals(des.message_to_hex(a), hex)

        a = 'Z0mg kittens! W0wz.'
        hex = '5A306D67206B697474656E7321205730777A2E'
        self.assertEquals(des.message_to_hex(a), hex)

    def test_get_hexwords(self):
        """Test that an ASCII message is broken into 64 bit hex words."""
        msg = 'abc123'
        hexwords = ['6162633132330000']
        self.assertEquals(des.get_hexwords(msg), hexwords)

        msg = 'Your lips are smoother than vaseline'
        hexwords = ['596F7572206C6970', '732061726520736D', '6F6F746865722074',
                    '68616E2076617365', '6C696E6500000000']
        self.assertEquals(des.get_hexwords(msg), hexwords)

    def test_encrypt(self):
        """Test that a message s encrypted via DES."""
        enc = des.encrypt(self.key, 'The message here.')
        s = '3EEB011DC9DF43117BB8DFB26CCB37485EBF13DCEE70A9E1'
        self.assertEquals(enc, s)

    def test_encrypt_hexword(self):
        """Test that a hexword gets DES encrypted."""
        enc = des.encrypt_hexword(self.key, '0123456789ABCDEF')
        s = '85E813540F0AB405'
        self.assertEquals(enc, s)
