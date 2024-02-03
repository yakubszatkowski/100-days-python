let autocomplete; 

function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('autocomplete'),
        {
            types: ['geocode'],
            componentRestrictions: {country: ['PL']},
            fields: ['place_id', 'geometry', 'name']
        }
    );
    autocomplete.addListener('place_changed', getGeometry);
}

function handleSearch() {  
    var arrowDownEvent = new KeyboardEvent('keydown', {key: 'ArrowDown', keyCode: 40,});
    var enterEvent = new KeyboardEvent('keydown', {key: 'Enter', keyCode: 13,});
    
    document.getElementById('autocomplete').dispatchEvent(arrowDownEvent);
    document.getElementById('autocomplete').dispatchEvent(enterEvent);
}

function getGeometry() {
    var place = autocomplete.getPlace();
    document.getElementById('geometry').value = place.geometry.location;
    document.getElementById('cafe-form').submit();
}

