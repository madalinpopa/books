// RULE 1: In rust a piece of data can have only 1 owner
// RULE 2: It is important to know where the data it is stored to identity the ownership: Stack or Heap
// RULE 3: The data in stack is copied automatically, the data in heap is not

fn main() {
    // name is the owner of string "Madalin"
    // the string is stored in heap
    let name: String = String::from("Madalin");

    // here you have two options: deap copy or return the ownership

    // OPTION 1: Copy the value from the main owner
    // say_hi(name);

    // OPTION 2: Return the ownership
    // at this point there is a move of the ownership
    let message = say_hello(name);
    println!("Hello {}", message);

    // Here we use the OPTION 2 but we change
    let new_name = change_name(message);
    println!("The new name is {}", new_name);
}

fn say_hello(name: String) -> String {
    println!("Hello {}", name);
    name
}

fn say_hi(name: String) {
    let new_name: String = name.clone();
    println!("Hi, {}", new_name)
}

fn change_name(mut name: String) -> String {
    name.push_str(" Popa");
    println!("The {} was changed", name);
    name
}
