# thread.pyの実装で、余計なブロックは発生しないのか
# 結論、する・・かと思いきや、この例だとスレッドが1個しかないじゃん

# A Python example doing parallel sorting
# of the nodes of a DAG in topological order

import threading
import queue
from graphlib import TopologicalSorter
import time
from datetime import datetime

# The queues
workQueue = queue.Queue()
doneQueue = queue.Queue()

# Worker thread function


def worker():
    while True:
        workPiece = workQueue.get()
        print(datetime.now(), f"start {workPiece}")
        time.sleep(workPiece)
        workQueue.task_done()
        doneQueue.put(workPiece)


# Create and start the worker thread
threading.Thread(target=worker, daemon=True).start()

# Define a workflow as a DAG using a Python dictionary
workflow = {
    4: [1],
    5: [2],
    6: [3]
}
topologicalSorter = TopologicalSorter(workflow)
topologicalSorter.prepare()

# Loop till the workflow is alive
while topologicalSorter.is_active():
    # Get a piece of work that is ready for execution
    for workPiece in topologicalSorter.get_ready():
        workQueue.put(workPiece)

    # Mark the completed workpiece as done
    node = doneQueue.get()
    topologicalSorter.done(node)
    print(node)

# Wait for the worker thread to complete
workQueue.join()

print(topologicalSorter.is_active())
