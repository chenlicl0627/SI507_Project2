# SI507 Project 2

## What this program can do?

This program can present the information about a movie database on website. This database contains thousands of movie records with movie names, directors, genres, ratings and etc.

More specifically, it displays the following information:

1. Go to `127.0.0.1:5000/` and you will find the number of movie records in the movie database out there.
2. Go to `127.0.0.1:5000//movies/ratings/` and you will see the names and IMBD rating of the first five movies in format like this "The Land Girls | 6.1
".

## What is the project structure?

The project contains multiple files. `README.md` (this file) is the description of the project. `requirements.txt` is used to help you install all dependencies of the project. `movies_tools.py` defines a Movie class. `SI507_project2.py` is a simple Flask app that routes incoming requests, validate these requests, process them using `movies_tools.py`, and return processed results to users.

## What are the dependencies?

You have to install Python and a python package called `Flask`. You can install `Flask` manually using `pip`, a Python package manager:

> pip install Flask

But you can install everything you need by using the included `requirements.txt` file.

Make sure you have `virtualenv` installed. If you don't, use the following command to install `virtualenv`:

> pip install virtualenv

Then, `cd` to the project directory and activate `virtualenv`:

> source venv/bin/activate

Then, you can install this project's dependencies:

> pip install -r requirements.txt

## How to run the project?

After you have your dependencies installed, run the following commands:

> export FLASK_APP=SI507_project2.py
> flask run

Then, you can check out the following URLs at your choice:

http://127.0.0.1:5000
http://127.0.0.1:5000//movies/ratings/
