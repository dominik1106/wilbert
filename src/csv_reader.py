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

def read_csv_into_dict(filepath) -> tuple[list[str], list[str]]:
    with open(filepath, "r", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")

        headers = list(reader.fieldnames)
        data = list(reader)

    return data, headers