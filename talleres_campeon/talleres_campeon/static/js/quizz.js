/*window.localStorage.removeItem("quiz")*/
if(window.localStorage.getItem("quiz")!=null 
    && JSON.parse(window.localStorage.getItem("quiz"))['fecha']!=new Date().toLocaleDateString("en-US")){
        window.localStorage.removeItem("quiz")
    }
document.querySelector(".button_play").addEventListener("click", () => {
    if(window.localStorage.getItem("quiz")==null){
        document.querySelector(".init").style.display = "none";
        document.querySelector(".game").style.display = "flex";
        var number = 0;
        var counter = setInterval(function(){
            number++
            document.querySelector(".counter").innerHTML=number    
            if(number==30){
                clearInterval(counter)
            }
        }, 1000);
        document.querySelectorAll(".answer").forEach(el => {
            el.addEventListener("click", () => {
                if(el.getAttribute("id")=="false"){
                    document.querySelector(".answer_false").style.display="flex";
                    clearInterval(counter)
                } else {
                    document.querySelector(".answer_true").style.display="flex";
                    clearInterval(counter)
                }
                window.localStorage.setItem("quiz",  JSON.stringify({"fecha":new Date().toLocaleDateString("en-US"), "participacion": true}))
            })
        })
    } else {
        document.querySelector(".error").style.display='flex'
        document.querySelector(".button_play").style.marginTop='0px'
    }
})

