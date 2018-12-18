myfile = open('aaabbbbccccc.txt')

print('==== FILE CONENT ====')
content = myfile.read()
print(content)

print('==== FILE CONENT ====')
content = myfile.read()
print('Read the again will result in empty content')
print(content)

print('==== READ AGAIN ====')
print('To read again, you need to reset the cursor')
myfile.seek(0)

list_of_lines = myfile.readlines()
print(list_of_lines)

myfile.close()


with open('aaabbbbccccc.txt', mode = 'r') as f:
	# After the block, the file will be closed.
	print(f.read())


with open('test_write.txt', mode = 'w') as f:
	# After the block, the file will be closed.
	f.write('This is the first line.\n')
	f.write('This is the second line.\n')

with open('test_append.txt', mode = 'a') as f:
	# After the block, the file will be closed.
	f.write('More lines is appended.\n')
