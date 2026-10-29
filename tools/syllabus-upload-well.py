"""Refine the original syllabus uploader; retain loading, duplicate, and review states."""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
def patch(a,b):
 global s
 assert s.count(a)==1,(a[:90],s.count(a));s=s.replace(a,b)
patch('"aria-modal":true,className:sn.surface,"data-stage":w?', '"aria-modal":true,className:`${sn.surface} syllabus-upload-dialog`,"data-stage":w?')
patch('className:sn.chooseFile,"aria-label":"Choose syllabus file"','className:`${sn.chooseFile} syllabus-upload-target`,"aria-label":"Choose syllabus file: PDF or Word, up to 20 MB"')
patch('children:[u.jsx(oQ,{"aria-hidden":"true"}),u.jsx("span",{id:R?a:void 0,className:R?sn.uploadError:void 0,children:R||"Drag and drop your files here"})]','children:[u.jsx("span",{className:"syllabus-upload-icon","aria-hidden":"true",children:u.jsx(oQ,{})}),u.jsx("span",{id:R?a:void 0,className:R?sn.uploadError:"syllabus-upload-label",children:R||"Click to upload your syllabus"}),u.jsx("span",{className:"syllabus-upload-secondary",children:"or drag and drop it here"}),u.jsx("span",{className:"syllabus-upload-formats",children:"PDF or Word (.docx) · Up to 20 MB"})]')
css='''<style>
/* Original syllabus selection well: one clear, full-size upload target. */
.syllabus-upload-dialog[data-stage="upload"] [class*="uploadArea"]{padding:0;min-height:164px;overflow:hidden;border-radius:var(--gnrc-border-radius-base-400);border-color:var(--gnrc-color-stroke-neutral-subtle);background:var(--gnrc-color-background-neutral-transparent);}
.syllabus-upload-dialog .syllabus-upload-target[class]{width:100%;min-height:164px;padding:var(--gnrc-spacing-component-base-500);margin:0;display:flex;align-items:center;justify-content:center;gap:var(--gnrc-spacing-component-base-200);border-radius:var(--gnrc-border-radius-base-400);white-space:normal;color:var(--gnrc-color-foreground-neutral-primary);}
.syllabus-upload-icon{width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin-bottom:var(--gnrc-spacing-component-base-100);border-radius:var(--gnrc-border-radius-base-300);background:var(--gnrc-color-background-neutral-subtle);color:var(--gnrc-color-foreground-neutral-secondary);}
.syllabus-upload-icon>svg{width:24px;height:24px;}
.syllabus-upload-label{font-family:var(--gnrc-font-family-functional);font-size:var(--gnrc-font-size-functional-body-medium);line-height:var(--gnrc-line-height-functional-body-medium);font-weight:var(--gnrc-font-weight-functional-semibold);}
.syllabus-upload-secondary,.syllabus-upload-formats{font-family:var(--gnrc-font-family-functional);font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);font-weight:var(--gnrc-font-weight-functional-regular);color:var(--gnrc-color-foreground-neutral-secondary);}
.syllabus-upload-formats{margin-top:var(--gnrc-spacing-component-base-100);}
.syllabus-upload-dialog[data-stage="upload"] [class*="uploadArea"][data-dragging]{background:var(--gnrc-color-background-brand-subtle);border-color:var(--gnrc-color-stroke-brand-loud);}
.syllabus-upload-dialog[data-stage="upload"] [class*="uploadArea"]:focus-within{overflow:visible;}
@media(forced-colors:active){.syllabus-upload-icon{border:1px solid CanvasText;}}
</style>'''
i=s.rfind('</body>');s=s[:i]+css+s[i:];p.write_text(s)
Path('/tmp/syllabus-upload-well.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
