/* global $ */
// Load jquery dynamically
const script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
script.onload = function () {
  // Adding an event listener to the element
  $('div#red_header').on('click', function () {
    $(this).addClass('red');
  });
};
document.head.appendChild(script);
