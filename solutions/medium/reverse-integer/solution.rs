impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut x_str = x.to_string();

        let is_negative = if x_str.chars().next() == Some('-') {
            x_str.remove(0);
            true
        } else {
            false
        };

        let reversed_x = x_str
            .chars()
            .rev()
            .collect::<String>()
            .parse::<i32>()
            .unwrap_or(0);

        if is_negative {
            -reversed_x
        } else {
            reversed_x
        }
    }
}
