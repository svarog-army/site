import 'flowbite';
import {Observer} from 'tailwindcss-intersect';

Observer.start();
export interface HTMXEventDetail {
  xhr: XMLHttpRequest;
  target: HTMLElement;
}

updateSelectedItems();

const themeToggleDarkIcons = document.querySelectorAll(
  '#theme-toggle-dark-icon',
);
const themeToggleLightIcons = document.querySelectorAll(
  '#theme-toggle-light-icon',
);

// Change the icons inside the button based on previous settings
if (
  localStorage.getItem('color-theme') === 'dark' ||
  (!('color-theme' in localStorage) &&
    window.matchMedia('(prefers-color-scheme: dark)').matches)
) {
  themeToggleLightIcons.forEach(function (el) {
    el.classList.remove('hidden');
  });
  document.documentElement.classList.add('dark');
} else {
  themeToggleDarkIcons.forEach(function (el) {
    el.classList.remove('hidden');
  });
  document.documentElement.classList.remove('dark');
}

const themeToggleButtons = document.querySelectorAll('#theme-toggle');

themeToggleButtons.forEach(function (themeToggleBtn) {
  themeToggleBtn.addEventListener('click', function () {
    // toggle icons inside button
    themeToggleDarkIcons.forEach(function (themeToggleDarkIcon) {
      themeToggleDarkIcon.classList.toggle('hidden');
    });

    themeToggleLightIcons.forEach(function (themeToggleLightIcon) {
      themeToggleLightIcon.classList.toggle('hidden');
    });

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
      if (localStorage.getItem('color-theme') === 'light') {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      }

      // if NOT set via local storage previously
    } else {
      if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      }
    }
  });
});

const detailsElement = document.getElementById('specialties-details');
const selectedItemsContainer = document.getElementById('selected-items');

document.addEventListener('click', (event: MouseEvent) => {
  if (
    detailsElement &&
    event.target instanceof Node &&
    !detailsElement.contains(event.target)
  ) {
    detailsElement.removeAttribute('open');
  }
});

detailsElement?.addEventListener('change', updateSelectedItems);

function updateSelectedItems() {
  if (!detailsElement || !selectedItemsContainer) return;

  const checkedInputs = detailsElement.querySelectorAll<HTMLInputElement>(
    'input[type="checkbox"]:checked',
  );
  const selectedItems = Array.from(checkedInputs).map(
    input => input.nextElementSibling?.textContent || '',
  );

  selectedItemsContainer.innerHTML =
    selectedItems.length > 0
      ? selectedItems.map(item => `<p>${item}</p>`).join('')
      : '';
}

const scrollTopButton = document.getElementById('scroll-top');
const statsButton = document.getElementById('stats-button');

window.addEventListener('scroll', () => {
  if (window.scrollY > 100) {
    scrollTopButton?.classList.add('show');
    statsButton?.classList.add('show');
  } else {
    scrollTopButton?.classList.remove('show');
    statsButton?.classList.remove('show');
  }
});

scrollTopButton?.addEventListener('click', () => {
  scrollTopButton.classList.remove('show');
  window.scrollTo({top: 0, behavior: 'smooth'});
});
