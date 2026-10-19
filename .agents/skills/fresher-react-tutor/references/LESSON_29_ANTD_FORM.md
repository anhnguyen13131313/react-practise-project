# Lesson #29 — Design Register Form (source-grounded teaching notes)

## Source rubric: Hỏi Dân IT / Eric, Fresher React TS
Original PDF page 36 (printed page 35), `course-materials/chapters/chapter-04-auth.md` at #29:
- Create a `/register` page.
- Design UI freely using Ant Design Form.
- Exactly four fields **as defined by the supplied Postman API collection** (PDF does **not** list their names).
- Required-field validation and valid email format.
- On submit, obtain values of all fields.
- Hint from teacher: use TypeScript and provided examples.

## Concept prerequisites (teach only when needed)
- **Route `/register`:** address that should show the page; check project's actual React Router configuration before instructing a change.
- **`Form`:** component managing a collection of fields and submission/validation.
- **`Form.Item`:** connects a named field with the Form's data handling, rules and error display. `name` identifies the key; the `label` is visible display text.
- **`Input` / `Input.Password`:** user-facing UI fields, not necessarily a manually managed `useState`.
- **`rules`:** runtime validation rules; `required` rejects missing input; `type: 'email'` validates email pattern, not existence of an actual mailbox.
- **`onFinish(values)`:** callback Ant Design Form calls when submission passes validation; `values` holds collected data keyed by `Form.Item name`.
- **`onFinishFailed`:** callback when validation fails (if configured). Do not claim `onFinish` runs on invalid form.
- **TypeScript:** type annotations are erased at runtime; they do not replace AntD validation rules.
- **HTML `htmlType="submit"`:** for AntD Button inside Form; distinguish from `onClick` when teaching actual code.

## Sequence for this particular exercise
1. Confirm current repo/layout and if routing exists. Don't assume no files.
2. Inspect Postman if student has it. If absent, say 4 field names UNKNOWN and ask for that evidence at relevant moment.
3. Ask student to build **one part**, e.g. route or one field. Do not paste a complete form page.
4. Review and test each criterion: render / fields / required / email format / valid submit obtains data.
5. If UI works but concepts not explained, mark function complete separately from understanding demonstrated.

## Pseudotrace (NOT project implementation)
```text
User enters "not-an-email" -> AntD's field value changes
User submits -> Form runs `rules`
Invalid email -> show field error; `onFinish` does not run
User enters "a@b.com" -> submits -> validates -> onFinish receives values
```
Only claim this if actual Form has those validation rules attached and correct submission wiring.

## Source vs outside knowledge
The rubric is sourced from course. The explanations of `Form`, `rules`, and `onFinish` are general API knowledge; prefer project-installed Ant Design version and its docs when exact props differ. Note that the course uses Ant Design 5.21.6; verify actual `package.json` instead of assuming.
