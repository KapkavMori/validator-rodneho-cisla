import pytest
from validatorRC import validator_rc


@pytest.mark.parametrize(
    "rodne_cislo, vysledek", [
        # chybná délka
        ("a48602851", False),
        # chybný r. narození, devítimístné RČ je možné pouze do r. 1953
        ("736228517", False),
        # chybné trojčíslí za lomítkem, nemohou tam být tři nuly
        ("435128000", False),
        # chybný měsíc narození, 63/13 neexistuje
        ("436328517", False),
        # chybný den narození v měsíci listopad
        ("431131517", False),
        # chybný den narození v měsíci únor, přestupný rok
        ("485230517", False),
        # chybný den narození v měsíci únor, nepřestupný rok
        ("5852295174", False),
        # není dělitelné 11 beze zbytku
        ("6410055169", False),
        # chybný měsíc, rok narození před r. 2004
        ("6430055082", False)
    ]
)
def test_validator_rc(rodne_cislo, vysledek):
    """
    :param rodne_cislo: rodne_cislo
    :param vysledek: vždy False, z důvodu ochrany osobních údajů nejsou v testu uvedena platná RČ
    :return: porovnání předpokládaného výsledku se skutečným výsledkem z validátoru
    """
    assert validator_rc(rodne_cislo) == vysledek
