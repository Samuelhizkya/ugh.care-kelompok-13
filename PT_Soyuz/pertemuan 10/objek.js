let spaceship = {
    homeplanet: 'earth',
    color: 'silver',
    terbang() {
        console.log('wusssssssss!');

},
crew: {
  captain:{
    nama: "amel",
    age: 20,
    job: "pilot",
  },
  pramugari: {
    nama: "isa",
    age: 18,
    job: "pilot",
  },
}
};

console.log(spaceship.crew.pramugari.nama);

for (let crewMember in spaceship.crew) {
        console.log('${crewMember}: ${spaceship.crew[crewMember].nama} ${spaceship.crew[crewMember].job}');
}
// console.log(spaceship.homeplanet);
// console.log(spaceship['fuel type']);

// const {homeplanet, color} = spaceship;
// console.log(homeplanet, color);

