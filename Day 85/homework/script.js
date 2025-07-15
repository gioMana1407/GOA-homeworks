let greeting = `Hello World!`;
let newGreeting = `${greeting}`;

console.log(newGreeting);


let თვე = prompt("შეიყვანე შენი საყვარელი თვე: იანვარი, მარტი, მაისი, აგვისტო ან დეკემბერი");

switch (თვე) {
  case "იანვარი":
    alert("ეს არის ზამთარი");
    break;

  case "მარტი":
    alert("ეს არის გაზაფხული");
    break;

  case "მაისი":
    alert("ეს არის გაზაფხული");
    break;

  case "აგვისტო":
    alert("ეს არის ზაფხული");
    break;

  case "დეკემბერი":
    alert("ეს არის ზამთარი");
    break;

  default:
    alert("შეიყვანე მხოლოდ შემდეგი თვეებიდან ერთი: იანვარი, მარტი, მაისი, აგვისტო ან დეკემბერი");
}


    let age = 19;

    let result = (age > 18) ? "Adult" : "Minor";

    console.log(result);



    let now = new Date();

    let year = now.getFullYear();       
    let month = now.getMonth() + 1;     
    let date = now.getDate();           
    let day = now.getDay();           
    let hour = now.getHours();          
  
    let text = `წელი: ${year} <br> თვე: ${month} <br> დღე კვირაში: ${day} <br> რიცხვი: ${date} <br> საათი: ${hour}:00`;

   
    document.getElementById("dateInfo").innerHTML = text;