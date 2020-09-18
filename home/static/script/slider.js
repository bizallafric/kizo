var slider = document.querySelector('.home-slider')
var slides = $('.home-slider-container .inner-slider').length
var sliderContainer = document.querySelector('.home-slider-container')
var previousbtn = document.querySelector('.previous') 
var nextbtn = document.querySelector('.next')
var slideSize = slider.offsetWidth;
var currentslide = 0;


setInterval(function(){
setTimeout(function(){
    nextSlide(),500
})
},3000)

function moveSlides(){
  
sliderContainer.style.transform ='translateX(-'+currentslide*slideSize+'px)'

}

function nextSlide(){
    console.log('slides',slides)  
    console.log('slidercnt',currentslide)
    if(currentslide ===slides){
    slides[-1]
    currentslide=0
    
 
}
else {
    currentslide+=1
}
moveSlides()
}

function previousSlide(){
    console.log('previous called')
    if(currentslide<=0){
      slides[-1]
    }
    else{
        currentslide -=1
    }
    moveSlides()
}

nextbtn.addEventListener('click',nextSlide)
previousbtn.addEventListener('click',previousSlide)
/**
generateShortCut()
function generateShortCut(){
    const shortcuts = document.createElement('div');
          shortcuts.classList.add('shortmain')
    for(let i=0;i<slides;i++){
        
        const dot = document.createElement('div')
        dot.classList.add('shortcust')

        dot.addEventListener('click',function(event){
            currentslide=i
            var items=$('.shortmain div').length
           console.log(items)

           for(let i=1;i<=items;i++){
            shortcuts.children.classList.remove('active-one')
           }
   
            moveSlides()
        })
     
        shortcuts.appendChild(dot)
    }
    shortcuts.firstChild.classList.add('active-one')
    slider.appendChild(shortcuts)
}
 **/