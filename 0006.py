a = 10
b = 20
c = b >> 2
#c的二进制后面8位为00010100，因此右移2为变为00000101
#因此为5
print(c)
d = a & b
#a的二进制后面8为为00001010//00010100
#因此为0
print(d)
