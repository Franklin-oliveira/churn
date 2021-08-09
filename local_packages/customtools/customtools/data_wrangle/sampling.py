"""contains customized resampling tools
"""

import numpy as np
import pandas as pd
from scipy.stats import ks_2samp


# During sampling, we need to check if the distributions
# are similar to the original data by setting a
# significance level
# and using Kolmogorov-Smirnoff method.
# TODO refactor this function into smaller blocks
def get_sample(df, sample_size=5000, significance=0.05, iterations=100):
    """Applies a sampling method to a dataframe assuring that the sampled \
data has the same distribution as the original dataset.

    By default, the function applied Kolmogorov-Smirnoff method to \
check the sampled distributions against the original data.

    :param df: pandas.DataFrame containing the original dataset
    :param significance: significance level applied in Kolmogorov-Smirnoff \
method, i.e., scipy.stats.ks_2samp (Default value = 0.05)
    :param sample_size: size of the new sampled data, i.e., total \
lines of the new dataframe (Default value = 5000)
    :param iterations: number of iterations to compose the new \
sample (Default value = 100)

    :return: new pandas.DataFrame containing resampled data

    >>> import numpy as np
        from scipy import stats

        np.random.seed(101)
        rng = np.random.default_rng()

        n1 = 200  # size of first sample
        n2 = 300  # size of second sample

        rvs1 = stats.norm.rvs(size=n1, loc=0., scale=1, random_state=rng)
        rvs2 = stats.norm.rvs(size=n2, loc=0.5, scale=1.5, random_state=rng)

        temp = pd.DataFrame([rvs1, rvs2], index=['rvs1', 'rvs2']).transpose()

        get_sample(temp, sample_size=1).values

    array([[0.57353548, 2.36881401]])
    """
    for i in range(iterations):
        sample = df.sample(sample_size)
        sample_indexes = sample.index
        retrieved = True

        for var in range(df.shape[1]):
            var_sample = np.array(sample.iloc[:, var])
            metrics = ks_2samp(df.iloc[:, var], var_sample)
            pvalue = round(metrics[1], 3)

            if pvalue < significance:
                retrieved = False
                break

        if retrieved:
            print('found sample after {} iterations'.format(i+1))
            return sample

    if not retrieved:
        raise ValueError(
            "Could not build samples with {} iterations, significane={}, \
and sample_size={}".format(iterations, significance, sample_size)
        )
