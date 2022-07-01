import numpy as np

with open("/Users/junrusong/PycharmProjects/try_mofan/covid19_day_wise.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
# print(data[:5])
# print(type(data))
covid = {
    "date": [],
    "data": [],
    "header": [h for h in data[0].strip().split(",")[1:]]
}
# print(covid["header"])
for row in data[1:]:
    split_row = row.strip().split(",")
    # print(split_row)
    covid["date"].append(split_row[0])
    # print(covid['date'])
    covid["data"].append([float(n) for n in split_row[1:]])
    # print(covid['data'])
    # exit(1)

# date_idx = covid['date'].index("2020-03-20")
new_data = np.array(covid["data"])
# for header,num in zip(covid["header"],new_data[date_idx]):
#     print("1",header,",",num)
#
# for header,num in zip(covid["header"],covid["data"][date_idx]):
#     print("2",header,",",num)
print(type(new_data))
date_idx2 = covid['date'].index("2020-01-24")
data_idx = covid['header'].index("Confirmed")
confirmed0124 = new_data[date_idx2,data_idx]
print(confirmed0124)


