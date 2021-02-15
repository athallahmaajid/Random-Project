print('input txt file path:')
while True:
	try:
		input_path = input()
		with open(input_path, 'r') as f:
			text = f.read()
	except FileNotFoundError:
		print('Please input correctly')
	else:
		break
print('output txt file path:')
output_path = input()
out = open(output_path, 'w+')
while True:
	print('Choose\n1.Binary to String\n2.String to binary')
	method = input()
	if method not in ('1', '2'):
		pass
	else:
		break

def to_binary(string):
    return "".join([format(ord(char),'#010b')[2:] for char in string])
def to_string(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])
if method == '1':
	out.write(to_string(text))
elif method == '2':
	out.write(to_binary(text))
out.close()