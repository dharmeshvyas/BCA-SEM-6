def hash_table(key,m):
    return key % m

m =7
print(f'the hash table for 3 is {hash_table(3,m)}')
print(f'the hash table for 2 is {hash_table(2,m)}')
print(f'the hash table for 9 is {hash_table(9,m)}')
print(f'the hash table for 11 is {hash_table(11,m)}')
print(f'the hash table for 7 is {hash_table(7,m)}')