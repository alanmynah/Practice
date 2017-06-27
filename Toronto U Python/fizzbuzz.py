def fizzbuzz(numForFizz, numForBuzz):
	
	range_start = int(input('Start: '))
	range_finish = int(input('Finish:'))
	for numGenerated in range(range_start, range_finish+1):
		message = ''
		if numGenerated % numForFizz == 0:
			message += 'Fizz'
		if numGenerated % numForBuzz == 0:
			message += 'Buzz'
		print(message or numGenerated)


def fizzbuzz(numForFizz, numForBuzz, range_start, range_finish):
	
	for numGenerated in range(range_start, range_finish+1):
		message = ''
		if numGenerated % numForFizz == 0:
			message += 'Fizz'
		if numGenerated % numForBuzz == 0:
			message += 'Buzz'
		print(message or numGenerated)
