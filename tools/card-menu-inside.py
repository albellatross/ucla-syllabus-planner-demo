"""Keep overflow action inside the card; stable left-aligned metadata pair."""
from pathlib import Path
p=Path('index.html');s=p.read_text()
changes=[('[aria-label="Syllabus cards"]{box-sizing:content-box;padding:12px;margin:-12px;gap:24px;}',''),('grid-template-columns:minmax(0,1fr) max-content;column-gap:var(--gnrc-spacing-component-base-100);align-items:center;}','grid-template-columns:minmax(0,max-content) max-content;justify-content:start;column-gap:var(--gnrc-spacing-component-base-100);align-items:center;padding-right:28px;box-sizing:border-box;}'),('right:-28px;top:-12px;','right:0;top:-2px;'),('border:var(--gnrc-stroke-width-thin) solid var(--gnrc-color-stroke-neutral-subtle);border-radius:var(--gnrc-border-radius-circular);background:var(--gnrc-color-surface-neutral-nearer);opacity:0;','border:0;border-radius:var(--gnrc-border-radius-base-100);background:var(--gnrc-color-background-neutral-transparent);opacity:0;')]
for a,b in changes:
 assert s.count(a)==1,(a,s.count(a));s=s.replace(a,b)
p.write_text(s)
