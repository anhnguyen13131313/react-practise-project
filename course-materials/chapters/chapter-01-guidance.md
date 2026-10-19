# Chapter 1 — Hướng dẫn khóa học

> Trích từ PDF gốc, giữ các mốc số trang để kiểm tra nguồn. Đây là giáo án, không phải toàn bộ lời nói của thầy.

> **Phạm vi:** PDF page 9–15.

<!-- pdf-page:9; printed-page:8 -->

<a id="pdf-page-9"></a>

## PDF page 9 · Trang in 8

## Chapter 1: Bắt buộc xem - Không bỏ qua chương học này
Hướng dẫn sử dụng khóa học hiệu quả  

### Video #1 — Hướng Dẫn Sử Dụng Khóa Học Hiệu Quả

Bạn vui lòng "xem video lần lượt" theo trình tự. Vì khóa học như 1 dòng chảy, video sau  
sẽ kế thừa lại kết quả của video trước đó.  

**1. Dành cho học viên "có ít thời gian"**
Nếu bạn vội, cần học nhanh, hoặc "bạn đã biết rồi", thì "vẫn xem video, cơ mà không cần  
code theo".  

Lưu ý: vẫn xem qua tài liệu khóa học để biết "video hướng dẫn gì".  
Đã "Không xem video", thì cần "đọc giáo án".  

Có như vậy mới biết khóa học nó làm cái gì.  

**2. Dành cho học viên "thông thường"**
Nguyên tắc:  
- Xem video lần lượt  
- Xem video kết hợp với giáo án. Bạn không cần take note, vì những điều quan trọng đã  
có trong giáo án  

- Bạn vui lòng code theo video.  
Nếu bạn "code theo ý bạn", vui lòng "không hỏi khi có bugs".  

Câu chuyện này giống như việc bạn đi khám bệnh, nhưng không tin lời bác sĩ  
=> Nếu bạn giỏi, bạn làm luôn bác sĩ, còn đi khám bệnh làm gì.  

- Bạn có thể "code theo ý bạn muốn", sau khi "đã kết thúc khóa học"  

- Nếu bạn có thắc mắc (hoặc có ý tưởng/nhận thấy bugs), take note lại, bạn hỏi, rồi mình  
giải đáp.  
Chứ không phải là "tự ý làm theo điều các bạn muốn".  
Vì đa phần, các bugs trong khóa học mình đã fix hết rồi.  

Nên là yên tâm để học theo bạn nhé.

<!-- pdf-page:10; printed-page:9 -->

<a id="pdf-page-10"></a>

## PDF page 10 · Trang in 9

**3. Về cách code.**

Bạn vui lòng code theo video, từ cách đặt tên biến, hàm. Vì mình đã tuân theo  
"convention tối thiểu" khi bạn đi làm đấy  

**4. Về bài tập thực hành**
Đối với bài tập thực hành, bạn cứ code theo cách bạn hiểu, và kết hợp với "search  
Google, stackoverflow..."  
KHÔNG DÙNG CHATGPT. Đây giống kiểu chưa học "phép tính", mà đã "dùng máy tính".  

Nên nhớ 1 điều, trước 2023, không có chat gpt, thì mình học như thế nào ?  
Khi bạn đã đi làm, bạn có quyền dùng cái gì bạn thích, còn với beginner, hãy biết say NO  
với CHAT GPT.  

tương tự bạn dạy con bạn:  
học lớp cấp 1: không chịu học tính nhầm => đưa luôn máy tính cho nó. Rời máy tính ra,  
là không biết làm phép tính  

còn với học sinh cấp 2, 3 : dùng máy tính tùy thích

<!-- pdf-page:11; printed-page:10 -->

<a id="pdf-page-11"></a>

## PDF page 11 · Trang in 10

### Video #2 — Tài liệu khóa học
`//todo`

<!-- pdf-page:12; printed-page:11 -->

<a id="pdf-page-12"></a>

## PDF page 12 · Trang in 11

### Video #3 — Demo kết quả đạt được

Video demo : https://youtu.be/z5ywlBpVusw  

**1.Trọng tâm của khóa học**
      -  100% code sử dụng TypeScript. Giúp code nhanh hơn và hạn chế bug so với  
      JavaScript (version cũ), đồng thời đáp ứng nhu cầu tuyển dụng của công ty.  

      -  Đây là dự án thực hành (project cuối khóa).  
     Nếu như rằng, bạn đi học trung tâm, luôn có dự án thực hành/thực chiến cuối  
      khóa học, thì đây chính là cơ hội để cho bạn được “thực hành” một dự án với  
      React sử dụng công cụ TypeScript  

      -  Backend dự án này sẽ được cung cấp sẵn (bạn không cần viết backend), chỉ dùng  
      và không sửa đổi.  
     Backend này đảm bảo yêu cầu trong thực tế, ví dụ như cơ chế JWT - JSON Web  
      Token (access token, refresh token…)  

      -  Khóa học này chính là thời gian cho bạn chuyển hóa kiến thức, có thể kể đến như  
       kiến thức React, React Router và việc kết hợp render giao diện với dữ liệu lấy từ  
      API backend.  

      -  Sử dụng Ant Design để tiết kiệm thời gian CSS và viết Component React.  
     Áp dụng Pro Component (Ant Design Pro), phục vụ đắc lực cho giao diện Admin  

**2. Công nghệ sử dụng**
Dự án thực hành: Website bán sách có tích hợp hình thức thanh toán (VNPAY)  

Frontend:  
      -  React 18, React Router 6 sử dụng với TypeScript  
      -  Cấu hình dự án React sử dụng React Vite (mô hình CSR - client side rendering)  
       với TypeScript từ số 0  
      -  Design giao diện với Antd (Ant Design) kết hợp với Pro Component (Ant Design  
      Pro) giúp thiết kế giao diện nhanh hơn và tiết kiệm thời gian CSS.

<!-- pdf-page:13; printed-page:12 -->

<a id="pdf-page-13"></a>

## PDF page 13 · Trang in 12

Backend (chính): Nestjs được cung cấp sẵn, chỉ dùng và không sửa đổi.  

Backend (phụ): được cung cấp code backend mẫu (có thể sửa đổi) hướng dẫn tích hợp  
ví VNPay dùng để thanh toán qua tài khoản ngân hàng.  

Lưu ý: không học code backend trong khóa học này, bạn không cần code logic backend,  
backend được cung cấp sẵn, chỉ việc sử dụng (có giải thích logic để tích hợp với  
Frontend)  

Database : MongoDB dùng miễn phí với MongoDB Atlas  

**3. Học viên nào có thể học ?**

Khóa học này là khóa học thứ 3 trong lộ trình React của Hỏi Dân IT, sau khi bạn đã học  
xong khóa học React Cơ Bản và khóa học React Pro Typescript Portfolio  

Vì vậy, học viên cần trang bị các kiến thức sau trước khi theo học:  

Yêu cầu 1: Biết React.js làm website sử dụng Typescript  
Nếu bạn chưa biết gì về React.js làm website, tham khảo tại đây  
Nếu bạn chưa biết code React.js với TypeScript, tham khảo tại đây  

Yêu cầu 2: Biết sử dụng Git để quản lý mã nguồn  

Kiến thức về Git sẽ giúp bạn 2 việc quan trọng:  
      -  Có khả năng backup code của chính bạn, tránh trường hợp máy tính bị hư hỏng,  
     dẫn tới mất code. Ngoài ra, khi cần mình support, bạn có thể gửi project cho mình  

      -  Bạn có khả năng sử dụng code mà khóa học cung cấp  

Nếu bạn chưa biết gì về Git, xem khóa học Git miễn phí tại đây  
Khóa học Git trả phí, tham khảo tại đây

<!-- pdf-page:14; printed-page:13 -->

<a id="pdf-page-14"></a>

## PDF page 14 · Trang in 13

### Video #4 — Tại sao khóa học này ra đời ?

**1.Các vấn đề được giải quyết trong khóa học**

      -  Tạo cơ hội cho bạn “thực hành” React (với backend được cung cấp sẵn)  
     Lưu ý: đa phần các video trong khóa học là video “định hướng”, phần còn lại bạn  
      cần thực hành.  
     Yên tâm là bạn sẽ được cung cấp source code theo từng video thực hành (nếu  
      cần)  

     Đây không phải là khóa học hướng dẫn bạn từng dòng code một. Vì đơn giản, nó  
        là khóa học thực hành.  
     Hãy tưởng tượng bạn đi học trung tâm, bạn có dự án thực hành cuối khóa, khóa  
     học này có ý nghĩa tương tự như vậy  

      -  Đưa ra yêu cầu (giả lập) trong thực tế mà các công ty có thể trông chờ.  

**2. Yêu cầu để học khóa học này**
Yêu cầu 1: Biết React.js làm website Typescript  
Nếu bạn chưa biết gì về React.js làm website, tham khảo tại đây  
Nếu bạn chưa biết code React.js với TypeScript, tham khảo tại đây  

Yêu cầu 2: Biết sử dụng Git để quản lý mã nguồn  

Kiến thức về Git sẽ giúp bạn 2 việc quan trọng:  
      -  Có khả năng backup code của chính bạn, tránh trường hợp máy tính bị hư hỏng,  
     dẫn tới mất code. Ngoài ra, khi cần mình support, bạn có thể gửi project cho mình  

      -  Bạn có khả năng sử dụng code mà khóa học cung cấp  

Nếu bạn chưa biết gì về Git, xem khóa học Git miễn phí tại đây  
Khóa học Git trả phí, tham khảo tại đây  

**3. Khóa học này nằm ở đâu trong lộ trình Frontend của tác giả Hỏi Dân IT**

Khóa học này là khóa học thứ 3 , sau khi bạn đã học xong khóa học React Cơ Bản và  
khóa học React Pro Typescript Portfolio  

Chi tiết về lộ trình Frontend React của tác giả Hỏi Dân IT, tham khảo tại đây.

<!-- pdf-page:15; printed-page:14 -->

<a id="pdf-page-15"></a>

## PDF page 15 · Trang in 14

### Video #5 + #6 — Về Tác giả
Về tác giả:  

Mọi thông tin về Tác giả Hỏi Dân IT, các bạn có thể tìm kiếm tại đây:  

Website chính thức: https://hoidanit.vn/  

Youtube “Hỏi Dân IT” : https://www.youtube.com/@hoidanit  

Tiktok “Hỏi Dân IT” : https://www.tiktok.com/@hoidanit  

Fanpage “Hỏi Dân IT” : https://www.facebook.com/askITwithERIC/  

Udemy Hỏi Dân IT: https://www.udemy.com/user/eric-7039/  

Nếu bạn muốn nói chuyện với mình (giao lưu trao đổi võ công :v), có thể xem mình  
livestream trực tiếp tối thứ 2 hàng tuần trên Youtube Hỏi Dân IT
