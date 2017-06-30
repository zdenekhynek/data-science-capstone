# Capstone project

This is a proof of concept project to explore similiarities between articles
about terrorist attacks as reported by The Guardian,

## Requirements

- python
- pip
- Homebrew
- mongodb

## Installation on Mac OS X

### Installing pipenv (dependency manager)

```
pip install pipenv
```

### Installing pyenv (python version manager)

```
brew update
brew install pyenv
```

### Install python 3 version

```
pyenv install 3.6.0
```

### Setup

- cd to your working directory

- Use the right version of python:

```
pyenv local 3.6.0
```

- install all the dependecies:

```
pipenv install
```


- make sure you have following environment variables set:

MONGODB_URI='' # connection string to your mongodb instance
GUARDIAN_API_KEY='' # api key for the guardian api


## Run project


- activate pipenv shell

```
pipenv shell
```

- now you should be able to run all the python scripts in the right environment
by simple running:

```
python <name_of_the_script>.py
```

If it's not working for you, you can try running the scripts specifically
through pipenv run command:

```
pipenv run python <name_of_the_script>.py
```

Following scripts are available:

### Fetch all articles

```
python fetch_data.py
```

### Run k-means clusterisation

```
python clusterisation.py
```

### Run LDA (topical modelling)

```
python lda.py
```

### Create cluster visualisation with plotly

```
python visualise_clusters.py
```


Data exploration

There are following jupyter notebooks created as part of the data exploration:

- Clusters.ipynb
- Comparison.ipynb
- Exploration.ipynb
- Hierarchical clustering.ipynb
- LDA.ipynb
