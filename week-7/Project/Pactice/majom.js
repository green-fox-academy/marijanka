'use strict';

console.log('mukodik');

var cim = document.querySelector('.majom');
console.log(cim);

cim.classList.add('piros');

var majomKep = document.querySelector('img');

majomKep.setAttribute('src', 'https://files.slack.com/files-pri/T0E3ZD06M-F0HQLS8TC/slack_for_ios_upload.jpg')

var bodyvaltozoban = document.querySelector('body');

function kepcsinalo(src) {
  var ujkep = document.createElement('img');

  ujkep.setAttribute('src', src);

  bodyvaltozoban.appendChild(ujkep);
}

for (var i = 0; i < 11; i++) {
  kepcsinalo('https://files.slack.com/files-pri/T0E3ZD06M-F0HQLS8TC/slack_for_ios_upload.jpg');
}

var kepek = ['https://slack-files.com/files-tmb/T0E3ZD06M-F0HKDD6BY-b83097e3ff/slack_for_ios_upload_1024.png',
'https://files.slack.com/files-pri/T0E3ZD06M-F0HJZ72J2/slack_for_ios_upload.jpg',
'https://files.slack.com/files-pri/T0E3ZD06M-F0HJXLPC0/slack_for_ios_upload.jpg',
'https://slack-imgs.com/?url=https%3A%2F%2F41.media.tumblr.com%2F84729c469ca431c8c80dad1cd4281205%2Ftumblr_o08zo7SJan1tx21ogo1_540.jpg',
'https://files.slack.com/files-pri/T0E3ZD06M-F0HJK1A9G/slack_for_ios_upload.jpg',
'https://files.slack.com/files-pri/T0E3ZD06M-F0HJCE9UL/slack_for_ios_upload.jpg',
'https://files.slack.com/files-pri/T0E3ZD06M-F0HJ9UVNZ/slack_for_ios_upload.jpg',
'https://slack-imgs.com/?url=http%3A%2F%2Flolworthy.com%2Fwp-content%2Fuploads%2F2015%2F12%2Fif-a-man-wore-pants-400x209.png',
'https://files.slack.com/files-pri/T0E3ZD06M-F0HHBSM2L/tough-questions-funny-if-dog-wear-pants-7.jpg',
'https://slack-imgs.com/?url=https%3A%2F%2Fgoo.gl%2F8C85vs']

for (var i = 0; i < kepek.length; i++) {
  kepcsinalo(kepek[i]);
}

//kepek.forEach(function(src)) {
//kepcsinalo(src); })

var gomb = document.querySelector('.csinal');

gomb.addEventListener('click', function() {
  alert('kattintottam!');
  kepcsinalo('https://slack-imgs.com/?url=https%3A%2F%2Fmedia.giphy.com%2Fmedia%2FvhsNmFjuN4WDS%2Fgiphy.gif');
});

window.addEventListener('scroll', function () {
  console.log('scoll');
  window.scrollY;
});


var cicagomb = document.querySelector('.cicat');
var kutyagomb = document.querySelector('.kutyat');
var valtoskep = document.querySelector('.cicakutyakep');

kutyagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'http://kutyafajtak.hu/kepek/beagle-kutya/beagle-kutya-04.jpg');
});

cicagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'http://www.mymacska.eoldal.hu/img/mid/7/cica.jpg');
});
