from collections import deque
 
class MinQueue():
    ''' Implement a queue with min() function.
    '''
    def __init__(self):
        # all_data is used to store all the raw data for this queue.
        self.all_data = deque()
        # min_data is used to store the data for min() function. The values
        # in min_data is in non-decreasing order.
        self.min_data = deque()
        return
    
    def enqueue(self, val):
        self.all_data.append(val)
        
        while self.min_data and self.min_data[-1] > val:
            self.min_data.pop()
        self.min_data.append(val)
        
        return
    
    def dequeue(self):
        # Check if the queue is empty.
        if not self.all_data:   return None
        
        # The to-dequeue value is the minimum in current queue.
        if self.all_data[0] == self.min_data[0]:
            self.min_data.popleft()
        
        return self.all_data.popleft()
    
    def dequeue_all_if(self, cond):
        ''' Remove all heading values, if they satisfy the condition "cond".
        '''
        while self.all_data and cond(self.all_data[0]):
            self.dequeue()
        return
        
    def min(self):
        ''' Return the minimal item in current queue. min() is O(1).
        '''
        if self.min_data:       return self.min_data[0]
        else:                   return None
def solution(A, B, C):
    # Step 1: Clear all wrapper planks. If there are two planks A and B:
    #                      A.start <= B.start <= B.end <= A.end
    #         A is a wrapper plank to B.
    #    Step 1.1: all these planks having the same start point, remove the
    #              longer wrapper planks. The time complexity is O(N).
    
    # There are at most 2 * len(C) planks.
    # If plank_end_points[i] is not zero, there is a plank, starting at i,
    # and ending at plank_end_points[i].
    plank_end_points = [0] * (len(C) * 2 + 1)
    for index in  range(len(A)):
        if plank_end_points[A[index]] == 0:
            plank_end_points[A[index]] = B[index]
        elif plank_end_points[A[index]] > B[index]:
            # Replace with the new and shorter one.
            plank_end_points[A[index]] = B[index]
        else:
            # Keep the old and shorter one.
            pass
    
    #    Step 1.2: Remove all the other planks, who do not share the same start
    #              points. The time complexity is O(N), because every plank
    #              after step 1.1 will enter the stack "planks" once and may or
    #              may not exit the queue (once or never).
    
    # All position values are in range [1..2*M]. Therefore 0 is never used.
    planks = []     # Pairs of (begin, end), sorting with begin position.
    for index in  range(1, len(plank_end_points)):
        if plank_end_points[index] != 0:
            # Here is a plank.
            while planks and planks[-1][1] >= plank_end_points[index]:
                # Remove all the wrapper planks to current one.
                planks.pop()
            planks.append((index, plank_end_points[index]))
    
    del plank_end_points
    
    # Step 2: counting sort the nails, while removing the duplicate nails.
    #         The time complexity is O(M).
    
    # If nails[i] is zero, there is not any nail in this place. Otherwise, if
    # nails[i] = j, the j(th) nail in C is placed in the i position of the
    # board.
    nails = [-1] * (len(C) * 2 + 1)
    for index in  range(len(C)):
        if nails[C[index]] == -1:
            # If multiple nails hold the same position, we only keep the
            # earliest one.
            nails[C[index]] = index
    
    # Step 3: find the minimum number of nails that must be used until all the
    #         planks are nailed. The time complexity is O(N+M), because:
    #         a) Every plank after step 1 is checked once and only once; O(N)
    #         b) After step 2, the nails, who are on top of any plank from a),
    #            will be enqueued once and only once; otherwise, the remaining
    #            nails are never touched; O(M)
    #         c) The enqueued nails will dequeue once OR never dequeue. O(M)
    
    previous_plank = (0, 0)
    # The content in nails_queue is (nail order in C, nail position in board)
    # Nail order in C is used to compute min() function.
    # Nail position in board is determining when to enter and exit queue.
    nails_queue = MinQueue()
    result = (-1, -1)       # An impossible result as the initial value.
    
    for plank in planks:
        # Remove all nails before this planks.
        nails_queue.dequeue_all_if(lambda x: x[1] < plank[0])
        
        # Add all nails on this plank, if they are not in the queue.
        # When this plank is overlapping with the previous one, the nails
        # between plank[0] and previous_plank[1]] are already included in
        # queue.
        for index in  range(max(plank[0], previous_plank[1]), plank[1] + 1):
            if nails[index] != -1:
                # Enqueue value: (nail order, nail position)
                nails_queue.enqueue((nails[index], index))
        
        # Maybe there is no nail on this plank.
        if nails_queue.min() == None:       return -1
        
        # Find the earliest nail, which can fix this plank.
        result = max(result, nails_queue.min())
    
    return result[0] + 1
