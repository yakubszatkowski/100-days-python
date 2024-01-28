let autocomplete
function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('autocomplete'),
        {
            componentRestrictions: {country: ['PL']},
            fields: ['place_id', 'geometry', 'name']
        }
    );
}
