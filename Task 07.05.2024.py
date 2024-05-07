"""
Дана строка, заканчивающаяся точкой.
Подсчитать, сколько слов в строке.
"""

s = b"Ezheviku dlja ezhat; Prinesli dva ezha."

s = s.replace(b',', b'')
s = s.replace(b';', b'')
s = s.replace(b':', b'')
s = s.replace(b'.', b'')

l = s.split()
print()

count = len(l)
print('Count: ', count)
