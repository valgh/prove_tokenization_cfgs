# train ASMTokenizer from scratch
import asmtokenizer
import os
from asmtokenizer import ASMTokenizer as astokenizer


def main():
	cwd = os.getcwd()
	path_input = cwd+'\\input.txt'
	asm_tokenizer = astokenizer()
	asm_tokenizer.train(path_input, min_frequency=1, max_tokens=400, multiprocessing=False)
	# multiprocessing = True -> outputs mp_vocab_asm.txt
	# multiprocessing = False -> outputs vocab_asm.txt
	# and they are the same

if __name__ == '__main__':
	main()