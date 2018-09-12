// lena calvin 082418

let person1 = {
    'first': 'calvin',
    'last': 'callast',
    'email': 'calemail',
}
let person2 = {
    'first': 'lena',
    'last': 'lenalast',
    'email': 'callemail',
}
let person3 = {
    'first': 'per3',
    'last': 'per3last',
    'email': 'per3email',
}

let people = [ person1, person2, person3]

// let stringify = function(personObject){
// }

// function stringify(personObject){
// }

// let stringify = (personObject) => { return personObject.first + " " + personObject.last}

// console.log(people.map(stringify, people));

let stringify = (personObject) => {return personObject.first + " " +personObject.last}
console.log(people.map(stringify,people))
