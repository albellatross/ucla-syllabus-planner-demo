"""Right-aligned status group with stable in-card actions; deadline countdowns."""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
def patch(a,b):
 global s
 assert s.count(a)==1,(a[:90],s.count(a));s=s.replace(a,b)
patch('grid-template-columns:minmax(0,max-content) max-content;justify-content:start;','grid-template-columns:minmax(0,1fr) max-content;justify-content:normal;')
patch('align-items:center;padding-right:28px;box-sizing:border-box;}', 'align-items:center;padding-right:32px;box-sizing:border-box;}')
# Fixed 24px action and 8px gap; never move or hide status on hover.
patch('/* The floating action is outside the content box; no countdown slot is lost. */','/* Figma card: right-aligned status and separate in-card action lane; no hover reflow. */')
a=s.index('function syllabusExamCountdown(');b=s.index('/* User decision: this prototype',a)
helper=r'''function syllabusIsDeadline(topic){if(syllabusIsExam(topic))return false;return /^(assignment|homework|project|deadline|due)$/i.test(topic.eventType??topic.kind??"")||/\bdue\b/i.test(topic.timing??"")}
function syllabusExamCountdown(topic,now){const exam=syllabusIsExam(topic),due=syllabusIsDeadline(topic);if((!exam&&!due)||!we(topic.date))return null;const clocks=[...(topic.time??"").matchAll(/(\d{1,2}):(\d{2})\s*(AM|PM)?/gi)],clock=due?clocks.at(-1):clocks[0];if(clock){let hour=Number(clock[1]);const suffix=clock[3]??(topic.time??"").match(/(AM|PM)\s*$/i)?.[1];if(suffix)hour=hour%12+(suffix.toUpperCase()==="PM"?12:0);const deadline=new Date(`${topic.date}T${String(hour).padStart(2,"0")}:${clock[2]}:00`),minutes=Math.ceil((deadline-now)/60000);if(minutes<0)return due?"Overdue":"Exam ended";if(minutes===0)return due?"Due now":"Starting now";if(minutes<60)return `${minutes}m left`;const hours=Math.floor(minutes/60);return hours>=24?`${Math.floor(hours/24)}d ${hours%24}h left`:`${hours}h ${minutes%60}m left`}
const today=new Date(now.getFullYear(),now.getMonth(),now.getDate()),deadline=new Date(`${topic.date}T00:00:00`),days=Math.round((deadline-today)/864e5);return days<0?(due?"Overdue":"Exam ended"):days===0?(due?"Due today":"Today"):days===1?"1 day left":`${days} days left`}

'''
s=s[:a]+helper+s[b:]
# Use the same deadline definition in priority filtering and calendar marks.
patch('const type=topic.eventType??topic.kind;if(/^(exam|quiz|midterm|final|final exam|midterm exam|test|assignment|homework|project|deadline)$/i.test(type??""))return type;','const type=topic.eventType??topic.kind;if(/^(exam|quiz|midterm|final|final exam|midterm exam|test|assignment|homework|project|deadline|due)$/i.test(type??""))return type;if(/\\bdue\\b/i.test(topic.timing??""))return "Assignment";')
patch('countdown===\"Exam ended\"?`${bA.topic.title} has ended`:`Time until ${bA.topic.title}`','countdown===\"Exam ended\"?`${bA.topic.title} has ended`:countdown===\"Overdue\"?`${bA.topic.title} is overdue`:`Time until ${bA.topic.title}`')
patch('/^(assignment|project|deadline|homework)$/i.test(syllabusImportantType(topic)??"")?"due":null','syllabusIsDeadline(topic)?"due":null')
p.write_text(s)
Path('/tmp/syllabus-right-due.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
# Deterministic separate QA file, not published.
qa='''const qaCourse=c=>({...c,topics:c.topics.map(t=>({...t,kind:"Assignment",eventType:"Assignment",time:"12:30–1:45 PM",title:"Assignment: "+t.title+" — apply the concepts and explain your reasoning"})),keyDates:c.keyDates.map(t=>({...t,kind:"Assignment",title:"Assignment: "+t.title+" — apply the concepts and explain your reasoning"}))});A=qaCourse(A);t=t.map(qaCourse);'''
Path('qa-due-cards.html').write_text(s.replace('const syllabusPreviewMode=new URLSearchParams(location.search)',qa+'const syllabusPreviewMode=new URLSearchParams(location.search)',1))
