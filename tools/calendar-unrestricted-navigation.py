"""Allow browsing empty dates; missing course events do not disable calendar days."""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
patches=[('showWeekNumbers:!1,selectableWeeks:e,referenceDate:l,eventMarks:','showWeekNumbers:!1,referenceDate:l,eventMarks:'),('"aria-label":"Previous date range",disabled:W<=Zi[0],','"aria-label":"Previous date range",'),('"aria-label":"Next date range",disabled:W>=Zi[Zi.length-1],','"aria-label":"Next date range",')]
for a,b in patches:
 assert s.count(a)==1,(a,s.count(a));s=s.replace(a,b)
s=s.replace('</head>','<style>button._day_k5kpl_23:not(:disabled){cursor:pointer;}</style></head>',1)
p.write_text(s);Path('/tmp/syllabus-calendar-open.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
