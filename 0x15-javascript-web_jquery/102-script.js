/* global $ */
document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').on('click', function () {
    const urlHello = 'https://hellosalut.stefanbohacek.dev/hello/?lang=';
    const langInput = $('INPUT#language_code').val();
    $.ajax({
      method: 'GET',
      url: `${urlHello}${langInput}`,
      success: function (data) {
        $('DIV#hello').text(data.hello);
        console.log(data.hello);
      }
    });
  });
});
