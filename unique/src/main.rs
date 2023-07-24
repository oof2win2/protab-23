use std::{collections::HashSet, io::stdin};

fn main() {
    let mut seen_lines = HashSet::new();

    let mut line = String::with_capacity(64);

    loop {
        match stdin().read_line(&mut line) {
            Ok(0) => {
                println!("done");
                break;
            }
            Ok(_) => {
                if seen_lines.contains(&line) {
                    line.clear();
                    continue;
                };
                seen_lines.insert(line.clone());
                println!("{}", &line);
                line.clear();
            }
            Err(e) => {
                println!("Error: {}", e);
                break;
            }
        }
    }

    println!("done");
}
