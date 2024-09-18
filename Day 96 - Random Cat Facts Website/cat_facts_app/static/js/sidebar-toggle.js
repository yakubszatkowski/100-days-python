const hamBurger = document.querySelector(".toggle-btn");
var windowWidth = window.innerWidth;
var MOBILEWIDTH = 768 

if (windowWidth > MOBILEWIDTH) {
  hamBurger.addEventListener("click", function () {
    document.querySelector("#sidebar").classList.toggle("expand");
  });
} else {
  hamBurger.addEventListener("click", function () {
    document.location.href="/";
  });
}


