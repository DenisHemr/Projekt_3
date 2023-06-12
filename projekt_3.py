"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Denis Hemr
email: dennis.hemmr@gmail.com
discord: Denis H.#3249
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys


def extract_code(href: str) -> str:
    """
    Extrahuje kód obce z odkazu.

    Parametry:
        href (str): Odkaz obsahující kód obce.

    Návratová hodnota:
        str: Kód obce.

    """
    if href is not None:
        return href.split("&xobec=")[1].split("&")[0]
    return None


def get_data(url: str, kod_obce: str) -> tuple:
    """
    Získává data o volbách z daného odkazu.

    Parametry:
        url (str): Odkaz na stránku s výsledky voleb pro konkrétní obec.
        kod_obce (str): Kód obce.

    Návratová hodnota:
        tuple: Tuple obsahující následující údaje:
            - obec (str): Název obce.
            - volici (str): Počet voličů v seznamu.
            - obalky (str): Počet vydaných obálek.
            - platne (str): Počet platných hlasů.
            - parties (list): Seznam tuple obsahující názvy stran a počet hlasů.

    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    obec = soup.find_all("h3")[2].text.split(":")[1].strip()

    table1 = soup.find_all("table")[0]
    volici = table1.find_all("tr")[2].find_all("td")[3].text
    obalky = table1.find_all("tr")[2].find_all("td")[4].text
    platne = table1.find_all("tr")[2].find_all("td")[7].text

    table2 = soup.find_all("table")[1]
    rows = table2.find_all("tr")[2:]
    parties = []
    for row in rows:
        party = row.find_all("td")[1].text
        votes = row.find_all("td")[2].text
        parties.append((party, votes))

    return obec, volici, obalky, platne, parties


def get_links(url: str) -> list:
    """
    Získává seznam odkazů na stránky s výsledky voleb pro jednotlivé obce.

    Parametry:
        url (str): Odkaz na hlavní stránku s výsledky voleb.

    Návratová hodnota:
        list: Seznam odkazů na stránky s výsledky voleb pro jednotlivé obce.

    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find_all("table")[0]
    rows = table.find_all("tr")[2:]
    links = []
    for row in rows:
        link = row.find("a")["href"]
        links.append("https://volby.cz/pls/ps2017nss/" + link)
    return links


def main() -> None:
    """
    Hlavní funkce programu.

    Zpracovává argumenty příkazové řádky, získává odkazy na stránky s výsledky voleb
    pro jednotlivé obce, získává data o volbách a ukládá je do CSV souboru.

    """
    if len(sys.argv) != 3:
        print("Please provide the URL and the output file name as arguments.")
        return

    url = sys.argv[1]
    output_file = sys.argv[2]

    print("Probíhá extrakce dat...")
    links = get_links(url)
    all_data = []
    for link in links:
        kod_obce = extract_code(link)
        obec, volici, obalky, platne, parties = get_data(link, kod_obce)
        for party, votes in parties:
            row = [kod_obce, obec, volici, obalky, platne, party, votes]
            all_data.append(row)
    df = pd.DataFrame(
        all_data,
        columns=[
            "Kód obce",
            "Obec",
            "Voliči v seznamu",
            "Vydané obálky",
            "Platné hlasy",
            "Strana/název",
            "Celkem",
        ],
    )
    df.to_csv(output_file, index=False, encoding="utf-8", sep=" ")
    print("Extrakce dat dokončena. Data uložena v souboru", output_file)


if __name__ == "__main__":
    main()
