/**
 * Created by Борисов on 08.02.2017.
 */

$(document).ready( function() {
    setHalfsSizes();

    // почему-то не работает display: none;
    $('.cat_info').fadeOut();

    // $('.cat').click(function() {
    //     var a = $(this).find('a');
    //     $(a).trigger('click');
    // });

    $('.cat').click( function() {
        left_side = $('.left_side');
        $.getJSON('/get_missions' + $(this).find('a').attr('href'),
            function (data) {
                left_side.empty();

                jQuery.each(data, function () {
                    left_side.prepend(
                        '<div class="mission_wrap_wrap">' +
                        '<div class="mission_wrap">' +
                        '<div class="mission" ' +
                        'style="background-color:' + this.bg_color + '; color:' + this.color + ';">' +
                        this.name +
                        '</div>' +
                        '<div class="ok_button"></div>' +
                        '<div class="del_button"></div>' +
                        '</div>' +
                        '</div>'
                    );
                });
            });
    });

    $(".slider").hover(
        function() {
            $(".arrow").css({
                'backgroundImage': 'url(http://192.168.0.9:8000/static/images/arrow_white.png)'
            });
        },
        function() {
            $(".arrow").css({
                'backgroundImage': 'url(http://192.168.0.9:8000/static/images/arrow_black.png)'
            });
        }
    );

    $(".slider").click(moveSlider);

    $(".hello").click(function() {
       $(".slider").trigger("click");
    });

    $('.mission_wrap').click( function() {

        var parent = $(this);
        var mission = $(this).find('.mission');
        var okButton = $(this).find('.ok_button');
        var delButton = $(this).find('.del_button');
        var width = $(this).outerWidth();

        $(okButton).click( function() {
            var curMisWidth = $(mission).width();
            mission.text('DONE');
            mission.css({'text-align': 'center', 'width': String(curMisWidth)});
            mission.css({'background-color': '#ffffff', 'color': '#20a911'});
            parent.delay(500).fadeOut(1500);
        });

        $(delButton).click( function() {
            parent.animate({"margin-left": $(window).width() + 'px', opacity: '0'}, 250);
            parent.fadeOut();
        });

        if ($(this).hasClass('.clicked')){
            $(delButton).fadeOut(200);
            $(okButton).delay(100).fadeOut(200);
            $(this).removeClass('.clicked');
        } else {
            // располагаем элементы справа от заметки.
            $(okButton).css({'margin-left': width + 10 + 'px'});
            $(delButton).css({'margin-left': width + 70 + 'px'});

            $(okButton).fadeIn(200);
            $(delButton).delay(100).fadeIn(200);
            $(this).addClass('.clicked');
        }
    });
});

function setHalfsSizes(){
    $(".left_side").css({
        'width':  $(window).width()/2  + 'px',
        'height': $(window).height() - 15 + 'px'
    });

    $(".hello_wrap").css({
        'width':  $(window).width()/2  + 'px',
        'height': $(window).height() - 15 + 'px'
    });

    $(".right_side").css({
        'width':  $(window).width()/2  + 'px',
        'height': $(window).height() + 'px',
        'left': $(window).width() - 76 + 'px'
    });

    $(".cover").css({
        'width':  $(window).width() + 'px',
        'height': $(window).height() + 'px'
    });

    $(".slider").css({
        'height': $(window).height() + 'px'
    })
}

function moveSlider() {
    if ($('.slider').hasClass('.clicked')) {
        $('.arrow').animate({transform: 'rotate(360deg)'}, 300);
        $('.right_side').animate({'left': $(window).width() - 76 + 'px'}, 1000, 'easeInOutExpo');
        $('.cover').delay(600).fadeOut();
        $('.cat_wrap_wrap').delay(600).fadeOut();
        $('.slider').removeClass('.clicked');
    } else {
        $('.cat_wrap_wrap').fadeIn();
        $('.cover').fadeIn();
        $('.arrow').animate({transform: 'rotate(180deg)'}, 300);
        $('.right_side').animate({'left': $(window).width() / 2 + 16 + 'px'}, 1000, 'easeInOutExpo');
        $('.slider').addClass('.clicked');
    }
}