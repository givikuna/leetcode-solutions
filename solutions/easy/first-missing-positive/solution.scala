object Solution {
    def firstMissingPositive(nums: Array[Int]): Int = {
        if (nums.length == 0) {
            return 1
        }

        var l: Int = nums.length
        println(l)
        var arr: Array[Int] = nums.filter(num => num > 0 && num < l)

        var i: Int = 0
        while (i < arr.length) {
                var temp: Int = arr(arr(i) - 1)
                arr(arr(i) - 1) = arr(i)
                arr(i) = temp
                i += 1
        }

        i = 1
        while (i < arr.length) {
            if (arr(i) != i) {
                return i
            } else {
                i += 1
            }
        }

        return i + 1
    }
}
