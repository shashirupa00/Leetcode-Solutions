class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        res = sum(abs(student - seat) for student, seat in zip(students, seats))

        return res