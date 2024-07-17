import sys
import getopt
import argparse
from operations import data_extract , polynomial, exponential

def parserInit():
    parser = argparse.ArgumentParser(description='Run regression models on .csv data.')
    parser.add_argument('filename', help="File to regress")
    parser.add_argument('-p','--polynomial', action='store_true', help='Use the polynomial regression model.')
    parser.add_argument('-e','--exponential', action='store_true', help='Use the polynomial regression model.')
    args = parser.parse_args(['-p', 'C:/Users/nleavitt/Python/Acoustic_test/data_2.csv' ])
    #args = parser.parse_args()
    return args

def parserLogic(args):
    file = args.filename
    poly = args.polynomial
    exp = args.exponential
    if not (poly or exp)== True:
        argparse.ArgumentError
        print("No regression model selected.")
        sys.exit("No regression model selected.")

    if not file.endswith('.csv'):
        argparse.ArgumentError
        print('Invalid filetype, select a .csv file')
        sys.exit('Invalid filetype, select a .csv file')


def main():
    args = parserInit()
    print(args.filename)    
    print(args.polynomial)
    print(args.exponential)
    parserLogic(args)

    file = args.filename
    poly = args.polynomial
    exp = args.exponential

    data = data_extract(file)
    #print(data)
    test = exponential(data[:,0], data[:,2])
    print(test.soln)
    print(test.rsqd)
    print(test.rss)
    print(test.tss)

if __name__ == "__main__":
    main()