import pandas

original_data = pandas.read_excel('worker-data2.xlsx')

# print(original_data)

all_locations = list()
all_industry = list()

for i, tmp_row in original_data.iterrows():
    all_locations.append(str(tmp_row['就业中心名']))
    all_industry.append(str(tmp_row['行业代码']))

all_industry = list(set(all_industry))
all_locations = list(set(all_locations))

main_dict = dict()

for industry in all_industry:
    main_dict[industry] = dict()
    for location in all_locations:
        main_dict[industry][location] = 0

for i, tmp_row in original_data.iterrows():
    tmp_industry = str(tmp_row['行业代码'])
    tmp_location = str(tmp_row['就业中心名'])
    tmp_value = tmp_row['企业数']
    if isinstance(tmp_value, int) and tmp_industry in main_dict and tmp_location in main_dict[tmp_industry]:
        main_dict[tmp_industry][tmp_location] += tmp_value

#for tmp_location in main_dict:
#    tmp_sum = 0
#    for tmp_industry in all_industry:
#       tmp_sum += main_dict[tmp_location][tmp_industry]
#    if tmp_sum > 0:

#        for tmp_industry in all_industry:
#            main_dict[tmp_location][tmp_industry] /= tmp_sum

for tmp_industry in main_dict:
    tmp_sum = 0
    for tmp_location in all_locations:
        tmp_sum += main_dict[tmp_industry][tmp_location]
    if tmp_sum > 0:

        for tmp_location in all_locations:
            main_dict[tmp_industry][tmp_location] /= tmp_sum

result = pandas.DataFrame(main_dict)
print(result)
#result = result.T
#print(result)
result.to_csv('result.csv')

print('end')
