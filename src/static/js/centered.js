// Used for centering container horizontally and vertically
// Thanks: http://tutorialzine.com/2010/03/centering-div-vertically-and-horizontally/
(function() {
    $(window).resize(function(){

        $('.container').css({
            position:'absolute',
            left: ($(window).width() - $('.container').outerWidth())/2,
            top: ($(window).height() - $('.container').outerHeight())/2
        });

    });

    // To initially run the function:
    $(window).resize();
}());
