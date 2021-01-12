const buttonRight = document.getElementById('scroll-right');
const buttonLeft = document.getElementById('scroll-left');
var clientWidth = document.getElementById('carousel').clientWidth;

buttonRight.onclick = function () {
  document.getElementById('carousel').scrollLeft += clientWidth;
};
buttonLeft.onclick = function () {
  document.getElementById('carousel').scrollLeft -= clientWidth;
};
