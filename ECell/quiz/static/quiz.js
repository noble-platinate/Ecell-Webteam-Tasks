document.addEventListener('DOMContentLoaded', () => 
{
    setInterval(count, 1000);
});

let qorder = (Math.floor(Math.random()*10))%4;

let counter = 120,score=0;
function count() 
{
    counter--;
    if (counter < 0) 
    {
        alert(`Time up! Score: ${score}`)
    }
    document.querySelector('.card-title').innerHTML = "Time left: " + counter;
}


document.querySelector('.submit').onclick= function() 
{
    alert(`You submitted, score: ${score}`)
    let qorder = (Math.floor(Math.random()*10))%4;
    location.href="http://127.0.0.1:8000/quiz"
}


let i=0;

function quiz_question()
{
    questions=[
        [["A fruit starting with A is: "],["apple","orange","banana","grapes"]],
    [["Earth has how many moons"],["1","2","3","4"]],
    [["How many states are there in India?"],["29","25","15","30"]],
    [["Which one is vowel?"],["a","b","c","d"]],
    [["Which one is consonant?"],["z","a","e","i"]],
    [["Which one is prime number?"],["2","4","6","8"]],
    [["Which one is composite number?"],["4","2","3","5"]],
    [["Which one is even number?"],["2","3","5","7"]],
    [["Which one is odd number?"],["3","4","6","8"]],
    [["Which word doesn't exist?"],["abcd","ball","cat","dog"]],
    [["Which word does exist?"],["apple","bcde","cdef","defg"]]];
    list1=[[0,1,2,3],[1,2,3,0],[2,3,0,1],[3,0,1,2]];
    list2=[[0,7,8,9,10],[2,4,1,6,5],[1,2,3,4,5],[3,4,1,2,9]];

    list=list2[qorder];
    random = (Math.floor(Math.random()*10))%4;
    document.querySelector('#question').innerHTML=questions[list[i]][0];
    document.querySelector('.option1').innerHTML=questions[list[i]][1][list1[random][0]];
    document.querySelector('.option2').innerHTML=questions[list[i]][1][list1[random][1]];
    document.querySelector('.option3').innerHTML=questions[list[i]][1][list1[random][2]];
    document.querySelector('.option4').innerHTML=questions[list[i]][1][list1[random][3]];
}
let countmax=0;
quiz_question()
document.querySelector('.form-check-input').onclick = function() {}
document.querySelector('.next').onclick = function()
{
    i++;
    if(document.getElementById('0').checked)
        {
            if((list1[random][0]==0))
            {score+=10;}

        }
    else if(document.getElementById('1').checked)
    {
        if((list1[random][1]==0))
        {score+=10;}

    }
    else if(document.getElementById('2').checked)
    {
        if((list1[random][2]==0))
        {score+=10;}

    }
    else if(document.getElementById('3').checked)
    {
        if((list1[random][3]==0))
        {score+=10;}

    }
    (document.getElementById('0').checked)=false;
    (document.getElementById('1').checked)=false;
    (document.getElementById('2').checked)=false;
    (document.getElementById('3').checked)=false;
    console.log(score);
    if (i==5)
    {
        alert(`You Finished, score: ${score}`);
        location.href="http://127.0.0.1:8000/quiz"
        let qorder = (Math.floor(Math.random()*10))%4;
    }
    quiz_question();
}




