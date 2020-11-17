###############
# tokenize seqs
###############
from transformers import BertTokenizer
import json
import os


def tokenize(sequences, tokenizer, out_path):
    json_file = 'tokenized_load_file.json'
    out_seqs = []
    for seq in sequences:
        tok_seq = tokenizer.encode(seq)
        out_seqs.append(tok_seq)
    with open(out_path + json_file, 'w') as f:
        json.dump(out_seqs, f)
    print('\nDone.\n')


def main():
    cwd = os.getcwd()
    pretrained = cwd+'\\'
    path_seqs = cwd+'\\load_file.json'
    bert_tokenizer = BertTokenizer.from_pretrained(pretrained)
    with open(path_seqs, 'r') as f:
        sequences = json.load(f)
    tokenize(sequences, bert_tokenizer, out_path=pretrained)
    print('\nExit.\n')


if __name__ == '__main__':
    main()
