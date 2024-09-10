from termcolor import colored, cprint, COLORS

print('')
cprint('Dit is helemaal rood', 'red')
print('Dit is deels', colored('rood', 'red'))
cprint('Deze heeft een rode achtergrond', on_color='on_red')

print('')
print(colored('Deze is paars op groen', 'magenta', 'on_green'))

print('')
cprint('Je kan het zelfs dikgedrukt maken', attrs=['bold'])

woord = 'variable'
print('')
print(f'Maar je kan ook alleen de {colored(woord, 'yellow', attrs=['bold'])} kleuren.')

print('')
print('De beschikbare kleuren in termcolor zijn:', ', '.join([colored(color, color) for color in COLORS.keys()]))

link = colored('https://www.unicode.org/emoji/charts/full-emoji-list.html', 'blue', attrs=['underline'])

print('')
print('Of emoji\'s gebruiken zoals deze: 👍')
print('Hier vindt je de lijst met emojis:', link)

print('')