'use instrict'

function textMultyply(string, number) {
  var output = '';
  for (i = 0; i < number; i++) {
    output += string;
  }
  return output;
}

function textMultyply2(string, number) {
    return number ? string + textMultyply2(string, number -1) : '';
}

console.log(textMultyply('alma', 3));
console.log(textMultyply('alma', 0));
console.log(textMultyply2('alma', 3));
