class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

function addTwoNumbers(
    l1: ListNode | null | undefined,
    l2: ListNode | null | undefined,
): ListNode | null {
    const arr1: number[] = [];
    const arr2: number[] = [];

    for (let i: number = 0; ; i++) {
        arr1.push(l1?.val as number);
        l1 = l1?.next;
        if (l1 == null) break;
    }
    for (let i: number = 0; ; i++) {
        arr2.push(l2?.val as number);
        l2 = l2?.next;
        if (l2 == null) break;
    }

    const arr3: number[] = [arr1, arr2]
        .map((arr: number[]): bigint => BigInt(arr.reverse().join("")))
        .reduce((a: bigint, b: bigint): bigint => a + b, BigInt(0))
        .toLocaleString("fullwide", { useGrouping: false })
        .split("")
        .reverse()
        .map((s: string): number => parseInt(s));

    let l3: ListNode = new ListNode();
    l3.val = arr3[0];
    console.log(arr3);
    let answer: ListNode = l3;

    for (let i: number = 1; i < arr3.length; i++) {
        l3.next = new ListNode(arr3[i]);
        l3 = l3.next;
    }

    return answer;
}
