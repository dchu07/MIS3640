#chr(ord('K')+2)

encrypted_msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
decoded_msg = ''
for letter in encrypted_msg:
    if letter.isalpha():
        decoded_msg += chr(ord(letter)+2)
    else:
        decoded_msg += letter
print(decoded_msg)

import math
ratio = 100
print(math.log10(ratio))
