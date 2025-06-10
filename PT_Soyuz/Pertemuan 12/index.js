let nama = document.getElementById("nama");
let menu = document.getElementById("menu");

menu.addEventListener("change", function (e) {
  nama.innerText = `menekan: ${e.target.value}`;
});