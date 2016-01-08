'use strict';

var pictures = ['http://zsavigre.uw.hu/cica.jpg',
'http://www.animalutul.ro/upload/3/article/95/11_original.jpg',
'http://users2.ml.mindenkilapja.hu/users/cicus-fan/uploads/cica-017-1.jpg',
'http://users3.ml.mindenkilapja.hu/users/felfoldigepard/uploads/cica.jpg',
'http://users2.ml.mindenkilapja.hu/users/cica-cat/uploads/cica.jpg',
'http://www.mymacska.eoldal.hu/img/mid/7/cica.jpg'
];

var leftButton = document.querySelector('.left');
var rightButton = document.querySelector('.right');
var curr_Picture = document.querySelector('.picture');
var in_thumb = document.querySelector('.thumbnail');
var index = 0;
var timer;
var fade_step = 0.05;


rightButton.addEventListener('click', function() {
  if (index < pictures.length-1) {
    index++;
  } else {
    index = 0;
  }
  currentPictureCreate(pictures[index]);
});

leftButton.addEventListener('click', function() {
  if (index > 0) {
    index--;
  } else {
    index = pictures.length-1;
  }
  currentPictureCreate(pictures[index]);
});

in_thumb.addEventListener('click', function(event) {
  if (event.target.src) {
    indexAddThumbnails(event.target);
    currentPictureCreate(pictures[index]);
  }
});

function indexAddThumbnails(something) {
  var sieblings = in_thumb.querySelectorAll('img');
  for (var i = 0; i < sieblings.length; i++) {
    if(sieblings[i] === something) {
      index = i;
    }
  }
}

function createThumbnails(src) {
  var picture = document.createElement('img');
  picture.setAttribute('src', src);
  in_thumb.appendChild(picture);
}

for (var n = 0; n < pictures.length; n++) {
  createThumbnails(pictures[n]);
}

function currentPictureCreate(curr_image) {
	timer = setInterval('fading("' + curr_image + '")', 20);
}

function fading(curr_image) {
  var new_opacity = curr_Picture.style.opacity - fade_step;
	if (new_opacity > 0) {
  	curr_Picture.style.opacity = new_opacity;
  } else {
  	clearTimeout(timer);
    curr_Picture.style.opacity = 0;
    curr_Picture.setAttribute('src', curr_image);
    timer = setInterval('darker()', 20);
  }
}

function darker() {
  var new_opacity = curr_Picture.style.opacity*1 + fade_step*1;
	if (new_opacity < 1) {
  	curr_Picture.style.opacity = new_opacity;
  } else {
		clearTimeout(timer);
	  curr_Picture.style.opacity = 1;
  }
}

currentPictureCreate(pictures[0])
