// search flow
const searchInputAdmin: HTMLInputElement = document.querySelector(
  '#table-search-admins',
);
const searchInputAdminButton = document.querySelector(
  '#table-search-admin-button',
);
if (searchInputButton && searchInputAdmin) {
  searchInputButton.addEventListener('click', () => {
    const url = new URL(window.location.href);
    url.searchParams.set('q', searchInputAdmin.value);
    window.location.href = `${url.href}`;
  });
}
