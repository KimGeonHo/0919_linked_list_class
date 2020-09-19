print(s.print_list())



class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0 # 사이즈가 0이면 비어있다! 리턴

    def insert_front(self, item):
        if self.is_empty(): # 만약 비어있다면
            self.head = self.Node(item, None) # 헤드에 새 노드를 참조시킨다.
        else:
            self.head = self.Node(item, self.head) # 처음 self.head는 head가 새로 가리킬 node를 의미
                                                # 두번째 self.head는 처음에 head가 가리키고 있던 Node. 즉 새로운 노드가 기존에 맨 앞 노드를 가리킨다.
        self.size += 1

    def insert_after(self, item, p): # p가 가르키는 노드 다음에 새로운 노드를 추가하겠다.
        p.next = self.Node(item, p.next) # p는 s.head.next.next... 이런식으로 입력 받아진다.
        # self.head.next = self.Node(item, self.head.next)
        self.size += 1
    
    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p): # p = s.head.next....
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            p.next = p.next.next
            self.size -= 1
    
    def search_index(self, target): # target = 'apple'
        t = self.head
        for i in range(self.size):
            if t.item == target:
                return i
            else:
                t = t.next
        return None

    def print_list(self):
        p = self.head
        
        while p:
            if p.next != None:
                print(p.item + " -> ", end='')
            else:
                print(p.item)
            p = p.next

class EmptyError(Exception):
    pass


s = SList()
s.insert_front('apple')
s.insert_front('orange')
s.insert_front('banana')
s.print_list()
s.insert_after('kiwii', s.head.next)
print("키위를 오렌지 뒤에 삽입: ", end='')
s.print_list()
s.delete_after(s.head.next)
print("키위 삭제: ", end='')
s.print_list()
print(s.search_index('apple'))