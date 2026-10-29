"""Use Bella's original syllabus uploader as the material upload visual reference."""
from pathlib import Path
import ast,re
p=Path('index.html');s=p.read_text();tree=ast.parse(Path('tools/syllabus-upload-well.py').read_text())
for n in reversed(tree.body):
 if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name) and n.value.func.id=='patch':
  a,b=[ast.literal_eval(x) for x in n.value.args];assert s.count(b)==1;s=s.replace(b,a)
css=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='css' for t in n.targets));assert s.count(css)==1;s=s.replace(css,'')
a='u.jsx("span",{className:"topic-material-icon","aria-hidden":"true",children:u.jsx(CE,{})}),u.jsx("span",{className:"topic-material-upload-label",children:"Click to upload or drag files here"}),u.jsxs("span",{className:"topic-material-file-details",children:[u.jsx("span",{children:"PDF, Word, PowerPoint, TXT or Markdown"}),u.jsx("span",{children:"Up to 20 MB per file"})]})'
b='u.jsx(oQ,{"aria-hidden":"true"}),u.jsx("span",{className:"topic-material-upload-label",children:"Drag and drop your files here"})';assert s.count(a)==1;s=s.replace(a,b)
a='m.length>0&&u.jsx("ul",{className:"syllabus-material-files"';assert s.count(a)==1;s=s.replace(a,'u.jsx("p",{className:"topic-material-reference-formats",children:"PDF, Word, PowerPoint, TXT or Markdown · Up to 20 MB each"}),'+a)
css='''<style>
/* Exact upload-well pattern from Bella's reference screenshot. */
.topic-material-dialog .topic-material-drop{min-height:164px;box-sizing:border-box;padding:var(--gnrc-spacing-component-base-400) calc(var(--gnrc-spacing-component-base-600) - var(--gnrc-stroke-width-thin));border-radius:var(--gnrc-border-radius-base-400);border:var(--gnrc-stroke-width-thin) dashed var(--gnrc-color-stroke-neutral-subtle);background:oklch(from var(--gnrc-color-surface-neutral-nearer) l c h / 49%);}
.topic-material-dialog .topic-material-drop>button[class]{min-height:0;padding:0;gap:var(--gnrc-spacing-component-base-300);border-radius:var(--gnrc-border-radius-base-100);background:var(--gnrc-color-background-neutral-transparent);color:var(--gnrc-color-foreground-neutral-secondary);}
.topic-material-dialog .topic-material-drop>button[class]>svg{width:24px;height:24px;margin:0;}
.topic-material-dialog .topic-material-upload-label{font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);font-weight:var(--gnrc-font-weight-functional-bold);color:var(--gnrc-color-foreground-neutral-secondary);}
.topic-material-reference-formats{margin:var(--gnrc-spacing-component-base-300) 0 0;font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);font-weight:var(--gnrc-font-weight-functional-regular);color:var(--gnrc-color-foreground-neutral-secondary);}
.topic-material-dialog .topic-material-drop:has(button:enabled):hover{background:var(--gnrc-color-background-neutral-transparent-hover);}
</style>'''
i=s.rfind('</body>');s=s[:i]+css+s[i:];p.write_text(s)
Path('/tmp/syllabus-reference-restore.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
