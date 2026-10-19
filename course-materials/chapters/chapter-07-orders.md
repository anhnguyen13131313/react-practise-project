# Chapter 7 — Module Orders

> Trích từ PDF gốc, giữ các mốc số trang để kiểm tra nguồn. Đây là giáo án, không phải toàn bộ lời nói của thầy.

> **Phạm vi:** PDF page 70–77.

<!-- pdf-page:70; printed-page:69 -->

<a id="pdf-page-70"></a>

## PDF page 70 · Trang in 69

## Chapter 7: Module Orders
Tính năng đặt hàng sản phẩm  

### Video #76 — Tổng quan về chapter
`//todo`

### Video #77 — Bài tập Add/Remove Product

Yêu cầu: Xử lý tăng giảm button và input  

Nhấn trừ => số lượng giảm 1, và giảm tới 1, không là số âm  
Nhấn cộng => số lượng tăng 1, và tăng không quá max quantity  

Nhập input thì chỉ cho phép nhập số, và không tăng quá max quantity  

### Video #78 — Bài Tập Lưu Data Giỏ Hàng

**1. Quy trình xử lý khi người dùng nhất tăng/giảm sản phẩm**
Lưu data tại phía Frontend hay gọi API backend ?  

**2. Sử dụng React Context/Local Storage**
`//todo`
[{_id: currentBook?._id, quantity: currentQuantity , detail: currentBook}]

<!-- pdf-page:71; printed-page:70 -->

<a id="pdf-page-71"></a>

## PDF page 71 · Trang in 70

### Video #79 — Bài Tập Hiển Thị Số Lượng Giỏ Hàng

Yêu cầu:  
- Cập nhật số lượng products trên header  
- Thông báo thêm thành công  

### Video #80 — Bài Tập Preview Cart
Sử dụng popover: https://ant.design/components/popover  

https://ant.design/components/popover#popover-demo-arrow  

Gồm 2 bước:  
- build hardcode  
- build dynamic items  

**1. Lưu ý về css**
Modal, Popover... không render trong <div id="root">  
https://react.dev/reference/react-dom/createPortal  

Ở đây là css global => lưu ý về đặt tên class  

Note 1: css-dev-only class  
https://github.com/ant-design/ant-design/discussions/38753  

Note 2: không cần check trên mobile vì không có sự kiện hover => bắt buộc phải click  
để xem chi tiết

<!-- pdf-page:72; printed-page:71 -->

<a id="pdf-page-72"></a>

## PDF page 72 · Trang in 71

### Video #81 — Bài tập Order Page

Yêu cầu:  

- render động list carts  

- tăng giảm số lượng sản phẩm  

- xóa sản phẩm  

- tính tổng số tiền

<!-- pdf-page:73; printed-page:72 -->

<a id="pdf-page-73"></a>

## PDF page 73 · Trang in 72

### Video #82 — Bài tập Checkout Page

Các component sử dụng:  
- Hiển thị steps:  
https://ant.design/components/steps  

https://ant.design/components/empty  

Hiển thị textarea:  
https://ant.design/components/input#input-demo-textarea  

Yêu cầu:  
Quá trình đặt hàng gồm 3 bước:  
Bước 1: Thông tin đơn hàng  
      -  Cho phép tăng/giảm số lượng sản phẩm  
      -  Nếu không có sản phẩm trong giỏ hàng, hiển thị thông báo Empty  
      -  Nhấn button ‘mua hàng’ để chuyển qua bước 2. Nếu không có sản phẩm trong  
       giỏ hàng thì chặn không cho qua bước 2  

Bước 2: Thông tin đặt hàng  
      -  Không cho phép tăng/giảm số lượng sản phẩm  
      -  Yêu cầu điền thông tin đặt hàng, bao gồm: tên, số điện thoại, địa chỉ  
      -  Nhấn nút “Đặt hàng” để gọi API  
      -  Nếu đặt hàng thành công, chuyển qua bước 3. Có lỗi thì hiển thị thông báo lỗi  

Bước 3: Hiển thị kết quả  
      -  Cho phép xem lịch sử đơn hàng

<!-- pdf-page:74; printed-page:73 -->

<a id="pdf-page-74"></a>

## PDF page 74 · Trang in 73

### Video #83 — API Create An Order

Antd button:  
https://ant.design/components/button#button-demo-color-variant  

https://ant.design/components/result  

Bước 1: Gọi API  
API Create Order  
POST : /api/v1/order  

Bước 2: clear Carts  

### Video #84 — Bài tập View Order History
https://ant.design/components/table  

API history:  
GET http://localhost:8080/api/v1/history

<!-- pdf-page:75; printed-page:74 -->

<a id="pdf-page-75"></a>

## PDF page 75 · Trang in 74

### Video #85 — Bài tập Update Current User

**1. Update User Info**
- Có thể update được avatar và thông tin của người dùng  

Lưu ý:  
Để cập nhật Avatar, cần gọi api để upload file ảnh, tương tự như upload image book  

POST http://localhost:8080/api/v1/file/upload  
Sử dụng form-data, với header: upload-type === “avatar”  

Để cập nhật được thông tin của người dùng, cần gọi API update:  

PUT http://localhost:8080/api/v1/user  
(cần truyền lên avatar, kết quả của việc upload ở trên)  

Để cập nhật được thông tin user, sau khi update thành công, cần cập nhật thông tin lưu  
trong React Context, bao gồm fullName, avatar và phone  

**2. Update password**
POST http://localhost:8080/api/v1/user/change-password  

Cần truyền lên: email, oldpass, newpass

<!-- pdf-page:76; printed-page:75 -->

<a id="pdf-page-76"></a>

## PDF page 76 · Trang in 75

### Video #86 — Bài Tập Display Order page + API Dashboard

Cài đặt thư viện:  
npm install --save-exact react-countup@6.5.3  

https://ant.design/components/statistic#statistic-demo-animated  

https://ant.design/components/card#card-demo-border-less

<!-- pdf-page:77; printed-page:76 -->

<a id="pdf-page-77"></a>

## PDF page 77 · Trang in 76

### Video #87 — Các bugs còn tồn đọng

**1.Fix bugs**
      -  Fix lỗi logout clear carts (local Storage và react context)  

      -  Chưa đăng nhập, không thêm product vào giỏ hàng  

      -  Tại trang xem chi tiết sản phẩm, xử lý button “mua ngay”  

      -  Thêm breadcrumb để điều hướng trang  
https://ant.design/components/breadcrumb#breadcrumb-demo-withicon  

      -  Với admin, f5 lại trang thì chưa đúng active menu  
https://stackoverflow.com/questions/41054657/react-routerantd-how-to-highligh  
      t-a-menu-item-when-press-back-forward-button  

Test full luồng a tới z với normal user (đăng ký/đăng nhập tới order)  

**2. Bonus tính năng**
      -  CSS Scrollbar  

      -  Thanh search tại client  
https://reactrouter.com/en/main/hooks/use-outlet-context  
     Tương tự như search theo tên sách  

**3. Giao diện mobile**

- Tự CSS giao diện  
https://github.com/ant-design/ant-design/issues/10144  

https://www.npmjs.com/package/react-device-detect  

npm i --save-exact react-device-detect@2.2.3
