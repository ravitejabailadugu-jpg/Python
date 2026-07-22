b=bytes([10,20,30,40,50])
ba=bytearray([10,20,30,40,50])
fz=frozenset({10,20,30,40,50})
print(10 in b)
print(10 in ba)
print(102 in fz)



b=bytes([1,2,3,4,5])
ba=bytearray([1,2,3,4,5,])
fz=frozenset({1,2,3,4,5,})
print(1 not in b)
print(2 not in ba)
print(8 not in fz)