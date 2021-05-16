import json
import re

data = input()

data_json = json.loads(data)
bus_id_lst = []
for bus_line in data_json:
    bus_id_lst.append(bus_line['bus_id'])

names_stops = {key: [] for key in set(bus_id_lst)}

for bus_line in data_json:
    names_stops[bus_line['bus_id']].append(bus_line['stop_name'])

print("Line names and number of stops:")
for key, value in names_stops.items():
    print(f'bus_id: {key}, stops: {len(set(value))}')
