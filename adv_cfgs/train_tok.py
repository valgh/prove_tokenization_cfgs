from tokenizers import BertWordPieceTokenizer
import os

cwd = os.getcwd()
path_to_train = cwd+'\\tok_train.txt'
path_to_save = cwd+'\\'
bert_tokenizer = BertWordPieceTokenizer()
print('Training tokenizer...\n')
bert_tokenizer.train(files=path_to_train, vocab_size=400, min_frequency=1, special_tokens=["[SEP]", "[CLS]", "[PAD]", "[UNK]", "[MASK]"])
print('Finished training.\n')
bert_tokenizer.save_model(path_to_save)