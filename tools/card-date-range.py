"""Preserve full date/time range in accessible label and hover tooltip."""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
a='function syllabusExamVisible(topic,week)';helper=r'''function syllabusCardDateLabel(topic){const day=new Intl.DateTimeFormat("en-US",{month:"short",day:"numeric",timeZone:"UTC"}).format(Dr(topic.date));const range=topic.time||topic.timing.match(/\d{1,2}:\d{2}\s*(?:AM|PM)?\s*(?:[–—-]\s*\d{1,2}:\d{2}\s*(?:AM|PM)?)?/i)?.[0];return day+(range?`, ${range.trim()}`:"")}
'''
assert s.count(a)==1;s=s.replace(a,helper+a)
a='bA.topic.date?u.jsxs("time",{dateTime:bA.topic.date,children:[';start=s.index(a);end=s.index('}):u.jsx("span",{children:va(bA.topic,bA.course)',start)
s=s[:start]+'bA.topic.date?u.jsx("time",{dateTime:bA.topic.date,title:syllabusCardDateLabel(bA.topic),"aria-label":syllabusCardDateLabel(bA.topic),children:syllabusCardDateLabel(bA.topic)'+s[end:]
p.write_text(s)
Path('/tmp/syllabus-card-range.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
# Separate deterministic QA fixture. Never published or used as product data.
fixture='''const qaCourse=c=>({...c,topics:c.topics.map(t=>({...t,time:"12:30–1:45 PM",title:t.title+" — applying the concepts to unfamiliar situations and comparing alternative explanations"})),keyDates:c.keyDates.map(t=>({...t,title:t.title+" — applying the concepts to unfamiliar situations and comparing alternative explanations"}))});A=qaCourse(A);t=t.map(qaCourse);'''
qa=s.replace('const syllabusPreviewMode=new URLSearchParams(location.search)',fixture+'const syllabusPreviewMode=new URLSearchParams(location.search)',1)
Path('qa-long-cards.html').write_text(qa)
