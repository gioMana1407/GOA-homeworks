// let UserNumber = Number(prompt("enter number"))
// let i = 1
// while(i < UserNumber ){
//     if(i % 3 == 0 && i % 5 == 0){
//         console.log(i)
        
//     }
//     i ++
// }

let UserNum = Number(prompt("enter num"))
let userChoice = prompt("even||odd||cube||3x")
let i = 1
while(i < UserNum){
    if(i % 2 == 0 && userChoice == "even"){
        console.log(i)
    }else if(i % 2 == 1 && userChoice == "odd"){
        console.log(i)
    }else if(userChoice == "cube"){
        console.log(i ** 2)
    }else if(i % 3 == 0 && userChoice == "3x"){
        console.log(i)
    }
    i ++
}