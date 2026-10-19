# Chapter 2 — Setup Environment

> Trích từ PDF gốc, giữ các mốc số trang để kiểm tra nguồn. Đây là giáo án, không phải toàn bộ lời nói của thầy.

> **Phạm vi:** PDF page 16–23.

<!-- pdf-page:16; printed-page:15 -->

<a id="pdf-page-16"></a>

## PDF page 16 · Trang in 15

## Chapter 2: Setup Environment
Cài đặt & chuẩn bị môi trường thực hiện dự án  

### Video #7 — Chuyện Cài Đặt Công Cụ (Bắt Buộc Xem)

**1.Mục đích**
Chương học này sẽ hướng dẫn chi tiết cách cài đặt các công cụ cần thiết để phục vụ  
cho khóa học. Vì vậy, bạn vui lòng không bỏ qua video nào, xem lần lượt theo thứ tự  

Có 2 sai lầm mà các bạn hay gặp phải, đặc biệt là những bạn “đã biết 1 chút”  

Sai lầm 1: Bỏ qua các video cài đặt công cụ vì bạn cho rằng bạn “đã biết rồi”  

Hãy nhớ rằng, cài công cụ là 1 phần, đang còn phải “cấu hình” nó nữa.  

Khóa học được sinh ra, và đã tối ưu. Bạn chỉ dành 5 tới 10 phút để xem video, đổi lại tiết  
kiệm cho bạn cả giờ đồng hồ ngồi mò mẫm.  

Sai lầm 2: Không quan tâm tới version của phần mềm  

Khi thực hiện khóa học, bạn vui lòng download và cài đặt version phần mềm giống như  
video. Điều này sẽ đảm bảo môi trường thực thi code là giống nhau. (hạn chế tối đa bug  
có thể xảy ra)  

**2. Version Phần Mềm theo thời gian**

Bạn đừng sợ phần mềm (công cụ) nó thay đổi version, hay thậm chí là “chê bai” version  
cũ. Vì vốn dĩ, công nghệ nó là vậy, luôn thay đổi theo thời gian.  

Bạn yêu cầu “version mới nhất” cho cái bạn học, mình đã làm điều đó tại thời điểm quay  
video khóa học, tuy nhiên, sẽ là cố định 1 version.  

Lý do: công nghệ sẽ cập nhật theo thời gian. Cho dù bạn muốn hay không, hoặc thậm  
chí lắp tên lửa vào đít, đuổi cũng không kịp.

<!-- pdf-page:17; printed-page:16 -->

<a id="pdf-page-17"></a>

## PDF page 17 · Trang in 16

Điều bạn cần làm là: học 1 version, và quan trọng hơn, là bạn học, bạn cần hiểu nó  

Sau đấy, nếu cần thiết, bạn học version mới hơn. Điểm khác biệt ở đây, là khi học version  
mới, bạn không phải là người bắt đầu từ số 0 (do đã có base từ version cũ)  

Chỉ không học version cũ khi và chỉ khi: sản phẩm của version cũ không dùng được  

Đấy là lý do tại sao các khóa học của mình, khi học xong, mình mới hướng dẫn nâng cấp  
version.

<!-- pdf-page:18; printed-page:17 -->

<a id="pdf-page-18"></a>

## PDF page 18 · Trang in 17

### Video #8 — Cài đặt Node.js

Tài liệu: https://nodejs.org/en  

**1.Nodejs là gì ?**
Nodejs không phải là thư viện (library), không phải framework của javascript.  

Nodejs là môi trường để bạn thực thi code javascript, tại browser và server.  

Bạn học React (viết bằng Javascript), nên bạn cần Nodejs để có thể chạy được nó (code  
javascript)  

Điều này tương tự với:  

Bạn học cách sử dụng Microsoft Excel (react)  
Bạn cần cài hệ điều hành Windows để có thể học nó (nodejs)  

**2. Cài đặt Nodejs**
Sai lầm của beginners, là không quan tới tới version của phần mềm. Nên nhớ, công nghệ  
nó thay đổi theo thời gian, vì vậy, để hạn chế tối đa lỗi tối đa, bạn nên dùng version phần  
mềm như khóa học hướng dẫn.  

Điều này tương tự với:  
Bạn đang chơi 1 con game rất ngon trên Windows 7, bạn vác lên Windows 10 để chạy,  
có điều gì để đảm bảo rằng “sẽ không có lỗi xảy ra” ?  

Trong khóa học này, mình sử dụng version Node.js là 20.14.0.  

Vì vậy, để hạn chế tối đa lỗi có thể xảy ra, bạn vui lòng cài đặt chính xác version nodejs ở  
trên  

Khi code giống nhau, môi trường thực thi code giống nhau (version nodejs), thì rất hiếm  
khi lỗi xảy ra.

<!-- pdf-page:19; printed-page:18 -->

<a id="pdf-page-19"></a>

## PDF page 19 · Trang in 18

Link tải nodejs v20.14.0:  
https://nodejs.org/download/release/v20.14.0/  

Sau khi cài đặt xong, kiểm tra bằng cách gõ câu lệnh:  

node -v  

**3. Trường hợp dùng nhiều version Nodejs**
//áp dụng cho windows  
https://github.com/coreybutler/nvm-windows  

Video hướng dẫn cài nvm cho window, xem tại đây  

//áp dụng cho macos  
Video hướng dẫn cài nvm cho mac, xem tại đây  

https://dev.to/ajeetraina/how-to-install-and-configure-nvm-on-mac-os-5fgi

<!-- pdf-page:20; printed-page:19 -->

<a id="pdf-page-20"></a>

## PDF page 20 · Trang in 19

### Video #9 — Cài đặt Visual Studio Code
Công cụ code trong dự án sử dụng VSCode, 1 Editor hoàn toàn miễn phí  

Link download:  
https://code.visualstudio.com/download  

### Video #10 — Cấu hình Visual Studio Code
**1. Format Code**
Setup Format on Save  
Mục đích: Mỗi lần nhấn Ctrl + S , code sẽ được auto format trông cho đẹp/dễ nhìn  

**2. Cài đặt Extensions**

Lưu ý: off các extension như eslint, prettier … để tránh xung đột  
Fact: đi làm, người ta cấu hình eslint, prettier..thông qua code, vì mỗi 1 dự án (1 khách  
hàng 1 yêu cầu), cài global qua extension thì cái nào cũng giống cái nào  

Đồng thời, với rule trên sẽ đảm bảo mọi thành viên trong team sẽ có cấu hình giống  
nhau  

Các extensions cài đặt thêm:  
- Code Spell Checker : hỗ trợ check chính tả khi đặt tên tiếng anh  

- Auto Complete Tag : hỗ trợ code nhanh HTML

<!-- pdf-page:21; printed-page:20 -->

<a id="pdf-page-21"></a>

## PDF page 21 · Trang in 20

### Video #11 — Tại sao mình dùng VScode ?

Có rất nhiều IDE hỗ trợ bạn code React (Javascript):  
      -  Visual Studio Code (gọi tắt là VSCode)  
      -  WebStorm  
      -  Sublime Text  
      -  Notepad, Notepad ++ 😂  

IDE/Editor thực chất là công cụ code, giúp gợi ý code và phát hiện lỗi  
=> dùng công cụ code nào mà bạn "thoải mái nhất"  

Mình chọn VScode vì:  
- miễn phí (nếu bạn code Frontend thì chắc chắn bạn sẽ thích)  
- có gợi ý code và phát hiện lỗi  
- theme dark :v  
- hỗ trợ git out-of-the-box  
- support mạnh mẽ cho "frontend" => tức là 1 IDE cho cả frontend/backend  

Trong khóa học này, chỉ cần bạn code giống mình, dùng IDE nào không quan trọng,  
điều quan trọng, chính là cách chúng ta code ra làm sao :v  

Recommend: dùng VScode, để đảm bảo bạn và mình giống nhau 100%, từ coding cho  
tới debug :v  

Yên tâm 1 điều là: điều quan trọng nhất chính là khả năng bạn “tư duy” (mindset), bạn  
có thể dùng những điều học được, để áp dụng sang IDE bạn thích.  

Fact: mình đã từng rơi vào công ty (khá to), cơ mà không mua license bản quyền phần  
mềm (trong khi không cho dùng crack)  
=> bắt buộc phải dùng các công cụ free @@

<!-- pdf-page:22; printed-page:21 -->

<a id="pdf-page-22"></a>

## PDF page 22 · Trang in 21

### Video #12 — Cài đặt và sử dụng Git
- Nếu bạn chưa biết gì về Git, xem nhanh tại đây  

- Sử dụng Git theo nguyên tắc:  
**1. Học xong video nào, commit đẩy lên Github/Gitlab**
=> tạo cơ hội để thực hành câu lệnh của Git, ví dụ:  
git add  
git commit  
git push...  

**2. Git là công cụ "mặc định bạn phải biết" khi đi làm phần mềm**
=> điều 1 ở trên giúp bạn thực hành  

**3. Thói quen học xong video nào, đẩy code lên Git, giúp bạn tạo ra bản "backup" cho**
project của bạn  

Ví dụ máy tính bạn bị hỏng đột xuất/bị mất  
=> vẫn còn code, chỉ cần pull về code tiếp mà không phải code từ đầu.  

**4. Trong trường hợp bạn bị bug**
=> bạn có thể gửi link github/gitlab cho mình xem => support fix bug  

=> Mục đích sử dụng git ở đây là : backup code + thực hành công cụ đi làm mà bạn  
"phải biết" nếu muốn đi thực tập/đi làm.

<!-- pdf-page:23; printed-page:22 -->

<a id="pdf-page-23"></a>

## PDF page 23 · Trang in 22

### Video #13 — Cài đặt Google Chrome

Ở đây, sử dụng google chrome vì nó là ứng dụng phổ biến nhất (trình duyệt web được  
dùng nhiều nhất)  

Bạn nên dùng Google Chrome (thay vì Firefox/Edge…) để đảm bảo rằng thao tác sử  
dụng giữa bạn và mình là giống nhau (tránh gây khó khăn không cần thiết)  

Lưu ý: sử dụng version tiếng anh  
=> change language  

Mục tiêu:  
      -  Sử dụng Google Chrome để chạy ứng dụng web  

      -  Ngôn ngữ hiển thị là Tiếng Anh  

      -  Set default app là google chrome (nếu nó mở app, thì chạy với google chrome)  

    Xem hướng dẫn setup default app cho windows tại đây
