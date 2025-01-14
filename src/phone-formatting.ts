document.addEventListener('DOMContentLoaded', () => {
  const phoneInput = document.getElementById(
    'phone',
  ) as HTMLInputElement | null;

  if (!phoneInput) return;

  phoneInput.value = '+380 ';

  phoneInput.addEventListener('input', (event: Event) => {
    const input = event.target as HTMLInputElement;

    const cursorPosition = input.selectionStart || 0;

    let rawValue = input.value.replace(/[^\d]/g, '');

    if (!rawValue.startsWith('380')) {
      rawValue = '380' + rawValue.replace(/^380/, '');
    }

    const numbersOnly = rawValue.slice(3);

    let formattedValue = '+380 ';

    if (numbersOnly.length > 0) {
      formattedValue += `(${numbersOnly.slice(0, 2)}`;
    }

    if (numbersOnly.length > 2) {
      formattedValue += `) ${numbersOnly.slice(2, 5)}`;
    }

    if (numbersOnly.length > 5) {
      formattedValue += `-${numbersOnly.slice(5, 7)}`;
    }

    if (numbersOnly.length > 7) {
      formattedValue += `-${numbersOnly.slice(7, 9)}`;
    }

    const diff = formattedValue.length - input.value.length;
    const newCursorPosition = cursorPosition + diff;

    input.value = formattedValue;

    const adjustedCursorPosition = Math.max(newCursorPosition, 5);

    input.setSelectionRange(adjustedCursorPosition, adjustedCursorPosition);
  });

  phoneInput.addEventListener('keydown', (event: KeyboardEvent) => {
    const input = event.target as HTMLInputElement;

    if (
      event.key === 'Backspace' &&
      input.selectionStart &&
      input.selectionStart <= 5
    ) {
      event.preventDefault();
    }
  });

  phoneInput.addEventListener('focus', () => {
    if (!phoneInput.value.startsWith('+380')) {
      phoneInput.value = '+380 ';
    }

    phoneInput.setSelectionRange(5, 5);
  });

  phoneInput.addEventListener('click', () => {
    if (phoneInput.selectionStart && phoneInput.selectionStart < 5) {
      phoneInput.setSelectionRange(5, 5);
    }
  });
});
