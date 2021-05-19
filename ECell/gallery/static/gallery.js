var modal = document.getElementById("myModal");

var img = document.getElementsByClassName("card-img-top");
var modalImg = document.getElementById("img01");

function check(index)
{
  if (index==(0))
  {
    index=7;
  }
  if (index==8)
  {
    index=0;
  }
  return index;
}
for (let index = 0; index < img.length; index++) 
{
    const element = img[index];
    element.onclick = function(){modal.style.display = "block"; modalImg.src = this.src; 
  
    next.onclick = function(func) 
      {
        modal.style.display = "block";
        index=check(index+1);
        modalImg.src = img[index].src;
        func()
      }
    previous.onclick = function(func) 
    {
      modal.style.display = "block";
      index=check(index-1);
      modalImg.src = img[index].src;
      func()
    }
}
    
}


var span = document.getElementsByClassName("close")[0];
var next = document.getElementsByClassName("next")[0];
var previous = document.getElementsByClassName("previous")[0];

span.onclick = function() { 
  location.href=" "
}

document.querySelector('h2').onclick= function() {
    location.href="http://127.0.0.1:8000/gallery/"
}