# Lotto simulation
Symulator gry w lotto. Przy każdym uruchomieniu losuje 6 liczb do momentu, gdy trafi zestaw zdefiniowany w zmiennej `my_lucky_numbers`.

### Założenia:
- `weekly_frequency` - liczba losowań w tygodniu,
- `cost` - koszt jednego zakładu,
- `prize` - nagroda I stopnia.

### Wynik - wypisanie na ekranie tekstu z podsumowaniem:
Moje szczęśliwe liczby to: [*, *, *, *, *, *]\
Brawo, wygrałeś * PLN w * losowaniach)\
Koszt zakładów wyniósł * PLN\
Twój wynik to: * PLN\
Wygrana zajęła Ci * lat, * miesięcy, * tygodni, * dni.

### Inne informacje:
napisano z wykorzystaniem:
- [pylint](https://pylint.pycqa.org/en/latest/)
- [pytest](https://docs.pytest.org/en/latest/)