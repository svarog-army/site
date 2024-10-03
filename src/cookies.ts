import {Modal} from 'flowbite';
import type {ModalOptions, ModalInterface} from 'flowbite';

const $cookiesModal: HTMLElement = document.querySelector('#cookiesModal');
const modalOptions: ModalOptions = {
  placement: 'bottom-right',
  backdrop: 'dynamic',
  backdropClasses:
    'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40',
  closable: true,
};
const modal: ModalInterface = new Modal($cookiesModal, modalOptions);

document.addEventListener('DOMContentLoaded', function () {
  if (!checkConsentModeExists()) {
    console.log('consentMode does not exist');
    modal.show();
  }
});

const checkConsentModeExists = () => {
  if (localStorage.getItem('consentMode') === null) {
    return false;
  } else {
    return true;
  }
};
// Accept all cookies button flow
const acceptAllCookiesButton = document.querySelector(
  '#acceptAllCookiesButton',
);

acceptAllCookiesButton.addEventListener('click', () => {
  localStorage.setItem('consentMode', 'all');
  modal.hide();
});

// Decline cookies button flow
const declineCookiesButton = document.querySelector('#declineCookiesButton');

declineCookiesButton.addEventListener('click', () => {
  localStorage.setItem('consentMode', 'decline');
  modal.hide();
});

// Accert necessary cookies button flow
const acceptNecessaryCookiesButton = document.querySelector(
  '#acceptNecessaryCookiesButton',
);

acceptNecessaryCookiesButton.addEventListener('click', () => {
  localStorage.setItem('consentMode', 'necessary');
  modal.hide();
});

// Close cookies modal button flow
const closeCookiesModalButton = document.querySelector(
  '#closeCookiesModalButton',
);

closeCookiesModalButton.addEventListener('click', () => {
  localStorage.setItem('consentMode', 'decline');
  modal.hide();
});
