// let number = Number(prompt("enter number"))

// let sum = 0
// for(var i = 0; i <= number;i++){
//     if(i% 2 == 0){
//         sum+=i
//     }
// }
// console.log(sum)

// let list = [1,2,3,4,12,2,6,89]
// let sum = 0
// for(let i = 0;i < list.length;i++){
//     sum+=list[i]
// }
// console.log(sum)

let arr = [4,51,2,1,4,56,4,34,12,11]
let sum = 0
for(let i of arr){
    if(i% 2 == 0){
        sum += i**2
    }
}console.log(sum)