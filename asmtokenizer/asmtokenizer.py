#####################
## ASMTokenizer
#####################

import os


class ASMTokenizer:
	""" Tokenizer for ASM language to give as input to BERT """
	def __init__(self):
		self.vocab = {}
		self.decode_vocab = {}
		self.default_file_name = 'vocab_asm.txt'
		self.min_frequency = 2
		self.max_tokens = 32000
		self.max_len_tokens = 100000


	def get_vocab_length(self):
		return len(self.vocab)


	def process_line(self, line):
		words = line.split() # split on space char
		for word in words:
			if word not in self.vocab:
				self.vocab[word] = 1
			else:
				self.vocab[word] += 1
		return

	def train(self, path_to_vocab, min_frequency, max_tokens):
		assert isinstance(path_to_vocab, str)
		if not os.path.exists(path_to_vocab):
			print('ERROR: Invalid path input.')
			return None
		if max_tokens > self.max_len_tokens:
			print('ERROR: max_tokens > 100.000')
			return
		self.min_frequency = min_frequency
		self.max_tokens = max_tokens
		with open(path_to_vocab, 'r') as f:
			while True:
				line = f.readline()
				if not line:
					break
				if line == '\n':
					continue
				else:
					self.process_line(line.strip())
		print('Training process complete.\n')
		self.save(os.getcwd())
		print('Vocab file saved under your cwd as {}'.format(self.default_file_name))
		print('\nReload the tokenizer with load_pretrained method to use it.')
		return


	def save(self, path_to_save):
		assert isinstance(path_to_save, str)
		if not os.path.exists(path_to_save):
			print('ERROR: Invalid path input.')
			return None
		if not self.vocab:
			print('ERROR: you have not trained this tokenizer!')
			return
		print('Saving results, might take a while...')
		to_save_vocab = sorted(self.vocab.items(),
							key=lambda item: item[1],
							reverse=True)
		if path_to_save[:-1] != '/':
			path_to_save = path_to_save+'/'
		with open(path_to_save+self.default_file_name, 'w') as f:
			f.write('[CLS]')
			f.write('\n')
			f.write('[SEP]')
			f.write('\n')
			f.write('[UNK]')
			f.write('\n')
			f.write('[PAD]')
			f.write('\n')
			f.write('[MASK]')
			f.write('\n')
		count = 5
		with open(path_to_save+'\\'+self.default_file_name, 'a') as f:
			for v in to_save_vocab:
				if v[1] >= self.min_frequency:
					count+=1
					f.write(v[0])
					f.write('\n')
				if count > self.max_tokens:
					break
		return


	def load_pretrained(self, path_to_pretrained):
		assert isinstance(path_to_pretrained, str)
		if not os.path.exists(path_to_pretrained):
			print('ERROR: Invalid path input.')
			return None
		self.vocab = {}
		self.decode_vocab = {}
		index = 0
		with open(path_to_pretrained, 'r') as f:
			while True:
				line = f.readline()
				if not line:
					break
				self.vocab[line.strip()] = index
				self.decode_vocab[index] = line.strip()
				index+=1
		print('Tokenizer loaded.')
		return


	def encode(self, line):
		output = []
		for word in line.split():
			if word in self.vocab:
				encoding = self.vocab[word]
			else:
				encoding = self.vocab['[UNK]']
			output.append(encoding)
		return output


	def decode(self, seq):
		output = ''
		for s in seq:
			output += self.decode_vocab[s]+' '
		return output



	def __call__(self, line):
		""" This will have to implement also BERT masks etc.."""

