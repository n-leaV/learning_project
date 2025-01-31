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
    #print(row)
    #print(matrix)
    for j in range(0, row):                      #downward phase of row reduction, iterates through and reveals pivots. should be scalable
        for i in range(j, row-1):
            matrix[i+1,:] = matrix[i+1,:] - np.multiply(matrix[i+1,j]/matrix[j,j], matrix[j,:])
            #print(matrix)
            i += 1
        j += 1

    for i in range(0, row):                      #normalizing pivot rows to a pivot value of 1
        matrix[i,:] = matrix[i,:]/matrix[i,i]
        #print(matrix)
        i +=1

    for j in range(row-1, 0, -1):                #upward phase of row reduction, iterates through and solves for pivots. decrementing loop
        for i in range(j, 0, -1):
            matrix[i-1,:] = matrix[i-1,:] - np.multiply(matrix[i-1,j], matrix[j,:])
            #print(matrix)
    
    return matrix

def totalSquares (y):                                                                                 #where y is the measured data
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
    return data

class polynomial:                                                       #defining poly regression
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

    def matrix(self, x):                                                #polynomial matrix construction method
        left = np.multiply(x, x)
        self.A = np.column_stack((left, x, np.ones(self.datalength)))
        self.symmetric = np.matmul(self.A.transpose(), self.A)
    
    def residualSum (self, x, y, c):                                        #where x is xvals, y is measured vals, and c is the solution vector
        sum = 0
        for i in range(0, self.datalength, 1):
            sum = sum + (y[i]-(x[i]**2*c[0]+x[i]*c[1]+c[2]))**2
        self.rss = sum

    pass

class exponential:                                                      #defining exp regression
    def __init__(self, x, y, *args, **kwargs):
        self.datalength = len(x)
        self.matrix(x)
        self.z = np.log10(y)
        self.zmod = np.matmul(self.A.transpose(),self.z)
        self.augment = np.column_stack((self.symmetric, self.zmod)) 
        self.echelon = reduction(self.augment)
        self.soln = self.echelon[:,-1]
        self.m = self.echelon[0,-1]
        self.b = self.echelon[1,-1]
        self.a = 10**self.b
        self.residualSum(x, self.z, self.soln)
        self.tss = totalSquares(self.z)
        self.rsqd = rSquared(self.rss, self.tss)

    def matrix(self, x):                                                #exponential matrix construction method
        self.A = np.column_stack((x, np.ones(self.datalength)))
        self.symmetric = np.matmul(self.A.transpose(), self.A)

    def residualSum (self, x, y, c):                                    #exponential residual sums method
        sum = 0
        for i in range(0, self.datalength, 1):
            sum = sum + (y[i]-(x[i]*c[0]+c[1]))**2
        self.rss = sum        
    
    pass




def main():
    #file = select_file()
    #print(file)
    file = "C:/Users/nleavitt/Python/Acoustic_test/data_2.csv"
    data = data_extract(file)
    print(data)
    test = exponential(data[:,0], data[:,2])
    # print(test.echelon)
    print(test.soln)
    print(test.rsqd)
    print(test.rss)
    print(test.tss)



if __name__ == "__main__":
    main()