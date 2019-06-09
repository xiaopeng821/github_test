import pandas

original_data = pandas.read_excel('worker-data.xlsx')

# print(original_data)

all_locations = list()
all_industry = list()

for i, tmp_row in original_data.iterrows():
    all_locations.append(str(tmp_row['XIANG']))
    all_industry.append(str(tmp_row['行业代码']))

all_industry = list(set(all_industry))
all_locations = list(set(all_locations))

main_dict = dict()
for location in all_locations:
    main_dict[location] = dict()
    for industry in all_industry:
        main_dict[location][industry] = 0

for i, tmp_row in original_data.iterrows():
    tmp_location = str(tmp_row['XIANG'])
    tmp_industry = str(tmp_row['行业代码'])
    tmp_value = tmp_row['RY']
    if isinstance(tmp_value, int) and tmp_location in main_dict and tmp_industry in main_dict[tmp_location]:
        main_dict[tmp_location][tmp_industry] += tmp_value

for tmp_location in main_dict:
    tmp_sum = 0
    for tmp_industry in all_industry:
        tmp_sum += main_dict[tmp_location][tmp_industry]
    if tmp_sum > 0:

        for tmp_industry in all_industry:
            main_dict[tmp_location][tmp_industry] /= tmp_sum

result = pandas.DataFrame(main_dict)
print(result)
result = result.T
print(result)
result.to_csv('result.csv')

print('end')
