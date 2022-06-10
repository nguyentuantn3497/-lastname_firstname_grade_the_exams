# Read files Grade the exams and check ID, student grading by Python

N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D

Viết một chương trình để chấm điểm các bài thi cho một phần nhất định. Kỳ thi gồm 25 câu hỏi, trắc nghiệm. Đây là một chuỗi đại diện cho các câu trả lời:

Answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

Chương trình sử dụng những câu trả lời này để tính điểm cho mỗi dòng dữ liệu hợp lệ. Điểm có thể được tính như sau:

1. +4 điểm cho mỗi câu trả lời đúng

2. 0 điểm cho mỗi câu trả lời bị bỏ qua

3. -1 điểm cho mỗi câu trả lời sai

Và tính toán các thống kê sau cho toàn bộ lớp:

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

