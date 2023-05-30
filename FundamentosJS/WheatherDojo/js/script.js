console.log("Hello World");
function changeCity(){
    alert("Loading weather report...");
}
function acceptCookies(element)
{
    var cookieContainer=element.closest(".cookies");
    cookieContainer.remove();
}
function changeMetric(element)
{
    console.log(element.value);

    var temp=document.querySelectorAll(".max,.min");
    console.log(temp[0],[0]);
        for(var i=0;i<temp.length;i++){
            console.log(i);
            var currentTemp=parseInt(temp[i].innerHTML);
            console.log(currentTemp[i]);
            if(element.value ==="celsius") 
            {
                let celciusResult=(currentTemp-32)/1.8;
                temp[i].textContent=parseInt(celciusResult) + "°";
            }
            else
            {
                let farenheitResult=(currentTemp*1.8)+32;
                temp[i].textContent=parseInt(farenheitResult) + "°";
            }
        }
        
}
