studentsScores = [
    ["Alice", 85, 88, 95],
    ["Bob", 70, 90, 87],
    ["Charlie", 92, 86, 90],
    ["Diana", 78, 82, 85],
    ["Ethan", 89, 95, 84]
  ]

for student in studentsScores:
    
    name = student[0] # the name is in the element[0]
    total = 0 # zero bcuz it hasn't been calculated ye!
    
    for score in student[1:]: 
        # students' scores are the elements after zero elements
        # ["name(0)", scores1(1), score2(2)]
        #             here [1:]!!
               
        total = total + score  # u must print the total variable then!
    print(f"{name}: {total}")
    
    
# total = 0
# FORMULA
# totalFromCalculation = total + score
 
 
# totalFromCalculation = 0 + 85[1] = 85
# 85 + 88[2]  = 173
# 73 + 95[3] = 268

