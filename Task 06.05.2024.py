"""
Переписать задачи из предыдущего урока для байтовых строк
(массивов байт)
"""

s = b"Ezheviku dlja ezhat " \
    b"Prinesli dva ezha. " \
    b"Ezheviku ele-ele" \
    b"Ezhata vozle eli s'eli."

count_E = s.count(b'E')
count_e = s.count(b' e')
count_res = count_E + count_e
print('Count: ', count_res)
