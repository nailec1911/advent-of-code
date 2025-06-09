use crate::utils::{read_input, split_lines};

pub fn run() {
    let input = read_input(2);
    let input = split_lines(&input);

    let mut surface = 0;
    let mut ribbon = 0;

    for line in input.iter() {
        let dims: Vec<u32> = line
            .split('x')
            .map(|s| s.parse::<u32>().expect("Invalid integer"))
            .collect();
        let [l, w, h]: [u32; 3] = dims.try_into().expect("Expected 3 dimensions");
        let mut sides = [l, w, h];
        sides.sort();
        let areas = [l * w, w * h, h * l];

        let surface_area = 2 * areas.iter().sum::<u32>();
        let smallest_side = areas.iter().min().unwrap();

        ribbon += 2*sides[0] + 2*sides[1] + l*w*h;
        surface += surface_area + smallest_side;
    }

    println!("Part 1: {}", surface);
    println!("Part 2: {}", ribbon);
}
