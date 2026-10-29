"""Compact material uploader with an explicit primary action and shared dialog shell."""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
def patch(a,b):
 global s
 assert s.count(a)==1,(a[:90],s.count(a));s=s.replace(a,b)
patch('className:sn.surface,"data-stage":"upload","aria-labelledby":"topic-material-upload-title"','className:`${sn.surface} topic-material-dialog`,"data-stage":"upload","aria-labelledby":"topic-material-upload-title"')
patch('id:"topic-material-upload-title",children:"Upload course materials"','id:"topic-material-upload-title",children:"Add study materials"')
patch('children:"Add slides, readings, or notes for this topic. You can also add them later from References."','children:"Add slides, readings, or notes for this topic."')
patch('u.jsx("div",{className:sn.uploadArea,onDragOver:','u.jsx("div",{className:`${sn.uploadArea} topic-material-drop`,onDragOver:')
patch('children:[u.jsx(CE,{"aria-hidden":"true"}),u.jsx("span",{children:"Drag and drop your files here"})]','children:[u.jsx(CE,{"aria-hidden":"true"}),u.jsx("span",{children:"Drop your files here"}),u.jsx("span",{className:"topic-material-formats",children:"PDF, Word, PowerPoint, TXT or Markdown"}),u.jsx("span",{className:"topic-material-formats",children:"Up to 20 MB per file"})]')
patch('u.jsx("p",{className:sn.fileHint,children:"PDF, Word, PowerPoint, TXT or Markdown · Up to 20 MB each"}),u.jsx("p",{className:sn.status,children:"Preview: files are kept in References; their contents are not read."})','u.jsx("p",{className:"topic-material-note",children:"You can add materials later in References."}),u.jsx("p",{className:"topic-material-preview",children:"Prototype: files are kept as references; their contents aren’t read."})')
patch('m.length>0&&u.jsx(EA,{appearance:"primary",onClick:()=>{R("references");closeMaterialGate()},children:"Continue"})','u.jsx(EA,{appearance:"primary",onClick:()=>{if(m.length){R("references");closeMaterialGate()}else materialGateInput.current?.click()},children:m.length?"Continue":"Choose files"})')
css='''<style>
/* Compact topic uploader; preserve original Popover modal and focus management. */
.topic-material-dialog{width:min(448px,calc(100vw - var(--gnrc-spacing-layout-base-400)));padding:var(--gnrc-spacing-component-base-600);}
.topic-material-dialog h2#topic-material-upload-title{font-size:var(--gnrc-font-size-functional-title-small);line-height:var(--gnrc-line-height-functional-title-small);margin:0 0 var(--gnrc-spacing-component-base-200);}
.topic-material-dialog #topic-material-upload-description{font-size:var(--gnrc-font-size-functional-body-medium);line-height:var(--gnrc-line-height-functional-body-medium);color:var(--gnrc-color-foreground-neutral-secondary);margin:0 0 var(--gnrc-spacing-component-base-500);}
.topic-material-dialog .topic-material-drop{min-height:136px;padding:var(--gnrc-spacing-component-base-400);border-radius:var(--gnrc-border-radius-base-400);background:var(--gnrc-color-background-neutral-transparent);}
.topic-material-dialog .topic-material-drop>button[class]{gap:var(--gnrc-spacing-component-base-200);align-items:center;justify-content:center;min-height:100px;font-size:var(--gnrc-font-size-functional-body-medium);line-height:var(--gnrc-line-height-functional-body-medium);font-weight:var(--gnrc-font-weight-functional-regular);}
.topic-material-dialog .topic-material-drop>button>svg{width:24px;height:24px;margin-bottom:var(--gnrc-spacing-component-base-100);}
.topic-material-dialog .topic-material-formats{font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);font-weight:var(--gnrc-font-weight-functional-regular);color:var(--gnrc-color-foreground-neutral-secondary);}
.topic-material-note,.topic-material-preview{font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);font-weight:var(--gnrc-font-weight-functional-regular);color:var(--gnrc-color-foreground-neutral-secondary);}
.topic-material-note{margin:var(--gnrc-spacing-component-base-300) 0 0;}.topic-material-preview{margin:var(--gnrc-spacing-component-base-100) 0 0;}
.topic-material-dialog>div:last-child{padding-top:var(--gnrc-spacing-component-base-500)!important;}
.topic-material-dialog .syllabus-material-files{margin-top:var(--gnrc-spacing-component-base-300);max-height:140px;}
.topic-material-dialog .syllabus-material-files li{font-size:var(--gnrc-font-size-functional-body-medium);line-height:var(--gnrc-line-height-functional-body-medium);border-bottom:var(--gnrc-stroke-width-thin) solid var(--gnrc-color-stroke-neutral-subtle);}
@media(prefers-reduced-motion:reduce){.topic-material-dialog{animation:none;transition:none;}}
</style>'''
i=s.rfind('</body>');s=s[:i]+css+s[i:];p.write_text(s)
Path('/tmp/syllabus-material-refine.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
