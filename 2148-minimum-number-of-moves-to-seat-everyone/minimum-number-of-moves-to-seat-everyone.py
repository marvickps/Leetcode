class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        students.sort()
        seats.sort()
        count=0

        for i in range(len(students)):
            count = count + abs(students[i]-seats[i])
        return count

        
        

        