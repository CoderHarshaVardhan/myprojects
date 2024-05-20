let userScore = 0;
let compScore = 0;

let userChoice;
let compChoice;

playGame = () =>{
    let choices = ["rock" , "paper", "scissors"];
    let index = Math.floor(Math.random() * 3);
    compChoice = choices[index];
}

checkWinner = () =>{
    if(userChoice===compChoice){
        console.log("Draw");
        let msg = document.querySelector("#msg");
        msg.innerText = "Draw";
        msg.style.backgroundColor = "#081b31";
    }else {
        let userWin = true;
        if(userChoice === "rock"){
        userWin = compChoice==="paper"? false:true;
    }else if(userChoice === "paper"){
        userWin = compChoice === "scissors"? false:true;
    }else if(userChoice === "scissors"){
        userWin = compChoice === "rock"? false:true;
    }
    showWinner(userWin);
}
}

showWinner = (userWin) =>{
    let msg = document.querySelector("#msg");
    if(userWin){ 
        console.log("you win....");
        msg.innerText = "You win.....";
        msg.style.backgroundColor = "green";
        let us = document.querySelector("#user-score");
        userScore++;
        us.innerText = userScore;
    }else{
        console.log("computer win....");
        msg.innerText = "you lose.....";
        msg.style.backgroundColor = "red";
        let cs = document.querySelector("#comp-score");
        compScore++;
        cs.innerText = compScore;
    }
}

let choices = document.querySelectorAll(".choice");

choices.forEach(
    (choice)=>{
        choice.addEventListener("click",()=>{
            userChoice = choice.getAttribute("id");
            playGame();
            checkWinner();
        })
    }
);


