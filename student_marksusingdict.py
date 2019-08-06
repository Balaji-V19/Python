if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks)
    for x,y in student_marks.items():
        if x == query_name:
            le=len(y)
            #print(le)
            sum=0.0
            for i in range(le):
                #print(y[i])
                sum +=y[i]
                #print(sum)
            break
        else:
            continue       
    #print(sum)
    avr=sum/3        
    print("%.2f"%avr)                

            



