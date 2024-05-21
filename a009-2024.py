# 金鑰 = ord(明文字元) - ord(密文字元)
key = ord('*') - ord('1')

line = input()
for ciphertext in line:
    plaintext = chr(ord(ciphertext) + key)
    print(plaintext, end='')