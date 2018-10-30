import math
import textwrap

initial_number = input('Введите исходное число: ')
base = input('Введите систему исходного числа: ')
target_base = input('Введите систему целевого числа: ')

# Находим степень двойки
def find_two_power(number):
	count = 1
	while True:
		number = number / 2
		if number == 1:
			return count
		else:
			count = count + 1

# получаем ключ по значению
def get_key_by_value(dictionary, search_value):
	for key, value in dictionary.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
	    if value == search_value:
	        return key

# Определяем на сколько разрядов нужно разбить число
if int(target_base) == 2:
	divide_into = find_two_power(int(base))

translate_table_64 = {
	'000000': '0', '000001': '1', '000010': '2', '000011': '3', '000100': '4', '000101': '5', '000110': '6', '000111': '7',
	'001000': '8', '001001': '9', '001010': 'A', '001011': 'B', '001100': 'C', '001101': 'D', '001110': 'E', '001111': 'F',
	'010000': 'G', '010001': 'H', '010010': 'I', '010011': 'J', '010100': 'K', '010101': 'L', '010110': 'M', '010111': 'N',
	'011000': 'O', '011001': 'P', '011010': 'Q', '011011': 'R', '011100': 'S', '011101': 'T', '011110': 'U', '011111': 'V',
	'100000': 'W', '100001': 'X', '100010': 'Y', '100011': 'Z'
}

translate_table_32 = {
	'00000': '0', '00001': '1', '00010': '2', '00011': '3', '00100': '4', '00101': '5', '00110': '6', '00111': '7',
	'01000': '8', '01001': '9', '01010': 'A', '01011': 'B', '01100': 'C', '01101': 'D', '01110': 'E', '01111': 'F',
	'10000': 'G', '10001': 'H', '10010': 'I', '10011': 'J', '10100': 'K', '10101': 'L', '10110': 'M', '10111': 'N',
	'11000': 'O', '11001': 'P', '11010': 'Q', '11011': 'R', '11100': 'S', '11101': 'T', '11110': 'U', '11111': 'V'
}

translate_table_16 = {
	'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
	'1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

translate_table_8 = {
	'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'
}

translate_table_4 = {
	'00': '0', '01': '1', '10': '2', '11': '3'
}

# Определяем таблицу по числу
def define_table_by_number(n):
	if n == '64':
		print('Вибираю систему 64')
		return translate_table_64
	if n == '32':
		print('Вибираю систему 32')
		return translate_table_32
	if n == '16':
		print('Вибираю систему 16')
		return translate_table_16
	if n == '8':
		print('Вибираю систему 8')
		return translate_table_8
	if n == '4':
		print('Вибираю систему 4')
		return translate_table_4

# если исходная система больше целевой 8 -> 2
if int(base) > int(target_base):
	# разбиваем число на части	
	nums = list(initial_number)
	print('Числа которые нужно перевести: ', nums)
	# переводим по таблице
	s = ''
	d = define_table_by_number(base)
	for num in nums:
		s = s + get_key_by_value(d, num)

	print('Result of {}({})->?({}) is: {}'.format(initial_number, base, target_base, int(s)))
