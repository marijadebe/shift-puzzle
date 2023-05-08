
# Technická dokumentace

Aplikace se skládá ze dvou oddělených částí, server a uživatelské rozhraní.

## Server

Server je strukturován jako Python balíček. Bohatě stačilo udělat ho zcela minimalistickým, tedy zajišťuje routovaní a ošetřuje vyjímky. 

### Routing

Cesty mají jednoduchou barebones strukturu
`./`
`./game/<int:velikost_hry>`
Povolená velikost hrací plochy je 3,4,5,6,7. Ostatní cesty se routují na chybovou stránku.

## User Interface

Na uživatelském rozhraní je implementována logika hry a veškeré její mechaniky. Ty jsou koncipované do tří částí.

### Třída Box

Třída Box je přepravka, v níž se ukládají hodnoty jednotlivého hracího pole, její hlavní úloha je umět sebe sama vykreslit.

### Třída Board

Třída Board je hlavní částí aplikace. Hrací plocha je reprezentována jako 2D pole. Třída Board zpracovává kliknutí, stisknutí klávesy a zamíchání plochy při začátku hry.  
Zamíchání funguje tak, že se prohazují zcela náhodně Boxy, kromě prázdného pole, to musí zůstat fixní, aby výsledná pozice byla validní. Navíc je potřeba zajistit, aby výsledná permutace byla sudá. Algoritmus, který toto testuje, počítá v lineárním čase cykly sudé velikosti.

### Kódová obsluha

Komunikace Document Object Modelu s logickou reprezentací Board zajišťuje kódová obsluha souboru game.py.

### Design

Aplikace využívá UI knihovnu Bootstrap, která zajišťuje flexibilitu a responsivnost rozhraní.