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

    autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged() {
    var place = autocomplete.getPlace();
    document.getElementById('geometry').value = place.geometry.location
    document.getElementById('cafe-form').submit();
}

// TODO: if hitting search button with manual text select first 