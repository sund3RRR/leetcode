class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if isinstance(other, list):
            current = self
            i = 0
            while current is not None and i < len(other):
                if current.val != other[i]:
                    return False
                current = current.next
                i += 1
            return current is None and i == len(other)
        return NotImplemented

    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return "ListNode([" + ", ".join(values) + "])"

    @classmethod
    def from_list(cls, lst):
        if not lst:
            return None
        head = cls(lst[0])
        current = head
        for val in lst[1:]:
            current.next = cls(val)
            current = current.next
        return head
