import json
import os


# here we will have also a match with list of operands (because we may have 
# strings in upper case, lowercase check alone is not enough.
#. If it dosn't match, it's a string.

def convert_string(s, operators):
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
      if next_word != None:
        if next_word in operators or next_word.islower() and next_word != 'qword' and next_word != 'ptr' and not next_word.startswith('0x') and not next_word.startswith('['):
          out_string += start+curr_word+' '
        else:
          out_string += start+curr_word+delim
    else:
      if next_word != None:
	      if next_word in operators:
	        out_string += curr_word+' '
	      elif next_word.islower() and next_word != 'qword' and next_word != 'ptr' and not next_word.startswith('0x') and not next_word.startswith('['):
	       	out_string += curr_word+' '
	      else:
	        out_string += curr_word+delim
      else:
        out_string += curr_word
  return out_string

def main():
	cwd = os.getcwd()
	file_path = cwd+'/load_file.json'
	save_file = cwd+'/pre_load_file.json'
	operators = ['AAA', 'AAD', 'AAM', 'AAS', 'ADC', 'ADD', 'AND', 'CALL', 'CBW',
				'CLC', 'CLD', 'CLI', 'CMC', 'CMP', 'CMPSB', 'CMPSW', 'CWD', 'DAA',
				'DAS', 'DEC', 'DIV', 'ESC', 'HLT', 'IDIV', 'IMUL', 'IN', 'INC', 'INT',
				'INTO', 'IRET', 'JCC', 'JMP', 'LAHF', 'LDS', 'LEA', 'LES', 'LOCK', 
				'LODSB', 'LODSW', 'LOOP', 'LOOPE', 'LOOPNE', 'LOOPNZ', 'LOOPZ', 
				'MOV', 'MOVSB', 'MOVSW', 'MUL', 'NEG', 'NOP', 'NOT', 'OR', 'OUT',
				'POP', 'POPF', 'PUSH', 'RCL', 'RCR', 'REP', 'REPE', 'REPNE', 'REPNZ',
				'REPZ', 'RET', 'RETN', 'RETF', 'ROR', 'SAHF', 'SAL', 'SAR', 'SBB', 
				'SCASB', 'SCASW', 'SHL', 'SHR', 'STC', 'STD', 'STI', 'STOSB', 'STOSW', 
				'SUB', 'TEST', 'WAIT', 'XCHG', 'XLAT', 'XOR', 'POPA', 'PUSHA', 'OUTS', 'LEAVE',
				'INS', 'BOUND', 'ENTER', 'ARPL', 'CLTS', 'LAR', 'LGDT', 'LIDT', 'LMSW', 
				'LOADALL', 'LSL', 'LTR', 'SGDT', 'SIDT', 'SLDT', 'SMSW', 'STR', 'VERR', 'VERW',
				'BSF', 'BSR', 'BT', 'BTC', 'BTR', 'BTS', 'CDQ', 'CMPSD', 'CWDE', 'IBTS',
				'INSD', 'IRET', 'JECXZ', 'LFS', 'LGS', 'LSS', 'LOOPW', 'LOOPD', 'MOVSD',
				'MOVSX', 'MOVZX', 'OUTSD', 'POPAD', 'POPFD', 'PUSHFD', 'SCASD', 'SET', 
				'SHLD', 'SHRD', 'STOSD', 'XBTS', 'BSWAP', 'CMPXCHG', 'INVD', 'INVPLPG',
				'WBINVD', 'XADD', 'CPUID', 'RDMSR', 'RDTSC', 'WRMSR', 'RSM', 'CMPXCHG8B',
				'RDPMC', 'SYSCALL', 'SYSRET', 'UD2', 'SYSENTER', 'SYSEXIT', 'PREFETCH0', 
				'PREFETCH1', 'PREFETCH2', 'PREFETCHNTA', 'SFENCE', 'CLFLUSH', 'LFENCE', 'MFENCE'
				'MOVNTI', 'PAUSE', 'MONITOR', 'MWAIT', 'CRC32', 'CDQE', 'CQO', 'CMPSQ', 
				'CMPXCHG16B', 'IRETQ', 'JRCXZ', 'LODSQ', 'MOVSXD', 'POPFQ', 'PUSHFQ', 'RDTSCP',
				'SCASQ', 'STOSQ', 'SWAPGS', 'CLGI', 'INVLPGA', 'SKINIT', 'STGI', 'VMLOAD', 
				'VMMCALL', 'VMRUN', 'VMSAVE', 'VMCLEAR', 'VMREAD', 'VMWRITE', 'VMCALL', 
				'VMLAUNCH', 'VMXOFF', 'VMXON', 'VMRESUME', 'VMPTRST', 'VMPTRLD', 'VMFUNC', 
				'INVEPT', 'INVVPID', 'POPCNT', 'LZCNT', 'ANDN', 'BEXTR', 'BLSI', 'BLSMSK', 'BLSR', 'TZCNT',
				'BZHI', 'MULX', 'PDEP', 'PEXT', 'RORX', 'SARX', 'SHRX', 'SHLX', 'BLCFILL',
				'BLCI', 'BLCIC', 'BLCMSK', 'BLCS', 'BLSFILL', 'BLSIC', 'T1MSKC', 'TZMSK',
				'PCLMULQDQ', 'ADCX', 'ADOX', 'CMOVA', 'CMOVAE', 'CMOVB', 'CMOVBE', 'CMOVC'
				'CMOVE', 'CMOVG', 'CMOVGE', 'CMOVL', 'CMOVLE', 'CMOVNA', 'CMOVNAE', 'CMOVNB',
				'CMOVNBE', 'CMOVNC', 'CMOVNE', 'CMOVNG', 'CMOVNGE', 'CMOVNL', 'CMOVNLE', 'CMOVNO', 
				'CMOVNP', 'CMOVNS', 'CMOVNZ', 'CMOVO', 'CMOVP', 'CMOVPE', 'CMOVPO', 'CMOVS',
				'CMOVZ', 'PCLMULLQLQDQ', 'PCLMULHQLQDQ', 'PCLMULLQHQDQ', 'PCLMULHQHQDQ', 'JG', 'JNG',
				'JNZ', 'JZ', 'JMP', 'JE', 'JNE', 'JL', 'JNL']
	operands = [] # this will be the list of registers and other values like FS/CS/etc..
	with open(file_path, 'r') as f:
		to_preprocess = json.load(f)
	preprocessed = []
	for seq in to_preprocess:
		seq_preprocessed = convert_string(seq, operators)
		preprocessed.append(seq_preprocessed)
	with open(save_file, 'w') as f:
		json.dump(preprocessed, f)
	print('\n')
	print('Done. Exiting...')
	return

if __name__ == '__main__':
	main()
