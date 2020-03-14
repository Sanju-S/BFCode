import sys

code = []
var_hold = []
var = {}
inp = {}

file = open('/home/sanju/code/bf/test.bf', 'w')

def write(i):
	global file
	n = ord(i)
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
	global file
	file.write('>++[>+++++<-]>.')

def prnt(c):
	global var, var_hold
	l = []
	for k in c[1:]:
		if k.startswith('$'):
			if k[1:] in var:
				s = int(var[k[1:]].split(':')[0])
				e = int(var[k[1:]].split(':')[1])
				st = ''.join(var_hold[s:e])
				l.append(st)
			else:
				print("Error: var not found")
		else:
			l.append(k)
	l = ' '.join(l)
	for i in l:
		code.append(i)
		write(i)
	nl()


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
	elif c[1] == '=':
		if len(c) < 2:
			print("Error")
		else:
			if c[3] in ['+', '-']:
				pass
			else:
				pp = len(var_hold)
				for j in ' '.join(c[2:]):
					var_hold.append(j)
				var[c[0]] = str(pp)+':'+str(len(var_hold))