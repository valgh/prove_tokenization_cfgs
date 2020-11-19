import json
import os
import re

def filter_registers(asm_str):
	asm_str = re.sub(r'\b[RE]?[IS]P\b', 'REGPOINT', asm_str)
	asm_str = re.sub(r'\b[DA][HL]\b', 'REGDATA8', asm_str)
	asm_str = re.sub(r'\bRCX|R[0-9][0-5]?\b', 'REGGEN64', asm_str)
	asm_str = re.sub(r'\bECX|R[0-9][0-5]D?\b', 'REGGEN32', asm_str)
	asm_str = re.sub(r'\bCX|R[0-9][0-5]?W\b', 'REGGEN16', asm_str)
	asm_str = re.sub(r'\b[SD]IL|B[HP]L\b', 'REGADDR8', asm_str)
	asm_str = re.sub(r'\bC[HL]|R[0-9][0-5]?B\b', 'REGGEN8', asm_str)
	asm_str = re.sub(r'\b[DA]X\b', 'REGDATA16', asm_str)
	asm_str = re.sub(r'\bR[SD]I\b|\bRB[PX]\b', 'REGADDR64', asm_str)
	asm_str = re.sub(r'\bE[SD]I\b|\bEB[PX]\b', 'REGADDR32', asm_str)
	asm_str = re.sub(r'\b[SD]I\b|\bB[PX]\b', 'REGADDR16', asm_str)
	asm_str = re.sub(r'\bE[DA]X\b', 'REGDATA32', asm_str)
	asm_str = re.sub(r'\bR[DA]X\b', 'REGDATA64', asm_str)
	asm_str = re.sub(r'\bST[0-7]\b|\bXMM[0-9][0-5]?\b|\bFP[CS]R\b|\bFPTAG\b|\bFP[ID]\b \
						|\bMXCSR\b|\bMXCSR_MASK\b|\bXMM[0-7]_[LH]\b|\bXMM[189][0-5]?_[LH]\b', 'REGFLOAT', asm_str)
	return asm_str

def convert_string(s, operators, operands, not_to_sub, segments):
	delim = '_'
	out_string = ''
	string_split = s.split() # splits on space char
	l = len(string_split)
	for ix in range(l):
		curr_word = string_split[ix]
		next_word = None
		if ix < l-1:
			next_word = string_split[ix+1]
		if curr_word in operators:
			if next_word != None:
				if next_word in operators:
					out_string += curr_word+' '
				elif next_word in operands or next_word in not_to_sub or next_word in segments or next_word.startswith('[') or next_word.startswith('0x') or next_word[-1] == ']':
					out_string += curr_word+delim
				else:
					out_string += curr_word+' ' #it's a string
		else:
			if next_word != None:
				if next_word in operators:
					out_string += curr_word+' '
				elif next_word in operands or next_word in not_to_sub or next_word in segments or next_word.startswith('[') or next_word.startswith('0x') or next_word[-1] == ']':
					out_string += curr_word+delim
				else:
					out_string += curr_word+' ' #it's a string
			else:
				out_string += curr_word # last word
	return out_string

def main():
	cwd = os.getcwd()
	file_path = cwd+'\\load_file.json'
	save_file = cwd+'\\pre_load_file.json'
	operators_file = cwd+'\\op_x86.txt'
	operators = []
	operands = ['REGPOINT', 'REGFLOAT', 'REGGEN64', 'REGGEN32', 'REGGEN16', 'REGGEN8',
				'REGDATA64', 'REGDATA32', 'REGDATA16', 'REGDATA', 'REGADDR64', 'REGADDR32','REGADDR16', 'REGADDR8']
	not_to_sub = ['qword', 'dword', 'ptr', 'IMM', 'MEM', 'BB', 'FUN']
	segments = ['FS', 'ES', 'GS', 'CS', 'DS', 'SS']
	with open(operators_file, 'r') as f:
		while True:
			op = f.readline()
			if op:
				operators.append(op.strip())
			else:
				break
	with open(file_path, 'r') as f:
		to_preprocess = json.load(f)
	preprocessed = []
	for seq in to_preprocess:
		seq_filtered = filter_registers(seq)
		seq_preprocessed = convert_string(seq_filtered, operators, operands, not_to_sub, segments)
		preprocessed.append(seq_preprocessed)
	with open(save_file, 'w') as f:
		json.dump(preprocessed, f)
	print('\n')
	print('Done. Exiting...')
	return

if __name__ == '__main__':
	main()