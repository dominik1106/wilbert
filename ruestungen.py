from csv_reader import read_csv_into_dict, extract_column, extract_column_unique

def filter_nach_kategorie(kategorie: str):
    return [ruestung for ruestung in ruestungen if ruestung["Kategorie"] == kategorie]


ruestungen, ruestungen_header = read_csv_into_dict("./data/ruestungs_tabelle.csv")

ruestungen_namen = extract_column(ruestungen, "Name")
ruestungen_kategorien = extract_column_unique(ruestungen, "Kategorie")