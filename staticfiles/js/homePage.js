console.log("hello");

var doc1 = document.getElementById("diamond1");

var doc2 = document.getElementById("diamond2");
var doc3 = document.getElementById("diamond3");

var doc4 = document.getElementById("dima1");
var doc5 = document.getElementById("dima2");
var doc6 = document.getElementById("dima3");

var doc7 = document.getElementById("mobilediv");

function myFunction(x) {
  if (x.matches) {
    // If media query matches
    doc4.onclick = function () {
      doc7.innerHTML = doc1.innerHTML;
      doc4.style.backgroundColor = "purple";
      doc5.style.backgroundColor = "#0266d9";
      doc6.style.backgroundColor = "#0266d9";
    };
    doc5.onclick = function () {
      doc7.innerHTML = doc2.innerHTML;
      doc5.style.backgroundColor = "purple";
      doc4.style.backgroundColor = "#0266d9";
      doc6.style.backgroundColor = "#0266d9";
    };
    doc6.onclick = function () {
      doc7.innerHTML = doc3.innerHTML;
      doc6.style.backgroundColor = "purple";
      doc5.style.backgroundColor = "#0266d9";
      doc4.style.backgroundColor = "#0266d9";
    };

    setInterval(function () {
      if (doc7.innerHTML == doc1.innerHTML) {
        doc7.innerHTML = doc2.innerHTML;
        doc5.style.backgroundColor = "purple";
        doc4.style.backgroundColor = "#0266d9";
        doc6.style.backgroundColor = "#0266d9";
      } else if (doc7.innerHTML == doc2.innerHTML) {
        doc7.innerHTML = doc3.innerHTML;
        doc6.style.backgroundColor = "purple";
        doc5.style.backgroundColor = "#0266d9";
        doc4.style.backgroundColor = "#0266d9";
      } else {
        doc7.innerHTML = doc1.innerHTML;
        doc4.style.backgroundColor = "purple";
        doc5.style.backgroundColor = "#0266d9";
        doc6.style.backgroundColor = "#0266d9";
      }
    }, 5000);
  }
}

var x = window.matchMedia("(max-width: 700px)");
myFunction(x); // Call listener function at run time
x.addListener(myFunction); // Attach listener function on state changes

document.getElementById("aboutid").addEventListener("click", function (e) {
  e.preventDefault();
  document.getElementById("about-us-section").scrollIntoView(true, {
    behavior: "smooth",
    block: "start",
    inline: "nearest",
  });
});
document.getElementById("howit").addEventListener("click", function (e) {
  e.preventDefault();
  document.getElementById("how-it-work-section").scrollIntoView(true, {
    behavior: "smooth",
    block: "start",
    inline: "nearest",
  });
});
document.getElementById("contactid").addEventListener("click", function (e) {
  e.preventDefault();
  document.getElementById("contact-us-section").scrollIntoView(true, {
    behavior: "smooth",
    block: "start",
    inline: "nearest",
  });
});

const openmodalbuttons = document.querySelectorAll("[data-modal-target]");
const closemodalbuttons = document.querySelectorAll("[data-close-button]");
const overlay = document.getElementById("overlay");
console.log(overlay);

openmodalbuttons.forEach((button) => {
  button.addEventListener("click", () => {
    const modal = button.closest(".modal");
    closeModal(modal);
  });
});

closemodalbuttons.forEach((button) => {
  button.addEventListener("click", () => {
    const modal = document.querySelector(button.dataset.modalTarget);
    openModal(modal);
  });
});

function openModal(modal) {
  if (modal == NULL) return;
  modal.classList.add("active");
  overlay.classList.add("active");
}

function closeModal(modal) {
  if (modal == NULL) return;
  modal.classList.add("active");
  overlay.classList.add("active");
}