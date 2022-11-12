## Validátor rodného čísla (RČ)

### Funkce validator_rc ověřuje následující podmínky:
* RČ se skládá z 9 číslic (do data narození 31.12.1953) nebo 10 číslic (od data narození 1.1.1954).
* Devítimístné RČ má koncovku za lomítkem v rozsahu 001 až 999, desetimístné v rozsahu 0000 až 9999.
* Prvních šest číslic v obou případech popisují datum narození ve formátu RRMMDD (s případnou úvodní nulou).
* Ženy mají k měsíci narození připočteno číslo 50.
* Desetimístné RČ je beze zbytku dělitelné jedenácti.
* Kontrolní číslice
  * Poslední číslice desetimístného rodného čísla je zbytek po celočíselném dělení (tzv. modulo) prvních devíti čísel
      desetimístného rodného čísla jedenácti.
    * Z tohoto pravidla existuje následující výjimka: Pokud je zbytek po dělení prvních devíti čísel desetimístného
    rodného čísla roven číslu 10 (a neexistuje tedy žádná kontrolní číslice z rozsahu 1–9, kterou by bylo možno docílit
    splnění předchozího pravidla), jako kontrolní číslice se použije číslice 0, přičemž celé takové desetimístné rodné
    číslo pak dělitelné 11 není. Tato výjimka však byla použita jen zhruba u 1 000 rodných čísel, přidělování takovýchto 
    rodných čísel bylo roku 1985 podle vnitřního předpisu FSÚ Č. Vk. 2898/1985 ukončeno, i když není však zcela vyloučeno,
    že se v minimálním počtu vyskytla i po tomto roce.
* Od roku 2004 je zavedena možnost v případě, že jsou v některý den již vyčerpána všechna platná čtyřčíslí, použít
    alternativní rodné číslo, kde se k číslu měsíce narození přičte ještě číslo 20.

### Testy
* Soubor test_validator.py obsahuje negativní testy funkce validator_rc.
* Pozitivní testy nezveřejňuji, protože nechci uvádět citlivý údaj (platné rodné číslo) žádné osoby.

Zdroje: [MVČR](https://www.mvcr.cz/clanek/rady-a-sluzby-dokumenty-rodne-cislo.aspx) a [WIKIPEDIE](https://cs.wikipedia.org/wiki/Rodn%C3%A9_%C4%8D%C3%ADslo)