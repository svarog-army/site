/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!**********************!*\
  !*** ./src/stats.ts ***!
  \**********************/
// set statistic period input date fields
var beginStatPeriodInput = document.querySelector('#begin-stats-period');
var endStatPeriodInput = document.querySelector('#end-stats-period');
if (beginStatPeriodInput && endStatPeriodInput) {
    var update = function () {
        var url = new URL(window.location.href);
        url.searchParams.set('start', beginStatPeriodInput.value);
        url.searchParams.set('end', endStatPeriodInput.value);
        window.location.href = "".concat(url.href);
    };
    beginStatPeriodInput.addEventListener('change', update);
    endStatPeriodInput.addEventListener('change', update);
}

/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoianMvc3RhdHMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7QUFBQSx5Q0FBeUM7QUFDekMsSUFBTSxvQkFBb0IsR0FBcUIsUUFBUSxDQUFDLGFBQWEsQ0FDbkUscUJBQXFCLENBQ0YsQ0FBQztBQUV0QixJQUFNLGtCQUFrQixHQUFxQixRQUFRLENBQUMsYUFBYSxDQUNqRSxtQkFBbUIsQ0FDQSxDQUFDO0FBRXRCLElBQUksb0JBQW9CLElBQUksa0JBQWtCLEVBQUU7SUFDOUMsSUFBTSxNQUFNLEdBQUc7UUFDYixJQUFNLEdBQUcsR0FBRyxJQUFJLEdBQUcsQ0FBQyxNQUFNLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQyxDQUFDO1FBQzFDLEdBQUcsQ0FBQyxZQUFZLENBQUMsR0FBRyxDQUFDLE9BQU8sRUFBRSxvQkFBb0IsQ0FBQyxLQUFLLENBQUMsQ0FBQztRQUMxRCxHQUFHLENBQUMsWUFBWSxDQUFDLEdBQUcsQ0FBQyxLQUFLLEVBQUUsa0JBQWtCLENBQUMsS0FBSyxDQUFDLENBQUM7UUFDdEQsTUFBTSxDQUFDLFFBQVEsQ0FBQyxJQUFJLEdBQUcsVUFBRyxHQUFHLENBQUMsSUFBSSxDQUFFLENBQUM7SUFDdkMsQ0FBQyxDQUFDO0lBQ0Ysb0JBQW9CLENBQUMsZ0JBQWdCLENBQUMsUUFBUSxFQUFFLE1BQU0sQ0FBQyxDQUFDO0lBQ3hELGtCQUFrQixDQUFDLGdCQUFnQixDQUFDLFFBQVEsRUFBRSxNQUFNLENBQUMsQ0FBQztDQUN2RCIsInNvdXJjZXMiOlsid2VicGFjazovL3N0YXRpYy8uL3NyYy9zdGF0cy50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBzZXQgc3RhdGlzdGljIHBlcmlvZCBpbnB1dCBkYXRlIGZpZWxkc1xuY29uc3QgYmVnaW5TdGF0UGVyaW9kSW5wdXQ6IEhUTUxJbnB1dEVsZW1lbnQgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFxuICAnI2JlZ2luLXN0YXRzLXBlcmlvZCcsXG4pIGFzIEhUTUxJbnB1dEVsZW1lbnQ7XG5cbmNvbnN0IGVuZFN0YXRQZXJpb2RJbnB1dDogSFRNTElucHV0RWxlbWVudCA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXG4gICcjZW5kLXN0YXRzLXBlcmlvZCcsXG4pIGFzIEhUTUxJbnB1dEVsZW1lbnQ7XG5cbmlmIChiZWdpblN0YXRQZXJpb2RJbnB1dCAmJiBlbmRTdGF0UGVyaW9kSW5wdXQpIHtcbiAgY29uc3QgdXBkYXRlID0gKCkgPT4ge1xuICAgIGNvbnN0IHVybCA9IG5ldyBVUkwod2luZG93LmxvY2F0aW9uLmhyZWYpO1xuICAgIHVybC5zZWFyY2hQYXJhbXMuc2V0KCdzdGFydCcsIGJlZ2luU3RhdFBlcmlvZElucHV0LnZhbHVlKTtcbiAgICB1cmwuc2VhcmNoUGFyYW1zLnNldCgnZW5kJywgZW5kU3RhdFBlcmlvZElucHV0LnZhbHVlKTtcbiAgICB3aW5kb3cubG9jYXRpb24uaHJlZiA9IGAke3VybC5ocmVmfWA7XG4gIH07XG4gIGJlZ2luU3RhdFBlcmlvZElucHV0LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIHVwZGF0ZSk7XG4gIGVuZFN0YXRQZXJpb2RJbnB1dC5hZGRFdmVudExpc3RlbmVyKCdjaGFuZ2UnLCB1cGRhdGUpO1xufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9