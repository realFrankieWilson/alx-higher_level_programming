/* global $ */
document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });

  function translate () {
    const urlHello = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: `${urlHello}${lang}`,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }
});
