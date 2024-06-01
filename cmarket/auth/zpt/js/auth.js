function emailErro(email){
    var erroEmail = document.getElementById("erro-email");
    var certoEmail = document.getElementById("certo-email");
    email = email.value

    if(email == ''){
        erroEmail.style.display = "none";
        certoEmail.style.display = "none";
    } else {
        setTimeout(function(){
            if(validarEmail(email)){
                erroEmail.style.display = "none";
                certoEmail.style.display = "inline";
            } else {
                erroEmail.style.display = "inline";
                certoEmail.style.display = "none";
            }
        }, 1000)
    }    
}

function validarEmail(email){
    const valido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return valido.test(email);
}