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


#print(fooi_pp(b,p))


def onderstreep(tekst=''):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst)*'=')
    return uit

def som(dictionary):
    waarden = dictionary.values()
    for i in waarden:
        return sum(waarden)
    