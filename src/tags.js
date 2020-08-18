const actorTagContainer = document.querySelector('.actor-tag-container');

const actorInput = document.querySelector('.actor-tag-container input');

const genreTagContainer = document.querySelector('.genre-tag-container');

const genreInput = document.querySelector('.genre-tag-container input');

const searchBtn = document.querySelector('button');

var actorTags = [];

var genreTags = [];

function createActorTag(label) {
	const div = document.createElement('div');
	div.setAttribute('class', 'actorTag');

	const span = document.createElement('span');
	span.innerHTML = label;

	const closeBtn = document.createElement('i');
	closeBtn.setAttribute('class', 'material-icons');
	closeBtn.setAttribute('data-item', label);
	closeBtn.innerHTML = 'close';

	div.appendChild(span);
	div.appendChild(closeBtn);
	return div;
}

function actorTagReset() {
	document.querySelectorAll('.actorTag').forEach(function(actorTag) {
		actorTag.parentElement.removeChild(actorTag);
	})
}

function addActorTags() {
	actorTagReset();
	actorTags.slice().reverse().forEach(function(actorTag) {
		const input = createActorTag(actorTag);
		actorTagContainer.prepend(input);
	})
}

actorInput.addEventListener('keyup', function(e) {
	if (e.key === 'Enter') {
		actorTags.push(actorInput.value);
		addActorTags();
		actorInput.value = '';
	}
})

function createGenreTag(label) {
	const div = document.createElement('div');
	div.setAttribute('class', 'genreTag');

	const span = document.createElement('span');
	span.innerHTML = label;

	const closeBtn = document.createElement('b');
	closeBtn.setAttribute('class', 'material-icons');
	closeBtn.setAttribute('data-item', label);
	closeBtn.innerHTML = 'close';

	div.appendChild(span);
	div.appendChild(closeBtn);
	return div;
}

function genreTagReset() {
	document.querySelectorAll('.genreTag').forEach(function(genreTag) {
		genreTag.parentElement.removeChild(genreTag);
	})
}

function addGenreTags() {
	genreTagReset();
	genreTags.slice().reverse().forEach(function(genreTag) {
		const input = createGenreTag(genreTag);
		genreTagContainer.prepend(input);
	})
}

genreInput.addEventListener('keyup', function(e) {
	if (e.key === 'Enter') {
		genreTags.push(genreInput.value);
		addGenreTags();
		genreInput.value = '';
	}
})

document.addEventListener('click', function(e){
	if (e.target.tagName === 'I') {
		const value = e.target.getAttribute('data-item');
		const index = actorTags.indexOf(value);
		actorTags = [...actorTags.slice(0, index), ...actorTags.slice(index + 1)]
		addActorTags();
	}
	if (e.target.tagName === 'B') {
		const value = e.target.getAttribute('data-item');
		const index = genreTags.indexOf(value);
		genreTags = [...genreTags.slice(0, index), ...genreTags.slice(index + 1)]
		addGenreTags();
	}
})

$(document).ready(function () {
    $("#search").click(function (e) {
    	urlToSend = "http://127.0.0.1:5000/api/v1/movierec?"
    	if (actorTags.length == 0 && genreTags.length == 0){
                alert("You did not provide any actors or genres")
        }

        if (actorTags.length != 0) {
            urlToSend = urlToSend + "actors="
			for (x of actorTags) {
				var name = x.split(" ");
				for(y of name) {
					urlToSend = urlToSend + y + "+"
				}
				urlToSend = urlToSend.substring(0, urlToSend.length-1)
				urlToSend = urlToSend + ","
	        }
	        urlToSend = urlToSend.substring(0, urlToSend.length-1)
	    }

	    if (genreTags.length != 0) {
	        if (actorTags.length != 0) {
	            urlToSend = urlToSend + "&genres="
	        } else {
	            urlToSend = urlToSend + "genres="
	        }
	        for (x of genreTags) {
	            var name = x.split(" ")
	            for (y of name) {
	            	urlToSend = urlToSend + y + "+"
	            }
	            urlToSend = urlToSend.substring(0, urlToSend.length-1)
				urlToSend = urlToSend + ","
	        }
	        urlToSend = urlToSend.substring(0, urlToSend.length-1)
	    }
        $.ajax({
            type: "GET",
            url: urlToSend,
            dataType: "json",
            success: function (result, status, xhr) {
            suggestions = result["Selection"]

                var tableSuggest = $("<table><tr><th>Movie</th><th>Summary</th><th>Rating</th><th>Genres</th></tr>");

                for (movie of suggestions) {
                	tableSuggest.append("<tr><td>"+movie["movie"]+"</td>"+"<td>"+movie["summary"]+"</td>"+"<td>"+movie["rating"]+"</td>"+"<td>"+movie["genres"]+"</td>")
                }
  
                $("#movie-suggestions").html(tableSuggest);

                recommendations = result["Recommendation"]

                var tableRec = $("<table><tr><th>Movie</th><th>Summary</th><th>Rating</th><th>Genres</th></tr>");

                for (movie of recommendations) {
                	tableRec.append("<tr><td>"+movie["movie"]+"</td>"+"<td>"+movie["summary"]+"</td>"+"<td>"+movie["rating"]+"</td>"+"<td>"+movie["genres"]+"</td>")
                }
  
                $("#movie-recommendations").html(tableRec);

            },
            error: function (xhr, status, error) {
                alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
            }
        });
        
    });
    actorTags = []
    genreTags = []
});



