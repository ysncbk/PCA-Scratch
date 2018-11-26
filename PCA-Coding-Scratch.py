"Machine Learning- PCA- Yasin"

import numpy as np
import matplotlib.pyplot as plt
#Loading the dataset
X=np.loadtxt('/home/yasin/mfeat-pix.txt')
X
#Plot the five first digits
def plot_database(database):
    for i in range (5):
        for j in range (5):
            plt.subplot(1, 5, j+1) #make a 1 by 5 grid, and paste in each grid the jth element, note that j starts with zero, therefore jth+1 for the first element
            databases=database[j + 200 * i,].reshape(16, 15) #select the first row,240 digits, of the digits array, and reshape them in a matrix 16x15 
            plt.imshow(databases, cmap='gray') #plot a grid, where the number is the "gray" value
            plt.axis('off') #Turn plot axis off
        plt.show() # show the graph
plot_database(database=X)

# Plot first five digits according to entered explained variance value
def eigenvalvec(ind_exp_var,AdjMt,M,f1):
    evec = U[:,:ind_exp_var] # Taking specified columns of eigenvecotr matix
    enc_x=np.dot(AdjMt,evec) #Using the specified eigenvectors to compress X, in a lower dimension (200*4)
    domf=np.dot(enc_x,evec.T)+M #Usind compressed X and transpose of eigenvectors to uncompress images 
    for i in range (5):
        plt.subplot(1, 5, i+1) #make a 1 by 5 grid, and paste in each grid the jth element, note that j starts with zero, therefore jth+1 for the first element
        domf_a=domf[i,:].reshape(16,15) #select the first row,240 digits, of the digits array, and reshape them in a matrix 16x15 
        plt.imshow(domf_a,cmap='gray')  #plot a grid, where the number is the "gray" value
        plt.axis('off')#Turn plot axis off
    plt.show() # show the graph
    print("The number of eigenvectors used:",ind_exp_var," and the % of variation explained:",f1*100) # Printing number of eigenvectors used for explaining variation
#-------------------------------------------------------------------------------
ones=X[200:400,0:240] #Selecting number ones (1) from the data base
ones

#Calculate mean of 200 vectors
M=np.mean(ones, axis=0)
print(M)
#Subtract Mean from every vector
AdjMt = ones-M
print(AdjMt)
#Data Covariance matrix of Ones
R  = np.dot(AdjMt.T,AdjMt) / (ones.shape[0]-1)
#SVD of Covariance Matrix
U, s, V = np.linalg.svd(R, full_matrices=True)
# Sorting Eigenvectors and corresponding Singular values
idx = s.argsort()[::-1]   
s = s[idx]
U = U[idx]
#Entering 
while True:
    f1=float(input("How much variations should be explained (values bw 0<= val<=1)or to exit press Enter?\n"))# User input value bw 0<=f1<=1,
    exp_var=np.cumsum(s)/sum(s) #Taking cumulative proportion of variation explained by sv's and corresponding eigenvectors 
    ind_exp_var=np.searchsorted(exp_var,f1)+1 # Comaparing cumulative proportion of variation explained by sv's and corresponding eigenvectors and the entered value by user
    if f1 == 1 : # Because of decimals, before the last vector summation of sv's reach 1, That is why we add this condition to take into considereation all eigenvectors
        ind_exp_var=240
    if f1 == " ":# condition for breaking while loop
        break
    eigenvalvec(ind_exp_var,AdjMt,M,f1)#Calling the funcction defined above
