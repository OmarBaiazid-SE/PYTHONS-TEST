# One of the simple challenges I faced was the gravity test where you are given a matrix and you have to consider each number as a cube and you have to move the big cube to the end and the small cube to the beginning. The explanation was more complicated than the solution, but with one function the question was solved.


from typing import List
def gravity_flip(columns: List[int]) -> List[int]:
    return sorted(columns)
            

print(gravity_flip(columns = [3, 2, 1, 2]))
-----------------------------------------------------------------------------------------
# Original solution without function


from typing import List

def gravity_flip(columns: List[int]) -> List[int]:
    for i in range(len(columns)):  
        for j in range(len(columns) - 1):  
            if columns[j] > columns[j + 1]: 
                
                columns[j], columns[j + 1] = columns[j + 1], columns[j]
    return columns 


print(gravity_flip(columns=[3, 2, 1, 2]))
