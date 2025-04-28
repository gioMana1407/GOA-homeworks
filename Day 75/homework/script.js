// function checkCondition(condition) {
//     if (condition === "good" || condition === "bad") {
//         console.log(`Car is in ${condition} condition.`)
//     } else {
//         console.log("Condition is unknown.")
//     }
// }

// let car = {
//     company: "Toyota",
//     model: "Corolla",
//     milage: 150000,
//     year: 2015,
//     condition: "good",
//     checkCondition: checkCondition
// }


// car.checkCondition(car.condition)

// car.color = "red"
// car.price = 10000
// delete car.milage

// console.log(car)
// let user = {
//     name: "გიორგი",
//     age: 18,
//     email: "giorgi@125.com",
//     city: "თბილისი"
// }

// for (let key in user) {
//     console.log(key + ": " + user[key])
// }

let student = {
    fullName: "luka pitnava",
    scores: [85, 90, 78, 92, 88],
    averageScore: function () {
        let sum = 0
        for (let i = 0; i < this.scores.length; i++) {
            sum += this.scores[i]
        }
        return sum / this.scores.length
    },
    checkStudent: function () {
        let avg = this.averageScore()
        if (avg > 90) {
            console.log("საუკეთესო სტუდენტი")
        } else if (avg > 60) {
            console.log("კარგი მოსწავლე")
        } else {
            console.log("ნორმალური მოსწავლე")
        }
    }
}
student.checkStudent()