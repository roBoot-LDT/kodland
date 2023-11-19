let condition = true;
let start = 0;
let end = 0;

function forwards(){
    anime({
        targets: '.menu-small',
        translateX: ['-100%', '0'],
        easing: 'easeInOutQuad',
        direction: 'alternate',
        duration: 1000,
        loop: false
    });
    anime({
        targets: '.menu_small_icon',
        rotate: 90,
        easing: 'easeInOutQuad',
        direction: 'alternate',
        duration: 1000,
        loop: false
    });
    anime({
        targets: '.stick',
        rotate: 180,
        easing: 'easeInOutQuad',
        direction: 'alternate',
        duration: 1000,
        loop: false
    });
    condition = false;
}

function backwards(){
    anime({
        targets: '.menu-small',
        translateX: ['0', '-100%'],
        easing: 'easeInOutQuad',
        direction: 'alternate',
        duration: 1000,
        loop: false                                                                                                    
    });    
    anime({
        targets: '.menu_small_icon',
        rotate: 0,
        easing: 'easeInOutQuad',
        direction: 'alternate',
        duration: 1000,
        loop: false
    });
    anime({
        targets: '.stick',
        rotate: 0,
        easing: 'easeInOutQuad',
        direction: 'alternate',
        duration: 1000,
        loop: false
    });
    condition = true;                                      
}

$('.menu_small_icon').click(function(){
    if(condition) {
        forwards();
    }
    else {
        backwards();
    }
})

$('.container').on('touchstart', function(event){
    start = event.originalEvent.touches[0].pageX;
})

$('.container').on('touchend', function(event){
    end = event.originalEvent.changedTouches[0].pageX;
    if(end - start >= 100 && condition){
        forwards();
    }
    else if(start - end >= 100 && !condition) {
        backwards();
    }
})
