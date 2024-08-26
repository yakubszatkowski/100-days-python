const breedInputElement = document.querySelector('#search-breed-input');
const breedSuggestions = document.querySelector('#breed-list');
const fetchedBreedList = ['apple', 'ananas'] //fetch('/static/json/breeds.json');
const submitbutton = document.querySelector('.cats-button')

function search(str) {
    let results = [];
    const val = str.toLowerCase();

	for (let i = 0; i < fetchedBreedList.length; i++) {
		if (fetchedBreedList[i].toLowerCase().indexOf(val) > -1) {
			results.push(fetchedBreedList[i]);
		}
	}
	return results;
};


function searchHandler(e) {
	const inputVal = e.currentTarget.value;
	let results = [];
	if (inputVal.length > 0) {
		results = search(inputVal);
	}
	showSuggestions(results, inputVal);
}


function showSuggestions(results, inputVal) {
    breedSuggestions.innerHTML = '';

	if (results.length > 0) {
		for (let i = 0; i < results.length; i++) {
			let item = results[i];
			const match = item.match(new RegExp(inputVal, 'i'));
			item = item.replace(match[0], `<strong>${match[0]}</strong>`);
			breedSuggestions.innerHTML += `<li>${item}</li>`;
		}
	} else {
		results = [];
		breedSuggestions.innerHTML = '';
	}
}


function useSuggestion(e) {
	breedInputElement.value = e.target.innerText;
	breedInputElement.focus();
	breedSuggestions.innerHTML = '';
	document.querySelector('.form-wrapper').submit();
}


breedInputElement.addEventListener('keyup', searchHandler);
breedSuggestions.addEventListener('click', useSuggestion);
