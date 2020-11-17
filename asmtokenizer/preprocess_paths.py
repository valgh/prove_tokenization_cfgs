import json
import os


def preprocess_string(s, operators):
	start = 'X_'
	delim = '_'
	out_string = ''
	string_split = s.split() # splits on space char
	l = len(string_split)
	for ix in range(l):
		curr_word = string_split[ix]
		if ix < l-1:
			next_word = string_split[ix+1]
		else:
			next_word = None
		if curr_word in operators:
			out_string += start+curr_word+delim
		elif curr_word == 'RET':
			if next_word is None:
				out_string += start+curr_word
			else:
				out_string += start+curr_word+' '
		else:
			if next_word in operators or next_word == 'RET':
				out_string += curr_word+' '
			elif next_word != None:
				out_string += curr_word+delim
			else:
				out_string += curr_word
	return out_string

def main():
	cwd = os.getcwd()
	file_path = cwd+'\\load_file.json'
	save_file = cwd+'\\pre_load_file.json'
	operators = ['MOV', 'CALL', 'JNZ', 'JZ', 'JMP', 'XOR', 'MOVSXD', 'MOVSX', 'JG', 'ADD', 'LEA', 'PUSH', 'POP', 'SUB', 'TEST']
	with open(file_path, 'r') as f:
		to_preprocess = json.load(f)
	preprocessed = []
	for seq in to_preprocess:
		seq_preprocessed = preprocess_string(seq, operators)
		preprocessed.append(seq_preprocessed)
	with open(save_file, 'w') as f:
		json.dump(preprocessed, f)
	print('\n')
	print('Done. Exiting...')
	return

if __name__ == '__main__':
	main()


####### Output for one string:
##
##
#Original string:
#
#MOV qword ptr [RSP] IMM MOV qword ptr [RSP 0x10] IMM MOV RDI RBX JNZ IMM XOR EAX EAX MOV RDI R13        
#LEA R13 [RSP 0x20] MOV R12 RAX CALL sigemptyset CALL FUN PUSH R13 PUSH R12 PUSH RBP PUSH RBX MOV RBX RDI MOV RBP RAX SUB RSP 0xb8
#TEST EAX EAX CALL FUN MOV RSI RAX CALL FUN MOV EAX dword ptr [R12 0xd8] MOV RDI RBX MOV RAX qword ptr FS [0x28]
#
#String preprocessed:
#
#X_MOV_qword_ptr_[RSP]_IMM X_MOV_qword_ptr_[RSP_0x10]_IMM X_MOV_RDI_RBX X_JNZ_IMM_XOR_EAX_EAX X_MOV_RDI_R13 X_LEA_R13_[RSP_0x20] 
#X_MOV_R12_RAX X_CALL_sigemptyset X_CALL_FUN X_PUSH_R13 X_PUSH_R12 X_PUSH_RBP X_PUSH_RBX X_MOV_RBX_RDI X_MOV_RBP_RAX X_SUB_RSP_0xb8 
#X_TEST_EAX_EAX X_CALL_FUN X_MOV_RSI_RAX X_CALL_FUN X_MOV_EAX_dword_ptr_[R12_0xd8] X_MOV_RDI_RBX X_MOV_RAX_qword_ptr_FS_[0x28]