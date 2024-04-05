function valid(){
    var n=document.f1.first.value
    var a="^[A-Z]"
    var r=document.f1.second.value

    if(n[0]!=a){
        alert("enter name with capital letter")
        return false
       }
    if(r.length!=12){
        alert("enter full roll no")
        return false
    }
   
}