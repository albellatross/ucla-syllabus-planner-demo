"""Use original syllabus upload classes directly; remove material-well overrides."""
from pathlib import Path
p=Path('index.html');s=p.read_text()
changes=[('className:`${sn.uploadArea} topic-material-drop`','className:sn.uploadArea'),('u.jsx("span",{className:"topic-material-upload-label",children:"Drag and drop your files here"})','u.jsx("span",{children:"Drag and drop your files here"})'),('.topic-material-dialog{width:min(448px,calc(100vw - var(--gnrc-spacing-layout-base-400)));padding:var(--gnrc-spacing-component-base-600);}', '.topic-material-dialog{width:min(448px,calc(100vw - var(--gnrc-spacing-layout-base-400)));padding:var(--gnrc-spacing-component-base-700);}')]
for a,b in changes:
 assert s.count(a)==1,(a,s.count(a));s=s.replace(a,b)
p.write_text(s)
