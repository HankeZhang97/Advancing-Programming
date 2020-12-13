
class Employee {
    constructor(name, age, gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    desc () {
        console.log('Name: ' + this.name + ' +, age: ' + this.age + ', gender: ' + this.gender)
    }

    call () {
        console.log("The employee...")
    }
}