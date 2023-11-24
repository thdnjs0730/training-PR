from c12.data_helper import DataHelper
from c12.station import Station

data_helper = DataHelper('지하철_시간대별_이용현황.csv', 2)

header = data_helper.get_header()
data = data_helper.get_data()

index = 0

station_list = []
for time in header[0][4:-1:2]:
    station = Station()
    station.time = time
    max_count = 0

    for d_row in data:
        count = int(d_row[4 + index * 2]) + int(d_row[5 + index * 2])
        if count > max_count:
            max_count = count
            station.set_data_by_row(d_row, index)

    station_list.append(station)
    index += 1

for station in station_list:
    station.show()
    print(station.get_total_count())