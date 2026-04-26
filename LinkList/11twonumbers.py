class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SumClass:

    def addtwolinkedlist(head1, head2):

        temp1 = head1
        temp2 = head2

        dummy_node = Node(-1)
        current = dummy_node
        carry = 0

        while temp1 or temp2:

            total = carry

            if temp1:
                total += temp1.data
                temp1 = temp1.next

            if temp2:
                total += temp2.data
                temp2 = temp2.next

            new_node = Node(total % 10)
            carry = total // 10

            current.next = new_node
            current = current.next

        if carry:
            current.next = Node(carry)

        return dummy_node.next