var news = document.getElementsByClassName("new_more");
for(const el of news){
    el.onclick = function(){
        location.href = '/noticia/'+el.id
    }
};