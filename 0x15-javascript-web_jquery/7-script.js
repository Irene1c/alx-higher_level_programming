// script that fetches the character name from URL

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  const charName = data.name;
  $('#character').text(charName);
}).fail(function (error) {
  console.error(error);
});
