function noop() {}

function maxStrength(nums: number[]): number {
    let positive: number = 0;
    let negative: number = 0;

    for (let i: number = 0; i < nums.length; i++) {
        if (nums[i] < 0) negative = negative === 0 ? nums[i] : negative * nums[i];
        else if (nums[i] > 0) positive = positive === 0 ? nums[i] : positive * nums[i];
        else noop();
    }

    return 0;
}
