window.onload = function() {
    loadFlavors();
    listFlavors();
 };

//const flavors = [];
const flavors = [
    {
        id: 0,
        name: "Blackberry",
        imgUrl: "main_images/blackberry.jpg"
    },
    {
        id: 1,
        name: "Chocolate",
        imgUrl: "main_images/chocolate.jpg"
    },
    {
        id: 2,
        name: "Cookies & Cream",
        imgUrl: "main_images/cookies.jpg"
    },
    {
        id: 3,
        name: "Cotton Candy",
        imgUrl: "main_images/cotton_candy.jpg"
    },
    {
        id: 4,
        name: "Mango",
        imgUrl: "main_images/mango.jpg"
    },
    {
        id: 5,
        name: "Pistachio",
        imgUrl: "main_images/pistachio.jpg"
    },
    {
        id: 6,
        name: "Toffee",
        imgUrl: "main_images/toffee.jpg"
    },
    {
        id: 7,
        name: "Strawberry",
        imgUrl: "main_images/strawberry.jpg"
    },
    {
        id: 8,
        name: "Vanilla",
        imgUrl: "main_images/vanilla.jpg"
    }
];

//This function gets a name and image url then saves it to the flavor array
function addFlavor(){

    var Name = document.getElementById("title").value;
    var url = document.getElementById("URL").value;
    var lastId = flavors[flavors.length-1].id;

    flavors.push({
        id: lastId+1,
        name: Name,
        imgUrl: url
    });

    var flavor ='<tr id="tflavor">'+
                    '<td>'+(lastId+1)+'</td>'+
                    '<td>'+Name+'</td>'+
                    '<td>'+url+'</td>'+
                '</tr>';

    document.getElementById("tflavor").innerHTML += flavor;
    save();
}

//This function lists flavors on the page
function listFlavors(){

    flavors.forEach(function (arrayItem){
        let flavor='<tr id="flavor">'+
                        '<td>'+arrayItem.id+'<td>'+
                        '<td>'+arrayItem.name+'</td>'+
                        '<td>'+arrayItem.imgUrl+'</td>'+
                    '</tr>';

        document.getElementById("tflavor").innerHTML += flavor;
    });
}

//This function finds a flavor based on the flavors id then deletes it
function deleteFlavor(){

    let id = parseInt(document.getElementById("deleteID").value);

    var remove = flavors.findIndex(x => x.id===id);

    if(remove !== -1){
        flavors.splice(remove,1);
    }else{
        alert("Flavor not found");
    }
    
    save();
    window.location.reload();
} 

//This function takes a flavor id, name, and URL then updates the flavor with the given id
function updateFlavor(){
    
    let id = parseInt(document.getElementById("updateId").value);
    let newName = document.getElementById("updateName").value;
    let newUrl = document.getElementById("updateUrl").value;
    
    var update = flavors.findIndex(x => x.id===id);
    
    if(update !== -1){
        flavors[id].name = newName;
        flavors[id].imgUrl = newUrl;
    }else{
        alert("Flavor not found");
    }

    save();
    window.location.reload();
}

//This function saves flavors into a json string then stores it in localStorage
function save(){localStorage.flavors = JSON.stringify(flavors);}

//This function parses the json from localStorage then pushes them to the flavor array
function loadFlavors(){
    const flavorsParse = JSON.parse(localStorage.getItem("flavors"));
    
    for (var i=0;i<flavorsParse.length;i++) {
        flavors.push(flavorsParse[i]);
     }
}
