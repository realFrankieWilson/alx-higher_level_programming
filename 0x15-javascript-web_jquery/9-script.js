/* global $ */

// Creates a new script that allows script to run when imported
// on the head tag
const script = document.createElement('script');
// Set the source script.
script.src = '9-script.js';
script.defer = true;
// Append script to the head of the document
document.head.appendChild(script);

$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (resp) {
      console.log(resp.hello);

      $('DIV#hello').html(resp.hello);
    }
  });
});
