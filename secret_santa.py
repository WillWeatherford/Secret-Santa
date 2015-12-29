import random

INPUT = '''
Sean
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
Alex Andrea
'''


def main(names_input):
    families = families_dict(names_input)
    chain = chain_list(families)
    santas = santas_dict(chain)
    test_santas(santas, families)


def families_dict(names_input):
    lines = names_input.split('\n')
    families = {n: str(fam_id) for fam_id, line in enumerate(lines)
                for n in line.split() if line}
    return families


def chain_list(families):
    names = list(families.keys())
    chain = []

    while names:
        if chain:
            santa = chain[-1]
            valid_recips = [n for n in names if families[santa] != families[n]]
            print('{} has {} valid recipients'.format(santa, len(valid_recips)))
            recip = random.choice(valid_recips)
        else:
            recip = random.choice(names)
        names.remove(recip)
        chain.append(recip)

    return chain


def santas_dict(chain):
    santas = {}
    for indx, santa in enumerate(chain):
        recipient = chain[indx - 1]
        santas[santa] = recipient
        print(' --> '.join((santa, recipient)))
    return santas


def test_santas(santas, families):
    for santa, recip in santas.items():
        assert families[santa] != families[recip], (
            'Santa {} in the same family as recip {}'.format(santa, recip))
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


if __name__ == '__main__':
    main(INPUT)
