// script that adds a <li> element to a list when the user clicks on the tag DIV#add_item

$('#add_item').on('click', function () {
  const newItem = $('<li>Item</li>');
  $('.my_list').append(newItem);
});
