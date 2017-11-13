import movie_class
import fresh_tomatoes

m1_title = "Murder on the Orient Express"
m1_storyline = "A lavish trip through Europe quickly unfolds into a race against time to solve a murder aboard a train."
m1_poster = "http://nothingbutgeek.com/wp-content/uploads/2017/10/Murder-on-the-Orient-Express-02.jpg"
m1_trailer = "https://www.youtube.com/watch?v=Mq4m3yAoW8E"
MOTOE = movie_class.Movie(m1_title,m1_storyline,m1_poster,m1_trailer)

m2_title = "Justice League"
m2_storyline = "Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists newfound ally Diana Prince to face an even greater threat."
m2_poster = "http://www.konbini.com/us/files/2017/07/league.jpg"
m2_trailer = "https://www.youtube.com/watch?v=r9-DM9uBtVI"
JL = movie_class.Movie(m2_title,m2_storyline,m2_poster,m2_trailer)

movies = [MOTOE,JL]

#fresh_tomatoes.open_movies_page(movies)

print(movie_class.Movie.RATINGS)
