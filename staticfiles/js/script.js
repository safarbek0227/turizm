$('.icon').on('click', function (e) {
    $('nav').toggleClass('active')
})
var deviceheight = window.outerHeight;

window.onscroll = function () {
    if(0 < window.pageYOffset) {
        $('nav').addClass('scroll')
    }else{
        $('nav').removeClass('scroll')
    }
  }

$(".main-carousel").owlCarousel({
    margin: 0,
    loop: true,
    autoplay: true,
    dots: false,
    nav: false,
    autoplayTimeout: 10000,
    autoplayHoverPause: false,

    responsive: {
        0: {
        items: 1
        },
        768: {
        items: 1
        },
        1336: {
        item: 1
        },
        1340: {
        items: 1
        }
    }
})

$(".iframe-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: true,
    nav: false,
    navText: [],
    autoplay: false,
    responsive: {
        0: {
        items: 1
        },
        768: {
        items: 2
        },
        1336: {
        item: 3
        },
        1340: {
        items: 3
        }
    }
})

$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

$(document).on('click', 'li a, .scrollto', function(e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      e.preventDefault();
      var target = $(this.hash);
      if (target.length) {

        var scrollto = target.offset().top;

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500);
        return false;
      }
    }
  });

$(document).ready(function() {
    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav)) {
        var scrollto = $(initial_nav).offset().top;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1500);
      }
    }
  });

$('input, textarea').on('click', function (e) {
  $(this).parent().find('label').addClass('active')
})
$('input, textarea').on('blur', function (e) {
  if ($(this).val() == ''){
    $(this).parent().find('label').removeClass('active')
  }
})