// search flow
const searchInput: HTMLInputElement = document.querySelector(
  '#table-search-recruits',
);
const searchInputButton = document.querySelector(
  '#table-search-recruit-button',
);
if (searchInputButton && searchInput) {
  searchInputButton.addEventListener('click', () => {
    const url = new URL(window.location.href);
    url.searchParams.set('q', searchInput.value);
    window.location.href = `${url.href}`;
  });
}
