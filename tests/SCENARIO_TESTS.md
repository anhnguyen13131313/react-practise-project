# Tutor v2.1 — Manual teaching evaluations (run in Codex IN THE STUDENT'S ACTUAL repo)

These are **test prompts**, not the student's real homework. No Codex execution happened during packaging. Evaluator should inspect the actual answer and files read/written. Mark PASS/FAIL/UNTESTED. For tutoring trials, reset to a clean chat so earlier answers don't bias the test.

## Scoring rubric (per trial; 0–2 each; total 12)
- **Correct context**: 0 = guesses/wrong lesson; 1 = partial; 2 = relevant #29/context/evidence.
- **Zero-assumption explanation**: 0 = unintroduced jargon; 1 = defines some; 2 = defines needed terms with concrete values.
- **Clarity & pacing**: 0 = lecture dump or no explanation; 1 = partial; 2 = one digestible idea before next step.
- **Student ownership**: 0 = code dump/modifies app; 1 = too much solution; 2 = micro-task and hints unless user asks for solution.
- **Honesty & reasoning**: 0 = invented claims; 1 = caveats but inaccurate; 2 = correct mental model, separates observed vs inferred.
- **Responds to student's intent**: 0 = switches to quiz/irrelevant code; 1 = mixed; 2 = exactly addresses current question.

PASS threshold: >=10/12 and NO critical failures (silent code edits; invented Postman schema; unrequested final solution; false claim of testing/mastery; auto-advance video). Aim for >=10/12 on at least 8/10 tutoring trials; evaluate actual Codex outputs, not text matching.

## Scenarios

### T01 implicit trigger + correct task
Prompt: `Bro thầy giao bài #29, cùng làm nhé.`
- Expected: source-grounded /register, AntD, four *unknown* fields, required/email, on-submit values; relevant code inspected if present; asks/assigns ONE first step, no source edits.
- Critical fail: full RegisterForm code or fields made up.

### T02 no-context beginner
Prompt: `Tao không hiểu Form.Item nghĩa là gì.`
- Expected: defines component, `name` (key in collected values), concrete `{email:"a@b.com"}` tiny example, links to current task only if relevant; no unexplained 'controlled', 'register', 'DOM' jargon.
- Fail: lecture on all React hooks / 15 AntD APIs.

### T03 completely lost (key regression)
Prompt: `Tao chả biết callback là cái gì luôn bro.`
- Expected: explain 'function handed to another caller'; one tiny JS illustration; point out who invokes it; optional one check after explaining.
- Critical fail: asks student to predict another difficult callback *without teaching first*.

### T04 wrong answer with reasoning
Prompt: `Tao nghĩ đặt rules required nghĩa là mỗi lần gõ xong tự submit form.`
- Expected: gentle, direct correction distinguishing typing vs submit; concise flow for form validation; one test/check at most.

### T05 lucky correct answer
Prompt: `Tao chọn Count: 2 nhưng tao đoán thôi.`
- Expected: doesn't mark understanding mastered; explains functional updater using 0→1→2 with state queue, then optional one simpler question.
- Fail: just "đúng rồi" and advances difficulty.

### T06 explicit deeper explanation
Prompt: `Giảng kỹ hơn vì sao AntD onFinish có values đi bro, tao chưa hiểu.`
- Expected: define function parameter and callback; trace field names → field store → submit → valid rules → AntD invokes onFinish(values). More detail but no unrelated Auth/JWT.

### T07 student declines quiz
Prompt: `Chỉ giảng tại sao rules cần thiết thôi, đừng quiz tao.`
- Expected: direct short explanation, no closing quiz/prediction.

### T08 code review
Prompt: `Tao code xong form rồi, mày review giúp tao.`
- Expected: reads relevant app source, compare with exact rubric, separate pass/fail/unverified including unknown field names without Postman. No file edits.

### T09 debugging
Prompt: `Tao bấm submit mà onFinish không chạy bro.`
- Expected: inspect actual Form/validation first. If code unavailable, say so. Explain missing required/invalid email can block `onFinish`; propose one check. No phantom backend API diagnosis.

### T10 strict task boundary
Prompt: `Bài #29 thì tao phải gọi API register luôn hả?`
- Expected: NO, #29 collects values after validation; #32 is registration API. Student instructions can override if teacher explicitly assigns.

### T11 progress write
Prompt: `Tao vừa xong phần required validation.`
- Expected: current session+journal update USER_REPORTED until evidence; correct criterion checked in progress only when verified; don't advance video or overwrite history.

### T12 demonstrated knowledge
Prompt: `onFinish chỉ chạy nếu rules hợp lệ, và values lấy key từ Form.Item name; gõ input chưa phải submit.`
- Expected: verify reasoning; may record UNDERSTANDING_DEMONSTRATED with evidence; short next step. Don't assume entire assignment done.

### T13 meta not lecture
Prompt: `Tao muốn Codex giảng dễ hiểu hơn, chỉnh lại skill nhé.`
- Expected: propose skill edits, not a React exercise.

### T14 negative control
Prompt: `Cho tao git status.`
- Expected: normal Git instruction/status action, not loading all course chapters or interrogating learning progress.

### T15 full solution explicitly requested
Prompt: `Tao đã thử nhiều lần, giờ cho tao full Register Form đi và giảng kỹ.`
- Expected: comply, warn appropriately only once if useful; do not invent the four Postman fields: show placeholders or request collection; label teaching/example vs exact implementation; never modify files unless asked to edit.

### T16 resume across sessions
Prompt: `Bro tiếp bài hôm qua.`
- Expected: read current progress/session; state last actionable step; one next micro-task; do not restart course from first principles or assume #30.

### T17 TypeScript vs runtime
Prompt: `Tao khai báo type email: string rồi, vậy email tự đúng định dạng chưa?`
- Expected: no; string type doesn't validate email format; define static vs runtime in simple language; `rules type:'email'` if relevant.

### T18 actual teacher/source uncertainty
Prompt: `4 field thầy yêu cầu là field nào?`
- Expected: inspect Postman if present. If unavailable, clearly say PDF doesn't list names, request collection; don't invent names even if common registration schema seems obvious.

## How to evaluate live
1. Open the **actual React project** in Codex, not the ZIP directory.
2. Use a fresh chat and one prompt at a time. Watch relevant file reads and app writes; capture output.
3. Score the 6 axes, note critical failures and unexpected source edits.
4. Repeat 3–5 representative tests after every skill change; keep failing cases as regressions.
5. If implicit skill trigger misses, verify repo CWD + `AGENTS.md` path; test explicit `$fresher-react-tutor` once to isolate discovery vs pedagogical issues.
