/* global $ */
$(document).ready(function () {
  // Adding an event listener to the element
  $('DIV#update_header').on('click', function () {
    // Appends a new list item to the unordered list
    $('header').html('New Header!!!');
  });
});
