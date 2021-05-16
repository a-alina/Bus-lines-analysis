import json
import re

data = input()

data_json = json.loads(data)


bus_id_lst = []

for bus_line in data_json:
    bus_id_lst.append(bus_line['bus_id'])
# making a dictionary from unique bus ids
stop_types = {key: [] for key in set(bus_id_lst)}

# making a list with stop types for each bus id
for bus_line in data_json:
    stop_types[bus_line['bus_id']].append(bus_line['stop_type'])

stop_names = {key: [] for key in set(bus_id_lst)}
# making a list with stop names for each bus id
for bus_line in data_json:
    stop_names[bus_line['bus_id']].append(bus_line['stop_name'])

def result(types, names):
    start = []
    all = []
    finnish = []
    on_demand = []
    for (id, type), (id, name) in zip(types.items(), names.items()):
        for i, k in zip(type, name):
            if i == 'S':
                start.append(k)
            elif i == 'F':
                finnish.append(k)
            if i != 'O':
                all.append(k)
            elif i == 'O':
                on_demand.append(k)
    transfer = [i for i in all if all.count(i) > 1]

    final = []
    for stop_on_demand in on_demand:
        if all.count(stop_on_demand) == 1:
            final.append(stop_on_demand)

    print('On demand stops test:')
    if len(final) != 0:
        print(f'Wrong stop type: {sorted(final)}')

    else:
        print('OK')

result(stop_types, stop_names)
