const numberInp = getId("number-inp");
const form = getId("form");
const votar = getId("votar");

numberInp.addEventListener("keydown", (e) => {
  if ((numberInp.value.length + 1 > 2 || isNaN(e.key)) && e.key != "Backspace") {
    e.preventDefault();
  }

  if (e.key == "Enter") {
    votar.click();
  }
})

function getId(id) {
  return document.getElementById(id);
}