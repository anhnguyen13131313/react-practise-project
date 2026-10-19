# Chapter 6 — Module Books

> Trích từ PDF gốc, giữ các mốc số trang để kiểm tra nguồn. Đây là giáo án, không phải toàn bộ lời nói của thầy.

> **Phạm vi:** PDF page 59–69.

<!-- pdf-page:59; printed-page:58 -->

<a id="pdf-page-59"></a>

## PDF page 59 · Trang in 58

## Chapter 6: Module Books
Xây dựng giao diện client/admin về CRUD Books  

### Video #60 — Tổng quan về chapter
`//todo`

### Video #61 — Bài tập Hiển Thị/Filter/Sort Books

todo: tương tự như chức năng users  

API sử dụng:  
GET http://localhost:8080/api/v1/book?current=1&pageSize=10  

(truyền thêm filter và sort nếu cần thiết)

<!-- pdf-page:60; printed-page:59 -->

<a id="pdf-page-60"></a>

## PDF page 60 · Trang in 59

### Video #62 — Bài tập design chức năng xem chi tiết Book

Mục tiêu:  
      -  Hiển thị các thông tin cơ bản của sách  
      -  Tích hợp component hiển thị danh sách hình ảnh  

Gợi ý cách làm:  
- Sử dụng component upload để hiển thị ảnh  
https://ant.design/components/upload#upload-demo-picture-card  

- Để hiển thị ảnh => sử dụng base64  
https://ant.design/components/image  

- customize để ko hiển thị icon remove => showUploadList  

### Video #63 — Hoàn thiện chức năng xem chi tiết Book

Cài đặt thư viện: https://www.npmjs.com/package/uuid  
npm install --save-exact uuid@11.0.3  

- hiển thị hình ảnh với url từ backend  

- merge images thành list images

<!-- pdf-page:61; printed-page:60 -->

<a id="pdf-page-61"></a>

## PDF page 61 · Trang in 60

### Video #64 — Design Form Add New Book

Yêu cầu:  
Tạo form thêm mới sách:  
      -  Hiển thị giá tiền với format  
https://ant.design/components/input-number  

      -  Hiển thị category với Select component  
      API get category: GET http://localhost:8080/api/v1/database/category  

     sử dụng component Select: https://ant.design/components/select  

      -  Hiển thị form upload (single/multiple), đồng thời validate (kiểu file và file size)  
https://ant.design/components/upload  
https://ant.design/components/upload#upload-demo-avatar  

Mục tiêu: submit form, lấy được data trên form  

Lỗi 1: Warning: [antd: Upload] value is not validate prop, do you mean fileList?  
https://ant.design/components/form#why-cant-switchcheckbox-bind-data  

Normal file upload với antd:  
https://github.com/ant-design/ant-design/issues/21563

<!-- pdf-page:62; printed-page:61 -->

<a id="pdf-page-62"></a>

## PDF page 62 · Trang in 61

### Video #65 — Bài tập Upload File

API Upload Images  
POST http://localhost:8080/api/v1/file/upload  

trong đó:  
Header truyền thêm 'upload-type' = book  

data body truyền theo định dạng form-data:  
fileImg: file ảnh raw upload  

```typescript
export const callUploadBookImg = (fileImg) => {  
  const bodyFormData = new FormData();  
  bodyFormData.append('fileImg', fileImg);  
  return axios({  
    method: 'post',  
      url: '/api/v1/file/upload',  
    data: bodyFormData,  
    headers: {  
       "Content-Type": "multipart/form-data",  
       "upload-type": "book"  
       },  
   });  
}  
```

<!-- pdf-page:63; printed-page:62 -->

<a id="pdf-page-63"></a>

## PDF page 63 · Trang in 62

//Prevent showing failed uploaded images:  
https://ant.design/components/upload#upload-demo-upload-png-only  

 return isJpgOrPng && isLt2M || Upload.LIST_IGNORE;  

//import type  
https://github.com/ant-design/ant-design/issues/28713#issuecomment-789154925  

//controlled component  
https://ant.design/components/upload#upload-demo-filelist  

Yêu cầu:  
- sau khi upload file thành công  
=> lưu vào state của react (cần lưu vào state react để submit form)  

- handle remove file  

- khi close modal => reset form  

### Video #66 — Bài tập Create a New Book
`//todo`
API Create Book  
POST http://localhost:8080/api/v1/book

<!-- pdf-page:64; printed-page:63 -->

<a id="pdf-page-64"></a>

## PDF page 64 · Trang in 63

### Video #67 — Bài tập Update a Book

- ý tưởng: clone create book  
- add initial data  
- build file list (control with state)  
- truyền thêm _id cho api  

API Update Book  
PUT http://localhost:8080/api/v1/book/id-book  

### Video #68 — Bài tập Delete a Book & Export Data

Yêu cầu :  
**1. Delete a book**
     Lưu ý: tạo mới book, rồi xóa book đấy. Vì phần data book này sẽ hiển thị tại client  

      API sử dụng:  

     DELETE http://localhost:8080/api/v1/book/id-book  

**2. Export books dưới dạng .csv**

<!-- pdf-page:65; printed-page:64 -->

<a id="pdf-page-65"></a>

## PDF page 65 · Trang in 64

### Video #69 — Bài tập Design Giao Diện Client (homepage)
Yêu cầu:  
- category (filter)  
- list book  
- lưu ý: có paginate  

- design base giao diện (hardcode dữ liệu)  

Các component sử dụng:  
https://ant.design/components/checkbox#checkbox-demo-group  

https://ant.design/components/rate  

https://ant.design/components/tabs  

https://ant.design/components/pagination

<!-- pdf-page:66; printed-page:65 -->

<a id="pdf-page-66"></a>

## PDF page 66 · Trang in 65

### Video #70 — Bài Tập Hiển Thị HomePage
Sử dụng các API sau:  
- API get category: GET http://localhost:8080/api/v1/database/category  

- API get list book (with paginate)  
GET http://localhost:8080/api/v1/book?current=1&pageSize=10  

- thêm component loading:  
https://ant.design/components/spin#spin-demo-tip  

### Video #71 — Bài tập Filter/Sorter HomePage

- update tabPane -> order by query  

- làm reset filter  

- filter by category and price:  
https://www.npmjs.com/package/api-query-params  
Toán tử $in, $lte, $gte

<!-- pdf-page:67; printed-page:66 -->

<a id="pdf-page-67"></a>

## PDF page 67 · Trang in 66

### Video #72 — Bài tập Design View Detail Page (Part 1)
Yêu cầu:  
Bước 1: Tạo url ứng với xem chi tiết từng book  
Ví dụ: (1, 2, 3 là id của book)  
http://localhost:3000/book/1  
http://localhost:3000/book/2  
http://localhost:3000/book/3  

Bước 2: Lấy thông tin id của book  
https://reactrouter.com/en/main/hooks/use-navigate  

Id lấy trực tiếp từ Url: https://reactrouter.com/en/main/hooks/use-params  

Kết thúc bước 2, đã có được id của sách cần hiển thị  

Bước 3: Design giao diện chi tiết (hardcode dữ liệu)  
Cài đặt thư viện:  
npm i --save-exact react-image-gallery@1.3.0  
npm i --save-exact --save-dev @types/react-image-gallery@1.2.4  

https://www.npmjs.com/package/react-image-gallery  

Lưu ý về import scss:  
https://github.com/twbs/bootstrap/issues/40962#issuecomment-2448214806  

//vite.config.ts  
 css: {  
  preprocessorOptions: {  
   scss: {  
     api: 'modern-compiler', // or "modern"  
    silenceDeprecations: ['mixed-decls', 'color-functions', 'global-builtin', 'import']  
    }  
   }  
 }

<!-- pdf-page:68; printed-page:67 -->

<a id="pdf-page-68"></a>

## PDF page 68 · Trang in 67

### Video #73 — Bài tập Design View Detail Page (Part 2)

Bước 1: Lấy thông tin của Book theo id  
- API get book: GET http://localhost:8080/api/v1/book/id-book  

Bước 2: Build động data image  
`//todo`

### Video #74 — Thêm Loading Skeleton

Có nhiều thư viện hỗ trợ tạo skeleton:  

https://www.npmjs.com/package/react-content-loader  

https://www.npmjs.com/package/react-loading-skeleton  

hoặc sử dụng antd: https://ant.design/components/skeleton

<!-- pdf-page:69; printed-page:68 -->

<a id="pdf-page-69"></a>

## PDF page 69 · Trang in 68

### Video #75 — Tổng kết về chapter
`//todo`
- fix bug trên giao diện mobile  

//nguyên tắc khi code giao diện:  
- Design base (html-css)  
- Write react:  
+ (chia component nếu cần thiết)  
+ handle logic (xử lý các function và thao tác của người dùng)
