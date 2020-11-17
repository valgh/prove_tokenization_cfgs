###################
# advanced_cfg
###################
import json
import os


def split_path(p, max_length):
	first_split_point = max_length-1
	middle_split_point = max_length-2
	first = p[:first_split_point]
	last = p[-(first_split_point):]
	rest = p[first_split_point:]
	rest = rest[:-(first_split_point)]
	P = [rest[x:x+middle_split_point] for x in range(0, len(rest), middle_split_point)]
	return first, last, P


def longest_sequence(F_out, p, max_length, boundary, sep_token, cls_token, pad_token):
	first, last, P = split_path(p, max_length)
	xf = pad(first, max_length, sep_token, cls_token, pad_token)
	if xf not in F_out and len(F_out) < boundary:
		F_out.append(xf)
	xl = pad(last, max_length, sep_token, cls_token, pad_token, end_seq=True)
	if xl not in F_out and len(F_out) < boundary:
		F_out.append(xl)
	for x in P:
		if len(F_out) == boundary:
			break
		x = pad(x, max_length, sep_token, cls_token, pad_token, middle_seq=True)
		if x not in F_out:
			F_out.append(x)
	return F_out


def split_in_half(p):
	half = len(p)//2
	return p[:half], p[half:]


def longer_sequence(p, max_length, sep_token, cls_token, pad_token):
	p1, p2 = split_in_half(p)
	p1 = pad(p1, max_length, sep_token, cls_token, pad_token)
	p2 = pad(p2, max_length, sep_token, cls_token, pad_token, end_seq=True)
	return p1, p2


def pad(p, max_length, sep_token, cls_token, pad_token, end_seq=False, middle_seq=False):
	if middle_seq:
		p = [cls_token] + p
		p.append(sep_token)
	elif end_seq:
		p = [cls_token] + p # append cls_token
	else:
		p.append(sep_token) # append sep_token
	while len(p) != max_length:
		p.append(pad_token)
	return p


def adv_cfg(sequences, max_length, boundary=20, sep_token=0, cls_token=1, pad_token=2):
	F_out = []
	for p in sequences:
		if len(F_out) < boundary:
			if len(p) < max_length:
				p_out = pad(p, max_length, sep_token, cls_token, pad_token)
				F_out.append(p_out)
			elif len(p) <= (2*(max_length)-2):
				p1, p2 = longer_sequence(p, max_length, sep_token, cls_token, pad_token)
				if p1 not in F_out:
					F_out.append(p1)
				if p2 not in F_out and len(F_out) < boundary:
					F_out.append(p2)
			else:
				F_out = longest_sequence(F_out, p, max_length, boundary, sep_token, cls_token, pad_token)
		else:
			break
	return F_out


def trial():
	cwd = os.getcwd()
	tok_sequences_path = cwd+'\\tokenized_load_file.json'
	cfg_adv_path = cwd+'\\adv_tokenized__load_file.json'
	with open(tok_sequences_path, 'r') as f:
		tok_sequences = json.load(f)
	max_length = 100
	out = adv_cfg(tok_sequences, max_length)
	for p in tok_sequences:
		print(p)
		print('\n')
	print('\n')
	for b in out:
		print(len(b))
		print(b)
	print(len(tok_sequences))
	print(len(out))


def main():
	cwd = os.getcwd()
	tok_sequences_path = cwd+'\\tokenized_load_file.json'
	cfg_adv_path = cwd+'\\adv_tokenized_load_file.json'
	with open(tok_sequences_path, 'r') as f:
		tok_sequences = json.load(f)
	max_length = 100
	out = adv_cfg(tok_sequences, max_length)
	with open(cfg_adv_path, 'w') as f:
		json.dump(out, f)
	print('Done.')



if __name__ == '__main__':
	main()