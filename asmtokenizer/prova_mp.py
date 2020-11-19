#### prova apply_async + shared dict
import multiprocessing as mp
from multiprocessing import Manager, Lock

def func_add(d):
	print('called.')
	if 'hello' in d:
		d['hello'] +=1
	else:
		d['hello'] = 1
	lock.release()
	print(d)
	return


def main():
	manager = Manager()
	vocabulary = manager.dict()
	pool = mp.Pool(2)
	for i in range(10):
		pool.apply_async(func_add, (vocabulary,))
	pool.close()
	pool.join()
	print(vocabulary)




if __name__ == '__main__':
	main()