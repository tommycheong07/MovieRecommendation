# DELETE  FROM
#     moviegenre a
#         USING moviegenre b
# WHERE
#     a.id < b.id
#     AND a."movieID" = b."movieID";



# ALTER TABLE 'movieGenre' DROP CONSTRAINT movieidgenreconstraint;


from database import *

# MovieGenre.drop_table()

with db:
   db.create_tables([MovieGenre])

movieIDs = []

for row in Movie.select():
	movieIDs.append(row.movieID)

for movieID in movieIDs:
	movieIDSearch = movieID

	if movieID[0] == '-':
		movieIDSearch = movieID[1:]
	elif 'partment-' in movieID:
		movieIDSearch = movieID[9:]



	URL = get('https://www.imdb.com/title/'+ movieIDSearch +'/')
	movieSoup = BeautifulSoup(URL.text, 'html.parser')

	divs = movieSoup.findAll('div', class_='see-more inline canwrap')
	for div in divs:
		if (div.h4.text == 'Genres:'):
			for a in div.findAll('a', href=True):
				MovieGenre.insert(movieID=movieID, genre=a.text.strip()).execute()

	print(movieID)

