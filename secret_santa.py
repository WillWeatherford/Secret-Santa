import random


def test_santas(santas, families):
    for santa, recip in santas.items():
        assert families[santa] != families[recip], (
            'Santa {} in the same family as recip {}'.format(santa, recipient))
        chain = test_size(santas, santa)
        ls = len(santas)
        lc = len(chain)
        print('Chain starting with {} has a length of {}'.format(santa, lc))
        assert ls == lc, '{} items in chain vs {} in santas dict'.format(lc, ls)


def test_size(santas, santa, chain=None):
    if chain is None:
        chain = []
    if santa in chain or len(chain) >= len(santas):
        return chain
    recip = santas[santa]
    chain.append(santa)
    return test_size(santas, recip, chain)


names = '''Sean
Winnie
Brian Amy
Samir
Joe Bethany
Bruno Anna Matthew Lucas
Gabriel Martha Philip
Andre
Danielle
Leo Cinthia
Paula
Mary Jane
Anderson
Priscilla
Regis Julianna Arthur
Mark Marina
Alex Andrea'''

# Separate the input into a list of lists: names within families.
lines = names.split('\n')
families = {n: str(i) for i, line in enumerate(lines) for n in line.split()}

names = list(families.keys())

chain = []

while names:
    if not chain:
        chain.append(names.pop(random.randrange(len(names))))
    santa = chain[-1]
    valid_recips = [n for n in names if families[santa] != families[n]]
    print('{} valid recips found for {}'.format(len(valid_recips), santa))
    recip = random.choice(valid_recips)
    names.remove(recip)
    chain.append(recip)

santas = {}
for indx, santa in enumerate(chain):
    recipient = chain[indx - 1]
    print(' --> '.join((santa, recipient)))
    santas[santa] = recipient

test_santas(santas, families)
