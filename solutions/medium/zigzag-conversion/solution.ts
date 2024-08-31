function convert(s: string, numRows: number): string {
    if (numRows === 1 || numRows >= s.length) {
        return s;
    }

    const arr: string[] = ((l: number): string[] => {
        const xs: string[] = [];
        for (let i: number = 0; i < l; i++) {
            xs.push("");
        }
        return xs;
    })(numRows);
    let i: number = 0;
    let starter: number = numRows;
    for (let j: number = 0; j < s.length; j++) {
        if (starter === numRows) {
            arr[i] += s[j];
            i += 1;
            if (i === numRows) {
                starter -= 1;
                i = starter;
            }
        } else {
            if (starter === 1) {
                i = 1;
                starter = numRows;
                arr[0] += s[j];
            } else {
                arr[starter - 1] += s[j];
                starter -= 1;
            }
        }
    }
    return arr.join("");
}
