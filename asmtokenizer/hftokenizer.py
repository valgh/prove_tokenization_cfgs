# a way more efficient tokenizer to be trained on large 
# dataset, with equal vocabs we find in asmtokenizer

import os
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace, CharDelimiterSplit
from tokenizers.processors import TemplateProcessing


def main():
	cwd = os.getcwd()
	path_to_train = [cwd+'\\input.txt']
	tokenizer = Tokenizer(BPE())
	tokenizer.pre_tokenizer = CharDelimiterSplit(' ')
	tokenizer.post_processor = TemplateProcessing(
    	single="[CLS] $A [SEP]",
    	pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    	special_tokens=[("[CLS]", 1), ("[SEP]", 2)],
    )
	trainer = BpeTrainer(vocab_size=400, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
	tokenizer.train(trainer, files=path_to_train)
	print('Done.')
	tokenizer.save(cwd+'\\vocab_hftok.json')



if __name__ == '__main__':
	main()
