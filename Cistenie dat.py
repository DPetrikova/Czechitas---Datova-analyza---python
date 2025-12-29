"""Preprocessing dat z tsv súboru a uloženie vyčistených dat do JSON súboru."""

import json

titles = []

with open("netflix_titles.tsv", encoding="utf-8") as file:
    header = file.readline().split("\t")
    for line in file:
        (TCONST, TITLETYPE, PRIMARYTITLE, ORIGINALTITLE, ISADULT, STARTYEAR,
         ENDYEAR, RUNTIMEMINUTES, GENRES, AVERAGERATING, NUMVOTES,
         TITLETYPE_NEW, SHOW_ID, TYPE, TITLE, DIRECTOR, CAST, COUNTRY,
         DATE_ADDED, RELEASE_YEAR, RATING, DURATION, LISTED_IN, DESCRIPTION
         ) = line.split("\t")
        new_item = {
            "title": PRIMARYTITLE,
            "directors": list(DIRECTOR.split(', ')) if DIRECTOR else [],
            "cast": list(CAST.split(", ")) if CAST else [],
            "genres": list(GENRES.split(",")),
            "decade": int(STARTYEAR) - (int(STARTYEAR) % 10)}
        titles.append(new_item)

with open('hw02_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(titles, output_file, ensure_ascii=False, indent=4)
