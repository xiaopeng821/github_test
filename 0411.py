import pandas as pd

def No(str):
    No = 0
    for i in str:
        if i == '无':
            No += 1
        return No

def count_flight_number(input_file , output_file):
    tmp_data = pd.read_excel(input_file)
    print(tmp_data)

    city_flight_number = dict()
    for i,tmp_row in tmp_data.iterrows():
        if '出发城市' in tmp_row:
            city_name = tmp_row['出发城市']
        else :
            city_name = tmp_row['到达城市']
        schedule = tmp_row['每周班期']
        count_no = No(schedule)
        count_yes = 7 - count_no
        if city_name not in city_flight_number:
            city_flight_number[city_name] = 0
        city_flight_number[city_name] += count_yes

    all_data = list()
    for city_name in city_flight_number:
        tmp_data = dict()
        tmp_data['城市'] = city_name
        tmp_data['航班数'] = city_flight_number[city_name]
        all_data.append(tmp_data)
    df = pd.DataFrame(all_data)
    df.to_csv(output_file)

all_files = ['dl_air_arrive.xls','dl_air_leave.xls']
for tmp_name in all_files:
    tmp_input_name = 'data/' + tmp_name
    tmp_output_name = 'result/'+ tmp_name
    count_flight_number(tmp_input_name,tmp_output_name)




