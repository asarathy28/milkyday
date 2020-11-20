const buttonRight = document.getElementById('scroll-right');
const buttonLeft = document.getElementById('scroll-left');

buttonRight.onmousedown = function () {
  document.getElementById('carousel').scrollLeft += 200;
};
buttonLeft.onmousedown = function () {
  document.getElementById('carousel').scrollLeft -= 200;
};
