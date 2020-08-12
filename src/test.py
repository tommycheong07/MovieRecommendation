from recommend import *


actorList = []
genreList = []
while True:
	actor = input("Who would you like to search for? Enter after each actor/actress to add to search list.Press 1 to stop inputting.")
	if actor == '1':
		break
	actorList.append(actor)

while True:
	genre = input("What genre would you like to search for? Enter after each genre to add to list. Press 1 to stop inputting.")
	if genre == '1':
		break
	genreList.append(genre)


print("searching ... please wait")

if not actorList and not genreList:
	print("You did not provide an actor or genre to search")
elif not genreList:
	searchByActors(actorList)
elif not actorList:
	searchByGenres(genreList)
else:
	search(actorList, genreList)