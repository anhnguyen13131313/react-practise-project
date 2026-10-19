# Chapter 5 — Module Users

> Trích từ PDF gốc, giữ các mốc số trang để kiểm tra nguồn. Đây là giáo án, không phải toàn bộ lời nói của thầy.

> **Phạm vi:** PDF page 47–58.

<!-- pdf-page:47; printed-page:46 -->

<a id="pdf-page-47"></a>

## PDF page 47 · Trang in 46

## Chapter 5: Module Users
CRUD users  

### Video #42 — Tổng quan về chapter
`//todo`

### Video #43 — Giới Thiệu Table Component

Tương tự: https://www.npmjs.com/package/react-table  

Antd Table: https://ant.design/components/table/  

Antd Pro Table: https://procomponents.ant.design/en-US/components/table  

Bước 1:  
Cài đặt thư viện:  

npm i --save-exact @ant-design/pro-components@2.8.1  

Download file table component tại đây  

Đăng nhập bằng tài khoản: admin@gmail.com/123456  

Bước 2: Lưu ý về warning và error  
https://github.com/ant-design/ant-design/issues/48709  

Bước 3: sử dụng tiếng việt  
https://ant.design/components/config-provider

<!-- pdf-page:48; printed-page:47 -->

<a id="pdf-page-48"></a>

## PDF page 48 · Trang in 47

### Video #44 — API Hiển Thị Danh Sách User

POST: http://localhost:8080/api/v1/user?current=1&pageSize=2  

Lưu ý:  
      -  Cần truyền Bearer Token ở header request  
      -  current : trang hiện tại  
      pageSize: số lượng bản ghi muốn lấy  

### Video #45 — Bài Tập Hiển Thị Danh Sách User
`//todo`
**1.Xử lý data hiển thị trên table**
https://ant.design/components/icon  
https://react-icons.github.io/react-icons/  

**2.Xử lý data hiển thị pagination**
https://ant.design/components/pagination

<!-- pdf-page:49; printed-page:48 -->

<a id="pdf-page-49"></a>

## PDF page 49 · Trang in 48

### Video #46 — API Filter

sử dụng API:  
GET http://localhost:8080/api/v1/user?current=1&pageSize=2  

Quy tắc truyền filter: https://www.npmjs.com/package/api-query-params  

**1. Dạng basic**
Truyền thêm các tham số cần filter:  

ví dụ:  
http://localhost:8080/api/v1/user?current=1&pageSize=2&fullName=abc  
=> filter theo fullName = abc  

http://localhost:8080/api/v1/user?current=1&pageSize=2&fullName=abc&email=test@  
gmail.com  
=> filter theo fullName = abc và email = test@gmail.com  

**2. Filter với Regx**
ví dụ:  
http://localhost:8080/api/v1/user?current=1&pageSize=2&fullName=/abc/i  

=> filter theo fullName có chứa từ 'abc'. tương tự như điều kiện %like% của SQL

<!-- pdf-page:50; printed-page:49 -->

<a id="pdf-page-50"></a>

## PDF page 50 · Trang in 49

### Video #47 — Bài Tập Filter Danh Sách User

Về mongodb regx:  
https://www.mongodb.com/docs/manual/reference/operator/query/regex/  
Quy tắc truyền filter: https://www.npmjs.com/package/api-query-params  

https://procomponents.ant.design/en-US/components/schema#valuetype-lists  

Cài đặt thư viện:  
npm i --save-exact dayjs@1.11.13  

Bước 1:  
//Thêm data cho table (createdAt)  

Bước 2: Build Query  
`//todo`

//helper.ts  

import dayjs from "dayjs";  

export const FORMATE_DATE = "YYYY-MM-DD";  

export const dateRangeValidate = (dateRange: any) => {  
   if (!dateRange) return undefined;  

  const startDate = dayjs(dateRange[0], FORMATE_DATE).toDate();  
  const endDate = dayjs(dateRange[1], FORMATE_DATE).toDate();  

  return [startDate, endDate];  
};

<!-- pdf-page:51; printed-page:50 -->

<a id="pdf-page-51"></a>

## PDF page 51 · Trang in 50

### Video #48 — Bài tập Sorter

sử dụng API: GET http://localhost:8080/api/v1/user?current=1&pageSize=2  

Quy tắc truyền sort filter:  
https://www.npmjs.com/package/api-query-params#sort-operator  

Mặc định, sort theo ascending/descending, tuy nhiên, ở nosql, có thể dùng dấu - (minus)  

Ví dụ:  
http://localhost:8080/api/v1/user?current=1&pageSize=2&sort=fullName  

=> sort kết quả theo fullName (asc)  

http://localhost:8080/api/v1/user?current=1&pageSize=2&sort=-fullName  
=> sort kết quả theo fullName (desc)  

//giải thích về sort và filter của antd:  
https://ant.design/components/table

<!-- pdf-page:52; printed-page:51 -->

<a id="pdf-page-52"></a>

## PDF page 52 · Trang in 51

### Video #49 — Bài tập chức năng View Detail User

Tài liệu:  
https://ant.design/components/drawer  
https://ant.design/components/descriptions  

- Component Description (sử dụng để hiển thị data read-only)  
- Component này tương tự table html, tuy nhiên đã css sẵn  
- List props: https://ant.design/components/descriptions#descriptions  

Bước 1:  
Set trạng thái open/close cho Drawer  

Bước 2:  
Truyền data từ table sang drawer. Mỗi khi user click vào row, set data detail. Truyền data  
này sang Drawer  

Bước 3:  
Hiển thị data với Description  

### Video #50 — Hiển Thị Avatar (Extra)

Tài liệu:  
https://ant.design/components/avatar  
url hiển thị: (avatar)  
url-backend/images/avatar/image-id-here  

Hướng dẫn add custom header => render table header with buttons

<!-- pdf-page:53; printed-page:52 -->

<a id="pdf-page-53"></a>

## PDF page 53 · Trang in 52

### Video #51 — Bài tập chức năng Create User

Tài liệu:  
https://ant.design/components/modal  

sử dụng ref để submit  
https://ant.design/components/form#formuseform  

Bước 1: Tạo form và modal  

Làm tương tự như phần login và register  

Bước 2: Submit APIs  

Bước 3: Refresh table với ref

<!-- pdf-page:54; printed-page:53 -->

<a id="pdf-page-54"></a>

## PDF page 54 · Trang in 53

### Video #52 — Design Modal Upload File (Drag & Drop)
Giải pháp về upload file:  
Cách 1.  
User dùng browser(client) upload file lên website (file raw)  

 Client gửi file (raw) lên server  

 Server đọc file (raw) này, convert dữ liệu ra định dạng mong muốn (json),  

 Server xử lý và lưu dữ liệu vào database  

 Server trả về kết quả cho client  

Cách 2.  
User dùng browser(client) upload file lên website (file raw)  

Client đọc file upload, convert dữ liệu ra định dạng mong muốn (json),  

Client gửi dữ liệu json này lên server (không gửi file raw)  

Server đọc dữ liệu json gửi lên, xử lý, lưu dữ liệu vào database  

Server trả về kết quả cho Client  

html input accept excel  
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#accept  

https://stackoverflow.com/questions/11832930/html-input-file-accept-attribute-file-type  
-csv  

antd upload without action  

- upload component (with drag/drop)  
https://ant.design/components/upload#upload-demo-drag  

Cần custom upload component:  
- custom request (without upload)  
- accept only excel file  
- single file

<!-- pdf-page:55; printed-page:54 -->

<a id="pdf-page-55"></a>

## PDF page 55 · Trang in 54

### Video #53 — Read File Excel

Tài liệu:  
https://www.npmjs.com/package/exceljs  

Bước 1: cài đặt thư viện  

npm i --save-exact exceljs@4.4.0  

Bước 2: Read file excel  
- input: file excel  
- output: json object  

Tải file excel mẫu tại đây  
Link backup  

1.js file to excel  
import { Buffer } from 'buffer';  
https://stackoverflow.com/a/78535489  

2.excel file to json  
https://stackoverflow.com/a/69895611  

**3.đóng modal, reset data**

<!-- pdf-page:56; printed-page:55 -->

<a id="pdf-page-56"></a>

## PDF page 56 · Trang in 55

### Video #54 — Bài tập Chức năng Import User

API bulk create:  
POST http://localhost:8080/api/v1/user/bulk-create  

truyền thêm password (mặc định)  

### Video #55 — Download Sample File

Bước 1: JavaScript download file  
https://stackoverflow.com/a/31989444  

Bước 2: Khai báo type khi sử dụng Excel  
`//todo`
https://stackoverflow.com/a/51163365  

Bước 3: Import file Excel  
https://github.com/vitejs/vite/discussions/8271  

Lưu ý:  
For those who just want a URL that point to the origin file,  
append ?url at the end of the file path: import continentsCSV from  
'../../assets/SixContinentFirst.csv?url'.  

Link docs: https://vitejs.dev/guide/assets.html#explicit-url-imports

<!-- pdf-page:57; printed-page:56 -->

<a id="pdf-page-57"></a>

## PDF page 57 · Trang in 56

### Video #56 — Bài tập chức năng Export User (CSV)

**1.Tại sao csv, không phải excel ?**
`//todo`

**2.Export to CSV**

Cài đặt thư viện:  
npm i --save-exact react-csv@2.2.2  
npm i --save-exact --save-dev @types/react-csv@1.1.10  
https://www.npmjs.com/package/react-csv  

Bước 1: chuẩn bị data (array of object)  

Bước 2: download file  

### Video #57 — Bài tập chức năng Update User

Yêu cầu: cập nhật thông tin fullName và phone của user  

API update:  
PUT http://localhost:8080/api/v1/user

<!-- pdf-page:58; printed-page:57 -->

<a id="pdf-page-58"></a>

## PDF page 58 · Trang in 57

### Video #58 — Bài tập chức năng Delete User
Tài liệu: https://ant.design/components/popconfirm  

API delete user:  
DELETE http://localhost:8080/api/v1/user/ID-USER  

### Video #59 — Tổng kết về chapter

Các component đã sử dụng:  

- Table (với Paginate) : hiển thị danh sách người dùng  

- Form, Modal : create/update user  

- Drawer, Description: view detail user  

- Popover : delete user  

- Upload (with drag/drop): bulk create  

- Avatar/Dropdown: header  

Tập thói quen đọc document và đọc ngược lại source code thư viện (kết hợp với google)  

Bonus: bổ sung các tip/trick hay dùng với table (cách render custom data). Ví dụ với  
date chẳng hạn
