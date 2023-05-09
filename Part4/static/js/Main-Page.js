window.onload = function() {
    loadFlavors();
    listFlavors();
 };

const flavors = []
const items = [];

function listFlavors(){
    
    flavors.forEach(function (arrayItem){
        let flavor= '<div class="image" id="'+arrayItem.name+'">'+
                        '<img class="img" src="'+arrayItem.imgUrl+'"'+'alt="'+arrayItem.name+'">'+
                        '<div class="image_overlay">'+ 
                            '<button class="flavor" onclick="sendToCart()">'+arrayItem.name+'</button>'+
                        '</div>'+
                    '</div>';

        document.getElementById("main_body").innerHTML += flavor;
    });

    let btns = document.querySelectorAll("button.flavor"); //selecting buttons w/ class "flavor"

    for (let btn of btns){    //adding event handler to each flavor button
        btn.addEventListener("click", function (){  //function that both alerts user of selected flavor and adds to cart
            let txt = btn.textContent;  //getting button text
            items.push({id: txt});   // adding to items array
            let flavor_div = document.getElementById(txt); //getting id of selected div
            flavor_div.style.backgroundColor = ("#00CED1"); //changing background color of selcted div
        });
   }
}

function loadFlavors(){
    const flavorsParse = JSON.parse(localStorage.getItem("flavors"));
    
    for (var i=0;i<flavorsParse.length;i++) {
        flavors.push(flavorsParse[i]);
     }
}

function sentToCart(){  //sending selected flavor to cart by writing to JSON file
    let data = JSON.stringify(items);  //converting to string
    localStorage.setItem('selectedItems', data);
    window.location.href = 'checkout.html';
    location.href = "Checkout.html";
}
