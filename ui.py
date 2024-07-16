import sys
import getopt
import argparse

def main():
    class options:
      def __init__(self, argv):
            i=4

      pass  

    parser = argparse.ArgumentParser(description='Run regression models on .csv data.')
    parser.add_argument('filename')
    parser.add_argument('-p','--polynomial', action='store_true', help='Use the polynomial regression model.')
    parser.add_argument('-e','--exponential', action='store_false', help='Use the polynomial regression model.')



if __name__ == "__main__":
    main()