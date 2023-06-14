var tournament = document.querySelector(".tournaments")

tournament.addEventListener("change", () => {
    if(tournament.value == "Liga Profesional Argentina"){
        document.querySelector(".next_matches").style.display="none"
        document.querySelector(".liga_profesional").style.display="flex"
        document.querySelector(".copa_argentina").style.display="none"
    } else if (tournament.value == "Copa Argentina") {
        document.querySelector(".next_matches").style.display="none"
        document.querySelector(".liga_profesional").style.display="none"
        document.querySelector(".copa_argentina").style.display="flex"
    } else {
        document.querySelector(".next_matches").style.display="flex"
        document.querySelector(".liga_profesional").style.display="none"
        document.querySelector(".copa_argentina").style.display="none"
    }
})

setInterval(() => {
    var fechaInicio = new Date().getTime();
    var fechaFin    = new Date('2023-06-24 20:00:00').getTime();
    var diff = fechaFin - fechaInicio;
    var days = Math.round(diff/(1000*60*60*24))
    var hours = Math.round(diff/(1000*60*60))
    var minutes = Math.round(diff/(1000*60))
    if(fechaInicio<fechaFin){
        if(days>1){
            document.querySelector(".time").innerHTML = "Faltan "+Math.round(diff/(1000*60*60*24))+" dias"
        } else if(days< 2 && hours>1){
            document.querySelector(".time").innerHTML = "Faltan "+Math.round(diff/(1000*60*60))+"hrs"
        }
        if(hours==1 && minutes<61){
            document.querySelector(".time").innerHTML = "Faltan "+Math.round(diff/(1000*60))+"min"        
        } else if(hours==0){
            document.querySelector(".time").innerHTML = "Faltan "+Math.round(diff/(1000*60))+"min"        
        }
    } else {
        document.querySelector(".time").innerHTML = "En juego"      
    }
}, 1000);

