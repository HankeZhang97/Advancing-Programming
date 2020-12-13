
class Manager extends Employee{
    constructor(name, age, gender, skill){
        super(name, age, gender)
        this.skill = skill
    }

    say(){
        console.log(this.skill.join(", "))
    }
}

const manager = new Manager(
    "don",
    18,
    "male",
    ["es6","vue","react"]
)

console.log(manager)

manager.desc()

manager.say()