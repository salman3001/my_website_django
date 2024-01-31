export const checkLoaderFirst = () =>
  document.addEventListener("DOMContentLoaded", function () {
    const lodaer = document.getElementById("loader");
    if (lodaer) {
      lodaer.style.display = "none";
    }
  });
