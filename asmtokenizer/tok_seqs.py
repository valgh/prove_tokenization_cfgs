# encode with ASMTokenizer
import os
from asmtokenizer import ASMTokenizer as astokenizer
import json


def main():
	cwd = os.getcwd()
	json_file = cwd+'\\pre_load_file.json'
	vocab_path = cwd+'\\vocab_asm.txt'
	asm_tokenizer = astokenizer()
	asm_tokenizer.load_pretrained(vocab_path)
	with open(json_file, 'r') as f:
		seqs = json.load(f)
	out = []
	for seq in seqs:
		out.append(asm_tokenizer.encode(seq))
	print(out)
	for s in out:
		print(len(s))


if __name__ == '__main__':
	main()

# lengths of paths tokenized in this way, without padding/truncate:
#34
#30
#72
#38
#53
#110
#91
#34
#49
#53
#72
#68

# lenghts of paths tokenized by BertTokenizer without padding/truncate:
#133
#121
#253
#141
#195
#377
#319
#129
#183
##191
#257
#245