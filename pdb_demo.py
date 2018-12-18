import pdb

x = [1, 2, 3, 4, 5]
y = 2
z = 3

result = y + z
print(result)

# Set Breaking Point, like gdb
pdb.set_trace()

result2 = y + x
print(result2)
