/* global $ */
$(document).ready(function () {
  // Makes an AJAX request to the API endpoint
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (resp) {
    	// optain the character and store it in a variable
    	const titleList = resp.results.map(function (character) {
    		return character.title;
    	});
    	// The html element to use the tilels with
    	const htmlFile = $('UL#list_movies');

    	// iterate over the lists to get all the title value
    	titleList.forEach(function (title) {
      	htmlFile.append('<li>' + title + '</li>');
      });
    }
  });
});
