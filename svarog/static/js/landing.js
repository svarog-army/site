/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/landing.ts":
/*!************************!*\
  !*** ./src/landing.ts ***!
  \************************/
/***/ (function() {

var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
function createDragScroll(selector, options) {
    if (options === void 0) { options = {}; }
    var slider = document.querySelector(selector);
    if (!slider) {
        throw new Error("Element with selector \"".concat(selector, "\" not found"));
    }
    var isDown = false;
    var startX;
    var scrollLeft;
    var defaultOptions = {
        scrollSpeed: 3,
        activeClass: 'active',
    };
    var settings = __assign(__assign({}, defaultOptions), options);
    function handleMouseDown(e) {
        isDown = true;
        slider.classList.add(settings.activeClass);
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    }
    function handleMouseLeave() {
        isDown = false;
        slider.classList.remove(settings.activeClass);
    }
    function handleMouseUp() {
        isDown = false;
        slider.classList.remove(settings.activeClass);
    }
    function handleMouseMove(e) {
        if (!isDown)
            return;
        e.preventDefault();
        var x = e.pageX - slider.offsetLeft;
        var walk = (x - startX) * settings.scrollSpeed;
        slider.scrollLeft = scrollLeft - walk;
    }
    function addEventListeners() {
        slider.addEventListener('mousedown', handleMouseDown);
        slider.addEventListener('mouseleave', handleMouseLeave);
        slider.addEventListener('mouseup', handleMouseUp);
        slider.addEventListener('mousemove', handleMouseMove);
    }
    function removeEventListeners() {
        slider.removeEventListener('mousedown', handleMouseDown);
        slider.removeEventListener('mouseleave', handleMouseLeave);
        slider.removeEventListener('mouseup', handleMouseUp);
        slider.removeEventListener('mousemove', handleMouseMove);
    }
    addEventListeners();
    return {
        destroy: removeEventListeners,
    };
}
var vacancyGallery = createDragScroll('.vacancy-gallery', { scrollSpeed: 3 });


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module is referenced by other modules so it can't be inlined
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/landing.ts"]();
/******/ 	
/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,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QUFDLENBQUMsQ0FBQzs7Ozs7Ozs7VUUzRTlFO1VBQ0E7VUFDQTtVQUNBO1VBQ0EiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9zdGF0aWMvLi9zcmMvbGFuZGluZy50cyIsIndlYnBhY2s6Ly9zdGF0aWMvd2VicGFjay9iZWZvcmUtc3RhcnR1cCIsIndlYnBhY2s6Ly9zdGF0aWMvd2VicGFjay9zdGFydHVwIiwid2VicGFjazovL3N0YXRpYy93ZWJwYWNrL2FmdGVyLXN0YXJ0dXAiXSwic291cmNlc0NvbnRlbnQiOlsiaW50ZXJmYWNlIERyYWdTY3JvbGxPcHRpb25zIHtcbiAgc2Nyb2xsU3BlZWQ/OiBudW1iZXI7XG4gIGFjdGl2ZUNsYXNzPzogc3RyaW5nO1xufVxuXG5pbnRlcmZhY2UgRHJhZ1Njcm9sbFJlc3VsdCB7XG4gIGRlc3Ryb3k6ICgpID0+IHZvaWQ7XG59XG5cbmZ1bmN0aW9uIGNyZWF0ZURyYWdTY3JvbGwoXG4gIHNlbGVjdG9yOiBzdHJpbmcsXG4gIG9wdGlvbnM6IERyYWdTY3JvbGxPcHRpb25zID0ge30sXG4pOiBEcmFnU2Nyb2xsUmVzdWx0IHtcbiAgY29uc3Qgc2xpZGVyID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcihzZWxlY3RvcikgYXMgSFRNTEVsZW1lbnQ7XG4gIGlmICghc2xpZGVyKSB7XG4gICAgdGhyb3cgbmV3IEVycm9yKGBFbGVtZW50IHdpdGggc2VsZWN0b3IgXCIke3NlbGVjdG9yfVwiIG5vdCBmb3VuZGApO1xuICB9XG5cbiAgbGV0IGlzRG93biA9IGZhbHNlO1xuICBsZXQgc3RhcnRYOiBudW1iZXI7XG4gIGxldCBzY3JvbGxMZWZ0OiBudW1iZXI7XG5cbiAgY29uc3QgZGVmYXVsdE9wdGlvbnM6IFJlcXVpcmVkPERyYWdTY3JvbGxPcHRpb25zPiA9IHtcbiAgICBzY3JvbGxTcGVlZDogMyxcbiAgICBhY3RpdmVDbGFzczogJ2FjdGl2ZScsXG4gIH07XG5cbiAgY29uc3Qgc2V0dGluZ3M6IFJlcXVpcmVkPERyYWdTY3JvbGxPcHRpb25zPiA9IHsuLi5kZWZhdWx0T3B0aW9ucywgLi4ub3B0aW9uc307XG5cbiAgZnVuY3Rpb24gaGFuZGxlTW91c2VEb3duKGU6IE1vdXNlRXZlbnQpOiB2b2lkIHtcbiAgICBpc0Rvd24gPSB0cnVlO1xuICAgIHNsaWRlci5jbGFzc0xpc3QuYWRkKHNldHRpbmdzLmFjdGl2ZUNsYXNzKTtcbiAgICBzdGFydFggPSBlLnBhZ2VYIC0gc2xpZGVyLm9mZnNldExlZnQ7XG4gICAgc2Nyb2xsTGVmdCA9IHNsaWRlci5zY3JvbGxMZWZ0O1xuICB9XG5cbiAgZnVuY3Rpb24gaGFuZGxlTW91c2VMZWF2ZSgpOiB2b2lkIHtcbiAgICBpc0Rvd24gPSBmYWxzZTtcbiAgICBzbGlkZXIuY2xhc3NMaXN0LnJlbW92ZShzZXR0aW5ncy5hY3RpdmVDbGFzcyk7XG4gIH1cblxuICBmdW5jdGlvbiBoYW5kbGVNb3VzZVVwKCk6IHZvaWQge1xuICAgIGlzRG93biA9IGZhbHNlO1xuICAgIHNsaWRlci5jbGFzc0xpc3QucmVtb3ZlKHNldHRpbmdzLmFjdGl2ZUNsYXNzKTtcbiAgfVxuXG4gIGZ1bmN0aW9uIGhhbmRsZU1vdXNlTW92ZShlOiBNb3VzZUV2ZW50KTogdm9pZCB7XG4gICAgaWYgKCFpc0Rvd24pIHJldHVybjtcbiAgICBlLnByZXZlbnREZWZhdWx0KCk7XG4gICAgY29uc3QgeCA9IGUucGFnZVggLSBzbGlkZXIub2Zmc2V0TGVmdDtcbiAgICBjb25zdCB3YWxrID0gKHggLSBzdGFydFgpICogc2V0dGluZ3Muc2Nyb2xsU3BlZWQ7XG4gICAgc2xpZGVyLnNjcm9sbExlZnQgPSBzY3JvbGxMZWZ0IC0gd2FsaztcbiAgfVxuXG4gIGZ1bmN0aW9uIGFkZEV2ZW50TGlzdGVuZXJzKCk6IHZvaWQge1xuICAgIHNsaWRlci5hZGRFdmVudExpc3RlbmVyKCdtb3VzZWRvd24nLCBoYW5kbGVNb3VzZURvd24pO1xuICAgIHNsaWRlci5hZGRFdmVudExpc3RlbmVyKCdtb3VzZWxlYXZlJywgaGFuZGxlTW91c2VMZWF2ZSk7XG4gICAgc2xpZGVyLmFkZEV2ZW50TGlzdGVuZXIoJ21vdXNldXAnLCBoYW5kbGVNb3VzZVVwKTtcbiAgICBzbGlkZXIuYWRkRXZlbnRMaXN0ZW5lcignbW91c2Vtb3ZlJywgaGFuZGxlTW91c2VNb3ZlKTtcbiAgfVxuXG4gIGZ1bmN0aW9uIHJlbW92ZUV2ZW50TGlzdGVuZXJzKCk6IHZvaWQge1xuICAgIHNsaWRlci5yZW1vdmVFdmVudExpc3RlbmVyKCdtb3VzZWRvd24nLCBoYW5kbGVNb3VzZURvd24pO1xuICAgIHNsaWRlci5yZW1vdmVFdmVudExpc3RlbmVyKCdtb3VzZWxlYXZlJywgaGFuZGxlTW91c2VMZWF2ZSk7XG4gICAgc2xpZGVyLnJlbW92ZUV2ZW50TGlzdGVuZXIoJ21vdXNldXAnLCBoYW5kbGVNb3VzZVVwKTtcbiAgICBzbGlkZXIucmVtb3ZlRXZlbnRMaXN0ZW5lcignbW91c2Vtb3ZlJywgaGFuZGxlTW91c2VNb3ZlKTtcbiAgfVxuXG4gIGFkZEV2ZW50TGlzdGVuZXJzKCk7XG5cbiAgcmV0dXJuIHtcbiAgICBkZXN0cm95OiByZW1vdmVFdmVudExpc3RlbmVycyxcbiAgfTtcbn1cblxuY29uc3QgdmFjYW5jeUdhbGxlcnkgPSBjcmVhdGVEcmFnU2Nyb2xsKCcudmFjYW5jeS1nYWxsZXJ5Jywge3Njcm9sbFNwZWVkOiAzfSk7XG4iLCIiLCIvLyBzdGFydHVwXG4vLyBMb2FkIGVudHJ5IG1vZHVsZSBhbmQgcmV0dXJuIGV4cG9ydHNcbi8vIFRoaXMgZW50cnkgbW9kdWxlIGlzIHJlZmVyZW5jZWQgYnkgb3RoZXIgbW9kdWxlcyBzbyBpdCBjYW4ndCBiZSBpbmxpbmVkXG52YXIgX193ZWJwYWNrX2V4cG9ydHNfXyA9IHt9O1xuX193ZWJwYWNrX21vZHVsZXNfX1tcIi4vc3JjL2xhbmRpbmcudHNcIl0oKTtcbiIsIiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==