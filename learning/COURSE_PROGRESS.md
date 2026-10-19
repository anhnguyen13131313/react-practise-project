# COURSE_PROGRESS — single source for current lesson

## Course
- Title: React.js Thực Chiến — Luyện Tập Bài Test Fresher React (TypeScript), Hỏi Dân IT / Eric.
- **Active video:** #32 — Bài tập chức năng Register.
- Chapter: 4 — Module Auth.
- Reference: `course-materials/chapters/chapter-04-auth.md`.
- **Lesson status (#32):** COMPLETED (2026-10-19).
  - [x] Gọi API register qua axios customize (`src/services/api.ts`).
  - [x] Thông báo lỗi/thành công qua Antd App (`App.useApp()` + `message`).
  - [x] Đăng ký thành công redirect về `/login` bằng `useNavigate`.
  - [x] Đã bọc `<App>` trong `main.tsx` đúng chuẩn Antd v5.
  - [x] Quản lý loading button khi submit (`isSubmit`).
- **Next lesson:** #33 — Debug Ứng Dụng React Chuyên Nghiệp (Extra) / #34 — Bài tập Chức Năng Login (do NOT activate automatically).

## Video #29 — acceptance criteria (SOURCE: course guide)
Legend: [x] = SOURCE_REVIEWED in code; [~] = code present, runtime NOT verified.
- [x] `/register` route exists and renders a page (`src/main.tsx`).
- [x] Registration UI is designed using Ant Design Form.
- [x] Exactly 4 fields as in Postman Body (student screenshot): `fullName`, `email`, `password`, `phone`.
- [~] Required values cannot be submitted empty (`required: true` on all 4).
- [~] Email rejects invalid email format (`type: "email"`).
- [~] Submit makes the values of all entered inputs available (`onFinish` + `console.log`).
- Extra (teacher's hint): TypeScript `interface FieldType`; layout like sample.

## Understanding goals (separate from task pass/fail)
- [ ] Student demonstrates what `Form.Item` does in this project.
- [ ] Student explains where form values are stored / how onFinish receives them.
- [ ] Student traces one input-to-submit path.
- [ ] Student distinguishes TS type declarations from actual runtime validation when relevant.

## Notes on verification
- **Confirmed by student:** currently learning video #29.
- **Not confirmed:** progress within exercise, actual Postman fields, current repo structure, running UI behavior.
- Never mark a criterion checked without concrete evidence. Use `learning/LEARNING_JOURNAL.md` for individual attempts and partial milestones.
