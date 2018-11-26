# PCA-Scratch
PCA Scratch coding by Python

Task: pick one of the digits (e.g. the "ones"), which gives you a dataset of 200
image vectors. Carry out a K-means clustering on your chosen sample, setting
K = 1 (!), 2, 3, and 200 in four runs of this algorithm. Generate visualizations of the
images that are coded in the respective codebook vectors that you get (for the K = 200
case, only visualize a few). Discuss what you see.

The aim of this project is to compress and uncompress images with PCA by entered values.
Entered values should specify the amount of variance that user want to preserve. 
As can be seen from 0 to 1 (and the values between them can be entered) the uncomressed images become clear.

With  almost 50% variance preserved:
By Python code , we choosed the appropriate number ( in this case 4) of eigenvectors in order to preserve approximately
50 percent of variance. Since the original data is explained by 240 features ( R240), 
our expectation was to obtain blurred ones.

With  almost 80% variance preserved:
In order to preserve more variance we are supposed to include more eigenvectors. 
Since more eigenvectors are used, we expect more clear images compared to the first case. 
In order to preserve almost 80 percent of variance, 18 eigenvectors are used. 

With  almost 99% variance preserved:
Almost preserving 99% of variation means more similar images to original ones. 
In order to preserve 99 percent of variation, 109 eigenvectors are used.

With 100% variance preserved:
Theoratically in order to preserve 100% of variation, we used all (240) eigenvectors. 
And our expectation was to obtain the images itself again.  
