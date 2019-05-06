let hidden, visibilityChange
let visibilityHandlers = {
  onHide: null,
  onShow: null
}
let hideTimer = null

if (typeof document.hidden !== 'undefined') { // Opera 12.10 and Firefox 18 and later support 
  hidden = 'hidden'
  visibilityChange = 'visibilitychange'
} else if (typeof document.msHidden !== 'undefined') {
  hidden = 'msHidden'
  visibilityChange = 'msvisibilitychange'
} else if (typeof document.webkitHidden !== 'undefined') {
  hidden = 'webkitHidden'
  visibilityChange = 'webkitvisibilitychange'
}

function handleVisibilityChange (forcedFlag) {
  let visible = true
  if (typeof forcedFlag === 'boolean') {
    visible = forcedFlag
  } else {
    visible = !document.hidden
  }
  console.log('Visibility change: ' + visible)
  if (!visible && visibilityHandlers.onHide) {
    if (!hideTimer) {
      hideTimer = setTimeout(function () {
        visibilityHandlers.onHide()
        hideTimer = null
      }, 6000)
    }
  } else if (visible && visibilityHandlers.onShow) {
    if (hideTimer) {
      clearTimeout(hideTimer)
      hideTimer = null
    } else {
      visibilityHandlers.onShow()
    }
  }
}

if (typeof document.addEventListener === 'undefined' || hidden === undefined) {
  console.error('This page requires a browser, such as Google Chrome or Firefox, that supports the Page Visibility API.')
} else {
  document.addEventListener(visibilityChange, handleVisibilityChange, false)
  document.addEventListener('focus', function () {
    handleVisibilityChange(true)
  }, false)
  document.addEventListener('blur', function () {
    handleVisibilityChange(false)
  }, false)
  window.addEventListener('focus', function () {
    handleVisibilityChange(true)
  }, false)
  window.addEventListener('blur', function () {
    handleVisibilityChange(false)
  }, false)
}

export { visibilityHandlers }
