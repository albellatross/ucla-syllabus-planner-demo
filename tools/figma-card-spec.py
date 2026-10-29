"""Figma C5 2912:102496; instances 2905:102041/102121/102292/102364/102431.
Reuse bundled Fluent Card. Pinned Fluent package has no Badge export; existing
semantic span adapts Badge tint/rounded styling using the same token system.
"""
from pathlib import Path
import re
p=Path('index.html');s=p.read_text()
def patch(a,b):
 global s
 assert s.count(a)==1,(a[:80],s.count(a));s=s.replace(a,b)
patch('children:[DA&&u.jsx(oJ,{role:"img","aria-label":"Due soon"}),bA.topic.date?', 'children:[bA.topic.date?')
patch('countdown&&u.jsx("span",{className:"syllabus-exam-countdown","data-ended":countdown==="Exam ended"||undefined,title:countdown==="Exam ended"?`${bA.topic.title} has ended`:`Time until ${bA.topic.title}`,children:countdown})','countdown&&u.jsxs("span",{className:"syllabus-exam-countdown","data-tone":countdown==="Exam ended"?"neutral":we(bA.topic.date)&&(Dr(bA.topic.date)-Dr(o))/864e5<=7?"danger":"warning","data-ended":countdown==="Exam ended"||undefined,title:countdown==="Exam ended"?`${bA.topic.title} has ended`:`Time until ${bA.topic.title}`,children:[u.jsx(oJ,{"aria-hidden":"true"}),countdown]})')
css='''
/* Figma 2912:102496 — fixed Card and tint Badge composition. */
._topicCard_mtwhd_7{box-sizing:border-box;flex:0 0 240px;width:240px;height:160px;min-height:160px;padding:calc(var(--gnrc-spacing-component-base-300) - var(--gnrc-stroke-width-thin)) calc(var(--gnrc-spacing-component-base-400) - var(--gnrc-stroke-width-thin));gap:var(--gnrc-spacing-component-base-200);border-radius:var(--gnrc-border-radius-base-600);border:var(--gnrc-stroke-width-thin) solid var(--gnrc-color-stroke-neutral-subtle);background:var(--gnrc-color-surface-neutral-nearer);overflow:visible;}
._topicCard_mtwhd_7 ._cardTop_mtwhd_77{height:20px;min-height:20px;gap:var(--gnrc-spacing-component-base-100);}
._topicCard_mtwhd_7 ._sourceTiming_mtwhd_21,._topicCard_mtwhd_7[data-urgent] ._sourceTiming_mtwhd_21{display:block;min-width:0;margin:0;padding:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--gnrc-color-foreground-neutral-secondary);font-size:var(--gnrc-font-size-functional-body-medium);line-height:var(--gnrc-line-height-functional-body-medium);font-weight:var(--gnrc-font-weight-functional-regular);}
._topicCard_mtwhd_7 ._sourceTiming_mtwhd_21 time{white-space:nowrap;}
._topicCard_mtwhd_7 .syllabus-exam-countdown{display:inline-flex;align-items:center;flex:none;gap:var(--gnrc-spacing-component-base-100);height:20px;box-sizing:border-box;padding:0 var(--gnrc-spacing-component-base-150);border-radius:var(--gnrc-border-radius-base-200);font-family:var(--gnrc-font-family-functional);font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);font-weight:var(--gnrc-font-weight-functional-regular);background:var(--gnrc-color-background-warning-soft);color:var(--gnrc-color-foreground-warning-primary);}
.syllabus-exam-countdown svg{width:16px;height:16px;flex:none;}
._topicCard_mtwhd_7 .syllabus-exam-countdown[data-tone="danger"]{background:var(--gnrc-color-background-danger-soft);color:var(--gnrc-color-foreground-danger-primary);}
._topicCard_mtwhd_7 .syllabus-exam-countdown[data-tone="neutral"]{background:var(--gnrc-color-background-neutral-subtle);color:var(--gnrc-color-foreground-neutral-secondary);}
._topicCard_mtwhd_7 ._cardBody_mtwhd_24{flex:1;min-height:0;gap:0;}
._topicCard_mtwhd_7 ._cardCopy_mtwhd_25 h3,._topicCard_mtwhd_7 ._topicLink_mtwhd_32{font-family:var(--gnrc-font-family-functional);font-size:var(--gnrc-font-size-functional-body-large);line-height:var(--gnrc-line-height-functional-body-large);font-weight:var(--gnrc-font-weight-functional-bold);}
._topicCard_mtwhd_7 ._titleText_mtwhd_118{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:3;overflow:hidden;}
._topicCard_mtwhd_7 ._cardFooter_mtwhd_27{display:flex;align-items:center;justify-content:space-between;flex:none;gap:var(--gnrc-spacing-component-base-200);height:20px;min-height:20px;margin-top:0;margin-bottom:var(--gnrc-spacing-component-base-100);padding:0;}
._topicCard_mtwhd_7 ._kindLabel_mtwhd_29{display:inline-flex;align-items:center;height:20px;box-sizing:border-box;padding:0 var(--gnrc-spacing-component-base-150);border-radius:var(--gnrc-border-radius-base-200);font-size:var(--gnrc-font-size-functional-body-small);line-height:var(--gnrc-line-height-functional-body-small);font-weight:var(--gnrc-font-weight-functional-regular);background:var(--gnrc-color-background-neutral-subtle);color:var(--gnrc-color-foreground-neutral-primary);}
._topicCard_mtwhd_7 ._kindLabel_mtwhd_29[data-sensitive]{background:var(--gnrc-color-background-warning-soft);color:var(--gnrc-color-foreground-warning-primary);}
._topicCard_mtwhd_7 ._courseCode_mtwhd_28{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;text-align:right;font-size:var(--gnrc-font-size-functional-body-medium);line-height:var(--gnrc-line-height-functional-body-medium);color:var(--gnrc-color-foreground-neutral-secondary);}
._topicCard_mtwhd_7:has(._topicLink_mtwhd_32):hover{background:var(--gnrc-color-background-neutral-transparent-hover);}
._topicCard_mtwhd_7:is(:hover,:focus-within) .syllabus-exam-countdown{margin-right:var(--gnrc-spacing-component-base-600);}
@media(forced-colors:active){._topicCard_mtwhd_7 .syllabus-exam-countdown,._topicCard_mtwhd_7 ._kindLabel_mtwhd_29{border:1px solid CanvasText;background:Canvas;color:CanvasText;}}
@media(prefers-reduced-motion:reduce){._topicCard_mtwhd_7{transition:none;}}
'''
i=s.rfind('</body>');s=s[:i]+'<style>'+css+'</style>'+s[i:];p.write_text(s)
Path('/tmp/syllabus-card-spec.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
