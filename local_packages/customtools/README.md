# custom_tools

A python local module containing blocks of reusable code (in form of custom pre-built functions/classes) to be used on multiple steps of Machine Learning pipelines, from data cleansing, sampling and validation to constructing custom models pipelines and visualizations. 

## Authors
* [Marcelo B. Barata Ribeiro](https://www.linkedin.com/in/marcelobarataribeiro/)
* [Franklin Oliveira](https://www.github.com/Franklin-oliveira)

## submodules list

- **data_wrangle**: contains customly built functionalities for data manipulation and validation.
- **eda**: has custom functions/classes useful for Exploratory Data Analysis.

## Instalation

To use all of its functionalities into your scripts/notebooks anywhere across your Operating System, first you're gonna need to install the `custom_tools` package in editable mode by running the following command:

```bash
pip install -e .
```

> **p.s.:** make sure you run this command in your terminal instance inside the same folder as the `setup.py` file. 

### Dependencies

This module depends on other Python packages. Some of them are listed below:

```bash
numpy - pandas - scipy - sklearn
```

The full list of dependencies necessary to recreate the python environment can be found on `requirements.txt` file. All necessary libraries will be installed during the `custom_tools` instalation process, via `setup.py`.

Although, they can also be installed by running the following command:

```bash
pip install -r requirements.txt
```

## Demo

(some usage examples will be added later)