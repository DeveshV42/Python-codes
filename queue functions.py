def isempty(queue):
    if not queue:
        return True
    else:
        return False


def enqueue(queue,n):
    queue.append(n)
    return queue

def dequeue(queue):
    if isempty(queue):
     print("queue is empty")
    return False
    
queue=[]
print(queue)
enqueue(queue,2)
enqueue(queue,3)
enqueue(queue,4)
print(queue)

#dequeue(queue)
#dequeue(queue)
#dequeue(queue)
#print(queue)
