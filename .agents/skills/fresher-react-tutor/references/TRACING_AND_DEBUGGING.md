# Reference: tracing & evidence-first debugging

## Trace accurately without drowning a beginner
Find actual code, then isolate 3–7 crucial events and give concrete values. Do not invent a file, prop, result or network request.

```text
User interaction (what exactly: type/click/submit?)
→ handler or library callback (who invokes it?)
→ arguments/value origin (from where?)
→ changes to React state OR AntD's form field store
→ queued React render / async operation IF it actually occurs
→ visible effect (rendered text/error/navigation)
```

Explain each unknown name or syntax (`e`, `.target.value`, `prev`, `=>`, props) *at the point it appears*. Trace only necessary branches. If teacher asks for whole flow, expand deliberately, distinguishing render vs DOM changes and TS type vs runtime.

## Safe React / TS distinctions
- `setState` schedules an update; it doesn't immediately mutate the existing closure's variable. A functional updater sees the pending state in update queue.
- Render = React calling components to calculate UI; not every render causes a DOM change. Parent render usually leads to child evaluation unless React skips work through memoization or other optimizations; don't promise an exact number of renders without observing development Strict Mode.
- `useEffect` is for synchronization with external systems; distinguish timing of setup and cleanup, dependencies and dev Strict Mode. Don't teach that every async or data transformation "must be in useEffect".
- `async/await` yields at async boundary; don't show API success before response. Catch/error path when relevant.
- TypeScript interfaces/generics describe static shapes; JS runtime won't enforce them. Explain syntax before leaning on it.
- Ant Design `Form` maintains its own field values; a field named `name="email"` contributes an `email` key to `onFinish(values)` when configured. An individual React `useState` for every field is not assumed.
- When submit fails validation, default `onFinish` isn't called; there may be `onFinishFailed`. Debug validation before diagnosing HTTP.

## Debug protocol
1. Gather minimal evidence: actual error text, expected/actual, relevant file/line, dependency version, state/UI/Network evidence if available. Never ask again for known details.
2. Form **one** leading hypothesis tied to evidence. Separate observation from inference.
3. Propose **one falsifiable check** (e.g. inspect console, log handler entry, validate `name`/`rules`, network tab).
4. Wait for result before layering more possibilities; then allow student to make fix and verify.
5. If student is completely lost, explain the conceptual root cause and show an *independent* miniature example. Don't force guessing in the dark.

## Negative examples
- Don't treat a TypeScript error as a backend bug without evidence.
- Don't claim "button click must call API" in video #29 (API integration comes in later lesson).
- Don't tell student "React always renders twice"; depends on mode and code.
- Don't mark full homework correct after reading code alone if UI behavior remains unverified.
