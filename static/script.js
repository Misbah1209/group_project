window.onload = admin;

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