S = int(open('INPUT.TXT').read())
x = S // 6
k = 4 * x
open('OUTPUT.TXT', 'w').write(f'{x} {k} {x}')
