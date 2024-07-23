import sys
#import numpy
import getopt
import argparse
from operations import data_extract as dataExtract
from operations import select_file as selectFile
from operations import polynomial, exponential

def parserInit():
    parser = argparse.ArgumentParser(description='Run regression models on .csv data.')
    parser.add_argument('filename', help="File to regress")
    parser.add_argument('-p','--polynomial', action='store_true', help='Use the polynomial regression model.')
    parser.add_argument('-e','--exponential', action='store_true', help='Use the exponential regression model.')
    parser.add_argument('-g','--gui', action='store_true', help='Use the GUI to select a file')
    #args = parser.parse_args(['-p', 'C:/Users/nleavitt/Python/Acoustic_test/data_2.csv' ])
    args = parser.parse_args()
    return args

def errorLogic(args):
    file = args.filename
    poly = args.polynomial
    exp = args.exponential
    gui = args.gui
    if not (poly or exp)== True:
        argparse.ArgumentError
        #print("No regression model selected.")
        sys.exit("No regression model selected.")

    if not file.endswith('.csv'):
        argparse.ArgumentError
        #print('Invalid filetype, select a .csv file')
        sys.exit('Invalid filetype, select a .csv file')


def main():
    args = parserInit()
    #print(args.filename)    
    #print(args.polynomial)
    #print(args.exponential)
    file = args.filename
    
    if args.gui == True: file = selectFile()

    errorLogic(args)

    #poly = args.polynomial
    #exp = args.exponential

    data = dataExtract(file)
    #print(data)
    if args.polynomial == True: 
        test = polynomial(data[:,0], data[:,2])
        print("Polynomial regression selected")
    if args.exponential == True: 
        test = exponential(data[:,0], data[:,2])
        print("Exponential regression selected")

    print("\tRegression constants are", test.soln)
    print("\tThe R squared value is", test.rsqd)
    #print(test.rss)
    #print(test.tss)

if __name__ == "__main__":
    main()