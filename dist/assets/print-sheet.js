
const button = document.getElementById('print-sheet');
const art = document.getElementById('selected-art');
art.decode().then(() => {
  button.hidden = false;
  button.addEventListener('click', () => window.print());
}).catch(() => {
  const note = document.createElement('p');
  note.setAttribute('role', 'status');
  note.textContent = 'The drawing could not load. Try the original drawing link or reload this page.';
  button.parentElement.append(note);
});
