import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((e, p, i) for i, (e, p) in enumerate(tasks))

        res = []
        heap = []             
        t = 0
        i = 0
        n = len(tasks)

        while i < n or heap:

            # Si aucune tâche n'est disponible,
            # avancer directement au prochain enqueueTime.
            if not heap:
                t = max(t, tasks[i][0])

            # Ajouter toutes les tâches disponibles.
            while i < n and tasks[i][0] <= t:
                enqueue, process, idx = tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            # Exécuter la tâche la plus courte.
            process, idx = heapq.heappop(heap)
            res.append(idx)
            t += process

        return res