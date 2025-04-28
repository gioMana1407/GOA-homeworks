let Myinfo = {
    name : "giorgi",
    surname : "manashvili",
    age : 18,
    hobby : "watching movies",
    greet(){
        console.log("hello")
    }
}
// console.log(Myinfo["name"])
// console.log(Myinfo["surname"])
// console.log(Myinfo["age"])
// console.log(Myinfo["hobby"])

// Myinfo.group = "group 50"

// let info = {
//     welcome(){
//         console.log(hello)
//     }
// }


// let Myname = prompt("enter name")
// let Mysurname = prompt("enter surname")
// let Myage = prompt("enter age")
// let Myhobby = prompt("enter hobby")

// info.name = Myname
// info.surname = Mysurname
// info.age = Myage
// info.hobby = Myhobby

console.log(Object.values(Myinfo))
console.log(Object.keys(Myinfo))