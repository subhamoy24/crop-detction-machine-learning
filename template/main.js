function validate(v){
    try{
        v=parseFloat(v)
        return 1
    }catch{
        return 0
    }
}
function validate1(ah){
    if(ah>=10 && ah<=100 ){
        return 1
    }else {
        return 0
    }
}
function validate2(at){
    if(at>=15 && at<54){
        return 1
    }else{
        return 0
    }

}
function validate3(ph){
    if(ph>=4.5 && ph<=9.5){
        return 1

    }else{
        return 0

    }

}
function validate4(rf){
    if(rf>=22 && rf<300){
        return 1
    
    }else{
        return 0

    }
}
function onclicksubmit(){
    var ah=document.getElementById("air_humidity").value
    var at=document.getElementById("air_temp").value
    var sp=document.getElementById("soil_ph").value
    var rf=document.getElementById("rain_fall").value
    var p1=validate(ah)
    var p2=validate(at)
    var p3=validate(sp)
    var p4=validate(rf)
    p1==0?document.getElementById("air_humidity").style.border="2px red solid":""
    p2==0?document.getElementById("air_temp").style.border="2px red solid":""
    p3==0?document.getElementById("soil_ph").style.border="2px red solid":""
    p4==0?document.getElementById("rain_fall").style.border="2px red solid":""

    if(p1==1 && p2==1 &&p3==1 && p4==1){
        ah=parseFloat(ah)
        at=parseFloat(at)
        sp=parseFloat(sp)
        rf=parseFloat(rf)
        p1=validate1(ah)
        p2=validate2(at)
        p3=validate3(sp)
        p4=validate4(rf)
        p1==0?document.getElementById("air_humidity").style.border="2px red solid":""
        p2==0?document.getElementById("air_temp").style.border="2px red solid":""
        p3==0?document.getElementById("soil_ph").style.border="2px red solid":""
        p4==0?document.getElementById("rain_fall").style.border="2px red solid":""
        if(p1==1 && p2==1 && p3==1 && p4==1){
            var formdata = new FormData();
            formdata.append("Air_Humidity", ah.toString() );
            formdata.append("Air_Temp",at.toString() );
            formdata.append("Soil_pH", sp.toString());
            formdata.append("Rainfall", rf.toString());

            var requestOptions = {
                method: 'POST',
                body: formdata,
                redirect: 'follow'
            };

            fetch("http://127.0.0.1:5000/pred", requestOptions)
            .then((response) => response.json())
            .then(function(data){
                console.log(data);
                //var p=data.predicted_crop
                document.getElementById('oi').innerHTML=`${data.predicted_crop}`;
            })
            .catch(error => console.log('error', error));

        }

    }else{
        return 
    }

}