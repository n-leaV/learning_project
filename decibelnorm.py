import numpy as np
import sys
import argparse

from operations import data_extract as dataExtract
from operations import select_file as selectFile


def parserInit():                                                                                               #arg parsing initialize
    parser = argparse.ArgumentParser(description='Normalize decibel readings to 1ft.')
    parser.add_argument('filename', help="File to normalize")
    parser.add_argument('-c', '--columns', help="Number of columns to normalize", nargs='+', type = int)
    parser.add_argument('-s','--skipheader', action='store_true', help='Skip the header when normalizing data')
    #args = parser.parse_args(['C:/Users/nleavitt/Python/Acoustic_test/data_2.csv', '-c 0 2' ])
    args = parser.parse_args()
    return args

def errorLogic(args):                                                               #error logic ensuring no invalid arguments
    file = args.filename
    cols = args.columns
    # if cols < 1:
    #     argparse.ArgumentError
    #     #print("No regression model selected.")
    #     sys.exit("Cannot normalize 0 columns")

    if not file.endswith('.csv'):
        argparse.ArgumentError
        #print('Invalid filetype, select a .csv file')
        sys.exit('Invalid filetype, select a .csv file')


def dataPull(file, args):                                                   #pulling data from selected .csv
    cols = args.columns
    header = args.skipheader
    # collist = []
    # for i in cols:
    #     collist.append(i)
    #     i+=1
    data = np.genfromtxt(file, delimiter=',',skip_header=header, usecols = cols)
    return data



def main():
    file = ""
    args = parserInit()
    errorLogic(args)
    file = args.filename
    data = dataPull(file, args)
    print(data)


if __name__ == "__main__":
    main()