# train ASMTokenizer from scratch
import asmtokenizer
import os
from asmtokenizer import ASMTokenizer as astokenizer


def main():
	cwd = os.getcwd()
	path_input = cwd+'\\input.txt'
	asm_tokenizer = astokenizer()
	asm_tokenizer.train(path_input, 1, 400)

if __name__ == '__main__':
	main()