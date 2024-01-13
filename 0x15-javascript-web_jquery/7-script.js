/* global $ */
$(document).ready(function () {
  // Makes an AJAX request to the API endpoint
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function (resp) {
      // Update the header with the character's name
      const nameChar = $('header').text(resp.name);

      // HTML string to be used on
      const respInfo = '<p>Name: ' + nameChar + '</p>';

      // Input the value to the HTML file
      $('div.character').html(respInfo);
    }
  });
});
