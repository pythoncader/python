import reused.font as font
import sys

def producter(mylist):
	multiplicationterms = []
	for i in range(0, len(mylist)):
		if '*' in mylist[i]:
			multiplicationterms.append(mylist[i-1])
			multiplicationterms.append(mylist[i])
			print('multiplication terms: ', multiplicationterms)

			newstring = multiplicationterms[1].replace('*', '')
			multiplicationterms[1] = newstring
			
			if 'x' not in mylist[i] and 'x' not in mylist[i - 1]:
				first = float(multiplicationterms[0])
				second = float(multiplicationterms[1])
				multiplied = first * second
				print(multiplied)
		
				mylist[i] = str(multiplied)
				mylist[i - 1] = ''
				print(mylist)

				multiplicationterms.clear()
			
			elif 'x' in multiplicationterms[0] and 'x' not in multiplicationterms[1]:
				if 'x' != multiplicationterms[0]: 
					newstring = multiplicationterms[0].replace('x', '')
					multiplicationterms[0] = newstring
				elif 'x' == multiplicationterms[0]:
					newstring = multiplicationterms[0].replace('x', '1')
					multiplicationterms[0] = newstring

				first = float(multiplicationterms[0])
				second = float(multiplicationterms[1])
				multiplied = first * second
				print(str(multiplied) + 'x')
		
				mylist[i] = str(multiplied) + 'x'
				mylist[i - 1] = ''
				print(mylist)

				multiplicationterms.clear()
			
			elif 'x' not in multiplicationterms[0] and 'x' in multiplicationterms[1]:
				if 'x' != multiplicationterms[1]: 
					newstring = multiplicationterms[1].replace('x', '')
					multiplicationterms[1] = newstring
				elif 'x' == multiplicationterms[1]:
					newstring = multiplicationterms[1].replace('x', '1')
					multiplicationterms[1] = newstring

				first = float(multiplicationterms[0])
				second = float(multiplicationterms[1])
				multiplied = first * second
				print(str(multiplied) + 'x')
		
				mylist[i] = str(multiplied) + 'x'
				mylist[i - 1] = ''

				multiplicationterms.clear()
			
			elif 'x' in multiplicationterms[0] and 'x' in multiplicationterms[1]:
				print(font.textcolors.bold + font.textcolors.fail +'\nThis is not a valid equation (This is a quadratic equation)', font.textcolors.endc) #Throw an error
				sys.exit()


	while '' in mylist:
		mylist.remove('')
	for i in range(0, len(mylist)):
		if '+' not in mylist[i] and "/" not in mylist[i]:
			if '-' not in mylist[i]:
				mylist[i] = '+' + mylist[i]
	print("line 75 in multiplication terms", mylist)
	return mylist