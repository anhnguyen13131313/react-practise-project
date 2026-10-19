# Chapter 3 — React với TypeScript

> Trích từ PDF gốc, giữ các mốc số trang để kiểm tra nguồn. Đây là giáo án, không phải toàn bộ lời nói của thầy.

> **Phạm vi:** PDF page 24–32.

<!-- pdf-page:24; printed-page:23 -->

<a id="pdf-page-24"></a>

## PDF page 24 · Trang in 23

## Chapter 3: React với TypeScript
Sử dụng React sử dụng ngôn ngữ TypeScript từ số 0  

### Video #14 — Tổng quan về chapter
`//todo`

### Video #15 — Lựa chọn công nghệ

**1. Javascript hay Typescript ?**
Version cũ mình dùng JavaScript. Version mới, mình khuyến khích sử dụng Typescript  
Lý do 1: được support tối hơn, đặc biệt trong việc phát hiểu lỗi (bug) khi gõ code  
Lý do 2: yêu cầu của công ty ngày càng tăng cao, và dùng Typescript là điều bắt buộc  

**2. CRA (create-react-app) hay Vite**
Tính tới thời điểm 2025, create-react-app is dead. Và nếu muốn sử dụng React với mô  
hình CSR (client side rendering), sử dụng Vite  

**3. Manage State’s React**
Version Javascript (cũ), mình sử dụng React Toolkit  

Version Typescript (mới), mình sử dụng React Context.  
Lý do 1: đơn giản và hạn chế setup phức tạp như là cách làm với Redux  
Lý do 2: React hiện đại (ví dụ Next.js), không bắt buộc phải dùng Redux  
Lý do 3: Mình đã có khóa học React State Manager để hướng dẫn về Redux  

**4. Responsive layout**

Để tạo nhanh layout, mình sử dụng Antd thay vì Bootstrap.  

Lý do : khóa học React Ultimate (react cơ bản), mình đã dùng antd. Vì vậy, khóa học này  
sẽ kế thừa và phát triển thêm

<!-- pdf-page:25; printed-page:24 -->

<a id="pdf-page-25"></a>

## PDF page 25 · Trang in 24

### Video #16 — Setup Dự Án Thực Hành

**1.Chuẩn bị**
Đảm bảo rằng bạn đã cài đặt Git và Node.js (version 20.14.0)  
Chưa biết dùng git, học ngay và luôn tại đây  

Bạn vui lòng sử dụng chính xác nodejs v20.14.0 để hạn chế tối đa lỗi xảy ra  
(mình đã giải thích tại video #8)  

**2.Cài đặt dự án thực hành**
Lưu ý : đường dẫn nơi lưu dự án thực hành, không nên đặt tên tiếng việt để hạn chế lỗi  
các bạn nhé  

Ví dụ: D:/dự án/react-fresher-typescript => thay bằng: D:/du-an/react-fresher-typescript  
Bước 1: Download source code tại đây  

Bước 2: cài đặt thư viện cần thiết  
npm i  

Lưu ý về warning/error tại terminal  

Bước 3: chạy dự án  

npm start (hoặc câu lệnh : npm run dev)  

**3.Viết Hello World**
`//todo`
Rename app => layout, đồng thời, remove css

<!-- pdf-page:26; printed-page:25 -->

<a id="pdf-page-26"></a>

## PDF page 26 · Trang in 25

### Video #17 — Cách mình Setup Dự Án Thực Hành (Extra)

Lưu ý, bạn vui lòng không làm theo video này.  

Mục đích mình làm video này, để thỏa mãn tính tò mò của nhiều bạn.  

Bạn chỉ làm như video này, khi đã có khả năng tự fix bug và đọc tài liệu, cũng như đã  
học xong khóa học này rồi.  

Bạn vui lòng thực hành khóa học bằng cái tải source code mình cung cấp tại #16  

Nếu như bạn tự ý code “theo cách bạn hiểu” và không sử dụng source code tại #16  
mình sẽ không hỗ trợ support khi có lỗi xảy ra  

Tài liệu: https://vite.dev/guide/  

//hướng dẫn cách đẩy code lên github/gitlab của chính bạn  
Nếu bạn chưa biết gì về Git, học ngay và luôn tại đây  

Bước 1: Tạo repository trên github/gitlab  

Bước 2: Đẩy dự án lên repository vừa tạo  
git add .  
git commit -m "init project"  

https://stackoverflow.com/questions/2432764/how-do-i-change-the-uri-url-for-a-remote  
-git-repository  

git remote set-url origin new.git.url/here  

git push origin master  

Bước 3: Minh họa khi code xong 1 video, chỉ cần sử dụng 3 câu lệnh bên dưới  
git add .  
git commit  
git push

<!-- pdf-page:27; printed-page:26 -->

<a id="pdf-page-27"></a>

## PDF page 27 · Trang in 26

### Video #18 — Setup React Router
Tài liệu: https://reactrouter.com/en/main/start/tutorial  

Cài đặt thư viện:  
npm install --save-exact react-router-dom@6.27.0  

**1.Lưu ý về React Router**

Version của React Router thay đổi theo thời gian, nếu mà chạy theo công nghệ, lắp tên  
lửa vào đuổi cũng không kịp.  

Giải pháp để giải quyết vấn đề trên là bạn học và hiểu 1 version cụ thể (vì mindset nó  
không đổi giữa các version).  

Sau này, nếu chẳng may thư viện nó thay đổi, cần tìm đúng Component của thư viện, rồi  
đọc docs của nó, hoặc làm theo cách hiểu của bạn. Không thể trông chờ lúc nào tài liệu  
nó cũng giống hệt như video mình hướng dẫn được, ok ?

> **Trang có hình/screenshot:** ![Hình gốc trang 27](../images/pdf-page-27.png)


<!-- pdf-page:28; printed-page:27 -->

<a id="pdf-page-28"></a>

## PDF page 28 · Trang in 27

### Video #19 — Chia Layout và Cấu Trúc Project

**1.Chia layout**
`//todo`
login/register/home/book  

npm i --save-exact sass@1.80.4  
https://stackoverflow.com/a/79003101  

**2. Setup TypeScript Absolute Path**

Bước 1: cấu hình Vite  
npm i --save-exact --save-dev vite-tsconfig-paths@5.0.1  

https://stackoverflow.com/questions/68241263/absolute-path-not-working-in-vite-proje  
ct-react-ts  

https://github.com/aleclarson/vite-tsconfig-paths  

Bước 2: khai báo Typescript baseUrl và path  

Về typescript path: https://www.typescriptlang.org/tsconfig/#paths  

Bước 3: test import

<!-- pdf-page:29; printed-page:28 -->

<a id="pdf-page-29"></a>

## PDF page 29 · Trang in 28

### Video #20 — Cài đặt MongoDB Compass

MongoDB Compass không phải là database. Nó chỉ đơn thuần là một phần mềm cung  
cấp giao diện, giúp bạn thao tác với database (MongoDB)  

Database của khóa học sẽ được tạo tại các video tiếp theo (lưu trữ trên cloud)  

Link download: https://www.mongodb.com/try/download/compass  

### Video #21 — Tạo Tài Khoản MongoDB Atlas
Link đăng ký tài khoản MongoDB Atlas (miễn phí)  
https://www.mongodb.com/cloud/atlas/register  

### Video #22 — Tạo Database cho dự án
Lưu ý check allow anywhere  

Lưu lại thông tin kết nối tới database  

### Video #23 — Kiểm Tra Kết Nối Database
Công cụ: phần mềm Mongodb Compass  

Lưu lại connection để tiện sử dụng

<!-- pdf-page:30; printed-page:29 -->

<a id="pdf-page-30"></a>

## PDF page 30 · Trang in 29

### Video #24 — Kích hoạt dự án Backend

Lưu ý: backend này chỉ sử dụng và không sửa đổi.  

Bạn nào quan tâm về backend này mình viết như thế nào, tham khảo khóa học backend  

Nestjs của Hỏi Dân IT tại đây  

**1. Cài đặt backend**

Bước 1: download source code backend tại đây  

Bước 2: Cài đặt các thư viện cần thiết  

npm install --omit=dev  

Bước 3: update file .env  

Cập nhật tham số MONGO_DB_URL  

Bước 4: Chạy dự án thực hành  

npm start / npm run dev  

Bước 5: Test ứng dụng, truy cập: http://localhost:8080/

<!-- pdf-page:31; printed-page:30 -->

<a id="pdf-page-31"></a>

## PDF page 31 · Trang in 30

**2. Cài đặt luôn postman và import collections**

Download Postman tại đây: https://www.postman.com/  

Download file collections tại đây  

(trong source code backend đã có file collection)  

`//todo: test api và set tham số môi trường cho postman (nếu cần thiết)`

> **Trang có hình/screenshot:** ![Hình gốc trang 31](../images/pdf-page-31.png)


<!-- pdf-page:32; printed-page:31 -->

<a id="pdf-page-32"></a>

## PDF page 32 · Trang in 31

### Video #25 — Cấu trúc Module Thực Hành (Extra)

Dự án thực hành được chia thành các module riêng biệt, tương ứng với các chức năng  
website xây dựng.  

Đối tượng sử dụng hệ thống (actor) gồm 2 loại chính: user (người dùng bình thường) và  
admin (người quản trị).  

Như vậy, các chức năng chính được xây dựng là:  
      -  Module Auth (authentication và authorization) :  
     + user login/register  
     + check quyền theo role (role user hay admin)  
     + access token và refresh token  

      -  Module User (quản lý CRUD Users)  
     + import/export CSV  

      -  Module Book (quản lý CRUD Books)  
     + Hiển thị danh sách books (client)  
     + Hiển thị chi tiết book khi xem chi tiết (client)  

      -  Module Order (quản lý CRUD Orders)  
     + Hiển thị giỏ hàng (client)  
     + Chức năng đặt hàng, xem lịch sử đặt hàng.
