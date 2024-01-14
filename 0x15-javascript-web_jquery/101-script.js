/* global $ */

// Check for document parsing.
if (document.readyState == 'loading') {
  // Wait for the DOMContentLoaded event to ensure the script is imported
  // to the <head> tag
  document.addEventListener('DOMContentLoaded', function () {
    modifyFunction();
  });
} else {
  // Check if the document has already finished parsing, if so, the
  // function should be called immediately
  modifyFunction();
}

// Logic Defination
function modifyFunction () {
  $(document).ready(function () {
    $('div').on('click', function () {
      switch (this.id) {
        case 'add_item':
          $('<li>Item</li>').appendTo('ul.my_list');
          break;
        case 'remove_item':
          $('ul.my_list li').last().remove();
          break;
        case 'clear_list':
          $('ul.my_list').empty();
          break;
        default:
          break;
      }
    });
  });
}
