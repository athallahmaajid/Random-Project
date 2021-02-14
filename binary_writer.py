print('txt file path:')
while True:
	try:
		input_path = input()
		with open(input_path, 'r') as f:
			text = f.read()
	except FileNotFoundError:
		print('Please input correctly')
	else:
		break
print('output txt file path')
output_path = input()
out = open(output_path, 'w+')
l = []
res = []
for i in text:
    l.append(ord(i))
for i in l:
    res.append(bin(i)[2:])
out.write(''.join(res))
out.close()