function reverse(x: number): number {
    if (x === 0) return x;
    const num: number = parseInt(x.toString().replace(/0+$/, "").split("").reverse().join(""), 10);
    if (num > Math.pow(2, 31) - 1 || -num < Math.pow(-2, 31)) return 0;
    if (x < 0) return -num;
    return num;
}
