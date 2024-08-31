function twoSum(nums: number[], target: number): number[] {
    for (let i: number = 0; i < nums.length; i++) {
        for (let j: number = 0; j < nums.length; j++) {
            if (nums[i] + nums[j] === target && i !== j) {
                return [i, j];
            }
        }
    }
    return [];
}
