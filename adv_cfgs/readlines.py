import json
import os


def main():
	cwd = os.getcwd()
	json_file = cwd+'\\load_file.json'
	tok_train = cwd+'\\tok_train.txt'
	with open(json_file, 'r') as f:
		sequences = json.load(f)
	with open(tok_train, 'w') as f:
		for seq in sequences:
			f.write(seq)
			f.write('\n')
			f.write('\n')
	print('Readlines: done.')


if __name__ == '__main__':
	main()