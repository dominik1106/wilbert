from csv_reader import read_csv_into_dict, extract_column, extract_column_unique

def filter_nach_kategorie(kategorie: str):
    return [ruestung for ruestung in talente if ruestung["Kategorie"] == kategorie]


talente, talente_header = read_csv_into_dict("talente_tabelle.csv")

talente_namen = extract_column(talente, "Name")
talente_kategorien = extract_column_unique(talente, "Kategorie")