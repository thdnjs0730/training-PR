
class Station:

    def __init__(self):
        self.line_name = ''
        self.name = ''
        self.time = ''
        self.in_count = 0
        self.out_count = 0

    def set_data(self, line_name, name, time, in_cnt, out_cnt):
        self.line_name = line_name
        self.name = name
        self.time = time
        self.in_count = in_cnt
        self.out_count = out_cnt

    def show(self):
        print(f'{self.time} : {self.text_full(self.line_name + "-" + self.name, 30)}, 승차:{self.in_count:10,}, 하차:{self.out_count:10,}')

    def set_data_by_row(self, row, index):
        self.line_name = row[1]
        self.name = row[3]
        self.in_count = int(row[4 + index * 2])
        self.out_count = int(row[5 + index * 2])

    def get_total_count(self):
        return self.in_count + self.out_count

    def text_full(self, text, max_length = 25):
        text_length = 0
        for x in text:
            # print(x, ord(x))
            if ord('가') <= ord(x) <= ord('힝'):
                text_length += 2
            else:
                text_length += 1

        add_text = ''
        for i in range(max_length - text_length):
            add_text += ' '

        return text + add_text
# end-class

# station1 = Station()
# station1.set_data('1호선','구로','04:00 ~ 04:59', 100, 200)
# station1.show()


