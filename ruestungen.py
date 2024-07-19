import csv

def extract_column(data, column_name):
    values = list()

    for item in data:
        values.append(item[column_name])

    return values

def extract_column_unique(data, column_name):
    unique_values = set()

    for item in data:
        value = item[column_name].strip()
        unique_values.add(value)

    return list(unique_values)

def filter_nach_kategorie(kategorie: str):
    return [ruestung for ruestung in ruestungen if ruestung["Kategorie"] == kategorie]


with open("ruestungs_tabelle.csv", "r", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")

    ruestungen_header = csv_reader.fieldnames
    ruestungen = list(csv_reader)

ruestungen_namen = extract_column(ruestungen, "Name")
ruestungen_kategorien = extract_column_unique(ruestungen, "Kategorie")