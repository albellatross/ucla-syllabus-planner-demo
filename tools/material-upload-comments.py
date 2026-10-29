"""Bella's three browser comments: direct upload area, clearer guidance, no duplicate CTA."""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
def patch(a,b):
 global s
 assert s.count(a)==1,(a[:100],s.count(a));s=s.replace(a,b)
patch('children:"Add slides, readings, or notes for this topic."','children:/exam|midterm|final|quiz|test/i.test(`${n.eventType||n.kind} ${n.title}`)?"Add your instructor’s review sheet, slides for the covered chapters, or class notes. Choose materials that match the topics being tested.":"Add lecture slides, assigned readings, or class notes that explain this topic. Include worked examples or practice questions you want to revisit."')
patch('className:sn.chooseFile,"aria-label":"Choose course materials"','id:"topic-material-upload-area",className:sn.chooseFile,"aria-label":"Upload course materials: click to browse or drag files here"')
patch('children:[u.jsx(CE,{"aria-hidden":"true"}),u.jsx("span",{children:"Drop your files here"}),u.jsx("span",{className:"topic-material-formats",children:"PDF, Word, PowerPoint, TXT or Markdown"}),u.jsx("span",{className:"topic-material-formats",children:"Up to 20 MB per file"})]','children:[u.jsx("span",{className:"topic-material-icon","aria-hidden":"true",children:u.jsx(CE,{})}),u.jsx("span",{className:"topic-material-upload-label",children:"Click to upload or drag files here"}),u.jsxs("span",{className:"topic-material-file-details",children:[u.jsx("span",{children:"PDF, Word, PowerPoint, TXT or Markdown"}),u.jsx("span",{children:"Up to 20 MB per file"})]})]')
patch('document.getElementById("topic-material-primary")?.focus()','(document.getElementById("topic-material-primary")||document.getElementById("topic-material-upload-area"))?.focus()')
patch('u.jsx(EA,{id:"topic-material-primary",appearance:"primary",onClick:()=>{if(m.length){R("references");closeMaterialGate()}else materialGateInput.current?.click()},children:m.length?"Continue":"Choose files"})','m.length>0&&u.jsx(EA,{id:"topic-material-primary",appearance:"primary",onClick:()=>{R("references");closeMaterialGate()},children:"Continue"})')
css='''<style>
/* The whole upload well is the single file-selection target. */
.topic-material-dialog .topic-material-drop{padding:0;min-height:0;overflow:hidden;border-color:var(--gnrc-color-stroke-neutral-subtle);}
.topic-material-dialog .topic-material-drop>button[class]{width:100%;min-height:164px;margin:0;padding:var(--gnrc-spacing-component-base-500);gap:var(--gnrc-spacing-component-base-300);border-radius:var(--gnrc-border-radius-base-400);color:var(--gnrc-color-foreground-neutral-primary);}
.topic-material-icon{display:flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:var(--gnrc-border-radius-base-300);background:var(--gnrc-color-background-neutral-subtle);color:var(--gnrc-color-foreground-neutral-secondary);}
.topic-material-icon>svg{width:24px;height:24px;}
.topic-material-upload-label{font-size:var(--gnrc-font-size-functional-body-medium);line-height:var(--gnrc-line-height-functional-body-medium);font-weight:var(--gnrc-font-weight-functional-semibold);}
.topic-material-file-details{display:flex;flex-direction:column;gap:var(--gnrc-spacing-component-base-100);font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);font-weight:var(--gnrc-font-weight-functional-regular);color:var(--gnrc-color-foreground-neutral-secondary);}
.topic-material-dialog .topic-material-drop:focus-within{overflow:visible;}
@media(forced-colors:active){.topic-material-icon{border:1px solid CanvasText;}}
</style>'''
i=s.rfind('</body>');s=s[:i]+css+s[i:];p.write_text(s)
Path('/tmp/syllabus-upload-comments.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
