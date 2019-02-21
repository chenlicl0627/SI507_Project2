## Define Movie class
class Movie(object):

    def

    def __init__(self,movie_name, us_gross,world_gross, us_dvd_sales, production_budget, release_date, mpaa_rating, running_time, distributor, source, major_genre, creative_type, director, rotten_tomatos_rating,imbd_rating, imbd_votes):
        self.movie_name = movie_name
        self.us_gross = us_gross
        self.world_gross = world_gross
        self.us_dvd_sales = us_dvd_sales
        self.production_budget = production_budget
        self.release_date = release_date
        self.mpaa_rating = mpaa_rating
        self.running_time = running_time
        self.distributor = distributor
        self.source = source
        self.major_genre = major_genre
        self.creative_type = creative_type
        self.director = director
        self.rotten_tomatos_rating = rotten_tomatos_rating
        self.imbd_rating = imbd_rating
        self.imbd_votes = imbd_votes

    def __str__(self):
        return "{}|{}".format(self.movie_name,self.imbd_rating)
