document
  .getElementById("recommendationForm")
  .addEventListener("submit", function (event) {
    var submitButton = document.getElementById("submitButton");
    submitButton.innerHTML =
      '<span class="flex item-center gap-2"><span class="animate-spin"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-loader-circle"><path d="M21 12a9 9 0 1 1-6.219-8.56"/></svg></span><span>Loading...</span></span>';
    submitButton.disabled = true;
  });
