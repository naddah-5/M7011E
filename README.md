# M7011E
Project in dynamic web systems, basic web shop implemented in python Django with a relational database back end (SQLite).

## Requirements
In order to run this project you need to have Python 3 and pip installed, if you do not already have them installed you can find installation guides for them here:
> [Python 3](https://docs.python.org/3/using/windows.html)

> [pip](https://pip.pypa.io/en/stable/installation/)

## Set-up
Clone the repository and navigate to the directory:
```
> git clone https://github.com/naddah-5/M7011E.git
> cd M7011E
```
From this directory initiate a python venv, if you are unsure how to do this you can find a tutorial [here](https://docs.python.org/3/library/venv.html). After you have entered the venv, run the pip install for the requirements. This is done via the CLI like this:
```
> pip install -r requirements.txt
```
After all the requirements have been installed the database needs to be created and initiated. Do this by running the commands:
```
> python manage.py makemigrations
> python manage.py migrate
```

Once that is done we are ready to start the server by running the command:
```
> python manage.py runserver
```

You can then open the site by holding the ctrl-key and left-clicking the localhost ip-address.