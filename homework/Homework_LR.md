# 1. Dự đoán sản lượng lúa (kg) của nông dân miền Tây
**Input**: 
- Giống lúa
- Thời điểm gieo trồng (vụ đông-xuân, hè-thu, thu-đông)
- Diện tích đất canh tác
- Điều kiện thủy lợi
- Điều kiện thời tiết điển hình trong vụ đó

**Output**:
Sản lượng lúa (kg) trên tổng diện tích đất

**Thu thập dữ liệu**:
- Thu thập dữ liệu canh tác nông nghiệp tại các cơ quan hợp tác xã ở miền Tây bao gồm các thông tin phía trên.
- Có thể thu thập dữ liệu từ nông dân miền Tây qua các mùa
- Ghi chép và tổng hợp lại vào file .csv

**Xử lý dữ liệu**
- Loại bỏ các dữ liệu không ảnh hưởng nhiều tới output, (ví dụ như null data hoặc thiếu sót dữ liệu trong quá trình thu thập)
- Loại bỏ dữ liệu mà các giống lúa mới xuất hiện hoặc chưa từng xuất hiện trong quá khứ

# 2. Dự đoán tỉ lệ tử vong (%) của bệnh nhân mang bệnh nền và COVID-19.

**Input:**
- Số lượng người bệnh
- Thông tin của mỗi bệnh nhân: Họ tên, ngày tháng năm sinh, giới tính, quê quán, số lượng và danh sách bệnh nền của bệnh nhân đó.

**Output:**
- Con số từ 0-100 (%) thể hiện tỉ lệ tử vong của các bệnh nhân trên.
- **Note:** Tùy vào độ tuổi, số lượng bệnh nền, mức độ nghiêm 	trọng bệnh nền và tuổi bệnh nhân mà mô hình sẽ đưa ra dự đoán.
- **VD:** 1 bệnh nhân A mắc 4 bệnh nền (1 trong số đó có bệnh viêm phổi), 82 tuổi thì tỉ lệ tử vong sẽ rất cao. 

**Thu thập dữ liệu:**
- Kết hợp thu thập dữ liệu bệnh nhân từ trang: ncov.moh.gov.vn và mạng xã hội Facebook (nhưng phải kiểm tra tính đúng đắn và 	có 	chọn lọc).
- Ghi lại dữ liệu các bệnh nhân đã xin được từ các bệnh viện có bệnh nhân đã mắc cả COVID-19 và bệnh nền (nếu được nên có được sự đồng ý từ gia đình bệnh nhân với mục đích nghiên cứu hướng tích cực).
- Tất cả dữ liệu bệnh nhân được ghi vào các trường tương ứng, sau đó tạo 1 file *.csv để gom nhóm các thuộc tính đó lại. 

**Xử lý dữ liệu:**
- Loại bỏ các điểm dữ liệu bị trống do chưa có đầy đủ thông tin hoặc lí do nào khác.
- Loại bỏ các trường không cần thiết, không ảnh hưởng đến kết quả Output.
- Trực quan hóa dữ liệu.

# 3. Dự đoán hành vi trả nợ đúng hạn của khách hàng cá nhân tại các ngân hàng

**Input:**
- Độ tuổi
- Giới tính
- Tình trạng hôn nhân (1 hoặc 0)
- Mục đích vay (có thể phân loại đánh số)
- Tài sản thế chấp (1 hoặc 0)
- Thu nhập (phân loại: cao, thấp, trung bình)
- Thời hạn vay (phân loại: dài hạn, trung hạn, ngắn hạn)

**Output:**
- Trả nợ đúng hạn (1) hoặc trả nợ không đúng hạn (0)

**Cách thu thập dữ liệu:**
- Thu thập dữ liệu từ các ngân hàng bao gồm các thông tin như trên
- Lưu trữ dưới dạng file .csv

**Xử lý dữ liệu:**
- Loại bỏ các điểm dữ liệu thừa hoặc thiếu sót trong quá trình thu thập.



