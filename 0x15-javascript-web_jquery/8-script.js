// script that fetches and lists the title for all movies

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const films = data.results;
  films.forEach(function (movie) {
    const li = $('<li>').text(movie.title);
    $('#list_movies').append(li);
  });
}).fail(function (error) {
  console.error(error);
});
