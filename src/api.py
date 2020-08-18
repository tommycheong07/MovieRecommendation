import flask
from recommend import *
from flask import request, jsonify, Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/movierec', methods=['GET'])
@cross_origin()
def api_filter():
	query_parameters = request.args

	actors = query_parameters.get('actors')
	genres = query_parameters.get('genres')

	actorList = []
	genreList = []

	if actors is not None:
		actorList = actors.split(",")
	if genres is not None:
		genreList = genres.split(",")


	print("searching ... please wait")

	if len(actorList) == 0 and len(genreList) == 0:
		print("You did not provide an actor or genre to search")
	elif len(genreList) == 0:
		ret = searchByActors(actorList)
		return jsonify(ret)
	elif len(actorList) == 0:
		ret = searchByGenres(genreList)
		return jsonify(ret)
	else:
		ret = search(actorList, genreList)
		return jsonify(ret)

app.run()



