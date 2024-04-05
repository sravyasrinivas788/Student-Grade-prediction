function check(){
    var a =document.f2.age.value
    var b=document.f2.Medu.value
    var c=document.f2.Fedu.value
    var d=document.f2.traveltime.value
    var e=document.f2.studytime.value
    var f=document.f2.failures.value
    var g=document.f2.famrel.value
    var h=document.f2.freetime.value
    var i=document.f2.goout.value
    var j=document.f2.Dalc.value
    var k=document.f2.Walc.value
    var l=document.f2.health.value
    var m=document.f2.absences.value
    var g1 =document.f2.G1.value
    var g2=document.f2.G2.value
    if(a<15 ||a>21){
        alert("enter age between 15 and 22")
        return false
    }
    if(b>4){
        alert("enter valid values")
        return false
    }
    if(c>4){
        alert("enter valid values")
        return false
    }
    if(d>4){
        alert("enter valid values")
        return false
    }
    if(e>4){
        alert("enter valid values")
        return false
    }
    if(f>4){
        alert("enter 4 as number of failures")
        return false
    }
    if((g || h||i||j||k||l)>5){
        alert("enter values between 1 and 5")
        return false
    }
    if(m>93){
        alert("enter valid value")
    }
    if(g1>20){
        alert("enter valid marks")
    }
    if(g2>20){
        alert("enter valid marks")
    }




}