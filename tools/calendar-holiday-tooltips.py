"""Holiday names for the UCLA 2025–26 demo calendar.
Source: https://registrar.ucla.edu/portals/50/documents/calendar/academiccalendar25-26.pdf
"""
from pathlib import Path
import re,json
p=Path('index.html');s=p.read_text()
def patch(a,b):
 global s
 assert s.count(a)==1,(a[:70],s.count(a));s=s.replace(a,b)
holidays={'2026-01-01':'New Year’s Day','2026-01-19':'Martin Luther King, Jr. Day','2026-02-16':'Presidents’ Day','2026-03-27':'César Chávez Day','2026-05-25':'Memorial Day','2026-06-19':'Juneteenth','2026-07-03':'Independence Day (observed)','2026-09-07':'Labor Day'}
patch('function syllabusCalendarMarks(courses){const marks={};','function syllabusCalendarMarks(courses){const marks={};const holidays='+json.dumps(holidays,ensure_ascii=False)+';for(const [date,name] of Object.entries(holidays))marks[date]={exam:[],due:[],holiday:[name]};')
patch('const day=marks[topic.date]??(marks[topic.date]={exam:[],due:[]});','const day=marks[topic.date]??(marks[topic.date]={exam:[],due:[],holiday:[]});')
patch('[...mark.exam,...mark.due].join("; ")','[...(mark.holiday??[]),...mark.exam,...mark.due].join("; ")')
patch('title:dayMark?[...dayMark.exam,...dayMark.due].join("; "):undefined','title:dayMark?[...(dayMark.holiday??[]),...dayMark.exam,...dayMark.due].join("; "):undefined')
patch('"data-marked":Boolean(dayMark)||undefined','"data-marked":Boolean(dayMark)||undefined,"data-holiday":Boolean(dayMark?.holiday?.length)||undefined')
patch('dayMark.due.length>0&&u.jsx("span",{className:"syllabus-calendar-mark","data-kind":"due"})','dayMark.due.length>0&&u.jsx("span",{className:"syllabus-calendar-mark","data-kind":"due"}),dayMark.holiday?.length>0&&u.jsx("span",{className:"syllabus-calendar-holiday-focus",role:"tooltip",children:dayMark.holiday.join("; ")})')
a=s.index('function syllabusCalendarDayLabel(');b=s.index('function trA(',a)
s=s[:a]+'''function syllabusCalendarDayLabel(date,mark){if(!mark)return HU(date);return [HU(date),mark.exam.length?`${mark.exam.length} exam${mark.exam.length===1?"":"s"}`:"",mark.due.length?`${mark.due.length} due item${mark.due.length===1?"":"s"}`:"",[...(mark.holiday??[]),...mark.exam,...mark.due].join("; ")].filter(Boolean).join(". ")}\n'''+s[b:]
css='''<style>
/* Native title follows the pointer; keyboard focus gets the same holiday label. */
.syllabus-calendar-holiday-focus{display:none;position:absolute;z-index:10;bottom:calc(100% + 8px);left:50%;transform:translateX(-50%);width:max-content;max-width:220px;padding:var(--gnrc-spacing-component-base-200) var(--gnrc-spacing-component-base-300);border:var(--gnrc-stroke-width-thin) solid var(--gnrc-color-stroke-neutral-subtle);border-radius:var(--gnrc-border-radius-base-200);background:var(--gnrc-color-surface-neutral-near);color:var(--gnrc-color-foreground-neutral-primary);font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);white-space:normal;pointer-events:none;}
button:focus-visible .syllabus-calendar-holiday-focus{display:block;}
button[data-holiday]{text-decoration:underline;text-decoration-style:dotted;text-underline-offset:4px;}
</style>'''
s=s.replace('</head>',css+'</head>',1);p.write_text(s)
Path('/tmp/syllabus-holidays.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
