from algemene_functie import mijn_functie2

def aanbieding_1(smaak, prijs, korting):
    prijs_a = prijs - prijs*korting
    uitvoer = f'Vandaag in de aanbieding, emmertje ijs (1liter) in de smaak {smaak}, van {prijs} Euro voor {prijs_a} Euro.'
    return uitvoer
          
print(aanbieding_1('aardbei', 4, 0.1))

inkomsten = [220, 430, 125, 160, 205, 90, 345]

def inkomsten_totaal(a):
    totale_inkomen = sum(a)
    btw = totale_inkomen * 0.09
    uitvoer = f'Het totaal van alle inkomsten van deze week is {totale_inkomen} euro, waarover {btw} euro btw betaald dient te worden'
    return uitvoer 

print(inkomsten_totaal(inkomsten))

def laag_en_hoog(a):
    return max(a), min(a)

print(laag_en_hoog(inkomsten))

def gemiddelde(a):
    berekening = sum(a) / len(a)
    uitvoer = f'De gemiddelde inkomsten deze week zijn {berekening} euro.'
    return uitvoer

print(gemiddelde(inkomsten))

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
invoer_lijst_2 = [22, 57, 18, 21, 6]

def meervoudig(a):
    return laag_en_hoog(a)

print(meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie2(korte_lijst[0],korte_lijst[1])
    return uitvoer

print(combinatie(invoer_lijst_2))