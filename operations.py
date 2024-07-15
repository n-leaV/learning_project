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

def totalSquares (y):                                                                                 #where y is the measured data
    #lon = y.shape[0]
    avg = np.average(y)
    sum = 0
    for i in range(0, len(y), 1):
        sum = sum + (y[i]-avg)**2
    return sum

def rSquared(rss, tss):
    rsqrd = 1-(rss/tss)
    return rsqrd


def select_file():                                #Open file dialogue
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(          
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)            #grabbing the filename

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
    def __init__(self, x, y, *args, **kwargs):
        self.datalength = len(x)
        self.matrix(x)
        self.bmod = np.matmul(self.A.transpose(),y)
        self.augment = np.column_stack((self.symmetric, self.bmod)) 
        self.echelon = reduction(self.augment)
        self.soln = self.echelon[:,-1]
        self.a = self.echelon[0,-1]
        self.b = self.echelon[1,-1]
        self.c = self.echelon[2,-1]
        self.residualSum(x, y, self.soln)
        self.tss = totalSquares(y)
        self.rsqd = rSquared(self.rss, self.tss)

    def matrix(self, x):
        left = np.multiply(x, x)
        self.A =np.column_stack((left, x, np.ones(self.datalength)))
        self.symmetric = np.matmul(self.A.transpose(), self.A)
    
    def residualSum (self, x, y, c):                                        #where x is xvals, y is measured vals, and c is the solution vector
        sum = 0
        for i in range(0, self.datalength, 1):
            sum = sum + (y[i]-(x[i]**2*c[0]+x[i]*c[1]+c[2]))**2
        self.rss = sum

    pass


def main():
    file = select_file()
    data = data_extract(file)
    print(data)
    test = polynomial(data[:,0], data[:,2])
    print(test.echelon)
    print(test.soln)
    print(test.rsqd)



if __name__ == "__main__":
    main()