use std::fs;

pub fn read_input(day: u8) -> String {
    let filename = format!("inputs/day{:02}.txt", day);
    fs::read_to_string(filename).expect("Failed to read input file")
}

pub fn split_lines(input: &str) -> Vec<&str> {
    input.lines().collect()
}
