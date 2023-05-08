
# Shift Puzzle

Implementace klasické hry patnáctka, jakožto webové aplikace. Aplikace byla vytvořena jako zápočtový program.  
Osobní motivací tvorby aplikace bylo prozkoumat nové technologie, které umožňují Python programátorům vyvíjet webové aplikace.

## Uživatelská příručka

### Instalace

Aplikace je dostupná online na <https://shiftpuzzle.herokuapp.com/>. Chcete-li aplikaci spustit lokálně doporučuji použít virtuální prostředí.  
Ve složce s projektem vytvořte virtuální prostředí.
`python3 -m venv <nazev>`
Prostředí aktivujete příkazem
`<nazev>\Scripts\Activate` v případě Windows, pro Linux pak
`source <nazev>/bin/activate`
Všechny závislosti pak jednoduše nainstalujete příkazem
`pip3 install .`
Samotný Flask server spustíte příkazem
`flask --app shift run`
V tuto chvíli se lokálně spustí vývojový server. Standardně na portu 5000, případně na jiném portu, pokud Váš stroj port 5000 využívá.

### Herní ovládání

Ve hře jsou dostupné velikosti hrací plochy 3x3, až 7x7. Po výběru Vás aplikace nasměruje na cestu `/game/<velikost_hry>`.  
Hru lze ovládat šipkami, nebo klikáním na samotnou hrací plochu. Hra ukazuje čas a počet tahů. Po vyřešení hrací plochy se zobrazí roztomilá trofej.

## Závislosti, balíčky

Aplikace využívá následujících knihoven
**[Flask](https://flask.palletsprojects.com/en/2.3.x/)**
**[Gunicorn](https://gunicorn.org/)**
**[Pyscript](https://pyscript.net/)**
**[Bootstrap](https://https://getbootstrap.com/)**
