Webový scraper pro volební výsledky
----------------------------------
Tento projekt je webový scraper napsaný v jazyce Python, který získává volební výsledky z [https://volby.cz](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) a ukládá je do CSV souboru.



Instalace
---------
1. Naklonujte si tento repozitář na své zařízení:

![git clone](https://github.com/DenisHemr/Projekt_3/assets/128733185/a07bdd55-8017-4772-8da1-541ed8d54398)


2. Přejděte do složky s projektem:

![cd your rep](https://github.com/DenisHemr/Projekt_3/assets/128733185/39d782f8-d2e0-4aab-b31c-1a3ac53eefc5)


3. Je potřeba vytvořit a aktivovat virtuální prostředí:

![venv](https://github.com/DenisHemr/Projekt_3/assets/128733185/da28fd26-867b-4d36-80eb-637a0af503a8)


4. Nainstalujte potřebné knihovny ze souboru 'requirements.txt':

![req instal](https://github.com/DenisHemr/Projekt_3/assets/128733185/015d138a-c06f-43e2-aab9-84fe9025481a)


Použití
-------

Spusťte skript projekt_3.py s dvěma argumenty: URL adresou a názvem výstupního souboru:

![spousteni projekt](https://github.com/DenisHemr/Projekt_3/assets/128733185/efe133d3-f5db-4da7-adca-352498a99cc5)


- 'URL' - Odkaz na hlavní stránku se seznamem obcí
[volby.cz/pls/ps2017nss/ps3?xjazyk=CZ](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

- 'output.csv' - Název výstupního CSV souboru, do kterého budou uloženy volební výsledky.


Po spuštění skriptu budou data extrahována ze všech odkazů na stránky s výsledky voleb pro jednotlivé obce a uložena do CSV souboru.

Příklad
-------

![spousteni konsole](https://github.com/DenisHemr/Projekt_3/assets/128733185/8cb19e66-5799-42be-8c64-3cee41925360)


Tento příkaz extrahuje volební výsledky ze všech obcí uvedených na stránce

https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ a uloží je do souboru output.csv.


Struktura projektu
-----------------


 - 'main.py': Hlavní skript pro spuštění scraperu.
 - 'requirements.txt': Seznam závislostí projektu.
 - 'venv/': Virtuální prostředí projektu. 
 - 'README.md': Dokumentace projektu.


Autor
-----

- Denis Hemr
