# Read files Grade the exams and check ID, student grading by Python

N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D

Viết một chương trình để chấm điểm các bài thi cho một phần nhất định. Kỳ thi gồm 25 câu hỏi, trắc nghiệm. Đây là một chuỗi đại diện cho các câu trả lời:
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
Chương trình sử dụng những câu trả lời này để tính điểm cho mỗi dòng dữ liệu hợp lệ. Điểm có thể được tính như sau:
+4 điểm cho mỗi câu trả lời đúng
0 điểm cho mỗi câu trả lời bị bỏ qua
-1 điểm cho mỗi câu trả lời sai
Bạn cũng sẽ muốn tính toán các thống kê sau cho toàn bộ lớp:
Điểm trung bình
Điểm cao nhất
Điểm thấp nhất
Miền giá trị của điểm (cao nhất trừ thấp nhất)
Ví Dụ:
**** ANALYZING ****
No errors found!
**** REPORT ****
Total valid lines of data: 20
Total invalid lines of data: 0 
Mean (average) score: 75.60
Highest score: 91
Lowest score: 59
Range of scores: 32
Median score: 73
Enter a class to grade (i.e. class1 for class1.txt): class2
Successfully opened class2.txt 
**** ANALYZING **** 
Invalid line of data: does not contain exactly 26 values:
N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A 
Invalid line of data: N# is invalid
N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D 
Invalid line of data: N# is invalid
NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D 
Invalid line of data: does not contain exactly 26 values:
N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A 
**** REPORT **** 
Total valid lines of data: 21
Total invalid lines of data: 4 
Mean (average) score: 78.00
Highest score: 100
Lowest score: 66
Range of scores: 34
Median score: 76

Cuối cùng, yêu cầu chương trình tạo một tệp “kết quả” chứa các kết quả chi tiết cho từng học sinh trong lớp của bạn. Mỗi dòng chứa số ID của học sinh, dấu phẩy và sau đó là điểm của họ. Đặt tên tệp này dựa trên tên tệp gốc được cung cấp 
— Ví dụ: nếu người dùng muốn phân tích “class1.txt”,lưu trữ kết quả trong tệp có tên “class1_grades.txt”.

# this is what class1_grades.txt should look like                               
N00000001,59
N00000002,70
N00000003,84
N00000004,73
N00000005,83
N00000006,66
N00000007,88
N00000008,67
N00000009,86
N00000010,73
N00000011,86
N00000012,73
N00000013,73
N00000014,78
N00000015,72
N00000016,91
N00000017,66
N00000018,78
N00000019,78
N00000020,68
# this is what class2_grades.txt should look like
N00000021,68
N00000022,76
N00000024,73
N00000026,72
N00000028,73
N00000029,87
N00000030,82
N00000031,76
N00000032,87
N00000033,77
N00000034,69
N00000036,77
N00000037,75
N00000038,73
N00000039,66
N00000040,73
N00000041,91
N00000042,100
N00000043,86
N00000044,90
N00000045,67
