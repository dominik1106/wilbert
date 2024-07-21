import csv_reader

class Info:
    daten = dict()
    header = list()
    display_namen = dict()

    def namen_dict(self):
        self.display_namen = {item["Name"]: item for item in self.daten}

    def __init__(self, filename: str) -> None:
        self.daten, self.header = csv_reader.read_csv_into_dict(filename)
        self.namen_dict()

class WaffenInfo(Info):
    def namen_dict(self):
        self.display_namen = {"{Name} ({Kategorie})".format(**item): item for item in self.daten}