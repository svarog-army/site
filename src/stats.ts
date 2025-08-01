// set statistic period input date fields
const beginStatPeriodInput: HTMLInputElement = document.querySelector(
  '#begin-stats-period',
) as HTMLInputElement;

const endStatPeriodInput: HTMLInputElement = document.querySelector(
  '#end-stats-period',
) as HTMLInputElement;

if (beginStatPeriodInput && endStatPeriodInput) {
  const update = () => {
    const url = new URL(window.location.href);
    url.searchParams.set('start', beginStatPeriodInput.value);
    url.searchParams.set('end', endStatPeriodInput.value);
    window.location.href = `${url.href}`;
  };
  beginStatPeriodInput.addEventListener('change', update);
  endStatPeriodInput.addEventListener('change', update);
}
