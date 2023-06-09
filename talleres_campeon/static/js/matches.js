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

