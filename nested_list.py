if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    #students=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
        #assigning infinite value in variable min_score in float value
    min_score = float("inf")
    second_score= float("inf")
    #GOING through each values in students to find the minimum score
    for i in range(len(students)):
        #comparing if each value in length of students is less than 
        if students[i][1]<min_score:
            second_score=min_score
            min_score=students[i][1]
    # new_students=[]
    # for i in range(len(students)):
    #     if students[i][1]!=min_score:
    #         new_students.append(students[i])
    # min_score = float("inf")
    # for i in range(len(new_students)):
    #     if new_students[i][1]<min_score:
    #         min_score=new_students[i][1]
    min_score = second_score
    final_students = []
    for i in range(len(students)):
        if students[i][1]==min_score:
            final_students.append(students[i][0])
    for i in sorted(final_students):
        print(i)
        