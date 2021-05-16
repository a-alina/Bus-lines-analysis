import json
import re

data = input()

data_json = json.loads(data)

bus_id_lst = []

for bus_line in data_json:
    bus_id_lst.append(bus_line['bus_id'])

map = {key: [] for key in set(bus_id_lst)}

for bus_line in data_json:
    if bus_line['next_stop'] == 0:
        bus_line['stop_id'] = 100
    map[bus_line['bus_id']].append((bus_line['stop_id'], bus_line['stop_name'], bus_line['a_time']))

print('Arival time test:')
result = True
for bus_id, data in map.items():
    ok_order = sorted(data, key=lambda x: x[0])
    time_order = sorted(data, key=lambda x: x[2])
    if ok_order != time_order:
        result = False
        for i, e in enumerate(ok_order):
            try:
                if e[2] > ok_order[i+1][2]:
                    print(f"bus_id line {bus_id}: wrong time on station {ok_order[i+1][1]}")
                    break
            except IndexError:
                pass

if result == True:
    print('OK')
