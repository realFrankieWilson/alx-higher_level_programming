/* global $ */
// Load jquery dynamically
const script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
script.onload = function () {
  // Adding an event listener to the element
  $(document).on('click', 'div#red_header', function () {
    $(this).css('color', 'red');
  });
};
document.head.appendChild(script);
