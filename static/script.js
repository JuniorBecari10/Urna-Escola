const numberInp = getId("number-inp");
const form = getId("form");

numberInp.addEventListener("keydown", (e) => {
  console.log(e);

  if ((numberInp.value.length + 1 > 2 || isNaN(e.key)) && e.key != "Backspace") {
    e.preventDefault();
  }
})

numberInp.focus();

function getId(id) {
  return document.getElementById(id);
}