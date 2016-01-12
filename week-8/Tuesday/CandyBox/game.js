'use strict';

var candies = 0;
var lollipops = 0;
var candiesPerSec = 0;
var timer;
var createCandiesButton = document.querySelector('.createCandies');
var currentCandiesNumber = document.querySelector('.candies');
var buyLollipopsButton = document.querySelector('.buyLollipops');
var currentLollipopsNumber = document.querySelector('.lollipops');
var currentCandiesPerSecNumber = document.querySelector('.candiespersec')
var buyTenLollipopsButton = document.querySelector('.buyTenLollipops');

function candiesGrowing() {
  candies++;
  currentCandiesNumber.innerHTML = candies;
  theEnd();
}

createCandiesButton.addEventListener('click', function() {
  candiesGrowing();
});

buyLollipopsButton.addEventListener('click', function() {
  if (candies > 9) {
    candies -= 10;
    currentCandiesNumber.innerHTML = candies;
    lollipops++;
    currentLollipopsNumber.innerHTML = lollipops;
  }
  getSpeed();
});

buyTenLollipopsButton.addEventListener('click', function() {
  if (candies > 99) {
    candies -= 100;
    currentCandiesNumber.innerHTML = candies;
    lollipops += 10;
    currentLollipopsNumber.innerHTML = lollipops;
  }
  getSpeed();
});

function getSpeed() {
  if (lollipops > 9) {
    candiesPerSec = parseInt(lollipops / 10);
    currentCandiesPerSecNumber.innerHTML = candiesPerSec;
    candiesNumberGrowing();
  }
}

function candiesNumberGrowing() {
  clearTimeout(timer);
  timer = setInterval(function() {
  candies += candiesPerSec;
  currentCandiesNumber.innerHTML = candies;
  theEnd();
  }, 1000);
}

function theEnd() {
  if (candies === 1000) {
    alert('You win!!!!');
  }
}
