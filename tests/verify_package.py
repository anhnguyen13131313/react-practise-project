#!/usr/bin/env python3
"""Dependency-free structural checks for React Tutor v2.1 overlay.
This is NOT a Codex behavior test.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.agents/skills/fresher-react-tutor/SKILL.md'
AGENT = ROOT / 'AGENTS.md'
FILES = [
    SKILL, AGENT,
    ROOT/'course-materials/COURSE_INDEX.md',
    ROOT/'course-materials/chapters/chapter-04-auth.md',
    ROOT/'course-materials/react-test-fresher-ts.pdf',
    ROOT/'learning/COURSE_PROGRESS.md',
    ROOT/'learning/CURRENT_SESSION.md',
    ROOT/'learning/LEARNING_JOURNAL.md',
    ROOT/'learning/KNOWLEDGE_MAP.md',
    ROOT/'tests/SCENARIO_TESTS.md',
]
checks = []
for p in FILES:
    checks.append((p.exists(), f'file present: {p.relative_to(ROOT)}'))

body = SKILL.read_text(encoding='utf-8') if SKILL.exists() else ''
m = re.match(r'\A---\n(.*?)\n---\n', body, re.S)
checks.append((m is not None, 'YAML frontmatter delimiters'))
if m:
    keys = [x.split(':', 1)[0] for x in m.group(1).splitlines() if x and not x[0].isspace()]
    checks.append((keys == ['name','description'], 'frontmatter has name/description only'))
    checks.append(('name: fresher-react-tutor' in m.group(1), 'stable skill name'))
    checks.append((len(m.group(1)) < 500, 'short skill metadata'))
for ref in re.findall(r'`(references/[^`]+\.md)`', body):
    checks.append(((SKILL.parent / ref).exists(), f'linked reference: {ref}'))
agent = AGENT.read_text(encoding='utf-8') if AGENT.exists() else ''
checks.append(('.agents/skills/fresher-react-tutor/SKILL.md' in agent, 'automatic router path'))
checks.append(('read-only' in agent.lower(), 'no-app-edits default'))
checks.append(('COURSE_PROGRESS.md' in agent, 'progress source of truth'))
checks.append((bool(re.search(r'(?:four|4).{0,50}postman', body, flags=re.I|re.S)), 'unknown Postman field safeguards'))
checks.append(('#29' in (ROOT/'course-materials/chapters/chapter-04-auth.md').read_text(encoding='utf-8'), 'course #29 present'))
checks.append(('do not auto advance' in body.lower(), 'video transition safeguard'))

bad = [name for ok, name in checks if not ok]
for ok, name in checks:
    print(f'{"PASS" if ok else "FAIL"}: {name}')
print(f'\n{len(checks)-len(bad)}/{len(checks)} checks passed')
if bad: sys.exit(1)
