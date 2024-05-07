s = b"Lewa na polke klopa nawel"
s = s.lower()
s = s.replace(b' ', b'')

rev_s = s[::-1]

print(s)
print(rev_s)

print('Палиндром: ', s ==rev_s)