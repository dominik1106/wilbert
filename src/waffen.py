from csv_reader import read_csv_into_dict, extract_column, extract_column_unique

def filter_nach_kategorie(kategorie: str):
    return [ruestung for ruestung in waffen if ruestung["Kategorie"] == kategorie]


waffen, waffen_header = read_csv_into_dict("waffen_tabelle.csv")

waffen_namen = extract_column(waffen, "Name")
waffen_kategorien = extract_column_unique(waffen, "Kategorie")