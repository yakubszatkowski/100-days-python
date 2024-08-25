let breeds = [];
let fetchedBreedList = fetch('/static/json/breeds.json')
const breedListElement = document.querySelector('#breed-list');
const breedInputElement = document.querySelector('#search-breed-input');


function fetchBreeds() {
    fetchedBreedList
        .then((response) => response.json())
        .then((data) => {
            breeds = Object.values(data);
            breeds.sort()
            loadData(breeds, breedListElement)
        });
};

function loadData(data, element) {
    if (data) {
        element.innerHTML = "";
        let innerElement = "";
        data.forEach((item) => {
            innerElement += `<li>${item}</li>`;
        });

        element.innerHTML = innerElement
    };
};

function filterData(data, searchText) {
    return data.filter((x) => x.toLowerCase().includes(searchText.toLowerCase()));
};

fetchBreeds();

breedInputElement.addEventListener('input', function() {
    const filteredData = filterData(breeds, breedInputElement.value);
    loadData(filteredData, breedListElement)
})

