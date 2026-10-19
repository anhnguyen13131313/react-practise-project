# Chapter 8 — Triển khai

> Trích từ PDF gốc, giữ các mốc số trang để kiểm tra nguồn. Đây là giáo án, không phải toàn bộ lời nói của thầy.

> **Phạm vi:** PDF page 78–83.

<!-- pdf-page:78; printed-page:77 -->

<a id="pdf-page-78"></a>

## PDF page 78 · Trang in 77

## Chapter 8: Triển Khai Dự Án Thực Tế
Triển khai dự án thực hành  

### Video #88 — Mô hình triển khai

 Frontend => Backend => Database  

**1. Frontend React: triển khai miễn phí với Vercel**

**2. Backend Node.JS: triển khai miễn phí với Render**

**3. Database MongoDB: triển khai miễn phí với MongoDB Atlas (đã làm ở #22, khi setup**
dự án backend)  

Do database đã setup từ đầu => cần setup thêm frontend/backend

<!-- pdf-page:79; printed-page:78 -->

<a id="pdf-page-79"></a>

## PDF page 79 · Trang in 78

### Video #89 — Tạo Tài Khoản Render

**1. Triển khai ứng dụng Backend miễn phí với Render.com**
- Render cho phép triển khai ứng dụng Backend (node.js) miễn phí.  
(Trước 12/2022, chúng ta có Heroku)  

- Gói miễn phí phục vụ mục đích testing (học tập). Làm thực tế (chạy thật), không nên  
dùng Render.com  

Thông tin về gói miễn phí:  
https://render.com/docs/free  

Lưu ý: Sau 15 phút không hoạt động -> hibernate  

`//todo : tạo tài khoản Render`

<!-- pdf-page:80; printed-page:79 -->

<a id="pdf-page-80"></a>

## PDF page 80 · Trang in 79

### Video #90 — Triển Khai Backend với Render

Lưu ý: nếu bạn không có backend payment 8888 (thì không cần triển khai, chỉ xem video  
tham khảo)  

Chuẩn bị:  
      -  Đẩy source code backend lên github (gồm 2 dự án backend : backend 8080 và  
      backend payment 8888)  

      -  Đã đăng ký thành công tài khoản Render (xem video #89)  

Bước 1: Copy code backend sang thư mục mới, tránh ảnh hưởng tới code tại local  

Bước 2: Tạo 2 repository trên github và đẩy code lên github  

Bước 3: Cấu hình Render  

- Lưu ý về file .env (nếu có)  
`//todo`

- Cách đọc logs ứng dụng ???  

Sau khi triển khai, cần test postman (hoặc test frontend tại localhost, với Backend đã  
hosting)  

Lưu ý quan trọng về Backend Render khi dùng miễn phí:  
https://render.com/docs/free#spinning-down-on-idle  

Do backend này dùng miễn phí, vì vậy, sau 15 phút mà website không có lượt truy cập,  
backend này sẽ rơi vào trạng thái sleep/hibernate  

Ví dụ: bạn triển khai thành công backend với render tại thời điểm 3h0 phút, mọi thứ ok  

Do không có ai sử dụng website của bạn, vì vậy, tại thời điểm 3h15 phút (sau 15 phút),  
backend này sẽ tự động sleep/hibernate.  

Khi bị sleep/hibernate, và bạn truy cập website, bạn SẼ CẦN CHỜ cho nó wake-up.

<!-- pdf-page:81; printed-page:80 -->

<a id="pdf-page-81"></a>

## PDF page 81 · Trang in 80

Thông thường, sẽ chờ từ 30s cho tới 1 phút.  

Đây là giá khi dùng hàng FREE - Miễn Phí (chỉ phục vụ mục đích demo/học tập)  
### Video #91 — 1 Tạo Tài Khoản Vercel
Tạo tài khoản Vercel  
//nếu bạn đã có tài khoản Vercel, có thể bỏ qua phần này  
Thông tin về Vercel: https://vercel.com/pricing  

### Video #91 — 2 Link Vercel tới Github
`//todo`

### Video #92 — Triển khai Frontend với Vercel

**1.Triển khai dự án với Vercel**

Bước 1: cấu hình tại local  

với Vercel, khi F5 (refresh) thì bị lỗi. Để khắc phục, tạo file vercel.json tại thư mục root  
(tương tự như file .env), với nội dung:  
```json
{  
 "rewrites":  [  
  {"source": "/(.*)", "destination": "/"}  
  ]  
}  
```

Bước 2: Đẩy copy sang thư mục production & đẩy code lên github  

Bước 3: Triển khai với Vercel  
https://stackoverflow.com/a/50081316  

Lưu ý: sử dụng câu lệnh build với yarn  

Update file .env  

Update Google Link (chức năng login với google)  

Sau khi đã có url frontend, cần update file .env của Backend Payment

<!-- pdf-page:82; printed-page:81 -->

<a id="pdf-page-82"></a>

## PDF page 82 · Trang in 81

**2.Lưu ý về lỗi Refresh Token (không set Cookies)**

<!-- pdf-page:83; printed-page:82 -->

<a id="pdf-page-83"></a>

## PDF page 83 · Trang in 82

### Video #93 — Chuyện Học 1 Khóa Học
`//todo`

### Video #94 — Level Fresher là level như thế nào ?
`//todo`

### Video #95 — Học gì tiếp đây ?
`//todo`
