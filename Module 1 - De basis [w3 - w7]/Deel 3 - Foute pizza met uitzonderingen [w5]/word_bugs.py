a = str(input('Geef een woord: '))
b = str(input('Geef nog een woord: '))

if len(a) > len(b):     
    print('Woord 2 heeft meer letters dan woord 1')
elif len(a) < len(b):   
    print('Woord 2 heeft minder letters dan woord 1')
elif len(a) == len(b):                   
    print('Woord 1 en woord 2 hebben evenveel letters')