
const choices = [...document.querySelectorAll('.color-choice')];
const image = document.getElementById('selected-art');
const printButton = document.getElementById('print-button');
const download = document.getElementById('download-sheet');
const status = document.getElementById('sheet-status');
let revision = 0;

async function selectSheet(choice, push = false) {
  const version = ++revision;
  const {id, title, description, alt, file} = choice.dataset;
  for (const item of choices) item.setAttribute('aria-pressed', String(item === choice));
  printButton.disabled = true;
  printButton.hidden = false;
  document.body.classList.add('sheet-pending');
  document.getElementById('selected-title').textContent = title;
  document.getElementById('selected-description').textContent = description;
  status.textContent = 'Preparing ' + title + '…';
  const src = '../assets/free-coloring/' + file;
  image.alt = alt;
  if (image.getAttribute('src') !== src || !image.naturalWidth) image.src = src;
  download.href = src;
  download.download = file;
  if (push) {
    const url = new URL(location.href);
    url.searchParams.set('sheet', id);
    url.hash = 'color';
    if (url.href !== location.href) history.pushState(null, '', url);
  }
  try {
    await image.decode();
    if (version !== revision) return;
    document.body.classList.remove('sheet-pending');
    printButton.disabled = false;
    status.textContent = title + ' is ready to print.';
  } catch {
    if (version === revision) status.textContent = 'Drawing unavailable. Choose it again to retry or download the original.';
  }
}

function restoreSheet() {
  const id = new URLSearchParams(location.search).get('sheet');
  selectSheet(choices.find(choice => choice.dataset.id === id) || choices[0]);
}
for (const choice of choices) {
  // The anchor's static page remains available to assistive tools and in a new tab.
  choice.setAttribute('role', 'button');
  choice.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.altKey || event.shiftKey) return;
    event.preventDefault();
    selectSheet(choice, true);
  });
  choice.addEventListener('keydown', event => {
    if (event.key === ' ') {
      event.preventDefault();
      choice.click();
    }
  });
}
window.addEventListener('popstate', restoreSheet);
printButton.addEventListener('click', () => { if (!printButton.disabled) window.print(); });
restoreSheet();
