import csv
import sys

import psycopg2
from peewee import *

db = PostgresqlDatabase(
    'imdb_actor',
    user='postgres',
    password='password',
    host='localhost')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class Actor(BaseModel):
    nm = CharField()
    name = CharField()

# with db:
#    db.create_tables([Actor])


# with open(sys.argv[1]) as read_file:
#     rd = csv.reader(read_file, delimiter="\t", quotechar='"')
#     for row in rd:
#         parts = row[0].split(',')
#         Actor.create(nm=parts[0], name=parts[1])


class ActorMovie(BaseModel):
    nm = CharField()
    actorName = CharField()
    movieID = CharField()

class Movie(BaseModel):
    movieID = CharField()
    movie = CharField()
    summary = TextField()
    rating = CharField()

class MovieGenre(BaseModel):
    movieID = CharField()
    genre = CharField()

# ActorMovie.drop_table()
# Movie.drop_table()
# MovieGenre.drop_table()

# with db:
#    db.create_tables([ActorMovie])
#    db.create_tables([Movie])
#    db.create_tables([MovieGenre])


from requests import get
from bs4 import BeautifulSoup

query = Actor.select().order_by(Actor.nm).offset(678)

# query = ['nm0000028']


# loop through every id in the tuple
for actor in query:
    id = actor.nm
    # id = actor
    url = 'https://www.imdb.com/name/' + id + '/?ref_=nmls_hd'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('td', class_='name-overview-widget__section')
    if name is None:
        continue
    anm = name.h1.span.text
    # print(anm)

    movies = soup.find('div', class_='filmo-category-section')
    for movie in movies.findAll('div'):
        idTag = movie.get('id') 
        # idTag = actor-id or actress-id
        if idTag is None or 'soundtrack' in idTag or 'episodes' in idTag:
            continue
        if idTag[:5] == 'actor':
            mID = idTag[7:]
        else:
            mID = idTag[8:]

        # inserting into actorMovie table
        ActorMovie.insert(nm=id, actorName = anm, movieID=mID).execute()

        # print(id)
        # print(anm)
        # print(mID)

        # going into movie url to find movie name and genre
        movieURL = movie.find('a', href=True)
        title = movieURL.text
        # print(title)
        URL = get('https://www.imdb.com' + movieURL['href'])
        movieSoup = BeautifulSoup(URL.text, 'html.parser')

        plot = movieSoup.find('div', class_='summary_text')
        if plot is not None and plot.a is not None and plot.a.text == 'See full summary':
            extraSummary = get('https://www.imdb.com' + plot.a['href'])
            summSoup = BeautifulSoup(extraSummary.text, 'html.parser')

            summplot = summSoup.find('li', class_='ipl-zebra-list__item')
            summ = summplot.p.text.strip()
            
        elif plot is not None:
            summ = plot.text.strip()
        else:
            summ = ''

        # print(summ)
        
        divs = movieSoup.findAll('div', class_='see-more inline canwrap')
        for div in divs:
            if (div.h4.text == 'Genres:'):
                for a in div.findAll('a', href=True):
                    # print(a.text.strip())
                    if MovieGenre.select().where(MovieGenre.movieID==mID).count() == 0:
                        MovieGenre.insert(movieID=mID, genre=a.text).execute()

        rating = movieSoup.find('span', itemprop='ratingValue')
        if rating is not None:
            rate = rating.text
        else:
            rate = 0
        # print(rate)

        # inserting into movie table
        if Movie.select().where(Movie.movieID==mID).count() == 0:
            Movie.insert(movieID=mID, movie=title, summary = summ, rating = rate).execute()

    print(id)


# print(db.get_tables())
# print(db.get_columns('actormovie'))


# query = ActorMovie.select(ActorMovie.nm).distinct().order_by(ActorMovie.nm)

# for a in query:
#     print(a.nm)


