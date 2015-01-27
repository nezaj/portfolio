var hist = [];
var startUrl = '/iphone/index';

$(document).ready(function() {
  loadPage(startUrl);
});

function loadPage(url) {
  // We want to display a loading indicator while this function
  // is doing work. The indicator should be removed in the callback
  $('body').append('<div id="progress">Loading...</div>');

  // It's a good idea to scroll back to the top whenever a user navigates
  // to a new page
  scrollTo(0,0);

  if (url == startUrl) {
    var element = ' #header ul';
  } else {
    var element = ' #content';
  }

  $('#container').load(url + element, function() {
    hijackLinks(url);
  });
}

function hijackLinks(referrer_url) {
  // Update title
  var title = $('h2').html() || 'Hello!';
  $('h1').html(title);
  $('h2').remove();

  updateLeftButton(referrer_url, title);

  $('#container a').click(function(e) {
    var url = e.target.href;

    // Only hijack internal links!
    if (url.match(/(localhost|joeaverbukh)/)) {
      e.preventDefault();
      loadPage(e.target.href);
      console.log("Loadded " + e.target.href + "!")
    }
  });

  $('#progress').remove(); // Remove progress at end for responsiveness
}

function updateLeftButton(url, title) {
  $('.leftButton').remove();
  hist.unshift({'url':url, 'title':title}); // Add the current page to the stack
  if (hist.length > 1) {
    var prevPage = hist[1];
    $('#header').append('<div class="leftButton">' + prevPage.title + '</div>')
    $('#header .leftButton').click(function(e) {
      // There may be a delay loading the previous page
      // Slightly change the image of the back button when it's clicked to make
      // things feel more responsive
      $(e.target).addClass('clicked');

      // When clicking the back button, we remove the current page and the
      // previous page from the stack so that the back button points
      // to the link before the previous page
      // Ex: Suppose A -> B -> C -> D. If we hit the back button D
      // and get to C then the back button on C needs to point to B.
      hist.shift();
      hist.shift();
      loadPage(prevPage.url);
    });
  }
}
