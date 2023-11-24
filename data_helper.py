import csv


class DataHelper:

    def __init__(self, filename, header_line_count = 1):
        self.filename = filename
        self.header_line_count = header_line_count

    def get_header(self):
        csv_file = open(self.filename, 'r', encoding='utf-8-sig')
        csv_data = csv.reader(csv_file)

        header = []
        for i in range(self.header_line_count):
            header.append(next(csv_data))

        csv_file.close()

        if self.header_line_count < 2:
            return header[0]
        else:
            return header
    # end-def

    def get_data(self):
        csv_file = open(self.filename, 'r', encoding='utf-8-sig')
        csv_data = csv.reader(csv_file)

        for i in range(self.header_line_count):
            next(csv_file)

        data = []
        for line in csv_data:
            data.append(line)

        csv_file.close()

        return data
    # end-def

# end-class