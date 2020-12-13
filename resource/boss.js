
class Boss extends Manager {
    constructor(name, age, gender, skill, hobby, salary){
        super(name, age, gender, skill)
        this.hobby = hobby
        this.salary = salary
    }

    de = {'a': 3}
      test01 ( item )   {
        console.log("The boss...")
    }

    test_02 ( item, index )   {
        console.log("The boss...")
    }

    test03 (ok)   {
        console.log("The boss...")
    }

    test04 (ok,q)   {
        console.log("The boss...")
    }

    test05 ()   {
        console.log("The boss...")
    }

    test06  ()   {
        console.log("The boss...")
    }
}

const boss = new Boss(
    "don",
    {a: 18 },
    "male",
    ["es6","vue","react"],
    "study",
    "10k"
)

console.log(boss)

boss.desc()

boss.say()