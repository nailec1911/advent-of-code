use crate::utils::read_input;

pub fn run() {
    let input = read_input(1);

    let mut current = 0;
    let mut pos = 0;

    for (idx, c) in input.trim().chars().enumerate() {
        current += match c {
            '(' => 1,
            ')' => -1,
            _ => 0,
        };
        if current < 0 && pos == 0{
            pos = idx + 1;
        }
    }
    println!("Part 1: {}", current);
    println!("Part 2: {}", pos);
}
