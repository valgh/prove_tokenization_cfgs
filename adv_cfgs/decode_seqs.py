import json
from transformers import BertTokenizer
import os

cwd = os.getcwd()

tok_sequences_path = cwd+'\\tokenized_load_file.json'
cfg_adv_path = cwd+'\\adv_tokenized_load_file.json'
tok_path = cwd+'\\'

tokenizer = BertTokenizer.from_pretrained(tok_path)
with open(tok_sequences_path, 'r') as f:
	seqs_1 = json.load(f)
with open(cfg_adv_path, 'r') as f:
	seqs_2 = json.load(f)

seqs_1_decoded = []
seqs_2_decoded = []

for s in seqs_1:
	s_decoded = tokenizer.decode(s)
	seqs_1_decoded.append(s_decoded)
for s in seqs_2:
	s_decoded = tokenizer.decode(s)
	seqs_2_decoded.append(s_decoded)

print('Decoded sequences without splitting: \n')
print(seqs_1_decoded)
print('\nDecoded sequences with splitting: \n')
print(seqs_2_decoded)