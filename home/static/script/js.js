
// menu 
$('.categories a').hover(function(){
   
    $(this).addClass('text_menu_color')

},function(){
$(this).removeClass('text_menu_color')
}
)

// display sub categories when user hover on categories options
$(' .categories').hover(function(){
$('.sub-category-container',this).css({'display':'inherit'});
},function(){
    $('.sub-category-container',this).css({'display':'none'});
})



// display categories when user hover on menu option


$(' .subdiv').hover(function(){
$('.shop-options',this).css({'display':'inherit'});
},function(){
    $('.shop-options',this).css({'display':'none'});
})

/* 
click to zoom
*/

$(document).ready(function(){
$('.img-active').click(function(){
 $('.img-active-mobile').show();
});
$('.close-zoom').click(function(){
    $('.img-active-mobile').hide();
});
});