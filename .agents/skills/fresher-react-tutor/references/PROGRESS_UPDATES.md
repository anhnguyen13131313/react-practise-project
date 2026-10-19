# Reference: automatic progress & memory updates

User has explicitly authorized writing learning records on **meaningful milestones**. No repeated confirmation is required for these 4 Markdown files. Do not edit source code as part of logging.

## Update trigger → exact files

| User signal or verified event | File(s) to update | Status treatment |
| --- | --- | --- |
| "Xong bước 1", "tự code xong phần UI" | `learning/CURRENT_SESSION.md` + append `learning/LEARNING_JOURNAL.md` | User-reported until checked |
| "Check giúp tao, chạy rồi" with source/UI evidence | Above + `learning/COURSE_PROGRESS.md` checkbox for verified criterion | Verified criterion only |
| Student correctly traces / explains a concept | `learning/KNOWLEDGE_MAP.md` + brief `CURRENT_SESSION.md` | Demonstrated, link evidence |
| Student reveals actual misconception | `KNOWLEDGE_MAP.md` + brief `CURRENT_SESSION.md` | Needs review, no shaming |
| All assignment criteria verified | `COURSE_PROGRESS.md` + `CURRENT_SESSION.md` + journal | Task complete; don't auto-change video |
| "Tao đang qua video #30" | `COURSE_PROGRESS.md` + `CURRENT_SESSION.md` + journal | Confirm new active video; scope changes |
| "Nghỉ, mai học tiếp" | `CURRENT_SESSION.md` + journal | Save handoff |
| Casual discussion unrelated to completion | No update | Don't spam logs |

## Recording standard
- **Evidence levels:** USER_REPORTED, SOURCE_REVIEWED, BEHAVIOR_VERIFIED, UNDERSTANDING_DEMONSTRATED.
- Do not infer behavior verification just because code looks correct; don't infer understanding because result is right.
- Do not assume four fields of Postman; if absent record UNKNOWN.
- On user says "xong" but tests unavailable: log "user reports done; verification pending" and keep unchecked verified criteria.
- Put a short timestamp *only if available from environment/user*. Otherwise record date or sequence, don't invent exact time.
- Avoid repeated identical journal entries: check latest log before appending.
- Keep `CURRENT_SESSION.md` short (<80 lines) and overwrite obsolete blockers.
- On #29 completion, summarize what worked and what wasn't checked. Video #30 stays locked until explicitly selected by user.
- Inform student what was saved. If write fails or path absent, suggest text to paste, don't claim persistence.
