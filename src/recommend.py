from database import *

baseGenreList = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 
	'Documentary', 'Drama', 'Family', 'Fantasy', 'Game Show', 'History', 'Horror', 'Music', 
	'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport', 'Superhero', 
	'Talk Show', 'Thriller', 'War', 'Western']


def printQuery(query):
	for row in query:
		print(row)

def test():
	query = (ActorMovie.select(ActorMovie.nm, ActorMovie.actorName, ActorMovie.movieID).limit(5))

	printQuery(query)


def searchGenre(genres):
	query = (ActorMovie.select(ActorMovie.nm, ActActorMovieor.actorName, Movie.movieID, Movie.movie, MovieGenre.genre, Movie.rating, Movie.summary)
		.join(Movie, on=(ActorMovie.movieID == Movie.movieID))
		.join(MovieGenre, on=(Movie.movieID == MovieGenre.movieID))
		.where(Movie.genre in genres)
		.order_by(Movie.rating)
		.limit(10))

	printQuery(query)

def searchActor(actorNames):
	query = (ActorMovie.select(ActorMovie.nm, ActorMovie.actorName, Movie.movieID, Movie.movie, MovieGenre.genre, Movie.rating, Movie.summary)
		.join(Movie, on=(ActorMovie.movieID == Movie.movieID))
		.join(MovieGenre, on=(Movie.movieID == MovieGenre.movieID))
		.where(ActorMovie.actorName in actorNames)
		.order_by(Movie.rating)
		.limit(10))

	printQuery(query)

def search(actorNames='', genres=baseGenreList):
	actorNameList = actorNames.split(', ')
	if isinstance(genres, str):
		genres = genres.split(', ')

	if len(actorNameList) == 1 and actorNameList[0] == '' and len(genres) < 26:
		searchGenre(genresList)
	elif len(genres) == 26:
		searchActor(actorNameList)
	else:
		query = (ActorMovie.select(ActorMovie.nm, ActorMovie.actorName, Movie.movieID, Movie.movie, MovieGenre.genre, Movie.rating, Movie.summary)
		.join(Movie, on=(ActorMovie.movieID == Movie.movieID))
		.join(MovieGenre, on=(Movie.movieID == MovieGenre.movieID))
		.where(ActorMovie.actorName in actorNameList and MovieGenre in genres)
		.order_by(Movie.rating)
		.limit(10))

	printQuery(query)




# def recommend(actorNames, genres):
# 	# thinking: filter by movies of that actor, then select names of all the other actors in
# 	# those movies and have a count, then choose top 2 actors based on count and filter by
# 	# genre the user selected

# 	actorNameList = actorNames.split(', ')
# 	genreList = genres.split(', ')

# 	if len(actorNameList) == 1 and actorNameList[0] == '':
# 		movieID_query = (Movie.select(Movie.movieID)
# 		.join(ActorMovie, on(ActorMovie.movieID == Movie.movieID))
# 		.where(Movie.genre << fn.COALESCE(genreList, baseGenreList))
# 		.limit(10))
# 	else:
# 		movieID_query = (Movie.select(Movie.movieID)
# 		.join(ActorMovie, on(ActorMovie.movieID == Movie.movieID))
# 		.where(ActorMovie.actorName << actorNameList))

# 	otherActors = (ActorMovie.select(ActorMovie.nm, fn.COUNT(ActorMovie.nm))
# 	.join(Movie, on=(ActorMovie.movieID == Movie.movieID))
# 	.where(Movie.movieID << movieID_query)
# 	.order_by(fn.COUNT(ActorMovie.nm))
# 	.limit(3))

# 	recMovies = (Movie.select().join(ActorMovie, on=(Movie.movieID == ActorMovie.movieID))
# 	.where(ActorMovie.nm << otherActors.nm and Movie.genre << fn.COALESCE(genreList, baseGenreList)
# 		and Movie.movieID.not_in(movieID_query.movieID))
# 	.order_by(Movie.rating)
# 	.limit(5))

# import database.ActorMovie
# import psycopg2
# from peewee import *

# print(ActorMovie.select(ActorMovie.nm).distinct.count)

