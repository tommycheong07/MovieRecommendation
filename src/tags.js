const tagContainer = document.querySelector('.tag-container');

const input = document.querySelector('.tag-container input');



function createTag(label) {
	const div = document.createElement('div');
	div.setAttribute('class', 'tag');

	const span = document.createElement('span');
	span.innerHTML = label;

	const closeBtn = document.createElement('span');
	closeBtn.setAttribute('class', 'material-icons');
	closeBtn.innerHTML = 'close';

	div.appendChild(span);
	div.appendChild(closeBtn);
	return div;
}

tagContainer.prepend(createTag('Hello'))


input.addEventListener('keyup', function(e) {
	if (e.key === 'Enter') {
		const tag = createTag(input.value);
		tagContainer.prepend(tag);
		input.value = '';
	}
})
