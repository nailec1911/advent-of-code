mod utils;
mod days;

use clap::Parser;

/// Advent of Code runner
#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Day number to run
    #[arg(short, long)]
    day: u8,
}

fn main() {
    let args = Args::parse();

    match args.day {
        1 => days::day01::run(),
        // 2 => days::day02::run(),
        _ => eprintln!("Day {} not implemented yet!", args.day),
    }
}
