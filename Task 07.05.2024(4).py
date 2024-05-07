"""
Необходимо декодировать закодированную строку:
"""

encoded_s = b'\xd0\xa3\xd1\x87\xd0\xb5\xd1\x81\xd1\x82'

decoded_s = encoded_s.decode()
print(decoded_s)