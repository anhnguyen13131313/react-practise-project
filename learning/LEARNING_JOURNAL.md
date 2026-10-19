# LEARNING_JOURNAL — append-only meaningful milestones

> Append only on completed steps, reviews, newly established issues, lesson changes or pause/handoff. Mark evidence level: USER_REPORTED / SOURCE_REVIEWED / BEHAVIOR_VERIFIED / UNDERSTANDING_DEMONSTRATED. Avoid duplicating events.

## Initial checkpoint (2026-10-16)
- User confirmed studying **video #29** of React Test Fresher TS.
- Evidence: USER_REPORTED.
- Nothing else was claimed complete; no source code was inspected.
- Next: inspect current React project and Postman fields before tutoring the register form task.

## Video #29 code complete (2026-10-19)
- Student built the register form step by step and asked to record completion.
- Evidence: SOURCE_REVIEWED (code read in repo; Postman fields from student's screenshot). Browser behavior: **not verified**.
- Fixes along the way: import `Form`/`Input` from `antd` (was `react-router-dom`); `label` needs a value; `Input.Password` for password.
- Extras done: `interface FieldType` replaces `any`; card layout and `Divider`/`Link` like teacher's sample.
- Pending: run 3 cases in browser (empty / bad email / valid → 4 keys in Console). Understanding of `name` → `values` keys not yet demonstrated.

## Lesson change to #32 (2026-10-19)
- Student said "làm bài tập 32"; active video set to #32. Evidence: USER_REPORTED.
- Repo already has axios instance, `loginAPI`, `IBackendRes`; no `registerAPI` yet.

## Video #32 completed (2026-10-19)
- Completed register flow: `registerAPI`, custom axios instance, `useNavigate`, loading state on button.
- Updated `message` handling to modern Ant Design v5 standards: `<App>` wrapped in `src/main.tsx` and consumed via `App.useApp()` in `RegisterPage`.
- Cleaned unused imports (`loginAPI`), optimized `setIsSubmit(false)` placement.
- Evidence: SOURCE_REVIEWED & BEHAVIOR_VERIFIED (console response confirmed).
