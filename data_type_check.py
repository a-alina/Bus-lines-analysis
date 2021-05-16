import json

data = input()


data_json = json.loads(data)

bus_id = 0
stop_id = 0
stop_name = 0
next_stop = 0
stop_type = 0
a_time = 0
total = 0

for bus_line in data_json:

    if not isinstance(bus_line['bus_id'], int) or bus_line['bus_id'] == '':
        bus_id += 1
        total += 1
    if not isinstance(bus_line['stop_id'], int) or bus_line['stop_id'] == '':
        stop_id += 1
        total += 1
    if not isinstance(bus_line['stop_name'], str) or bus_line['stop_name'] == '':
        stop_name += 1
        total += 1
    if not isinstance(bus_line['next_stop'], int) or bus_line['next_stop'] == '':
        next_stop += 1
        total += 1
    if not isinstance(bus_line['stop_type'], str) or len(bus_line['stop_type']) > 1:
        stop_type += 1
        total += 1
    if not isinstance(bus_line['a_time'], str) or bus_line['a_time'] == '':
        a_time += 1
        total += 1

print(f"""Type and required field validation: {total} errors
bus_id: {bus_id}
stop_id: {stop_id}
stop_name: {stop_name}
next_stop: {next_stop}
stop_type: {stop_type}
a_time: {a_time}
""")
