var seconds=0;
var minutes=0;
var hours=0;
var myInterval;
var elapsedTime= hours+' h :'+minutes+' m :' + seconds+ ' s ';
document.getElementById('watchFace').innerHTML=elapsedTime;


function stopWatch(){
    
    if(seconds<59){
        seconds++;
    }
    else if(seconds==59 && minutes<59){
        minutes++;
        seconds=0;

    }
    else{
        hour++;
        minutes=0;

    }
    elapsedTime= hours+' h :'+minutes+' m :' + seconds+ ' s ';
    document.getElementById('watchFace').innerHTML=elapsedTime;

}

function startStopWatch(){
    document.getElementById('start').disabled=true;
    myInterval=setInterval(stopWatch, 1000);
}

function stopStopWatch(){
    clearInterval(myInterval);
    document.getElementById('start').disabled=false;


}

function resetFunction(){
    clearInterval(myInterval);
    seconds=0;
    minutes=0;
    seconds=0;
    elapsedTime= hours+' h :'+minutes+' m :' + seconds+ ' s ';
    document.getElementById('watchFace').innerHTML=elapsedTime;

}



