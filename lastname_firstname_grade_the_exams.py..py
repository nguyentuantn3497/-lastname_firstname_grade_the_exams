import numpy as np
import pandas as pd
while True:
    fn = input('Enter a class to grade (class1.txt):')
    if not fn:
        break
    else:
        def FileCheck(fn):
            try:
                open(fn, "r")
                return 'TASK_1: Successfully opened ' + fn
            except IOError:
                return "TASK_1: Error file does not appear to exist."
        result = FileCheck(fn)
        print (result)

        
    print('TASK_2: ANALYZING')
    data = open(fn,'r')

    '''Tạo 1 mảng data_open để lưu điểm của từng học sinh trong 1 class bằng cách loại bỏ các khoảng trắng ở các dòng 
    và tách các ký tự theo dấu phẩy'''

    data_open = np.array([i.strip().split(',') for i in data],dtype=list)
    print('Total rows in file:' + str(len(data_open)))
    
    ''' khai báo 3 biến để đếm tổng số dòng hợp lệ, không hợp lệ 
    và 1 list để lưu trữ các dòng hợp lệ dùng cho Task3 và Task4'''
    ok_rows = 0
    error_rows = 0
    list_rows_ok = []
    for i in range(len(data_open)):
        a = data_open[i]
        if len(a[0]) == 9 and a[0][0] == 'N' and a[0][1:].isdigit() == True and len(a) == 26:
            ok_rows +=1
            list_rows_ok.append(a)
            continue
        elif len(a[0]) !=9 or a[0][0] != 'N' or a[0][1:].isdigit() == False:
            error_rows +=1
            print('Invalid line of data: N# is invalid'+'\n',a)
            continue
        elif len(a) != 26:
            error_rows +=1
            print('Invalid line of data: does not contain exactly 26 values:' + '\n',a)
            continue
    if ok_rows == len(data_open):
        print('NO ERRORS FOUND!')

    ''' Đổi từ List sang mảng để tính toán dùng các method sẵn có'''
    list_rows_ok = np.array(list_rows_ok)
    print ('Total valid lines of data:' + str(ok_rows),\
        'Total invalid lines of data:' + str(error_rows), sep='\n')


    print('TASK_3: GET_GRADE')
    ''' tạo 2 biến để lưu điểm của các học sinh trong 1 class và 1 biến để lưu điểm của các class'''

    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(',')
    list_grades = []
    grades_class = []
    for i in range(len(list_rows_ok)):
        grade = 0
        for j in range(len(answer_key)):
            if list_rows_ok[i][j+1] == answer_key[j]:
                grade += 4
            elif list_rows_ok[i][j+1] == '':
                grade = grade
            else:
                grade -= 1
        list_grades.append(grade)
        grades_class.extend([[list_rows_ok[i][0],grade]])
    list_grades = np.array(list_grades)


    print('Mean (average) score: '+ str(np.mean(list_grades))\
        ,'Highest score: '+str(np.max(list_grades))\
        ,'Lowest score: '+ str(np.min(list_grades))\
        ,'Range of score: '+ str(np.max(list_grades)-min(list_grades))\
        ,'Median score: '+ str(np.median(list_grades)),sep='\n')
        

    print('TASK_4: DISPLAY_SCORE')
    for r in grades_class:
        with open('grades_'+str(fn),'a') as f:
            f.write(str(r[0]) + ','+ str(r[1]) + '\n')
fn.close()