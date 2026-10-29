from pathlib import Path
p=Path("index.html");s=p.read_text()
needle=',syllabusDemoDate&&u.jsx("p",{className:"syllabus-calendar-demo-date",children:`Demo date: ${HU(syllabusDemoDate)}`})'
assert s.count(needle)==1
p.write_text(s.replace(needle,""))
