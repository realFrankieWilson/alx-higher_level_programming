/* global $ */
$(document).ready(function () {
  // Adding an event listener to the element
  $('#add_item').on('click', function () {
    // Appends a new list item to the unordered list
    $('UL.my_list').append('<li>Item</li>');
  });
});
