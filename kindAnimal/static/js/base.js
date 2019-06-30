/* HEADER */
window.onload = function() {
  scrollFunction();
};
window.onscroll = function() {
  scrollFunction();
};

function scrollFunction() {
  if (document.documentElement.scrollTop > 70) {
    var header = document.getElementById("header");
    if (!header.classList.contains("nvb-fixed")) {
      header.classList.add("nvb-fixed");
      document.getElementsByTagName("body")[0].style.marginTop = "70px";
      header.style.display = "none";
      setTimeout(function() {
        header.style.display = "block";
      }, 40);
    }
  } else {
    var header = document.getElementById("header");
    if (header.classList.contains("nvb-fixed")) {
      header.classList.remove("nvb-fixed");
      document.getElementsByTagName("body")[0].style.marginTop = "0";
    }
  }
}

function menuToggle() {
  document.getElementById("menu").classList.toggle("show");
}

document.getElementById("toggleBtn").addEventListener("click", menuToggle);
