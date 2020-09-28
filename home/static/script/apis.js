
/* display cookie notification just once to user
*/


/* get accept cookie el */
$(document).ready(function(){
    displyCNofy()
    function displyCNofy(){

        var _state= getCookie('cookieaccepted') 
        if(_state==1){
         $('.cookies-notification').hide()
        }
        else{
         console.log(_state)
         $('.cookies-notification').show();
        }
     }
$('.accept-cookies').click(function(){

    var cname= "cookieaccepted"
    var  cvalue =1
    var exdays=365
    setCookie(cname, cvalue, exdays)
    $('.cookies-notification').hide('fast');

})
})
/* create and login user form */
const registerUserForm = document.querySelector('#registrationfm');
// submit form event listener
registerUserForm.addEventListener("submit",createUserFormSubmit)

function createUserFormSubmit(event){
    event.preventDefault()
    // disable sumit button
    const   rgbtn =  document.getElementById('rg-btn')
    rgbtn.disabled=true;
    $('.userlogin .connecting-user-gif').css({'visibility':'initial'});
  
    const myForm  = event.target
    const myFormData = new FormData(myForm)
    const csrftoken = getCookie('csrftoken')
    const url  = myForm.getAttribute("action")
    const method   = myForm.getAttribute("method")
    const  xhr  = new XMLHttpRequest()
    xhr.open(method,url)
    xhr.setRequestHeader("HTTP_X_REQUEST_WITH","XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-with","XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken",csrftoken)
    xhr.onload=function(){
        const     serverResponse  = xhr.response
        const     serverdata      = JSON.parse(serverResponse)   
        if(xhr.status === 200 ){
            if(serverdata.token){
            cname  = "user" 
            cvalue = serverdata.token
            exdays = 1
            setCookie(cname, cvalue, exdays)
            // user auth function, to verify if user
            //login 
            $('.userlogin').hide('fast');
            getAuthState()
             
            }
        
        }
      
     
    }
    xhr.onerror = function(){
        $('.internal-error').text('Unkown error')
    }
    xhr.send(myFormData)
}

// end of create user form




$(document).ready(function(){
    $('.customer-logos').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 3
            }
        }]
    });
});


// delete loadcount cookie
setCookie('loadcount', 0, -1)
// set cookie
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }


  // return domain name
function _domainName(){
    domain="/"
    return domain
}

//createElements
// for loaded products


function elments(htmlContainer,products,i){
    var       _domain = _domainName()
    const img      = document.createElement('img');
    const divtwo   = document.createElement('div')
    const imgdiv   = document.createElement('div')
    const button   = document.createElement('div')
    const h2       = document.createElement('h2')
    const p        = document.createElement('p')
    var btntext    = document.createTextNode("Qick View")
    // get the product name 
    // slice the product name
    /**
     add ... when product name length
     is greater than slice product name length
     * 
     */
    var   strname  = products[i].name
    var strslice   = strname.slice(0,16)
    if(strname.length>strslice.length){
        strslice = strslice +"..."
    }
    var name       = document.createTextNode(strslice)
    var price      = document.createTextNode(products[i].price)
    var  a         = document.createElement('a') 
    var  input     = document.createElement('input')
    _obj  = products[i]
      
    var mynumber  = "00237680288683"
    if(products[i].image){
     img.src=_domain+products[i].image
    }
  
   input.type ="hidden"
   input.value = _domain+"product/detail/"+products[i].slug
   button.className = "buybtn"
   imgdiv.className = "img-div"
   divtwo.className = "product-items"
   slug =products[i].slug
   input.className="hvalue"
   a.className="linka"
   button.appendChild(btntext)
   h2.appendChild(name);
   p.appendChild(price)
   imgdiv.appendChild(img)
   divtwo.appendChild(imgdiv)
   divtwo.appendChild(h2);
   divtwo.appendChild(p);
   a.appendChild(button)
   a.appendChild(input)
   divtwo.appendChild(a)
   // append final child to html dom element
   htmlContainer.appendChild(divtwo)
}
// create xhr for products receive
// XMLHttpRequest 

function xhrReturn(_url){
    const xhr = new XMLHttpRequest()
    const method =  "GET"
    const url    = _url
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.send()
    return xhr
}


// display products to user on page load
function loadProducts(){
    var       _domain = _domainName()
    __url = _domain +"home/products"
    const product_container = document.querySelector('.pd-display')
   
    xhr=xhrReturn(__url)
    
    xhr.onload=function(){
        
        const  serverResponse = xhr.response
        var    products  = serverResponse
        var i;
        if(products){
            
            $('.product-display .class-loader').hide();
            $('.product-display .load-more').show('fast');
            
        }
        for(i=0;i<6;i++){
            // create html dom elements
            elments(product_container,products,i)
            
        }
    }
    xhr.onerror=function(){
        $('.connection-lost').css({'visibility':'initial'});
    }
   
}


/* load products base on category and subcategory */

function loadSearchProducts(){
    
    const product_container = document.querySelector('#productsSeach')
    const _url= '/api/product/search'+window.location.pathname;
    xhr=xhrReturn(_url)
    
    xhr.onload=function(){
        
        const  serverResponse = xhr.response
        var    products  = serverResponse
        var i;
        if(products){
            
            $('.product-display .class-loader').hide();
            $('.product-display .load-more').show('fast');
            
        }
        for(i=0;i<6;i++){
            // create html dom elements
            elments(product_container,products,i)
            
        }
    }
    xhr.onerror=function(){
        $('.connection-lost').css({'visibility':'initial'});
    }
   
}




// load more products when user clicks the load more btn
const loaderEl = document.querySelector('#loadmoreproducts');
if(loaderEl){
loaderEl.addEventListener('click',LoadMore)
}
// load more search products
const loaderSearchEl = document.querySelector('#loadmoreSearch');
if(loaderSearchEl){
loaderSearchEl.addEventListener('click',LoadMore)
}
function LoadMore(){
    const el = document.querySelector('.product-container')
    $('.product-display  .load-more .loader-gif').show();
      var       _domain = _domainName()
    __url = _domain +"home/products"
    xhr =xhrReturn(__url);
    _loadMoreProducts(xhr,el)
    
}
// load more search products
function LoadMoreSearch(){
    const el = document.querySelector('#productsSeach')
    $('.product-display  .load-more .loader-gif').show();
    const _url= '/api/product/search'+window.location.pathname;
    xhr =xhrReturn(_url);
    _loadMoreProducts(xhr,el)
    
}
function _loadMoreProducts(xhr){
    xhr.onload=function(){
    $('.product-display  .load-more .loader-gif').hide();
    const  serverResponse = xhr.response
    var    products  = serverResponse
    var numberofproducts =0
    var  i=0
    // store the number of products user has loaded
    // in a cookie loadcount
    productsloaded=getCookie('loadcount')
    if (productsloaded){
        numberofproducts=3+parseInt(productsloaded)
        i=parseInt(productsloaded)
    }
    else{
        numberofproducts=12
        i=6

    }
   /* 
   set cookie, as long 
   as product loadcount cookie
   less than product length
   */
    if(numberofproducts<products.length){
        setCookie('loadcount',numberofproducts, 1)
          // start pulling products from the max
    //initial value of products loaded
    for(i;i<numberofproducts;i++){
        // create html dom elements
        elments(product_container,products,i)  
    }
    }   
    else{
        $('.product-display .load-more').hide('fast');
    } 
}
xhr.onerror=function(){
    $('.connection-lost').css({'visibility':'initial'});
}
}



// event delegation handler for dynamic generated button
// this will store the product url user has just visited to cookies
$(document).on('click','.linka',function(){
 var _val=$('.hvalue',this).val()
 cname  = "product_link" 
 cvalue = _val
 exdays = 1
 setCookie(cname, cvalue, exdays)
 window.location.href=_val

});

// when user clicks on contact seller 
$('#contact-seller').click(function(){
// get the product slug 
var  _half_slug = "product/detail/"
var product_slug=$('#pd-value',this).val()
var product_seller=$('#pd-num',this).val()
var _domain    = window.location.hostname
var _product_url = _domain+ "/"+ _half_slug+product_slug

// delete old cookies 
setCookie("product_link", 0, -1)
setCookie("seller_number", 0, -1)

// set a new product cookie
// and seller phone number of product
cname  = "product_link" 
 cvalue = _product_url
 exdays = 1
 setCookie(cname, cvalue, exdays)
 // set a seller number cookie
 nname= "seller_number"
 nvalue= product_seller
 nxdays= 1
 setCookie(nname, nvalue, nxdays)

 

 /* 
 check for user authentication state,
 then redirect the user to 
 the appropriate side 
 */
getAuthState()

});


// get user authentication state
function getAuthState(){

    var       _domain = _domainName()
    const xhr = new XMLHttpRequest()
    const method =  "GET"
    const url    = _domain +"load/auth"
    const responseType = "json"
    var get_seller_num = getCookie("seller_number")
    var get_product_url = getCookie("product_link")
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.send()
    xhr.onload=function(){
        const  serverResponse = xhr.response
        var    auth  = serverResponse 
       // user not login
       // activate login form for user
        if(auth.auth===0){
        
            // open login in form
            $('.userlogin').show('fast');
            
        } 
        // user login
        // redirect user to seller whatsapp account
        else{
            
            window.location.href="https://wa.me/"+get_seller_num+"/?text=" +"https://"+get_product_url +"%0a‎" +"Hello I am interested in product"
            
        }
    }
    xhr.onerror=function(){
    }
}

// load menus 
loadMenu()
function loadMenu(){

    var       _domain = _domainName()
    const xhr = new XMLHttpRequest()
    const method =  "GET"
    const url    = _domain +"load/menu"
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.send()
    xhr.onload=function(){
        const  serverResponse = xhr.response
        const  menuarray =serverResponse
 
    }
    xhr.onerror=function(){
    }
}


// load product deals 
loadDeals()
function loadDeals(){
    const xhr= new XMLHttpRequest()
    const method = "GET"
    var       _domain = _domainName()
    const url    = _domain +"laod/deals"
    const responseType = 'json'
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.send()
    xhr.onload=function(){
        const  dealElment = document.querySelector('.home-slider-container');
        const  serverResponse = xhr.response
        var  productArray =serverResponse
        
        for(let i=0;i<productArray.length;i++)
        {
            
            const innerSlider = document.createElement('div')
            const img         = document.createElement('img')
            const a           = document.createElement('a')
            const view        = document.createElement('div')
            const text        = document.createTextNode('View')
            
            a.href =productArray[i].contact
            img.src=productArray[i].image
            // add event listener

            a.addEventListener('click',function(event){
                cname  = "product_link" 
                cvalue = productArray[i].contact
                exdays = 1
                // this cookie is use to display similar products to user
                setCookie(cname, cvalue, exdays) 
            });
            view.className="dealView"
            view.appendChild(text)
            innerSlider.className = "inner-slider"
            innerSlider.appendChild(img) 
            innerSlider.appendChild(view)
            a.appendChild(innerSlider)
            dealElment.appendChild(a)
        }
       /* 
       call product slider function
       from slider.js
       */
        products = productArray
         hotSlider(products)
}
xhr.onerror=function(){
console.log('error occured')
}
}



