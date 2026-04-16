function hideLoadingScreen() {
  const loadingScreen = document.getElementById("loadingScreen");
  if (!loadingScreen) return;
  loadingScreen.classList.add("hidden");
  setTimeout(() => loadingScreen.remove(), 500);
}

function initLoadingScreen() {
  // Determinar tiempo de carga según la sede
  const body = document.body;
  let loadingDuration = 4000; // valor por defecto

  if (body.classList.contains("sede-nordelta")) {
    loadingDuration = 3500; // Nordelta: 3.5 segundos
  }

  window.addEventListener("load", hideLoadingScreen);
  setTimeout(hideLoadingScreen, loadingDuration);
}

// Initialize on load
initLoadingScreen();
