impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut v: Vec<i32> = vec![nums[0]];
        let mut last: i32 = nums[0];
        for i in 1..nums.len() {
            if last != nums[i] {
                last = nums[i];
                v.push(nums[i]);
            }
        }
        for i in 0..v.len() {
            nums[i] = v[i];
        }
        v.len() as i32
    }
}

struct Solution;

fn main() {
    println!(
        "{}",
        Solution::remove_duplicates(&mut vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    );
}
