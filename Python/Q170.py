class Node:

    def __init__(self, val, ex = None, next = None):
        self.val = val
        self.ex = ex
        self.next = next



    def modify_ex(self, ex):
        self.ex = ex
    


    def modify_next(self, next):
        self.next = next



  

class TwoSum:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0



    def add(self, number: int) -> None:
        if(self.size == 0):
            self.head = self.tail = Node(number)
            self.size += 1

        else:
            if(number <= self.head.val):
                current_head = self.head
                self.head = Node(number, next = current_head)
                current_head.modify_ex(self.head)

            elif(number > self.tail.val):
                current_tail = self.tail
                self.tail = Node(number, ex = current_tail)
                current_tail.modify_next(self.tail)

            else:
                left = self.head
                right = left.next

                while(right.val < number):
                    left = right
                    right = left.next

                new = Node(number, ex = left, next = right)
                left.modify_next(new)
                right.modify_ex(new)


    
    def find(self, value: int) -> bool:
        
        left = self.head
        right = self.tail

        while(left != right):
            if(left.val + right.val == value):
                return True

            if(left.val + right.val < value):
                left = left.next
            else:
                right = right.ex

        return False

def main():
    order = ["TwoSum","add","add","find"]
    numbers = [[],[0],[0],[0]]

    obj = TwoSum()

    for i in range(1, len(order)):
        k = numbers[i][0]

        if(order[i] == "add"):
            obj.add(k)

        else:
            print(obj.find(k))


if __name__ == "__main__":
    main()