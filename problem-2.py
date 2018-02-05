# Find the next n-th character in the alphabet from a given character
def findNthChar(char, n):
    return chr(ord(char) + n);

print findNthChar('a', 2); # c

hint = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

for char in hint:
    nextChar = findNthChar(char, 2)
    print nextChar,
