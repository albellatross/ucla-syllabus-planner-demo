"""Keep date, countdown and overflow action in fixed grid slots in every state."""
from pathlib import Path
p=Path('index.html');s=p.read_text()
a='._topicCard_mtwhd_7:is(:hover,:focus-within) .syllabus-exam-countdown{margin-right:var(--gnrc-spacing-component-base-600);}'
assert s.count(a)==1;s=s.replace(a,'')
css='''
/* The overflow slot exists at rest; revealing its button only changes opacity. */
._topicCard_mtwhd_7 ._cardTop_mtwhd_77{display:grid;grid-template-columns:minmax(0,1fr) max-content 24px;column-gap:var(--gnrc-spacing-component-base-100);align-items:center;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77 ._sourceTiming_mtwhd_21{grid-column:1;grid-row:1;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77 .syllabus-exam-countdown{grid-column:2;grid-row:1;margin:0;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button,._topicCard_mtwhd_7 ._cardTop_mtwhd_77>div{grid-column:3;grid-row:1;position:static;inset:auto;width:24px;min-width:24px;height:24px;margin:0;opacity:0;transition:opacity 100ms ease;}
._topicCard_mtwhd_7:is(:hover,:focus-within) ._cardTop_mtwhd_77>button,._topicCard_mtwhd_7:is(:hover,:focus-within) ._cardTop_mtwhd_77>div,._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button[aria-expanded="true"],._topicCard_mtwhd_7 ._cardTop_mtwhd_77>div:has(:popover-open){opacity:1;}
@media(hover:none){._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button,._topicCard_mtwhd_7 ._cardTop_mtwhd_77>div{opacity:1;}}
@media(prefers-reduced-motion:reduce){._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button,._topicCard_mtwhd_7 ._cardTop_mtwhd_77>div{transition:none;}}
'''
i=s.rfind('</body>');s=s[:i]+'<style>'+css+'</style>'+s[i:];p.write_text(s)
