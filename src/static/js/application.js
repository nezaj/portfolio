// Application-wide js

$(function(){
  // Only apply tooltips for Desktop devices
  var mq = window.matchMedia( "(min-width: 992px)" );
  if (mq.matches) {
    $('a[rel=tipsy]').tipsy({gravity: 's'})
  }
});
