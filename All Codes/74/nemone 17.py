student=[('alice',[80,85,90]),('bob',[70,82,88]),('charlie',[90,95,92])]

sorted_student=sorted(student,key=lambda x:sum(x[1]),reverse=True)

print(sorted_student)
