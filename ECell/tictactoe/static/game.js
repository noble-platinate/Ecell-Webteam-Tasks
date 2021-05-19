let list = ["a","b", "c", "d", "e", "f","g", "h","i"]
let k=0;
function symbol(k)
{
    if (k%2==0)
    {
        return "x";
    }
    return "o";
}

function check()
{
    winning_conditions=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6]];
    let data = document.querySelectorAll(".cell");
    console.log(data);
    for (let i = 0; i <9;i++)
    {
        list[i]=data[i].innerHTML;
    }
    
    for (let i = 0; i <8;i++)
    {
        let a = (list[winning_conditions[i][0]]);
        let b = (list[winning_conditions[i][1]]);
        let c = (list[winning_conditions[i][2]]);
        if ((a=='x') && (b=='x') && (c=='x'))
        {
            return 1;
        }
        if ((a=='o') && (b=='o') && (c=='o'))
        {
            return 2;
        }
    }
    return 3;
}

function clearall()
{
    document.querySelectorAll(".cell").forEach(function(cell) 
    {
        cell.innerHTML="";
    })
}
document.querySelectorAll(".cell").forEach(function(cell) {cell.addEventListener('click', function(cell)
{
    if ((this.innerHTML != 'o') && (this.innerHTML != 'x'))
    {
        if ((k%2)==0)
        {
            this.style.color = "blue";
        }
        else
        {
            this.style.color = "red";
        }
        this.innerHTML = symbol(k++);
    }
    let winner=check();
    if (winner==1)
    {
        alert("X won!")
        k=0;
        clearall();
    }
    if (winner==2)
    {
        alert("O won!")
        k=0;
        clearall();
    }
    if (k===9)
    {
        alert("It is tie!");
        k=0;
        clearall();
    }
})})


document.querySelector('#restart').onclick= function() 
{
    k=0;
    clearall();
}

document.querySelector('h5').onclick= function() {
    location.href="http://127.0.0.1:8000/"
}