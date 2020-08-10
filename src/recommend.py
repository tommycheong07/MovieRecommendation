from database import *

baseGenreList = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 
'Documentary', 'Drama', 'Family', 'Fantasy', 'Game Show', 'History', 'Horror', 'Music', 
'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport', 'Superhero', 
'Talk Show', 'Thriller', 'War', 'Western']


# def printQuery(movieInfo, genres):
# 	print(movieInfo.movie, movieInfo.summary, movieInfo.rating, genres)
# 	print("\n")

def appendGenreAndPrint(moviesQ, recMoviesQ):
	for row in moviesQ:
		genres = []
		genres_q = (MovieGenre.select().where(MovieGenre.movieID == row.movieID))

		for genre in genres_q:
			genres.append(genre.genre)

		print(row.movie, row.summary, row.rating, genres)
		print("\n")


def searchByGenres(genres):
	genreList = genres.split(', ')
	movies_q = (MovieGenre.select().where(MovieGenre.genre.in_(genreList)))

	movieIDList = []

	for row in movies_q:
		movieIDList.append(row.movieID)


	movieInfo_q = (Movie.select().where(Movie.movieID.in_(movieIDList)).order_by(Movie.rating.desc()).limit(10))

	return appendGenreAndPrint(movieInfo_q)

def searchByActors(actorNames):
	actorNamesList = actorNames.split(', ')
	actor_q = (ActorMovie.select().where(ActorMovie.actorName.in_(actorNamesList)))

	actorMovieList = []

	for row in actor_q:
		actorMovieList.append(row.movieID)


	movies_q = (Movie.select().where(Movie.movieID.in_(actorMovieList)).order_by(Movie.rating.desc()).limit(10))

	recommend_movies_q = recommendByActors(actorNamesList, actorMovieList)

	return appendGenreAndPrint(movies_q)

def search(actorNames, genres):
	actorNameList = actorNames.split(', ')
	genreList = genres.split(', ')

	movies_q = (MovieGenre.select().where(MovieGenre.genre.in_(genreList)))

	genreMovieList = []

	for row in movies_q:
		genreMovieList.append(row.movieID)


	actor_q = (ActorMovie.select().where(ActorMovie.actorName.in_(actorNameList)))

	actorMovieList = []

	for row in actor_q:
		actorMovieList.append(row.movieID)

	movieInfo_q = (Movie.select().where(Movie.movieID.in_(actorMovieList) and Movie.movieID.in_(genreMovieList)).order_by(Movie.rating.desc()).limit(10))

	return appendGenreAndPrint(movieInfo_q)


def recAppendGenreAndPrint(moviesQ):
	print("we also recommend these movies that you may be interested in:\n")
	for row in moviesQ:
		genres = []
		genres_q = (MovieGenre.select().where(MovieGenre.movieID == row.movieID))

		for genre in genres_q:
			genres.append(genre.genre)

		print(row.movie, row.summary, row.rating, genres)
		print("\n")

def recByActors(actorNamesList, movieList):
	otherActors = (ActorMovie.select(ActorMovie.nm, fn.COUNT(ActorMovie.nm))
								.join(Movie, on=(ActorMovie.movieID == Movie.movieID))
								.where(Movie.movieID.in_(movieList) and ActorMovie.actorName.not_in(actorNamesList))
								.limit(3))

	recMovies = (Movie.select().join(ActorMovie, on=(ActorMovie.movieID == Movie.movieID))
								.where(ActorMovie.nm.in_(otherActors.nm) and Movie.movieID.not_in(movieList))
								.order_by(Movie.rating.desc())
								.limit(5))

	return recMovies



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

