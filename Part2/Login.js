function login(){

    //These two variables create the mock databases to be used for the login system.
    let Employees = `{"Employees":[
        {"UserName":"Wyatt","Password":"asdf"},
        {"UserName":"Devis","Password":"asdf"},
        {"UserName":"Caleb","Password":"asdf"},
        {"UserName":"Cierra","Password":"asdf"}
    ]}`;
    let User=`{"Users":[
        {"UserName":"User1","Password":"asdf"}
    ]}`;

    //These two variables parse the json from the Employees and User variable
    const json = JSON.parse(Employees);
    const usjson= JSON.parse(User);
    
    //These two variables are used to get the text currently typed into the User and Pass text field
    var name = document.getElementById("User").value;
    var pass = document.getElementById("Pass").value;
    
    //This loop goes through the JSON document and checks if the username and password matches
    //an entry in the mock database. It goes about this in a very janky way I might add.
    for(var i = 0;i<=4;i++){
        if(i===4){
            alert("Incorrect Username or Passowrd");
            break;
        }
        if(name===json.Employees[i].UserName && pass===json.Employees[i].Password){
            window.location.href='Item-Management.html';
            break;
        }
    }
}