"""Restore menu surface sizing; share top-right space without layout shifts."""
from pathlib import Path
p=Path('index.html');s=p.read_text();a=s.rfind('<style>\n/* The overflow slot');assert a>=0;b=s.index('</style>',a)+len('</style>')
css='''<style>
/* Only the trigger is positioned; never constrain the menu surface. */
._topicCard_mtwhd_7 ._cardTop_mtwhd_77{position:relative;display:grid;grid-template-columns:minmax(0,1fr) max-content;column-gap:var(--gnrc-spacing-component-base-100);align-items:center;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77 ._sourceTiming_mtwhd_21{grid-column:1;grid-row:1;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77 .syllabus-exam-countdown{grid-column:2;grid-row:1;margin:0;transition:opacity 100ms ease;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button[aria-haspopup]{position:absolute;inset:auto;right:0;top:-2px;width:24px;min-width:24px;height:24px;margin:0;opacity:0;pointer-events:none;transition:opacity 100ms ease;}
._topicCard_mtwhd_7:hover ._cardTop_mtwhd_77>button,._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button:focus-visible,._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button[aria-expanded="true"]{opacity:1;pointer-events:auto;}
._topicCard_mtwhd_7:hover .syllabus-exam-countdown,._topicCard_mtwhd_7:has(._cardTop_mtwhd_77>button:focus-visible) .syllabus-exam-countdown,._topicCard_mtwhd_7:has(._cardTop_mtwhd_77>button[aria-expanded="true"]) .syllabus-exam-countdown{opacity:0;pointer-events:none;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77>div{position:fixed;inset:auto;width:max-content;min-width:0;height:auto;opacity:1;}
@media(hover:none){._topicCard_mtwhd_7 ._cardTop_mtwhd_77{padding-right:28px;}._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button{opacity:1;pointer-events:auto;}._topicCard_mtwhd_7 .syllabus-exam-countdown{opacity:1!important;}}
@media(prefers-reduced-motion:reduce){._topicCard_mtwhd_7 ._cardTop_mtwhd_77>button,._topicCard_mtwhd_7 .syllabus-exam-countdown{transition:none;}}
</style>'''
s=s[:a]+css+s[b:];p.write_text(s)
