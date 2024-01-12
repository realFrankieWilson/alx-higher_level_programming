/* global $ */
// Load jquery dynamically
const script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
script.onload = function () {
  // Adding an event listener to the element
  $('div#toggle_header').on('click', function () {
    // Toggles between classes
    $('header').toggleClass('green red');
  });
};
document.head.appendChild(script);
