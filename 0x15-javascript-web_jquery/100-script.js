// script that updates the text color of the <header> element to red (#FF0000)
// You must use document.querySelector to select the HTML tag
// Note: Your script must be imported from the <head> tag, not at the end of the HTML

document.addEventListener('DOMContentLoaded', () => {
  const element = document.querySelector('header');
  element.style.color = '#FF0000';
});
