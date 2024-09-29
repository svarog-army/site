/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!**********************!*\
  !*** ./src/admin.ts ***!
  \**********************/
// search flow
var searchInputAdmin = document.querySelector('#table-search-admins');
var searchInputAdminButton = document.querySelector('#table-search-admin-button');
if (searchInputButton && searchInputAdmin) {
    searchInputButton.addEventListener('click', function () {
        var url = new URL(window.location.href);
        url.searchParams.set('q', searchInputAdmin.value);
        window.location.href = "".concat(url.href);
    });
}

/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoianMvYWRtaW4uanMiLCJtYXBwaW5ncyI6Ijs7Ozs7QUFBQSxjQUFjO0FBQ2QsSUFBTSxnQkFBZ0IsR0FBcUIsUUFBUSxDQUFDLGFBQWEsQ0FDL0Qsc0JBQXNCLENBQ3ZCLENBQUM7QUFDRixJQUFNLHNCQUFzQixHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQ25ELDRCQUE0QixDQUM3QixDQUFDO0FBQ0YsSUFBSSxpQkFBaUIsSUFBSSxnQkFBZ0IsRUFBRTtJQUN6QyxpQkFBaUIsQ0FBQyxnQkFBZ0IsQ0FBQyxPQUFPLEVBQUU7UUFDMUMsSUFBTSxHQUFHLEdBQUcsSUFBSSxHQUFHLENBQUMsTUFBTSxDQUFDLFFBQVEsQ0FBQyxJQUFJLENBQUMsQ0FBQztRQUMxQyxHQUFHLENBQUMsWUFBWSxDQUFDLEdBQUcsQ0FBQyxHQUFHLEVBQUUsZ0JBQWdCLENBQUMsS0FBSyxDQUFDLENBQUM7UUFDbEQsTUFBTSxDQUFDLFFBQVEsQ0FBQyxJQUFJLEdBQUcsVUFBRyxHQUFHLENBQUMsSUFBSSxDQUFFLENBQUM7SUFDdkMsQ0FBQyxDQUFDLENBQUM7Q0FDSiIsInNvdXJjZXMiOlsid2VicGFjazovL3N0YXRpYy8uL3NyYy9hZG1pbi50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBzZWFyY2ggZmxvd1xuY29uc3Qgc2VhcmNoSW5wdXRBZG1pbjogSFRNTElucHV0RWxlbWVudCA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXG4gICcjdGFibGUtc2VhcmNoLWFkbWlucycsXG4pO1xuY29uc3Qgc2VhcmNoSW5wdXRBZG1pbkJ1dHRvbiA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXG4gICcjdGFibGUtc2VhcmNoLWFkbWluLWJ1dHRvbicsXG4pO1xuaWYgKHNlYXJjaElucHV0QnV0dG9uICYmIHNlYXJjaElucHV0QWRtaW4pIHtcbiAgc2VhcmNoSW5wdXRCdXR0b24uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG4gICAgY29uc3QgdXJsID0gbmV3IFVSTCh3aW5kb3cubG9jYXRpb24uaHJlZik7XG4gICAgdXJsLnNlYXJjaFBhcmFtcy5zZXQoJ3EnLCBzZWFyY2hJbnB1dEFkbWluLnZhbHVlKTtcbiAgICB3aW5kb3cubG9jYXRpb24uaHJlZiA9IGAke3VybC5ocmVmfWA7XG4gIH0pO1xufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9