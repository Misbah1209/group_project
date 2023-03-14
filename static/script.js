window.onload = admin;
window.onload = loadBasket;

function admin() {
    adminName=document.getElementById("nametag").innerText;

    if (adminName=="Hey admin! Welcome Back to FineWood"){
        console.log("yes");
        console.log(document.getElementById("admintag").innerHTML);
        document.getElementById("admintag").style.display = "block";
    }
    else{
        document.getElementById("admintag").style.display = "none";
        console.log("no");
    }
}

// This function gets/creates session basket.
function getBasket(){
    let basket;
    if(sessionStorage.basket === undefined || sessionStorage.basket === ""){
        basket = [];
    }
    else {
        basket = JSON.parse(sessionStorage.basket);
    }
    return basket;
}

//Adds an item to the basket
function addToBasket( prodName,prodPrice){
    let basket = getBasket();//Load or create basket
    
    //Add product to basket
    basket.push({name: prodName, price: prodPrice});
    
    //Store in local storage
    sessionStorage.basket = JSON.stringify(basket);
    alert('item added to cart');

}

//Deletes all products from basket
function emptyBasket(){
    sessionStorage.clear();
    loadBasket();
}

function loadBasket(){
    let basket = getBasket();//Load or create basket
    let htmlStr="";
    for(let i=0; i<basket.length; ++i){
        htmlStr +='<div style="margin-top: 5px;" class="summary-items">';
        htmlStr +='<h3>'+basket[i].name +'</h3>';
        htmlStr +='<p> £' + basket[i].price + '</p></div>';       
    }
    htmlStr += "<div class='summary-checkout'><button onclick='emptyBasket()'><i class='fa fa-trash fa-lg'></i>Empty Basket</button></div><br></div>";
    document.getElementById("cartDiv").innerHTML = htmlStr;

    let sum = basket.reduce((sum,item) => sum + Number(item.price) , 0);
    document.getElementById("Quantity").innerHTML = "<h3>No.Of Items</h3><p>"+basket.length+"</p>";
    document.getElementById("bill").innerHTML ="<h3>Subtotal</h3><p>£ <span>"+sum+"</span></p>";    
}