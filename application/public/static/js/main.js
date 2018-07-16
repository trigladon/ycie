(function ($) {
    "use strict";

    /* --------------------------------------------
     Page height classes creator 
     --------------------------------------------- */

    function page_height_classes_creator() {
        var minheight = $(window).height();
        var headerhight = $('.navbar').outerHeight(true);
        var hightoutput = minheight - headerhight;
        var half_height = minheight / 2;
        var thirdhaflhight = (hightoutput / 4) * 3.4;
        var thirdhaflcutedhight = (hightoutput / 4) * 0.56;
        var $min_half_height = $(".min_half_height");
        var $thirdhalf_height = $(".thirdhalf_height, .thirdhalf_height .item, .thirdhalf_height  .owl-carousel-item");
        var $halfheight_screen = $(".halfheight_screen, .halfheight_screen  .item, .halfheight_screen  .owl-carousel-item , .halfheight_screen  .horizontal-item");
        var $full_height = $(".full-screen .owl-carousel-item, .full-screen .bg-image, .full_height");
        var $full_height_minus_header = $(".full-screen-minus-header .owl-carousel-item, .full-screen-minus-header .bg-image");
        var $full_height_minus_header_border = $(".full-screen-minus-header-border .owl-carousel-item, .full-screen-minus-header-border .horizontal-item, .full-screen-minus-header-border .item");
        var $zero_one_carousel_img = $(".zero-one-carousel .owl-carousel-item-bg-image, .zero-one-carousel .owl-carousel-item-bg-image img");

        $min_half_height.css({
            'min-height': minheight / 2,
        });

        $thirdhalf_height.css({
            'height': thirdhaflhight
        });

        $halfheight_screen.css({
            'height': half_height
        });

        $full_height.css({
            'min-height': minheight,
            'height': minheight
        });

        $full_height_minus_header.css({
            'min-height': hightoutput,
            'height': hightoutput
        });

        $full_height_minus_header_border.css({
            'min-height': hightoutput - 42,
            'height': hightoutput - 42
        });

        if ($(window).height() < 800) {
            $zero_one_carousel_img.css({
                'min-height': hightoutput - 100,
                'height': hightoutput - 100
            });
        } else if ($(window).width() == 1024 && $(window).height() == 1366) {
            $zero_one_carousel_img.css({
                'min-height': hightoutput / 2 - 100,
                'height': hightoutput / 2 - 100
            });
            if ($('.zero-one-carousel').hasClass("full-screen-minus-header") || $('.zero-one-carousel').hasClass("full-screen") || $('.zero-one-carousel').hasClass("full-screen-minus-header-border")) {
                $full_height_minus_header.css({
                    'min-height': hightoutput / 2,
                    'height': hightoutput / 2
                });
            }
        } else {
            $zero_one_carousel_img.css({
                'min-height': hightoutput - 200,
                'height': hightoutput - 200
            });
        }

    }

    /* --------------------------------------------
     owl carousel calling function
     --------------------------------------------- */
    function owl_main_carousel() {
        if ($('#default-carousel').length) {
            var owl = $("#default-carousel");
            owl.owlCarousel({
                nav: false,
                dots: true,
                items: 1,
                autoplay: false,
                navText: ['<i class="fas fa-angle-left" aria-hidden="true"></i>', '<i class="fas fa-angle-right" aria-hidden="true"></i>'],
                afterAction: function (el) {
                    //remove class active
                    this.$owlItems.removeClass('active')
                    //add class active
                    this.$owlItems.eq(this.currentItem + 1).addClass('active')
                }
            });
        }
    }

    function owl_testimonials_carousel() {
        var owl = $("#testimonials");
        if (owl.length) {
            owl.owlCarousel({
                autoplay: true,
                nav: false, // Show next and prev buttons
                smartSpeed: 1000,
                dotsSpeed: 1000,
                items: 1,
            });
        }
    }

    function owl_testimonials_box_carousel() {
        var owl = $("#testimonials_box");
        if (owl.length) {
            owl.owlCarousel({
                autoplay: true,
                dots: true,
                nav: false,
                loop: true,
                smartSpeed: 1000,
                dotsSpeed: 1000,
                responsive: {
                    0: {
                        items: 1,
                        margin: 0,
                    },
                    1000: {
                        items: 2,
                        margin: 30,
                    },
                    1200: {
                        items: 3,
                        margin: 30,
                    }
                }
            });
        }
    }

    /* --------------------------------------------
       Isotope  calling function
    --------------------------------------------- */

    function Isotope_masonry_layout() {
        var $masonry_layout = $('.masonry_layout');
        if ($masonry_layout.length) {
            // init Isotope
            var $grid = $masonry_layout.isotope({
                percentPosition: true,
                hiddenStyle: {
                    opacity: 0,
                    transform: 'scale(0.001)'
                },
                visibleStyle: {
                    opacity: 1,
                    transform: 'scale(1)'
                },
                transitionDuration: '0.6s',
                masonry: {}
            });
            // Isotope filter
            var $items_filter = $('.items_filter');
            var $items_filter_span = $('.items_filter li span');
            $items_filter_span.on('click', function () {
                var $this = $(this);
                var filterValue = $this.attr('data-filter');
                $this.parent().removeClass('active');
                $this.parent().addClass('active');
                $grid.isotope({
                    filter: filterValue
                });
            });

            // layout Isotope after each image loads
            $grid.imagesLoaded().progress(function () {
                $grid.isotope('layout');
            });
        }
    }


    /* ---------------------------------------------
     Scripts initialization
     --------------------------------------------- */

    $(window).on('load', function () {
        "use strict"; // Start of use strict
        Isotope_masonry_layout();
    });

    $(document).ready(function () {
        "use strict"; // Start of use strict
        owl_main_carousel();
        owl_testimonials_carousel();
        owl_testimonials_box_carousel();
    });

    /* ---------------------------------------------
     On resize calling function
     --------------------------------------------- */
    $(window).on('resize', function () {
        "use strict"; // Start of use strict
        page_height_classes_creator();

    }).trigger('resize');

})(jQuery)