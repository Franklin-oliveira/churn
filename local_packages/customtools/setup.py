from setuptools import setup, find_packages

setup(
    author = "Franklin Oliveira and Marcelo Ribeiro",
    description = "Custom module containing data wrangling, EDA and machine learning functionalities.",
    name = "customtools",
    version = "0.1.0",  
    packages = find_packages(include = ['customtools', 'customtools.*']),
    python_requires = '>=3.7',   # TODO need to add more flexibility here
    install_requires = [         # these dependencies need to be further checked, tested and specified in future versionss
        'impyute>=0.0.8',
        'matplotlib>=3.0.0',
        'numpy>=1.19.1',
        'pandas>=0.25.3',
        'scipy>=1.5.2',
        'seaborn>=0.9.0',
        'scikit-learn>=0.23.0',
        'statsmodels>=0.11.1',
        'xgboost>=0.90'
    ]
)