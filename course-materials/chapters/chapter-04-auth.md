# Chapter 4 — Module Auth

> Trích từ PDF gốc, giữ các mốc số trang để kiểm tra nguồn. Đây là giáo án, không phải toàn bộ lời nói của thầy.

> **Phạm vi:** PDF page 33–46.

<!-- pdf-page:33; printed-page:32 -->

<a id="pdf-page-33"></a>

## PDF page 33 · Trang in 32

## Chapter 4: Module Auth
Login/Register với Access token và Refresh token  

### Video #26 — Tổng quan về chapter

Trong khóa học này, mình sử dụng access token và refresh token để xác thực người  
dùng (stateless).  

Access token lưu ở Local Storage vì:  
      -  Tiện cho việc truy cập và sử dụng. Chỉ cần dùng javascript là truy cập được,  
      thông qua method localStorage.getItem()  
      -  Thời gian sống của access token là ngắn, vì vậy, nếu có bị lộ token, nó cũng  
     không nguy hiểm (do data lưu ở local storage tồn tại mãi mãi, nên có xác suất bị  
       lộ token. Tuy nhiên xác suất này khá nhỏ)  

Refresh token lưu ở cookies vì:  
      -  Cookies sau 1 thời gian nhất định sẽ tự động hết hạn (tự động xóa dữ liệu lưu ở  
      cookies)  
      -  Cookies cho phép cấu hình để chặn truy cập cookies bằng javascript (thuộc tính  
httpOnly)  
      -  Thời gian sống của Refresh token lâu hơn access token. Lưu ở cookies sẽ giảm  
       thiểu rủi ro.  

Về cơ chế access token/refresh token, bạn nào muốn học sâu, thì học thêm backend  
nhé. Mình để cập các kiến thức này ở đấy.  

Tham khảo backend Nestjs tại đây

<!-- pdf-page:34; printed-page:33 -->

<a id="pdf-page-34"></a>

## PDF page 34 · Trang in 33

### Video #27 — Cài đặt thư viện UI Antd - Ant Design
Tài liệu: https://ant.design/docs/react/introduce  

Cài đặt antd:  
npm install --save-exact antd@5.21.6 @ant-design/icons@5.5.1  

antd: thư viện UI viết sẵn React Component  
ant-design/icons : thư viện icons  
**1. Tại sao dùng antd**
- Giúp design nhanh giao diện responsive thông qua component, tương tự như  
react-bootstrap  
https://ant.design/components/overview/  

**2. Controlled vs Uncontrolled component**
controlled: dữ liệu của component được lưu vào state của React  
uncontrolled: dữ liệu được lưu vào DOM (HTML)  

Ví dụ về controlled component: form login sử dụng state để lưu giá trị input  

Ví dụ uncontrolled component:  
https://react-hook-form.com/  
https://formik.org/  

Với các thư viện trên, chỉ giúp validate form, không có hỗ trợ component khác.  
antd hỗ trợ tất cả điều trên. amazing :v  

**3. Trade off**
Khối lượng bundle của antd lớn, cần tối ưu khi sử dụng  
=> thường dùng làm admin  

v5.3.1 => unpacked size = 51.1 MB  
bootstrap v5.2.3 = 9.1 MB

<!-- pdf-page:35; printed-page:34 -->

<a id="pdf-page-35"></a>

## PDF page 35 · Trang in 34

### Video #28 — Giới Thiệu Form Component

**1. Các vấn đề tồn đọng**
ví dụ về controlled component:  

```typescript
const LoginForm = () => {  

      const [email, setEmail] = useState("")  
      const [password, setPassword] = useState("")  

      return (  
                 <input value={email} onChange={(e)=> setEmail(e.target.value)}/>  
                 <input value={password} onChange={(e)=> setPassword(e.target.value)}/>  
          );  

}  
```

- Nhược điểm của cách làm trên:  
+ Chưa tối ưu hóa việc validate dữ liệu  
+ Bị render nhiều lần (khi form có nhiều dữ liệu cần nhập) => dẫn tới giật/lag  

=> đấy là lý do react hook form/formik ra đời  

Tuy nhiên, formik hay react hook form chỉ làm được form, phần còn lại của UI không làm  
được  

**2. Form component của Antd**
Tài liệu: https://ant.design/components/form

<!-- pdf-page:36; printed-page:35 -->

<a id="pdf-page-36"></a>

## PDF page 36 · Trang in 35

### Video #29 — Bài tập Design Register Form

Yêu cầu :  
- Tạo mới trang /register để đăng ký tài khoản mới  

- Giao diện tự thiết kế theo thẩm mỹ, sử dụng Antd Form  

- Gồm 4 fields như api postman  

- Validate dữ liệu không được để trống. Email có định dạng hợp lệ  

- Khi submit form, lấy được hết dữ liệu nhập tại input  

Gợi ý: sử dụng với TypeScript và làm theo ví dụ mẫu.

<!-- pdf-page:37; printed-page:36 -->

<a id="pdf-page-37"></a>

## PDF page 37 · Trang in 36

### Video #30 — Axios và Axios Customize (Part 1)

Tài liệu:  
https://www.npmjs.com/package/axios  

Cài đặt:  
npm install --save-exact axios@1.7.7  

**1. Tại sao cần customize Axios ?**
- Tập trung config lại 1 file  
- Can thiệp vào request (trước khi gửi lên server backend)  
- Can thiệp vào response (trước khi trả về cho client)  

**2. Sử dụng Axios với Typescript**

//setup instance  
https://github.com/axios/axios#creating-an-instance  

//sử dụng .env với Vite:  
https://vite.dev/guide/env-and-mode  

//cấu hình interceptor  
https://github.com/axios/axios?tab=readme-ov-file#interceptors  

//setup typescript for axios  
// https://github.com/axios/axios/issues/1510#issuecomment-448201698  

//axios.d.ts  
import axios from 'axios';  
declare module 'axios' {  
  export interface AxiosResponse<T = any> extends Promise<T> { }  
}

<!-- pdf-page:38; printed-page:37 -->

<a id="pdf-page-38"></a>

## PDF page 38 · Trang in 37

//định nghĩa global type  
https://bobbyhadz.com/blog/typescript-make-types-global#declare-global-types-in-type  
script  

//global.d.ts  
```typescript
export {};  

declare global {  
       interface IBackendRes<T> {  
          error?: string | string[];  
       message: string;  
        statusCode: number | string;  
         data?: T;  
         }  

         interface IModelPaginate<T> {  
          meta: {  
              current: number;  
             pageSize: number;  
            pages: number;  
                total: number;  
                   },  
            results: T[]  
            }  

  }  
```

<!-- pdf-page:39; printed-page:38 -->

<a id="pdf-page-39"></a>

## PDF page 39 · Trang in 38

### Video #31 — Axios và Axios Customize (Part 2)

`//todo`

### Video #32 — Bài tập chức năng Register

Yêu cầu:  
Sử dụng API: POST /api/v1/user/register  

- gọi api register thông qua axios (đã customize)  

- nếu có lỗi, thông báo lỗi  
https://ant.design/components/app  
https://ant.design/components/message  

- tạo mới thành công, redirect về trang login  

### Video #33 — Debug Ứng Dụng React Chuyên Nghiệp (Extra)

//sử dụng console.log  
//sử dụng debugger  
//sử dụng tab network  
//sử dụng breakpoint  

Chi tiết hơn, tham khảo khóa học debug của Hỏi Dân IT tại đây

<!-- pdf-page:40; printed-page:39 -->

<a id="pdf-page-40"></a>

## PDF page 40 · Trang in 39

### Video #34 — Bài tập Chức Năng Login

Yêu cầu:  
- Tự design giao diện login (tương tự như register)  

- Tạo input và validate dữ liệu (gồm 2 file username và password)  

- Gọi API login  
Sử dụng API: POST /api/v1/auth/login  

- Nếu gọi API thành công, redirect về trang chủ (/), đồng thời, lưu access_token vào  
Local Storage  

- Nếu thất bại, hiển thị thông báo lỗi  
https://ant.design/components/notification

<!-- pdf-page:41; printed-page:40 -->

<a id="pdf-page-41"></a>

## PDF page 41 · Trang in 40

### Video #35 — Access Token và Refresh Token (Extra)

Mục tiêu: bổ trợ kiến thức cho những bạn “chưa từng học” backend với mô hình  
stateless  

//thêm hiệu ứng delay khi submit api  

**1.Phân biệt LocalStorage, Session Storage và Cookies**

Local Storage, Session Storage hay Cookies, là 3 cách thông dụng nhất để lưu trữ data  
tại browser  

Local Storage: data được lưu trữ và tồn tại “forever” (vĩnh viễn). Data này chỉ bị mất, nếu  
bạn xóa nó đi. (đóng browser, tắt máy tính… không làm mất data)  

Session Storage: data được lưu trữ và tồn tại theo “phiên sử dụng” (session). Bạn đóng  
browser, là data sẽ bị xóa  

Cookies: data sẽ bị xóa theo thời gian cài đặt (expiration date). Tương tự như bom hẹn  
giờ, tới thời điểm là phát nổ.  

Cookies là con lai của 2 kiểu lưu trữ ở trên. Data sẽ bị xóa theo điều kiện nhất định.  

**2. Tác dụng của access token và refresh token**
Access token và refresh token được sử dụng trong mô hình stateless (session được sử  
dụng trong mô hình stateful)  

Hãy tưởng tượng bạn đi du lịch từ Việt Nam qua Lào:  

**1.Nước Lào không có thông tin cá nhân (CCCD) của bạn, tuy nhiên, bạn có hộ chiếu**
(passport)  

Để có hộ chiếu, bạn cần xin visa tại đại sứ quán. Nếu được duyệt => done  

Điều này tương tự với việc, bạn login, nếu thành công, bạn được cấp access token.  
Như vậy, access token (quyền truy cập) giúp định danh/xác thực bạn là ai.

<!-- pdf-page:42; printed-page:41 -->

<a id="pdf-page-42"></a>

## PDF page 42 · Trang in 41

**2.Bạn đi du lịch qua Lào, tại cửa khẩu/sân bay, bạn cần xuất trình hộ chiếu.**
Nếu hộ chiếu hợp lệ, bạn được nhập cảnh vào Lào  

Điều này tương tự, mỗi lần bạn sử dụng “tài nguyên của backend” (API), backend sẽ  
kiểm tra tính hợp lệ của “access token”  

Đấy là lý do tại sao, mỗi API, cần truyền thêm access token tại header.  

Nếu access token hợp lệ, bạn được toàn quyền sử dụng API  

**3. Hộ chiếu theo thời gian sẽ bị hết hạn, bạn cần làm mới (renew)**

Access Token sẽ bị hết hạn theo thời gian (tránh trường hợp bạn bị hacker trộm mất  
token và sử dụng ngoài ý muốn), khi này, cần sử dụng Refresh Token.  

Refresh Token giúp bạn “đổi lấy” một access token mới (với thời gian hết hạn mới)  

**3. Định dạng & nơi lưu trữ**

- Định dạng sử dụng là JWT (json web token) : jwt.io  

- Lưu access_token vào Local Storage (tiện để sử dụng, và cần set thời gian hết hạn  
ngắn). Lưu ý, không có cách nào để cập nhật token là hết hạn (sau khi đã tạo ra)  

- Lưu refresh_token vào cookies (an toàn)  

Dành cho những bạn nào muốn hiểu hơn về cách tạo ra Access Token (tương tự với  
Refresh Token) tại backend như nào, tham khảo khóa học miễn phí tại đây  

Version TypeScript (tương ứng với khóa học này), tham khảo tại đây

<!-- pdf-page:43; printed-page:42 -->

<a id="pdf-page-43"></a>

## PDF page 43 · Trang in 42

### Video #36 — Store User Login with React Context

Mục tiêu: sau khi login thành công, cần lưu thông tin user đăng nhập, sau đấy hiển thị tại  
các component khác nhau (ví dụ hiển thị tên đăng nhập tại header)  

- store user info to react context  
https://react.dev/reference/react/createContext#creating-context  

JSX children props:  
https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children  

Sử dụng với Context với typescript:  
https://react-typescript-cheatsheet.netlify.app/docs/basic/getting-started/context/

<!-- pdf-page:44; printed-page:43 -->

<a id="pdf-page-44"></a>

## PDF page 44 · Trang in 43

### Video #37 — Xử Lý F5 (Refresh page)
**1. Xử Lý Fetch Data**
- default, f5 refresh (clear) data lưu tại React => api fetch account  
GET /api/v1/auth/account  

- gán access token vào axios:  
https://stackoverflow.com/a/68162072  

lưu ý: với react 18, useEffect run twice (strict mode - không ảnh hưởng khi chạy  
production, chỉ có tại dev)  
https://github.com/facebook/react/issues/24502  

với việc sử dụng access token để xác định thông tin người dùng (và chỉ server mới  
decode được token này)  
=> cơ chế stateless  

mỗi lần f5 là react render lại từ đầu => cần gọi api để lấy lại thông tin user  

### Video #38 — Xử lý Loading

**1. Xử lý Loading**

npm install --save-exact react-spinners@0.14.1  

center screen: https://github.com/davidhu2000/react-spinners/issues/53

<!-- pdf-page:45; printed-page:44 -->

<a id="pdf-page-45"></a>

## PDF page 45 · Trang in 44

### Video #39 — Protected Page

//fix bug set Cookies (refresh token)  
Tối đa là 400 ngày:  
https://developer.chrome.com/blog/cookie-max-age-expires  

//Rule check:  
      -  Chưa đăng nhập (authentication)  
      -  Đã đăng nhập, nhưng không có quyền hạn (authorization)  

Ví dụ:  
      -  checkout page : user đặt hàng tiến hành thanh toán  

      -  create admin page (protected)  

Người dùng có Role = admin, mới có quyền vào ‘/admin’

<!-- pdf-page:46; printed-page:45 -->

<a id="pdf-page-46"></a>

## PDF page 46 · Trang in 45

### Video #40 — Bài Tập Design Layout

Cài đặt thư viện:  
npm i --save-exact react-icons@5.3.0  

Download source code thực hành tại đây  

**1. Tính năng logout**
POST /api/v1/auth/logout  
//clear LocalStorage và React Context  

**2.Phân tích source code xây dựng**
- Chia layout admin/client => design header bar/footer  

`//todo: Liệt kê ra các component của Antd đã sử dụng:`
https://ant.design/components/layout#components-layout-demo-side  

//cách hiển thị hình ảnh avatar  

### Video #41 — Tổng kết về chapter

//phần refresh token làm tại cuối khóa học (tương tự chưa xử lý trường hợp access  
token bị hết hạn)
