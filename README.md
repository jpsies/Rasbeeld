# Rasbeeld.nl

This is a tool developed by Wageningen University master students to assess the risk of rare Dutch domestic breeds to get extinct. The result of iRADAR, the analysis tool, is the score of the breed at 6 different indicators. This score is displayed in a radar graph. The tool comes with a website that allows interested people to view these scores and also makes it possible for association secretaries to enter new data. You can visit a live demo at [rasbeeld.nl](www.rasbeeld.nl).


![screenshot](http://rasbeeld.nl/images/screenshot_rasbeeld.png "Screenshot rasbeeld.nl")

## Requirements and dependencies

DutchRareBreeds requires the following in order to fully work:

- `Python >= 3.5`, older versions of Python won't work.

Pip should handle all the dependencies automatically, make sure you have [pip](https://pip.pypa.io/en/stable/installing/) pre-installed. 
The tool also requires a database to connect with, make sure you have [postgres](https://wiki.postgresql.org/wiki/Detailed_installation_guides) running and have created a database.


## Installation

DutchRareBreeds depends on a few libraries in order to work, installing it with pip should take care of everything automatically. 

First clone the repository using git and go into the new folder:
```bash
git clone git@github.com:jpsies/Rasbeeld.git
cd Rasbeeld
```

Install virtualenv
```bash
pip install virtualenv
```

Before installing DutchRareBreeds you should setup a virtual environment:
```bash
virtualenv -p python3 venv  # create virtual environment
source venv/bin/activate    # activate virtual environment
```

After you have successfully setup a virtual environment you can install DutchRareBreeds with [pip](https://pip.pypa.io/en/stable/installing/).  Run the following command while your virtual environment is active.

```bash
pip install -e .
```

Now we only need to setup the database. Make sure you already have [postgres](https://wiki.postgresql.org/wiki/Detailed_installation_guides) running and have created a database. Now open the **development.ini** file and change the sqlalchemy.url setting.

```bash
sqlalchemy.url = postgresql://<user>:<pass>@<host>/<db_name> 
```

To build the risk_factors, species and breeds tables you need to run:

```bash
alembic -c development.ini upgrade heads
```


## How to use it

Have you successfully installed everything? Awesome! Now you are ready to run DutchRareBreeds on your local machine. You can do this with one simple command:

```bash
pserve development.ini (--reload)
```

By adding the reload flag to you command you can enable auto-reload. This can be useful during development but should never be enabled on your production project.


## Tests

To make sure everything works as it supposed to do you can run tests. You can run all tests by executing the following command:

```bash
python setup.py test
```
