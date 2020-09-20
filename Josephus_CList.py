class CList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0
    
    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        n = self.Node(item, None)
        
        if self.is_empty():
            n.next = n # 새로운 노드 n의 next가 자기 자신을 가리키도록 한다.
            self.last = n # n이 last 노드가 된다. (사각형)

        else: # !!순서가 바뀌면 새로 들어온 노드가 자기를 가리킨다.
            n.next = self.last.next  # 새로운 노드의 다음이 last가 가리키고 있던 곳을 가리키도록 한다.
            self.last.next = n  # last가 새로운 노드를 가리키도록 바뀐다. (화살표)
            self.last = n # 새로운 노드가 last가 된다. (사각형)
        
        self.size += 1
    
    def pop(self, k):
        if self.is_empty():
            print("리스트가 비어있습니다.")

        else:
            t = self.last # t는 마지막에 들어온 노드가 된다. ex) 7
            print("<", end='')

            while self.size != 1: # 사이즈가 1이 될 때 까지 진행한다.
                for _ in range(k-1): # 입력한 k에서 -1을 한 만큼 last를 이동한다. ex) 2만큼 이동
                    t = t.next # 7 -> 1 -> 2 : last노드는 2가 된다.

                print(f"{t.next.item}, ", end='') #그 라스트 노드의 다음 노드가 가진 item을 출력한다. 3

                t.next = t.next.next # 출력한 노드의 연결을 끊는다.
                self.size -= 1

            print(f"{t.item}>")

    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')

        else:
            chk = self.last.item # 7
            f = self.last.next # 1부터 시작

            while f.item != chk: # 1부터 차례대로 출력할 것인데 노드의 item이 7이라면 pass한다. 화살표 예쁘게 그릴려고
                print(f"{f.item} -> ", end='')
                f = f.next

            print(chk)


s = CList()

n, k = map(int, input().split())

for i in range(1, n+1):
    s.insert_front(i)

s.pop(k)