/*
 script that fetches and displays the value of hello from that fetch in the HTML tag DIV#hello
 Your script must work when it is imported from the <head> tag
*/

$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    const charHello = data.hello;
    $('#hello').text(charHello);
  }).fail(function (error) {
    console.error(error);
  });
});
