// Common functions for agenda boards (Puertos & Torre)

// Wait for DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Cache DOM elements
  const agendaModal = document.getElementById("agendaModal");
  const agendaModalFrame = document.getElementById("agendaModalFrame");
  const closeAgendaModalBtn = document.getElementById("closeAgendaModalBtn");
  const dateTimeLabel = document.getElementById("dateTimeNow");

  // Card triggers
  const cardTitles = document.querySelectorAll(".card h3");
  const cardHints = document.querySelectorAll(".card .card-hint");

  // --- Functions ---

  function updateDateTimeNow() {
    if (!dateTimeLabel) return;
    const now = new Date();
    const dayName = now.toLocaleDateString("es-AR", { weekday: "long" });
    const dateValue = now.toLocaleDateString("es-AR", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    });
    const timeValue = now.toLocaleTimeString("es-AR", {
      hour: "2-digit",
      minute: "2-digit",
    });
    dateTimeLabel.textContent = `${dayName} ${dateValue} - ${timeValue}`;
  }

  function refreshBoard() {
    const ids = ["cal1", "cal2", "cal3"];
    const now = Date.now();
    for (const id of ids) {
      const iframe = document.getElementById(id);
      if (!iframe || !iframe.src) continue;
      const url = new URL(iframe.src);
      url.searchParams.set("_ts", String(now));
      iframe.src = url.toString();
    }
  }

  function openAgendaModal(src) {
    if (!agendaModal || !agendaModalFrame || !src) return;
    agendaModalFrame.src = src;
    agendaModal.classList.add("open");
    agendaModal.setAttribute("aria-hidden", "false");
    document.body.classList.add("modal-open");
  }

  function closeAgendaModal() {
    if (!agendaModal || !agendaModalFrame) return;
    agendaModal.classList.remove("open");
    agendaModal.setAttribute("aria-hidden", "true");
    agendaModalFrame.src = "";
    document.body.classList.remove("modal-open");
  }

  // --- Initializers ---

  function initDateTimeUpdater() {
    updateDateTimeNow();
    setInterval(updateDateTimeNow, 1000);
  }

  function initAutoRefresh() {
    refreshBoard();
    setInterval(refreshBoard, 300000); // 5 minutos
  }

  function initAgendaModal() {
    // Close button
    if (closeAgendaModalBtn) {
      closeAgendaModalBtn.addEventListener("click", closeAgendaModal);
    }

    // Click outside (on backdrop)
    if (agendaModal) {
      agendaModal.addEventListener("click", (event) => {
        if (event.target === agendaModal) closeAgendaModal();
      });
    }

    // Escape key
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") closeAgendaModal();
    });

    // Card titles (sala names)
    cardTitles.forEach((title) => {
      title.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        const card = title.closest(".card");
        const iframe = card ? card.querySelector("iframe") : null;
        if (iframe && iframe.src) {
          openAgendaModal(iframe.src);
        }
      });
      title.style.cursor = "pointer";
      title.title = "Haz clic para ampliar";
    });

    // Card hint icons (zoom icon)
    cardHints.forEach((hint) => {
      hint.style.cursor = "pointer";
      hint.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        const card = hint.closest(".card");
        const iframe = card ? card.querySelector("iframe") : null;
        if (iframe && iframe.src) {
          openAgendaModal(iframe.src);
        }
      });
    });
  }

  // --- Run all initializers ---
  initDateTimeUpdater();
  initAutoRefresh();
  initAgendaModal();
});
