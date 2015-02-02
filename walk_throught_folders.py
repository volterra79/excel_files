import os
from read_excel import parse_xls
def get_excel_files(ifolder):

    for f in os.listdir(ifolder):
        path = os.path.join(ifolder, f) #build the relative path of file/folder
        if os.path.splitext(f)[1] == '.xls':
            parse_xls(path)
        else:
            get_excel_files(path)

