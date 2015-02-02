import argparse
from walk_throught_folders import get_excel_files
parser = argparse.ArgumentParser(description="get all xls input")
parser.add_argument('-i','--input_folder', type=str, dest="ifolder")
parser.add_argument('-n','--name', default='output.xls', type=str, dest="name")
parser.add_argument('-o','--output_folder', type=str, dest="ofolder")
args = parser.parse_args()
if __name__ == '__main__':
    input_folder = args.ifolder
    output_folder = args.ofolder or input_folder
    get_excel_files(input_folder)



