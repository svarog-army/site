/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!************************!*\
  !*** ./src/recruit.ts ***!
  \************************/
// search flow
var searchInput = document.querySelector('#table-search-recruits');
var searchInputButton = document.querySelector('#table-search-recruit-button');
if (searchInputButton && searchInput) {
    searchInputButton.addEventListener('click', function () {
        var url = new URL(window.location.href);
        url.searchParams.set('q', searchInput.value);
        window.location.href = "".concat(url.href);
    });
}

/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoianMvcmVjcnVpdC5qcyIsIm1hcHBpbmdzIjoiOzs7OztBQUFBLGNBQWM7QUFDZCxJQUFNLFdBQVcsR0FBcUIsUUFBUSxDQUFDLGFBQWEsQ0FDMUQsd0JBQXdCLENBQ3pCLENBQUM7QUFDRixJQUFNLGlCQUFpQixHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQzlDLDhCQUE4QixDQUMvQixDQUFDO0FBQ0YsSUFBSSxpQkFBaUIsSUFBSSxXQUFXLEVBQUU7SUFDcEMsaUJBQWlCLENBQUMsZ0JBQWdCLENBQUMsT0FBTyxFQUFFO1FBQzFDLElBQU0sR0FBRyxHQUFHLElBQUksR0FBRyxDQUFDLE1BQU0sQ0FBQyxRQUFRLENBQUMsSUFBSSxDQUFDLENBQUM7UUFDMUMsR0FBRyxDQUFDLFlBQVksQ0FBQyxHQUFHLENBQUMsR0FBRyxFQUFFLFdBQVcsQ0FBQyxLQUFLLENBQUMsQ0FBQztRQUM3QyxNQUFNLENBQUMsUUFBUSxDQUFDLElBQUksR0FBRyxVQUFHLEdBQUcsQ0FBQyxJQUFJLENBQUUsQ0FBQztJQUN2QyxDQUFDLENBQUMsQ0FBQztDQUNKIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vc3RhdGljLy4vc3JjL3JlY3J1aXQudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gc2VhcmNoIGZsb3dcbmNvbnN0IHNlYXJjaElucHV0OiBIVE1MSW5wdXRFbGVtZW50ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcbiAgJyN0YWJsZS1zZWFyY2gtcmVjcnVpdHMnLFxuKTtcbmNvbnN0IHNlYXJjaElucHV0QnV0dG9uID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcbiAgJyN0YWJsZS1zZWFyY2gtcmVjcnVpdC1idXR0b24nLFxuKTtcbmlmIChzZWFyY2hJbnB1dEJ1dHRvbiAmJiBzZWFyY2hJbnB1dCkge1xuICBzZWFyY2hJbnB1dEJ1dHRvbi5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsICgpID0+IHtcbiAgICBjb25zdCB1cmwgPSBuZXcgVVJMKHdpbmRvdy5sb2NhdGlvbi5ocmVmKTtcbiAgICB1cmwuc2VhcmNoUGFyYW1zLnNldCgncScsIHNlYXJjaElucHV0LnZhbHVlKTtcbiAgICB3aW5kb3cubG9jYXRpb24uaHJlZiA9IGAke3VybC5ocmVmfWA7XG4gIH0pO1xufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9