// Native navigation and article reading work without JavaScript.
document.querySelectorAll('.page__content table:not(.highway-exhibit)').forEach((table, index) => {
  const region = document.createElement('div');
  region.className = 'table-scroll'; region.tabIndex = 0;
  region.setAttribute('role', 'region');
  region.setAttribute('aria-label', `Article table ${index + 1}; scroll horizontally if needed`);
  table.before(region); region.append(table);
  if (region.scrollWidth > region.clientWidth) {
    const hint = document.createElement('p'); hint.className = 'scroll-hint';
    hint.textContent = 'Scroll horizontally to read the whole table.'; region.after(hint);
  }
});
document.querySelectorAll('.page__content pre').forEach(pre => {
  pre.tabIndex = 0; pre.setAttribute('aria-label', 'Code sample; scroll horizontally if needed');
});
document.addEventListener('keydown', event => {
  if (event.key !== 'Escape') return;
  const menu = document.querySelector('.mobile-nav[open]');
  if (menu) { menu.open = false; menu.querySelector('summary').focus(); }
});
