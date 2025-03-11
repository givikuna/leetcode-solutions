class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []
        for c in s {
            switch c {
                case "(":
                    stack.append(")")
                    break
                case "[":
                    stack.append("]")
                    break
                case "{":
                    stack.append("}")
                    break
                case ")", "]", "}":
                    if stack.count == 0 || stack.last != c {
                        return false
                    } else {
                        stack.popLast()
                    }
                default:
                    return false
            }
        }
        return stack.count == 0 ? true : false
    }
}
