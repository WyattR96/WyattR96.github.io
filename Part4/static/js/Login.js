const entities = [
    {
        username: "Wyatt",
        password: "asdf",
        email: "wyattr67@hotmail.com",
        type: "E"
    },

    {
        username: "Cierra",
        password: "asdf",
        email: "asdf@asdf.com",
        type: "E"
    },

    {
        username: "Devis",
        password: "asdf",
        email: "asdf@asdf.com",
        type: "E"
    },

    {
        username: "Caleb",
        password: "asdf",
        email: "asdf@asdf.com",
        type: "E"
    },

    {
        username: "John",
        password: "jkl;",
        email: "asdf@asdf.com",
        type: "C"
    },

    {
        username: "Jake",
        password: "jkl;",
        email: "asdf@asdf.com",
        type: "C"
    }
]

function login(){
    //Gets the username and password from the text boxes
    var username = document.getElementById("User").value;
    var password = document.getElementById("Pass").value;

    //Finds the entity based on username
    const selectedItem = entities.find((entities) => entities.username === username);
    console.log(selectedItem);

    //Checks the users password as well as type, sending employees to the item management page
    //and customers to the main page
    if(selectedItem.password === password && selectedItem.type === "E"){
        location.href = "Item-Management.html";

    }else if(selectedItem.password === password && selectedItem.type === "C"){
        location.href = "Main-Page.html";
        
    }else{
        alert("Incorrect password");
    }
}


