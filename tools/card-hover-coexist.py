"""Keep countdown visible; floating menu action and shared pointer-dismiss boundary."""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
def patch(a,b):
 global s
 assert s.count(a)==1,(a[:100],s.count(a));s=s.replace(a,b)
patch('const[syllabusManageOpen,setSyllabusManageOpen]=f.useState(false),','const[cardMenuKey,setCardMenuKey]=f.useState(null),cardMenuTimer=f.useRef(null);function keepCardMenu(){clearTimeout(cardMenuTimer.current)}function leaveCardMenu(){clearTimeout(cardMenuTimer.current);cardMenuTimer.current=setTimeout(()=>setCardMenuKey(null),140)}f.useEffect(()=>()=>clearTimeout(cardMenuTimer.current),[]);const[syllabusManageOpen,setSyllabusManageOpen]=f.useState(false),')
patch('"data-testid":`improved-topic-${bA.topic.id}`,"data-kind":','"data-testid":`improved-topic-${bA.topic.id}`,onPointerEnter:keepCardMenu,onPointerLeave:leaveCardMenu,"data-kind":')
a='u.jsxs(xc,{positioning:{position:"below",align:"end"},children:[u.jsx($d,{children:u.jsx(EA,{appearance:"subtle",size:"small","aria-label":`More actions for ${bA.topic.title}`'
b='u.jsxs(xc,{open:cardMenuKey===bA.key,onOpenChange:(_,data)=>{keepCardMenu();setCardMenuKey(data.open?bA.key:null)},positioning:{position:"below",align:"end"},children:[u.jsx($d,{children:u.jsx(EA,{appearance:"subtle",size:"small","aria-label":`More actions for ${bA.topic.title}`'
patch(a,b)
patch('u.jsx(Mc,{children:u.jsxs(Xc,{"aria-label":`Actions for ${bA.topic.title}`','u.jsx(Mc,{onPointerEnter:keepCardMenu,onPointerLeave:leaveCardMenu,children:u.jsxs(Xc,{"aria-label":`Actions for ${bA.topic.title}`')
a=s.rfind('<style>\n/* Only the trigger');b=s.index('</style>',a)+8
css='''<style>
/* The floating action is outside the content box; no countdown slot is lost. */
[aria-label="Syllabus cards"]{box-sizing:content-box;padding:12px;margin:-12px;gap:24px;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77{position:relative;display:grid;grid-template-columns:minmax(0,1fr) max-content;column-gap:var(--gnrc-spacing-component-base-100);align-items:center;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77 ._sourceTiming_mtwhd_21{grid-column:1;grid-row:1;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77 .syllabus-exam-countdown{grid-column:2;grid-row:1;margin:0;opacity:1;pointer-events:auto;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button[aria-haspopup]{position:absolute;inset:auto;right:-28px;top:-12px;z-index:5;width:24px;min-width:24px;height:24px;margin:0;border:var(--gnrc-stroke-width-thin) solid var(--gnrc-color-stroke-neutral-subtle);border-radius:var(--gnrc-border-radius-circular);background:var(--gnrc-color-surface-neutral-nearer);opacity:0;pointer-events:none;transition:opacity 100ms ease;}
._topicCard_mtwhd_7:hover ._cardTop_mtwhd_77>button,._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button:focus-visible,._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button[aria-expanded="true"]{opacity:1;pointer-events:auto;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77>div{position:fixed;inset:auto;width:max-content;min-width:0;height:auto;opacity:1;}
@media(hover:none){._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button[aria-haspopup]{opacity:1;pointer-events:auto;}}
@media(prefers-reduced-motion:reduce){._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button{transition:none;}}
</style>'''
s=s[:a]+css+s[b:];p.write_text(s)
Path('/tmp/syllabus-coexist.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
