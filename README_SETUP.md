# Codex React Fresher Tutor — v2.1 (Teaching QA edition)

## TL;DR
**Active course:** Hỏi Dân IT / Eric — React.js Thực Chiến, luyện tập bài test Fresher React (TypeScript).
**Active lesson:** video #29 — Design Register Form; source of truth `learning/COURSE_PROGRESS.md`.
This is a **tutoring overlay**, not a React replacement project. It does not change `src/`, `package.json`, backend or environment.

## Installation into your existing React project
Unzip **the contents**, and copy to the project root (same folder as its `package.json`). The `AGENTS.md` must be at the repo root Codex is opened in.

```text
YOUR-REACT-REPO/
├── AGENTS.md                      # routes study questions into tutor skill
├── .agents/skills/fresher-react-tutor/
│   ├── SKILL.md                   # modes and instructional contract
│   └── references/
│       ├── TEACHING_PLAYBOOK.md   # important: when student doesn't understand
│       ├── TRACING_AND_DEBUGGING.md
│       ├── LESSON_29_ANTD_FORM.md # current homework specific, on-demand
│       └── PROGRESS_UPDATES.md
├── course-materials/             # PDF, converted MD, chapter index
├── learning/                     # progress + session + knowledge + journal
├── tests/                        # manual teaching eval prompts + structural test
├── package.json                  # existing app, not modified by overlay
└── src/                          # existing app, not modified by overlay
```

### Already installed v2? Recommended **patch ZIP**
Use `Codex_React_Fresher_Tutor_v2_1_PATCH.zip` and copy its `AGENTS.md`, `.agents/skills/fresher-react-tutor/` and `tests/` into your React project. Back up or merge `AGENTS.md` if you have unrelated existing instructions.

**Do not overwrite `learning/` with any installation archive if you have already used Codex.** Keep past progress and knowledge records; the patch has no `learning/` files. The patch also does not replace course materials, which are unchanged.

### Fresh install?
Use `Codex_React_Fresher_Tutor_v2_1_FULL.zip`. It contains the entire tutor overlay, including course Markdown and PDF, plus starter learning records. Only use the starter `learning/` files on first install.

### Privacy / copyright
PDF and its Markdown conversion are for personal course study. For a PUBLIC repository, add `/course-materials/` to `.gitignore` (and `/learning/` too if you want notes private). Do not publish course material or secrets. Avoid putting credentials inside progress/journal.

## Trigger model (no special prompt)
- `AGENTS.md` is the always-applicable repo-level route when Codex works from this root.
- The skill description also helps Codex discover appropriate tutoring requests.
- The tutor reads the current checkpoint, specific video section and relevant code only when those are necessary; NOT all 83 pages on every short question.
- Manual explicit fallback if your Codex version misses a trigger: `Dùng $fresher-react-tutor để giúp tao bài này`.
- Triggers are instruction-following, not a guaranteed executable event hook.

## Test examples
- `Bro tao đang học #29, thầy giao Design Register Form; cùng làm nhưng đừng code hộ.`
- `Tao không biết callback là gì, giải thích từ gốc đi.`
- `Tao bấm submit mà onFinish không chạy; xem code tao và giúp trace.`
- `Tao làm xong validation rồi, kiểm tra và cập nhật tiến độ.`
- `Tao chỉ muốn chỉnh cách mày dạy, không học bài lúc này.`

## How progress updates work
Only these files are authorized for meaningful milestone updates:
- `learning/CURRENT_SESSION.md`: last checkpoint / next action.
- `learning/LEARNING_JOURNAL.md`: factual milestones and evidence levels.
- `learning/COURSE_PROGRESS.md`: video or rubric status only when changed (never auto advance).
- `learning/KNOWLEDGE_MAP.md`: student demonstrated concept understanding or genuine misconceptions.
User reporting done and actual verified function are **different** statuses. Student source stays untouched unless specifically authorized.

## How to check teaching quality (don't just hope)
`tests/SCENARIO_TESTS.md` contains **18 realistic prompts**, score rubric and red flags. Test at least T01, T02, T03, T09 and T13 in **separate fresh Codex chats**, then check actual replies and file operations. T03 ("tao chả biết callback") and T13 ("chỉnh cách dạy") are important regression cases.

`python tests/verify_package.py` checks packaging only; it does NOT exercise the Codex model. Use the manual trials to establish real tutoring quality.

## What changed from v2
1. Lower cognitive load: no forced whole-course scan on a tiny concept question.
2. Specific beginner **teaching playbook**, bad/good explanations, and repair steps for "không biết".
3. Exact #29 AntD Form conceptual reference, without inventing Postman fields or doing #32 API prematurely.
4. Accurate code tracing, TypeScript/runtime and AntD Form distinctions.
5. Skill intent explicitly includes meta requests: teaching-style feedback must not become a React exercise.
6. 18 human-evaluable test prompts and a structural validator.
7. One tutor Skill (not a pile of overlapping skills). No external third-party skill needed to deliver the learning workflow.

## Limitations
- The course PDF is not a full teacher video transcript. If live teacher instructions differ, student-provided notes supersede where appropriate.
- PDF-to-MD extraction can lose formatting/links/images. Use original PDF when uncertain.
- The bundle has been **structurally checked** in packaging; live Codex behavior inside the student's Windows project still needs manual evaluation.
- Never run installer scripts from untrusted sources; this archive is just plain Markdown/PDF/test files.
