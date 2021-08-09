import numpy as np
import pandas as pd
from scipy.stats import ks_2samp


# During sampling, we need to check if the distributions are similar to the original data by setting a significance level 
# and using Kolmogorov-Smirnoff method.
def get_sample(df, significance = 0.05, sample_size = 5000, iterations = 100):
    for i in range(iterations):
        sample = df.sample(sample_size)
        sample_indexes = sample.index
        retrieved = True

        for var in range(df.shape[1]):
            var_sample = np.array(sample.iloc[:,var])
            metrics = ks_2samp(df.iloc[:,var], var_sample)
            pvalue = round(metrics[1], 3)

            if pvalue < significance: 
                retrieved = False
                break

        if retrieved == True: 
            print('found sample after {} iterations'.format(i+1) )
            return sample
            
    if not retrieved: raise ValueError("Could not build samples with {} iterations, significane={}, and sample_size={}"
                           .format(iterations,significance,sample_size))