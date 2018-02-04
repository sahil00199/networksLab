from decode import decode
from encode import encode

message = "100010001"
encoded = encode(message)
wrongMessage = "000000000"
rec = decode(wrongMessage + encoded)
print(rec)
print(message == rec)