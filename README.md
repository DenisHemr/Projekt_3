Webový scraper pro volební výsledky
----------------------------------
Tento projekt je webový scraper napsaný v jazyce Python, který získává volební výsledky z [https://volby.cz](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) a ukládá je do CSV souboru.



Instalace 
---------

1. Je potřeba instalovat knihovny ktere jsou uložené v dokumentu 'requirements.txt', nejprve doporučuji použít nové
virtuální prostředí a s nainstalovaným manažerem spustit instalaci následovně:


![isntalace knihoven](https://github.com/DenisHemr/Projekt_3/assets/128733185/745934f6-c390-4576-89fd-cee53ed83557)



Spouštění programu
-----------------

Spusťte skript projekt_3.py s dvěma argumenty: URL adresou a názvem výstupního souboru:

![spousteni projekt](https://github.com/DenisHemr/Projekt_3/assets/128733185/efe133d3-f5db-4da7-adca-352498a99cc5)


- 'URL' - Odkaz na hlavní stránku se seznamem obcí, v seznamu obcí vyberete výsledky konkrétní obce ('X')

Například:
![volby](https://github.com/DenisHemr/Projekt_3/assets/128733185/68dad565-98bc-4850-912b-8d066d948cd0)




[volby.cz/pls/ps2017nss/ps3?xjazyk=CZ](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

- 'output.csv' - Název výstupního CSV souboru, do kterého budou uloženy volební výsledky.


Po spuštění skriptu budou data extrahována ze všech odkazů na stránky s výsledky voleb pro jednotlivé obce a uložena do CSV souboru.


Struktura projektu
-----------------


 - 'main.py': Hlavní skript pro spuštění scraperu.
 - 'requirements.txt': Seznam závislostí projektu.
 - 'venv/': Virtuální prostředí projektu. 
 - 'README.md': Dokumentace projektu.
 - vysledky.csv


Autor
-----

- Denis Hemr
