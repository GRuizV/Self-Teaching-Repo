import random
import Queues_Implementation


'Regular Queues'

'   Queue based on circular implementation'
# my_queue = Queues_Implementation.MyQueue(size = 5)
# [my_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# my_queue.display()
# print()


# my_queue.enqueue('X')
# print()

# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')


# my_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')


# my_queue.enqueue('X')
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')


# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')


# my_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')




'   Queue based on circular implementation'

# my_queue = Queues_Implementation.ListQueue()
# [my_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# # my_queue.display()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}')
# print(f'Queue rear: {my_queue.queue[-1]}')
# print(f'Queue as att.: {my_queue.queue}')


# my_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}')
# print(f'Queue rear: {my_queue.queue[-1]}')
# print(f'Queue as att.: {my_queue.queue}')


# my_queue.enqueue('X')
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}')
# print(f'Queue rear: {my_queue.queue[-1]}')
# print(f'Queue as att.: {my_queue.queue}')



# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}')
# print(f'Queue rear: {my_queue.queue[-1]}')
# print(f'Queue as att.: {my_queue.queue}')



# my_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}' if not my_queue.is_empty() else None)
# print(f'Queue rear: {my_queue.queue[-1]}' if not my_queue.is_empty() else None)
# print(f'Queue as att.: {my_queue.queue}')





'Circular Queue'

# cir_queue = Queues_Implementation.MyCircularQueue(size = 5)

# # [cir_queue.enqueue(random.randint(0,5)) for _ in range(5)]
# [cir_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# # cir_queue.display()
# print()


# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# cir_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# cir_queue.enqueue('X')
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# cir_queue.enqueue('X')
# print()


# cir_queue.dequeue()
# cir_queue.dequeue()
# cir_queue.dequeue()
# cir_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# cir_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# [cir_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# print()



# cir_queue.enqueue('X')
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')





'Priority Queue'

# pr_queue = Queues_Implementation.MyPriorityQueue()

# # [pr_queue.enqueue(elem, priority = random.randint(1,4)) for elem in 'WXYZ']
# [pr_queue.enqueue(*elem) for elem in [('Z', 4), ('X', 3), ('Y', 1), ('W', 2)]]

# # pr_queue.display()




# print(f'Queue:', end=' ')
# pr_queue.display()
# print(f'Queue front: {pr_queue.queue[0]}')
# print(f'Queue rear: {pr_queue.queue[-1]}')
# print(f'Queue as att.: {pr_queue.queue}')


# pr_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# pr_queue.display()
# print(f'Queue front: {pr_queue.queue[0]}')
# print(f'Queue rear: {pr_queue.queue[-1]}')
# print(f'Queue as att.: {pr_queue.queue}')


# pr_queue.enqueue('A',5)
# pr_queue.enqueue('B',5)
# pr_queue.enqueue('Z',3)
# pr_queue.enqueue('D',1)
# pr_queue.enqueue('Z',3)
# print()


# print(f'Queue:', end=' ')
# pr_queue.display()
# print(f'Queue front: {pr_queue.queue[0]}')
# print(f'Queue rear: {pr_queue.queue[-1]}')
# print(f'Queue as att.: {pr_queue.queue}')



# pr_queue.dequeue()
# pr_queue.dequeue()
# pr_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# pr_queue.display()
# print(f'Queue front: {pr_queue.queue[0]}')
# print(f'Queue rear: {pr_queue.queue[-1]}')
# print(f'Queue as att.: {pr_queue.queue}')



# pr_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# pr_queue.display()
# print(f'Queue front: {pr_queue.queue[0]}' if not pr_queue.is_empty() else None)
# print(f'Queue rear: {pr_queue.queue[-1]}' if not pr_queue.is_empty() else None)
# print(f'Queue as att.: {pr_queue.queue}')





'Deque'


# deque = Queues_Implementation.MyDeque()

# # [deque.enqueue_right(random.randint(1,10)) for _ in range(5)]
# [deque.enqueue_right(elem) for elem in  [2, 1, 5, 7, 9]]
# # deque.display()


# print(f'Queue:', end=' ')
# deque.display()
# print(f'Queue front: {deque.queue[0]}')
# print(f'Queue rear: {deque.queue[-1]}')
# print(f'Queue as att.: {deque.queue}')


# deque.enqueue_left('X')
# print()


# print(f'Queue:', end=' ')
# deque.display()
# print(f'Queue front: {deque.queue[0]}')
# print(f'Queue rear: {deque.queue[-1]}')
# print(f'Queue as att.: {deque.queue}')


# deque.dequeue_right()
# print()


# print(f'Queue:', end=' ')
# deque.display()
# print(f'Queue front: {deque.queue[0]}')
# print(f'Queue rear: {deque.queue[-1]}')
# print(f'Queue as att.: {deque.queue}')


# deque.dequeue_left()
# print()


# print(f'Queue:', end=' ')
# deque.display()
# print(f'Queue front: {deque.queue[0]}')
# print(f'Queue rear: {deque.queue[-1]}')
# print(f'Queue as att.: {deque.queue}')


# deque.dequeue_left()
# deque.dequeue_right()
# deque.dequeue_left()
# deque.dequeue_right()
# print()


# print(f'Queue:', end=' ')
# deque.display()
# print(f'Queue front: {deque.queue[0]}' if not deque.is_empty() else None)
# print(f'Queue rear: {deque.queue[-1]}' if not deque.is_empty() else None)
# print(f'Queue as att.: {deque.queue}')




















