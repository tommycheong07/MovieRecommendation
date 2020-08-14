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

searchBtn.addEventListener('click', event => {
	alert("Button Clicked!")
})




