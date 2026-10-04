class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.map = {}

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            self._add_to_tail(node)
            if len(self.map) > self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.map[lru.key]
