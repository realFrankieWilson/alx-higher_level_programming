/* global $ */
const script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
script.defer = true;
document.head.appendChild(script);

script.onload = function () {
  $(function () {
    $('header').css('color', '#FF0000');
  });
};
