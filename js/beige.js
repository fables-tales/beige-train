 // JavaScript Document

<!--

var color = "ff00ff";

function getColor() {
    return color;
}

function recolor() {
    $.get("/getcolor", function(response) {
        document.bgColor = "#" + response;
        color = response
    });
}

window.onload = function() {
    document.bgColor = "#" + getColor();

    ticker();  // Start the countdown
    $("#isbeige").click(function() {
        console.log("/classify/1/" + getColor());
        initPage();
    });

    $("#notbeige").click(function() {
        $.get("/classify/0/" + getColor(), recolor);
        initPage();
    });
}

var countdown = 100;
var ticking = true;

function initPage()
{
    countdown = 100;

    // Enable buttons
    document.getElementById('isbeige').disabled = true;
    document.getElementById('notbeige').disabled = true;
    if(!ticking)
    {
        ticker();  // Start the countdown
    }
}

function ticker(){
    countdown-=3;
    if(countdown < 0)
    {
        countdown = 0;
        // Enable buttons
        document.getElementById('isbeige').disabled = false;
        document.getElementById('notbeige').disabled = false;
        ticking = false;
    }
    else
    {
        t = setTimeout("ticker();",40); // Should be 40 for normal running
    }

    document.getElementById('countdownbar').style.width = countdown+"%";
}

//-->
