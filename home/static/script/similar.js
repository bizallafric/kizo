// load  similar products


function xhrReturnSimilar(){
    var get_product_url = getCookie("product_link")
  
    var       _domain = _domainName()
    const xhr = new XMLHttpRequest()
    const method =  "GET"
    var url = ""
    if(get_product_url!=""){
     url    = _domain +"load/similar/products"+get_product_url
    }
    else{
    url    =""
}
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.send()
    return xhr
}

// load similar product
loadSimilarProducts()

function loadSimilarProducts(){
    
    const product_container = document.querySelector('#similar-product-container')
   
    xhr=xhrReturnSimilar()
    
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
