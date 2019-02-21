from flask import Flask, render_template
import movies_tools
import csv

f = open("movies_clean.csv",'r')
file_lines = []
reader = csv.reader(f)
for row in reader:
    file_lines.append(row)
f.close()

def movie_input(n):
    movie_parameters = file_lines[n]
    return movie_parameters

app = Flask(__name__)


# Routes

@app.route('/')
def home():
    num_lines = len(file_lines)
    return '<h1>{} movies recorded.</h1>'.format(num_lines)## need a method or instance variable to represent the amount of movies.
###??? Why is <h1> not specified in the template file?



@app.route('/movies/ratings/')
def return_movies():
    movie1 = movies_tools.Movie(*movie_input(1))
    movie2 = movies_tools.Movie(*movie_input(2))
    movie3 = movies_tools.Movie(*movie_input(3))
    movie4 = movies_tools.Movie(*movie_input(4))
    movie5 = movies_tools.Movie(*movie_input(5))
    five_movie_list = [movie1, movie2, movie3, movie4, movie5]

    result = ""
    for i in five_movie_list:
        result += '{} | {}'.format(i.movie_name,i.imbd_rating) + "<br>"
    return result

if __name__ == '__main__':
	app.run()
