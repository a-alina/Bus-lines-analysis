import json
import re

data = input()

data_json = json.loads(data)

bus_id_lst = []

for bus_line in data_json:
    bus_id_lst.append(bus_line['bus_id'])

stop_types = {key: [] for key in set(bus_id_lst)}

for bus_line in data_json:
    stop_types[bus_line['bus_id']].append(bus_line['stop_type'])

stop_names = {key: [] for key in set(bus_id_lst)}

for bus_line in data_json:
    stop_names[bus_line['bus_id']].append(bus_line['stop_name'])

def check():
    for bus_id, stop_type in stop_types.items():
        if stop_type.count('F') == 0 or stop_type.count('S') == 0:
            print(f'There is no start or end stop for the line: {bus_id}')
            exit()

def result(types, names):
    start = []
    all = []
    finnish = []
    for (id, type), (id, name) in zip(types.items(), names.items()):
        for i, k in zip(type, name):
            if i == 'S':
                start.append(k)
            elif i == 'F':
                finnish.append(k)
            if i != 'O':
                all.append(k)
    transfer = [i for i in all if all.count(i) > 1]
    print(f"""Start stops: {len(set(start))} {sorted(list(set(start)))}
Transfer stops: {len(set(transfer))} {sorted(list(set(transfer)))}
Finish stops: {len(set(finnish))} {sorted(list(set(finnish)))}""")


check()
result(stop_types, stop_names)
