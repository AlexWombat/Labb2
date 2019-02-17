from linkedQFile import LinkedQ
#from arrayQfile import ArrayQ


def main():
    a = input('Vilken ordning ligger korten i?')
    b = a.split()
    for i in b:
        if int(i)>13:
            return print('Värdet på kortet kan ej överstiga 13.')
    #q = ArrayQ()
    q = LinkedQ()
    for i in b[1::2]:
        q.enqueue(int(i))
    for i in b[0::2]:
        q.enqueue(int(i))
    if q.isEmpty() is True:
        print('Du måste mata i några kort för att beskåda magin.')
    else:
        right_order = []
        for i in range(len(b)):
            right_order.append(q.dequeue())
        print('Korten kommer ut i denna ordning:')
        for i in right_order:
            print(i, end=' ')


main()






