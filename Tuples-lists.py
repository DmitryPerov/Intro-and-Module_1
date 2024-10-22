Immutable_tuple = (1, 2, 'a', 'b')
# Immutable_tuple[1] = 20    -  error
Immutable_tuple += (1, 2, [10, 15, 20])

Mutable_list = [1, 2, 'a', 'b', 'Modified']
Mutable_list[4] = 12
print (Immutable_tuple, Mutable_list, sep = '\n')
