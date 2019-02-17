from array import array
# data type integer, 'i'


class ArrayQ:
    def __init__(self):
        self.__arr = array('i', [])        # privata variabler börjar med två understreck

    def enqueue(self, kort):
        self.__arr.append(kort)
        #print(self.__arr)

    def dequeue(self):
        return self.__arr.pop(0)
        #print(self.__arr)

    def isEmpty(self):
        [x, y] = self.__arr.buffer_info()
        return y == 0


if __name__ == '__main__':
    q = ArrayQ()       # Testkod för Array Q som inte körs eftersom modulen inte är huvudprogrammet
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if x == 1 and y == 2:
        print("Fungerar")
    else:
        print("Något är fel. 1 och 2 förväntades men vi fick", x, y)
