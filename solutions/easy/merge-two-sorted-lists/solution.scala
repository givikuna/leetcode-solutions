import scala.util.control.Breaks._

class ListNode(_x: Int = 0, _next: ListNode = null) {
    var next: ListNode = _next
    var x: Int = _x
}

object Solution {
    def mergeTwoLists(list1: ListNode, list2: ListNode): ListNode = {
        var curr1: ListNode = list1
        var curr2: ListNode = list2
        var head: ListNode = null
        var curr: ListNode = head

        var isFirst: Boolean = true;

        if curr1 == null then return curr2
        else if curr2 == null then return curr1
        else {
            breakable {
                while (curr1 != null || curr2 != null) {
                    if (curr1 == null) {
                        curr.next = curr2
                        break()
                    }
                    if (curr2 == null) {
                        curr.next = curr1
                        break()
                    }
                    if (isFirst) {
                        head = if (curr1.x <= curr2.x) curr1 else curr2
                        curr = head
                    }
                    if (curr1.x <= curr2.x) {
                        if !isFirst then curr.next = curr1
                        curr1 = curr1.next
                    } else {
                        if !isFirst then curr.next = curr2
                        curr2 = curr2.next
                    }
                    if !isFirst then curr = curr.next
                    isFirst = false
                }
            }
        }

        head
    }
}
