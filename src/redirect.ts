// redirect flow
const redirectTag: HTMLDivElement = document.querySelector('#redirect-url');
if (redirectTag) {
  const redirectUrl = redirectTag.dataset.url;
  if (redirectUrl) {
    window.location.href = redirectUrl;
  }
}
