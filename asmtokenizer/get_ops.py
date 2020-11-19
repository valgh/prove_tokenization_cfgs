# get string operations from file
import os

cwd = os.getcwd()
path = cwd+'\\operations_x86.txt'
out = cwd+'\\op_x86.txt'
ops = []
with open(path, 'r') as f:
	lines = f.readlines()
	for line in lines:
		op = line.strip().split('=')
		ops.append(op[1][:-1][1:].upper()) # get rid of "", to upper case)
ops.append('JNZ')
ops.append('JNE')
ops.append('JG')
ops.append('JGE')
ops.append('JZ')
ops.append('JA')
ops.append('JAE')
ops.append('JL')
ops.append('JLE')
ops.append('JB')
ops.append('JBE')
ops.append('JO')
ops.append('JNO')
ops.append('JS')
ops.append('JCXZ')
ops.append('JECXZ')
ops.append('JRCXZ')
with open(out, 'w') as f:
	for op in ops:
		f.write(op)
		f.write('\n')
print('Done.')