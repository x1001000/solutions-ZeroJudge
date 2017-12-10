key = ord('*') - ord('1')           # key = 右邊明文 - 左邊密文
while True:
    try:
        ciphertext = input()
    except:
        break
    plaintext = ''
    for x in ciphertext:
        plaintext += chr(ord(x)+key)# 右邊明文 = 左邊密文 + key
    print(plaintext)