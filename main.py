import time
import multiprocessing

def calc_square(numbers):
	for n in numbers:
		print("Process 1: Working")
		print('Squared = ' + str(n*n) + "\n")


def calc_cube(numbers):
	for n in numbers:
		print("Process 2: Working")
		print('Cubed = ' + str(n*n*n) + "\n")

if __name__	 == "__main__":
	arr = [2,3,8,9]
	p1 = multiprocessing.Process(target=calc_square, args=(arr,)) #the reason that we are using (arr,)) is because the arguement is a tuple. The line of code is setting a process 1 to do calculating the square root.
	p2 = multiprocessing.Process(target=calc_cube, args=(arr,)) #this line is doing process #2 to do calculating cubed


	p1.start()
	p2.start()

	p1.join()
	p2.join()
	print("Done!")