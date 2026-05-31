function maxStrength(nums: number[]): number {
    if (nums.length === 1) {
        return nums[0];
    }

    let positives: number[] = nums.filter((n: number): boolean => n > 0);
    let negatives: number[] = nums
        .filter((n: number): boolean => n < 0)
        .map((n: number): number => -1 * n);

    let curr: number =
        positives.length === 0 && negatives.length <= 1
            ? 0
            : positives.reduce((b: number, i: number): number => b * i, 1);

    if (negatives.length % 2 === 0) {
        return curr * negatives.reduce((b: number, i: number): number => b * i, 1);
    }

    negatives.splice(negatives.indexOf(Math.min(...negatives)), 1);

    return curr * negatives.reduce((b: number, i: number): number => b * i, 1);
}
