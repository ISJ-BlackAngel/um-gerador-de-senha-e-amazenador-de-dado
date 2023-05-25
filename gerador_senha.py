# bot_get_information_interweb.py
import os
try:
	import PySimpleGUI as sg
except:
	os.system('pip install pysimplegui')
	import PySimpleGUI as sg
import random, json


def gerator_password(digites, integers=True, upper_letter=True, specios_char=True):
	# from random import choice
	abc = 'qwertyuiopasdfghjklzxcvbnm'
	ABC = abc.upper()
	num = '1234567890'
	specius = '!@#$%&Çç'
	char_disponible = abc.replace('', ' ').split()
	if (integers): char_disponible.extend(num.replace('', ' ').split())
	if (upper_letter): char_disponible.extend(ABC.replace('', ' ').split())
	if (specios_char): char_disponible.extend(specius.replace('', ' ').split())
	return str(''.join([random.choice(char_disponible*2) for x in range(digites)]))

def save_passwords(passwords=[]):
	try:
		with (open('senhar.json', 'w')) as arquivo:
			arquivo.write(json.dumps(passwords, indent=4))
	except Exception as error:
		print(error)

def loading_passwords():
	try:
		with(open('senhar.json', 'r')) as file:
			return json.loads(file)
	except:
		return []

# integers = True
# upper_letter = True
# specios_char = False
# [print(f'password-{gerator_password(20, integers, upper_letter, specios_char)}') for _ in range(100)]
font_family = ('courier new', 16)

layout = [
	[sg.Text('Quantidade de senhar pra gerar'.title(), font=font_family), sg.Push(), sg.Button('Mostrar Todas as Senhas', key='-show-', font=font_family)],
	[sg.Input('25', key='-input-', size=(50, 1), font=font_family), sg.Push(), sg.Button('Gerar', key='-gerator-', font=font_family)],
	[sg.Text('tamanho da senha:'.upper(), font=font_family), sg.Input('25', key='-size-', size=(2, 1), font=font_family)],
	[sg.Output(key='terminal', size=(56, 15), font=font_family)]
]
window = sg.Window('Gerador de senha', layout, finalize=True)
all_passwords = loading_passwords()

while(True):
	event, values = window.read()
	if (event == sg.WIN_CLOSED):
		break
	if (event == '-gerator-'):
		roll = 10
		size_string = 25
		if (values['-input-'].strip().isnumeric()):
			roll = int(values['-input-'])
		if (values['-size-'].strip().isnumeric()):
			size_string = int(values['-size-'])
		window['terminal'].update('')
		for _ in range(roll):
			new_password = gerator_password(size_string)
			print(f'senha gerada: {new_password}')
			all_passwords.append(new_password)
			save_passwords(all_passwords)
	if (event == '-show-'):
		window['terminal'].update('')
		print('Senhas Geradas...')
		for text in all_passwords:
			print(f'{text}')
		if (len(all_passwords) <= 0):
			print('não tem senhas geradas.')
window.close()
