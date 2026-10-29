"""Remove caption; restore focus to the primary action after a file is removed."""
from pathlib import Path
p=Path('index.html');s=p.read_text()
changes=[
(',u.jsx("p",{className:"topic-material-preview",children:"Prototype: files are kept as references; their contents aren’t read."})',''),
('onClick:()=>g(files=>files.filter(item=>item.id!==file.id))','onClick:()=>{g(files=>files.filter(item=>item.id!==file.id));requestAnimationFrame(()=>document.getElementById("topic-material-primary")?.focus())}'),
('u.jsx(EA,{appearance:"primary",onClick:()=>{if(m.length){R("references");closeMaterialGate()}else materialGateInput.current?.click()},children:m.length?"Continue":"Choose files"})','u.jsx(EA,{id:"topic-material-primary",appearance:"primary",onClick:()=>{if(m.length){R("references");closeMaterialGate()}else materialGateInput.current?.click()},children:m.length?"Continue":"Choose files"})')]
for a,b in changes:
 assert s.count(a)==1;s=s.replace(a,b)
css='<style>.topic-material-dialog .syllabus-material-files li>button{flex:none;}.topic-material-dialog .syllabus-material-files li>span{min-width:0;overflow-wrap:anywhere;}</style>'
i=s.rfind('</body>');p.write_text(s[:i]+css+s[i:])
