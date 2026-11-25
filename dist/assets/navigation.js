
const toggle = document.querySelector('.menu-toggle');
const menu = document.getElementById('site-links');
function setMenu(open) {
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  menu.classList.toggle('open', open);
}
toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') === 'false'));
menu.addEventListener('click', event => {
  if (event.target.closest('a')) setMenu(false);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    toggle.focus();
  }
});

const mobileLayout = window.matchMedia(document.body.dataset.menuBreakpoint || '(max-width: 640px)');
mobileLayout.addEventListener('change', () => setMenu(false));
