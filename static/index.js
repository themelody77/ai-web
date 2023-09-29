var text1 = 'A AI initiative to help students';
var text2 = 'Obtain answers from your own recommended pdf sources';
var text3 = 'Summarize your large texts (abstractive/extractive) and save your time';
var text4 = 'Generate the maximum out of you with less time!'

var texts = [text1, text2, text3]; // Store the texts in an array
var speed = 60; /* The speed/duration of the effect in milliseconds */
var i=0,j=0,k=0,l=0;
document.getElementById("obj1").style.display = "list-item";
function typeWriter1() {
    if(i<text1.length){
        document.getElementById("obj1").innerHTML += text1[i++];
        setTimeout(typeWriter1,speed);
    }
    else{
        document.getElementById("obj2").style.display = "list-item";
        typeWriter2();
    }
}
function typeWriter2() {
    if(j<text2.length){
        document.getElementById("obj2").innerHTML += text2[j++];
        setTimeout(typeWriter2,speed);
    }
    else{
        document.getElementById("obj3").style.display = "list-item";
        typeWriter3();
    }
}
function typeWriter3() {
    if(k<text3.length){
        document.getElementById("obj3").innerHTML += text3[k++];
        setTimeout(typeWriter3,speed);
    }
    else{
        document.getElementById("obj4").style.display = "list-item";
        typeWriter4();
    }
}
function typeWriter4() {
    if(l<text4.length){
        document.getElementById("obj4").innerHTML += text4[l++];
        setTimeout(typeWriter4,speed);
    }
}

typeWriter1();