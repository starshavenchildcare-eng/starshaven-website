const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector("#site-nav");

if (toggle && nav) {
  document.documentElement.classList.add("has-js");
  toggle.hidden = false;

  const closeMenu = () => {
    toggle.setAttribute("aria-expanded", "false");
    nav.classList.remove("is-open");
  };

  toggle.addEventListener("click", () => {
    const isOpen = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!isOpen));
    nav.classList.toggle("is-open", !isOpen);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
      closeMenu();
      toggle.focus();
    }
  });

  nav.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });

  document.addEventListener("click", (event) => {
    if (!nav.contains(event.target) && !toggle.contains(event.target)) closeMenu();
  });

  window.matchMedia("(min-width: 901px)").addEventListener("change", (event) => {
    if (event.matches) closeMenu();
  });
}

const enrolmentForm = document.querySelector('form[name="pre-enrolment"]');

if (enrolmentForm) {
  const preferredDays = [...enrolmentForm.querySelectorAll('input[name="preferred-days"]')];
  const validatePreferredDays = () => {
    const message = preferredDays.some((day) => day.checked) ? "" : "Please select at least one preferred day.";
    preferredDays[0]?.setCustomValidity(message);
  };

  preferredDays.forEach((day) => day.addEventListener("change", validatePreferredDays));
  enrolmentForm.addEventListener("submit", validatePreferredDays);
}

document.querySelectorAll(".share-resource").forEach((button) => {
  button.addEventListener("click", async () => {
    const url = button.dataset.shareUrl;
    const title = button.dataset.shareTitle || document.title;
    const feedback = button.closest(".publication-copy")?.querySelector(".share-feedback");
    try {
      if (navigator.share) {
        await navigator.share({ title, url });
        if (feedback) feedback.textContent = "Share options opened.";
      } else if (navigator.clipboard) {
        await navigator.clipboard.writeText(url);
        if (feedback) feedback.textContent = "Link copied. You can now paste it into a message or email.";
      } else {
        window.prompt("Copy this resource link:", url);
      }
    } catch (error) {
      if (error?.name !== "AbortError" && feedback) feedback.textContent = "Use the Read issue link, then share the PDF from your browser.";
    }
  });
});
