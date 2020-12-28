const buttonRight = document.getElementById('scroll-right');
const buttonLeft = document.getElementById('scroll-left');

buttonRight.onclick = function () {
  document.getElementById('carousel').scrollLeft += 900;
};
buttonLeft.onclick = function () {
  document.getElementById('carousel').scrollLeft -= 900;
};
