def decoreer(tekst=''):
    lengte = len(tekst) + 4
    print()
    print(lengte * '*')
    print(f'*{tekst}*')
    print(lengte*'*')
    print()

def fooi_pp(b,p):
    try:
        bedrag_pp = b / p
    except:
        bedrag_pp = '??'
    return f'Het bedrag per persoon is {bedrag_pp} euro fooi.'
    
    
b = int(input('Welk bedrag zit er in fooienpot?'))
p = int(input('Over hoeveel mensen moet de pot verdeeld worden?'))

print(fooi_pp(b,p))