import numpy
import argparse

from operations import data_extract as dataExtract
from operations import select_file as selectFile


def parserInit():
    parser = argparse.ArgumentParser(description='Normalize decibel readings to 1ft.')
    parser.add_argument('filename', help="File to normalize")
    parser.add_argument('-c','--columns', action='store_true', help='Use the polynomial regression model.')
    #args = parser.parse_args(['-p', 'C:/Users/nleavitt/Python/Acoustic_test/data_2.csv' ])
    args = parser.parse_args()
    return args


def dataPull():
    i=2




def main():
    file = ""
    file = dataExtract()


if __name__ == "__main__":
    main()