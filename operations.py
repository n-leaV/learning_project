import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv
from io import StringIO
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def reduction(matrix):
    row = matrix.shape[0]

    for j in range(0, row):                      #downward phase of row reduction, iterates through and reveals pivots. should be scalable
        for i in range(j, row-1):
            matrix[i+1,:] = matrix[i+1,:] - np.multiply(matrix[i+1,j]/matrix[j,j], matrix[j,:])
            #print(aug)
            i += 1
        j += 1

    for i in range(0, row):                      #normalizing pivot rows to a pivot value of 1
        matrix[i,:] = matrix[i,:]/matrix[i,i]
        #print(aug)
        i +=1

    for j in range(row-1, 0, -1):                #upward phase of row reduction, iterates through and solves for pivots. decrementing loop
        for i in range(j, 0, -1):
            matrix[i-1,:] = matrix[i-1,:] - np.multiply(matrix[i-1,j], matrix[j,:])
            #print(aug)
    
    return matrix


def select_file():                                #Open file dialogue
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )

    #grabbing the filename
    global filename
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    return filename

def data_extract(filename):
    #global data
    #global lon
    headers = []
    cols = []
    data = []

    # pulling headers out via csvreader--probably time consuming if file is large
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)

    # finding non empty cols via headers
    for i in range(len(headers)):   
        if headers[i] != '':
            cols.append(i)
            i +=1

    # data extraction
    data = np.genfromtxt(filename, delimiter=',',skip_header=1, usecols = (cols[0],cols[1],cols[2]))   
    #lon = data.shape[0]
    return data

class polynomial:
    def __init__(self, data, *args, **kwargs):
        for i in range(data.shape[1])
    pass


def main():
    file = select_file()
    data = data_extract(file)

if __name__ == "__main__":
    main()