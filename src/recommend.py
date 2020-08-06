# baseGenreList = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 
# 	'Documentary', 'Drama', 'Family', 'Fantasy', 'Game Show', 'History', 'Horror', 'Music', 
# 	'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport', 'Superhero', 
# 	'Talk Show', 'Thriller', 'War', 'Western']


# def search(actorNames, genres):
# 	# how to protect against mis-spelled genre? check for each if it is in baseGenreList?
# 	actorNameList = actorNames.split(', ')
# 	genreList = genres.split(', ')

# 	if len(actorNameList) == 1 and actorNameList[0] == '':
# 		query = Actor.select(Actor.nm, Actor.ActorName, Movie.movieID, Movie.movie, Movie.genre, Movie.rating, Movie.summary)
# 		.join(ActorMovie, on=(Actor.nm == ActorMovie.nm))
# 		.join(Movie, on(ActorMovie.movieID == Movie.movieID))
# 		.where(Movie.genre << fn.COALESCE(genreList, baseGenreList))
# 		.order_by(Movie.rating)
# 		.limit(10)
# 	else:
# 		query = Actor.select(Actor.nm, Actor.ActorName, Movie.movieID, Movie.movie, Movie.genre, Movie.rating, Movie.summary)
# 		.join(ActorMovie, on=(Actor.nm == ActorMovie.nm))
# 		.join(Movie, on(ActorMovie.movieID == Movie.movieID))
# 		.where(ActorMovie.actorName << actorNameList and Movie.genre << fn.COALESCE(genreList, baseGenreList))
# 		.order_by(Movie.rating)
# 		.limit(10)

# def recommend(actorNames, genres):
# 	# thinking: filter by movies of that actor, then select names of all the other actors in
# 	# those movies and have a count, then choose top 2 actors based on count and filter by
# 	# genre the user selected

# 	actorNameList = actorNames.split(', ')
# 	genreList = genres.split(', ')

# 	if len(actorNameList) == 1 and actorNameList[0] == '':
# 		movieID_query = Movie.select(Movie.movieID)
# 		.join(ActorMovie, on(ActorMovie.movieID == Movie.movieID))
# 		.where(Movie.genre << fn.COALESCE(genreList, baseGenreList))
# 		.limit(10)
# 	else:
# 		movieID_query = Movie.select(Movie.movieID)
# 		.join(ActorMovie, on(ActorMovie.movieID == Movie.movieID))
# 		.where(ActorMovie.actorName << actorNameList)

# 	otherActors = ActorMovie.select(ActorMovie.nm, fn.COUNT(ActorMovie.nm))
# 	.join(Movie, on=(ActorMovie.movieID = Movie.movieID))
# 	.where(Movie.movieID << movieID_query)
# 	.order_by(fn.COUNT(ActorMovie.nm))
# 	.limit(3)

# 	recMovies = Movie.select().join(ActorMovie, on=(Movie.movieID = ActorMovie.movieID))
# 	.where(ActorMovie.nm << otherActors.nm and Movie.genre << fn.COALESCE(genreList, baseGenreList)
# 		and Movie.movieID.not_in(movieID_query.movieID))
# 	.order_by(Movie.rating)
# 	.limit(5)

import database.ActorMovie
import psycopg2
from peewee import *

print(ActorMovie.select(ActorMovie.nm).distinct.count)

