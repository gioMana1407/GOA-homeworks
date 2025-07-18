function me(name, age) {
  this.name = name;
  this.age = age;

  this.introduce = function() {
    console.log("Hi, my name is " + this.name + " and I am " + this.age + " years old.");
  };

  this.getName = function() {
    return this.name;
  };

  this.setName = function(newName) {
    this.name = newName;
  };

  this.getAge = function() {
    return this.age;
  };

  this.setAge = function(newAge) {
    this.age = newAge;
  };
}

var person1 = new Human("gio", 18);
person1.introduce(); 

console.log(person1.getName());
person1.setName("giorgi");
console.log(person1.getName()); 

person1.setAge(19);
person1.introduce();
