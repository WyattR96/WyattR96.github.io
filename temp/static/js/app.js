if("serviceWorker" in navigator){
    window.addEventListener("load",function(){
        this.navigator.serviceWorker
        .register("serviceWorker.js")
        .then(res=>console.log("Service Worker Registered"))
        .catch(err=>console.log("an error has occured",err))
    })
}