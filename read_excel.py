from xlrd import open_workbook

# with open('simple.xls','rb') as f:
# print open_workbook(
# file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
# )
# aString = open('simple.xls','rb').read()
# print open_workbook(file_contents=aString


def parse_xls(filename):

    xls = open_workbook(filename).sheets()[0]
    for row in xrange(xls.nrows):
        values = []
        for col in xrange(xls.ncols):
            value = xls.cell(row,col).value
            if value == '':
                break
            values.append(value)
            #print(','.join(values))

        print(values)

