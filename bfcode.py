import sys

code = []
var_hold = []
var = {}
inp = {}

if len(sys.argv) < 2:
	print("Usage: python3 bfcode.py <filename>")
	sys.exit(1)

file = open(sys.argv[1], 'w')

def write(i):
	global file, code
	n = ord(i)
	code.append(i)
	if n < 11:
		file.write('>'+'+'*n+'.')
	else:
		if n % 10 < 5:
			file.write('>'+'+'*10+'[>'+'+'*(n//10)+'<-]>'+'+'*(n%10)+'.')
		else:
			file.write('>'+'+'*10+'[>'+'+'*(n//10)+'+'+'<-]>'+'-'*(10-(n%10))+'.')

def prnt():
	global file
	file.write('.')

def nl():
	global file, code
	code.append('\n')
	file.write('>++[>+++++<-]>.')

def prnt(c):
	global var, var_hold, code
	l = []
	for e, k in enumerate(c[1:]):
		if k.startswith('$'):
			if k[1:] in var:
				s = int(var[k[1:]].split(':')[0])
				e = int(var[k[1:]].split(':')[1])
				st = ''.join(var_hold[s:e])
				for i in st:
					write(i)
			elif k[1:] in inp:
				s = int(inp[k[1:]])
				num = (len(code)-(s+1))*2
				file.write('<'*num+'.'+'>'*num)
			else:
				print("Error: var not found")
		else:
			for i in k:
				write(i)
		if len(c[1:]) != e+1:
			write(' ')
	nl()

def read(c):
	global var, var_hold, code, inp
	if len(c) > 2:
		prnt(c[1:])
		inp[c[1]] = len(code)
		code.append(',')
		file.write(',')
	else:
		inp[c[1]] = len(code)
		code.append(',')
		file.write(',')


while True:
	c = input("-> ").split()
	if len(c) == 0:
		continue
	elif c[0] == ':x':
		file.close()
		sys.exit(0)
	elif c[0] == 'print':
		if len(c) > 1:
			prnt(c)
		else:
			nl()
	elif c[0] == 'read':
		if len(c) < 2:
			print("Error")
		else:
			read(c)
	elif '=' in c:
		if len(c) < 2:
			print("Error")
		else:
			if '+' in c:
				pass
			else:
				pp = len(var_hold)
				for j in ' '.join(c[2:]):
					var_hold.append(j)
				var[c[0]] = str(pp)+':'+str(len(var_hold))