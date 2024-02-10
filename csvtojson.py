import csv
import json
import sys

def csv_to_json(csv_filepath, json_filepath):
    json_array = []
    with open(csv_filepath, encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            json_array.append(row)
    with open(json_filepath, 'w', encoding='utf-8') as jsonfile:
        json_string = json.dumps(json_array, indent=4)
        jsonfile.write(json_string)

filename = sys.argv[1]

csv_filepath = str(filename)
json_filepath = str(filename.strip('csv') + "json")

if __name__ == "__main__":
    csv_to_json(csv_filepath, json_filepath)