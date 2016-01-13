'use strict';

function Game() {
  var _this = this;
  this.candies = 0;
  this.lollipops = 0;
  this.candiesPerSec = 0;
  this.timer;
  this.currentCandiesNumber = document.querySelector('.candies');
  this.currentLollipopsNumber = document.querySelector('.lollipops');
  this.currentCandiesPerSecNumber = document.querySelector('.candiespersec');

  this.candiesGrowing = function() {
    this.candies++;
    this.currentCandiesNumber.innerHTML = this.candies;
    this.theEnd();
  }

  this.init = function() {
    document.querySelector('.createCandies').addEventListener('click', function() {
      _this.candiesGrowing();
    });

    document.querySelector('.buyLollipops').addEventListener('click', function() {
      if (_this.candies > 9) {
        _this.candies -= 10;
        _this.currentCandiesNumber.innerHTML = _this.candies;
        _this.lollipops++;
        _this.currentLollipopsNumber.innerHTML = _this.lollipops;
      }
      _this.getSpeed();
    });

    document.querySelector('.buyTenLollipops').addEventListener('click', function() {
      if (_this.candies > 99) {
        _this.candies -= 100;
        _this.currentCandiesNumber.innerHTML = _this.candies;
        _this.lollipops += 10;
        _this.currentLollipopsNumber.innerHTML = _this.lollipops;
      }
      _this.getSpeed();
    });
  }

  this.getSpeed = function() {
    if (this.lollipops > 9) {
      this.candiesPerSec = parseInt(this.lollipops / 10);
      this.currentCandiesPerSecNumber.innerHTML = this.candiesPerSec;
      this.candiesNumberGrowing();
    }
  }

  this.candiesNumberGrowing = function() {
    clearTimeout(this.timer);
    this.timer = setInterval(function() {
      _this.candies += _this.candiesPerSec;
      _this.currentCandiesNumber.innerHTML = _this.candies;
      _this.theEnd();
    }, 1000);
  }

  this.theEnd = function() {
    if (this.candies === 1000) {
      alert('You win!!!!');
    }
  }
}

var game = new Game;
game.init();
