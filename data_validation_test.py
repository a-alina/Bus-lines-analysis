import json
import re


data = input()

data_json = json.loads(data)

field_names = ['bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time']

stop_type_char = ['S', 'O', 'F', '']

error_count = {key: 0 for key in field_names}

for bus_line in data_json:

    if not isinstance(bus_line['bus_id'], int) or bus_line['bus_id'] == '':
        error_count["bus_id"] += 1
    if not isinstance(bus_line['stop_id'], int) or bus_line['stop_id'] == '':
        error_count["stop_id"] += 1
    if not isinstance(bus_line['next_stop'], int):
        error_count["next_stop"] += 1
    if not isinstance(bus_line['stop_type'], str) or not bus_line['stop_type'] in stop_type_char:
        error_count["stop_type"] += 1
    if not isinstance(bus_line['a_time'], str) or re.match('[0-2][0-9]:[0-5][0-9]\Z', bus_line['a_time']) == None:
        error_count["a_time"] += 1
    if not isinstance(bus_line['stop_name'], str) or re.match('[A-Z][a-z]+ ?[A-Z]?[a-z]+ (Road|Avenue|Street|Boulevard)\Z', bus_line['stop_name']) == None:
        error_count["stop_name"] += 1


total_errors = sum(i for i in error_count.values() if i != 0)

print(f"""Format valitaiton: {total_errors} total errors
stop_name: {error_count['stop_name']}
stop_type: {error_count['stop_type']}
a_time: {error_count['a_time']}""")
