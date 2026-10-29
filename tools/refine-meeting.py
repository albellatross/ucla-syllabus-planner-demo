"""Apply bounded, asserted changes to the published single-file prototype.
Source: Syllabus Design Catchup, 2026-10-27. Run against commit 2f93cc4.
The published repository has no editable React project; preserve its bundle.
"""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
def patch(old,new):
 global s
 assert s.count(old)==1,(old[:100],s.count(old))
 s=s.replace(old,new)
patch('[z,T]=f.useState("all"),w=f.useRef([])', '[z,T]=f.useState("important"),w=f.useRef([])')
patch('bt=[{id:"important",code:"",title:"Important events"},{id:"all",code:"All",title:"All courses"},...RA]', 'bt=[{id:"important",code:"Up next",title:"Upcoming exams and deadlines"},...RA]')
patch('DA=z==="important"?0:z==="all"?1:bA.findIndex(Ee=>Ee.id===z)+2', 'DA=z==="important"?0:bA.findIndex(Ee=>Ee.id===z)+1')
patch('children:IA.id==="important"?u.jsx("span",{className:"syllabus-important-star","aria-hidden":"true"}):IA.code','children:IA.code')
patch('"aria-label":IA.id==="important"?IA.title:void 0','"aria-label":IA.id==="important"?"Up next":void 0')
patch('YA=et.filter(({topic:IA,course:bA})=>va(IA,bA)===W||syllabusExamVisible(IA,W))','YA=et.filter(({topic:IA,course:bA})=>z==="important"?Boolean(syllabusImportantType(IA))&&we(IA.date)&&IA.date>=o&&IA.date<=dr(o,13):va(IA,bA)===W||syllabusExamVisible(IA,W))')
patch('className:ji.weekNavigation,role:"group"','className:ji.weekNavigation,hidden:z==="important",role:"group"')
patch('z==="important"?"No exams or deadlines scheduled for these dates.":"No items scheduled for these dates."','z==="important"?"No exams or deadlines in the next 14 days. Open a course to explore its topics.":"No items scheduled for these dates."')
patch('syllabusPlanLoading?u.jsx(SyllabusPlannerSkeleton,{})','u.jsx("p",{className:"syllabus-view-context",children:z==="important"?`Next 14 days · ${HU(o)} – ${HU(dr(o,13))}${syllabusPreviewMode?" · Demo date: "+HU(o):""}`:syllabusPreviewMode?`Demo date: ${HU(o)} · Countdowns stay relative to this date.`:"Countdowns are relative to today."}),syllabusPlanLoading?u.jsx(SyllabusPlannerSkeleton,{})')
patch('label:"Start date",value:i.start','label:e?"Course Start Date":"Start date",value:i.start')
patch('"Enter the first day of this course. We’ll use it to place week-based items on your planner. Events with exact dates stay unchanged."','"Enter the first day of this course."')
patch('title:"Edit start date",description:', 'title:"Course Start Date",description:')
patch('}. This start date is used to place undated items into date ranges. Existing event dates stay the same.`','}. Enter the first day of this course.`')
patch('function uN(i){return`Help me learn ${i}, refer related material in this notebook or remind me uploaded a file if not.`}', 'function uN(i){return`Help me study ${i}. Use relevant course materials already available in this notebook. If the scope or materials are missing, ask me for them before creating course-specific explanations or practice questions.`}')
patch('const[materialGateOpen,setMaterialGateOpen]=f.useState(!0),materialGateInput=f.useRef(null);','const materialGateKey=`syllabus-material-prompt:${i.key??i.course.id+"/"+i.topic.id}`;const[materialGateOpen,setMaterialGateOpen]=f.useState(()=>{try{return !(A?.resources?.length)&&sessionStorage.getItem(materialGateKey)!=="seen"}catch{return !(A?.resources?.length)}}),materialGateInput=f.useRef(null);f.useEffect(()=>{if(!materialGateOpen)try{sessionStorage.setItem(materialGateKey,"seen")}catch{}},[materialGateOpen,materialGateKey]);')
patch('children:"Your syllabus gives you the schedule. Add lecture slides, readings, or notes for this topic to keep them together in References."','children:"Add slides, readings, or notes for this topic. You can skip this step and add materials from References whenever you’re ready."')
patch('const[syllabusManageOpen,setSyllabusManageOpen]', 'o=`${syllabusNow.getFullYear()}-${String(syllabusNow.getMonth()+1).padStart(2,"0")}-${String(syllabusNow.getDate()).padStart(2,"0")}`;const[syllabusManageOpen,setSyllabusManageOpen]')
patch('if(r&&!A)return{answer:`## Prepare for ${l}', 'if(r)return{answer:`*Sample response — uploaded file contents are not read in this demo.*\n\n## Prepare for ${l}')
css='''
/* October 27 meeting: a readable Up next label and clear prototype clock. */
.syllabus-important-filter{width:auto!important;min-width:max-content!important;padding:var(--gnrc-spacing-component-base-150) var(--gnrc-spacing-component-base-300)!important;}
[hidden]{display:none!important;}
.syllabus-view-context{margin:0;padding:var(--gnrc-spacing-component-base-150) 0;color:var(--gnrc-color-foreground-neutral-secondary);font-family:var(--gnrc-font-family-functional);font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);}
'''
s=s.replace('</head>','<style>'+css+'</style></head>',1)
p.write_text(s)
Path('/tmp/syllabus-refined.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
print('Applied meeting refinements.')
