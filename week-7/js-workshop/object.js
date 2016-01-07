'use strict'

var humwee = {
  type: 'Rendes katonai Hummer',
  color: 'Terep',
  km: 20000
};

function oldride(car, km) {
  car.km += km;
}

oldride(humwee, 200);
console.log(humwee.km);


var humweee = {
  type: 'Rendes katonai Hummer',
  color: 'Terep',
  km: 20000,
  ride: function(km) {
    this.km += km;
  }
};


humweee.ride(200)

console.log(humwee.km);
