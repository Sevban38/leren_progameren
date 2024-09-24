print('Welk seizoen vind jij het fijnst?\n'
      'A) Lente\n'
      'B) Zomer\n'
      'C) Herfst\n'
      'D) Winter')
gekozen_seizoen = input('? ').lower()

weer_type = ''  

if gekozen_seizoen in ('a', 'c'):
    print('Dus jij vindt een tussenseizoen het fijnst...')
elif gekozen_seizoen == 'b':
    weer_type = 'warm'
elif gekozen_seizoen == 'd':
    weer_type = 'koud'

if len(weer_type) > 0:
    print(f'Dus jij houdt van {weer_type} weer!')