const breedInputElement = document.querySelector('#search-breed-input');
const breedSuggestions = document.querySelector('#breed-list');
const submitbutton = document.querySelector('.cats-button');
let fetchedBreedList = []
let keys = []

async function loadBreeds() {
	const response = await fetch('/static/json/breeds.json');
	const data = await response.json();
	keys = Object.values(data);
	fetchedBreedList = Object.keys(data);
};

function search(str) {
	let results = [];
	const val = str.toLowerCase();

	for (let i = 0; i < fetchedBreedList.length; i++) {
		if (fetchedBreedList[i].toLowerCase().indexOf(val) > -1) {
			results.push(fetchedBreedList[i]);
		};
	};
	return results;
};

function searchHandler(e) {
	const inputVal = e.currentTarget.value;
	let results = [];
	if (inputVal.length > 0) {
		results = search(inputVal);
	};
	showSuggestions(results, inputVal);
};

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
	};
};


function handleSearch() {  
	if (breedInputElement && breedInputElement.value.length > 0) {
		const firstSuggestion = breedSuggestions.querySelector('.form-wrapper ul li:first-child');
		breedInputElement.value = firstSuggestion.innerText.trim();
		breedInputElement.focus();
		breedSuggestions.innerHTML = '';
		document.querySelector('.form-wrapper').submit();  
	} else {
		location.reload();
	}
};

function useSuggestion(e) {  // add invisible input that will send the code
	breedInputElement.value = e.target.innerText;
	console.log(e.target.innerText)
	breedInputElement.focus();
	breedSuggestions.innerHTML = '';
	// document.querySelector('.form-wrapper').submit();
};

if (breedInputElement && breedSuggestions) {
	if (breedInputElement) {
		loadBreeds();
	}
	breedInputElement.addEventListener('keyup', searchHandler);
	breedSuggestions.addEventListener('click', useSuggestion);
	breedInputElement.addEventListener('keydown', function(e) {
		if (e.key === 'Enter') {
			e.preventDefault();
			handleSearch();
		}
	});
}

if (submitbutton) {
	submitbutton.addEventListener('click', handleSearch);
}
