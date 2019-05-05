let hidden, visibilityChange;
let visibility_handlers = {
	onHide: null,
	onShow: null
};
let hideTimer = null;

if (typeof document.hidden !== "undefined") { // Opera 12.10 and Firefox 18 and later support 
  hidden = "hidden";
  visibilityChange = "visibilitychange";
} else if (typeof document.msHidden !== "undefined") {
  hidden = "msHidden";
  visibilityChange = "msvisibilitychange";
} else if (typeof document.webkitHidden !== "undefined") {
  hidden = "webkitHidden";
  visibilityChange = "webkitvisibilitychange";
}

function handleVisibilityChange() {
  if (document[hidden] && visibility_handlers.onHide) {
  	if (!hideTimer) {
  	  hideTimer = setTimeout(function() {
  	    visibility_handlers.onHide()
  	    hideTimer = null
  	  }, 60)
  	}
  } else if (!document[hidden] && visibility_handlers.onShow) {
  	if (hideTimer) {
  	  clearTimeout(hideTimer)
  	  hideTimer = null;
  	} else {
  	  visibility_handlers.onShow()
  	}
  }
}

if (typeof document.addEventListener === "undefined" || hidden === undefined) {
  console.error("This page requires a browser, such as Google Chrome or Firefox, that supports the Page Visibility API.");
} else {
  // Handle page visibility change   
  document.addEventListener(visibilityChange, handleVisibilityChange, false);
}

export { visibility_handlers }
