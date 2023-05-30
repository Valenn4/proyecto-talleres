var news = document.getElementsByClassName("new");
for(const el of news){
    el.onclick = function(){
        location.href = '/noticia/'+el.id
    }
};

var news2 = document.getElementsByClassName("principally_new");
for(const el of news2){
    el.onclick = function(){
        location.href = '/noticia/'+el.id
    }
};


