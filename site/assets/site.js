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
