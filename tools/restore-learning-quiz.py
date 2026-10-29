"""Restore inline practice after analysis; authored scenario questions, not title recall."""
from pathlib import Path
import re,json
p=Path('index.html');s=p.read_text()
def patch(a,b):
 global s
 assert s.count(a)==1,(a[:80],s.count(a));s=s.replace(a,b)
patch('function sN(i,A){','function syllabusBaseLearning(i,A){')
packs=[{
'match':r'psych|sex|parent|love|attract|social|research',
'answer':'''## Read the evidence, not just the conclusion

*General psychology practice — not a prediction of your exam. This demo has not read your uploaded course materials.*

For this assessment, confirm the covered topics with your instructor’s review sheet. Meanwhile, use this short exercise to practise evaluating a psychological claim.

### Separate a finding from its explanation

An association between two measured variables does not establish which one causes the other. A third variable may influence both. A larger sample can improve precision without resolving that causal ambiguity.

### Apply it to a study

Suppose students who attend more campus events also report feeling more connected. Attending events might help, but students who already feel connected might attend more often. Living on campus could also influence both measures.

Randomly assigning an invitation to an event can help test the effect of receiving that invitation. It does not automatically identify the effect of actually attending: students still choose whether to go.

### Try the question below

Decide what the design lets you conclude, then identify the strongest remaining alternative explanation.

[Background: OpenStax · Analyzing Findings](https://openstax.org/books/psychology-2e/pages/2-3-analyzing-findings)''',
'quiz':{'question':'Students are randomly assigned either an event invitation or no invitation. Some invited students do not attend; some uninvited students attend anyway. The invited group later reports greater belonging. Which conclusion is best supported?', 'options':['Attending the event increased belonging; randomization isolates the effect of attendance.','Receiving the invitation increased reported belonging in this study, but the effect of attendance itself is not isolated.','The study is purely correlational because students chose whether to attend.','The invitation had no effect because not everyone complied with their assignment.'],'correctIndex':1,'explanation':'The correct option separates the randomized intervention (invitation) from the self-selected behavior (attendance). The attendance claim confuses those effects. Calling the study purely correlational overlooks random assignment. Claiming no effect treats incomplete participation as proof; it changes interpretation but does not erase the group difference. Revisit the distinction between what was assigned and what was measured.','hint':'Which variable did the researchers actually assign at random?','evidence':'Randomly assigning an invitation to an event can help test the effect of receiving that invitation.'}},
{'match':r'miller indices', 'answer':'''## Miller indices: check the geometry

Miller indices describe plane orientation using intercepts measured in unit-cell lengths. Take reciprocals, then clear fractions to obtain the smallest whole-number ratio. A plane parallel to an axis has a zero index on that axis.

### Worked example

For intercepts 1, 2, ∞, the reciprocals are 1, ½, 0, giving (210). Translating a parallel plane changes its intercept distances but preserves its orientation and reduced indices.

### Transfer the method

For a new plane, calculate the reciprocal ratio before looking at the answer choices. Check which axis the plane is parallel to.

[Background: Cornell-hosted teaching notes](https://www.classe.cornell.edu/~dms79/xrd/xtallography/Miller%20Indices.htm)''','quiz':{'question':'A plane intercepts the axes at 2a, 3b and ∞c. A second parallel plane intercepts them at 4a, 6b and ∞c. Which pair of reduced Miller indices is correct?','options':['(230) and (460)','(320) and (320)','(320) and (640)','(230) and (230)'],'correctIndex':1,'explanation':'The reciprocal ratios are (1/2, 1/3, 0) and (1/4, 1/6, 0); clearing fractions gives (320) for both. The (230) choices copy intercepts instead of reciprocating. The (640) choice fails to reduce the second ratio. The zero index confirms both planes are parallel to c.','hint':'Reduce each reciprocal ratio separately. Should translating a plane change its orientation?','evidence':'Translating a parallel plane changes its intercept distances but preserves its orientation and reduced indices.'}}
]
helper='function sN(i,A){const assessment=/exam|midterm|final|quiz|test/i.test(`${i.topic.eventType||i.topic.kind} ${i.topic.title}`);const text=`${A||i.topic.title}${assessment&&/psych/i.test(i.course.code)?" psychology research":""}`;const packs='+json.dumps(packs,ensure_ascii=False)+';for(const pack of packs){if(new RegExp(pack.match,"i").test(text))return {answer:pack.answer,quiz:[pack.quiz]}}return syllabusBaseLearning(i,A)}'
patch('function syllabusBaseLearning(i,A){',helper+'function syllabusBaseLearning(i,A){')
# Reuse authored question for Quiz creations too, including assessment cards.
patch('function EN(i,A,t){var h;','function EN(i,A,t){const authored=sN(i,A);if(t==="Quiz"&&authored.quiz?.length)return {answer:"## Apply what you learned\\n\\nChoose the strongest conclusion, then review the reasoning for each option.",quiz:authored.quiz};var h;')
patch('Each object must contain question, options (2–4 distinct strings), correctIndex (zero-based integer), explanation, and evidence','Use an application, comparison, or transfer scenario that requires reasoning from the article; avoid definition recall, answer copying, and implausible distractors. Explain the correct reasoning and why each distractor fails without claiming unverified exam alignment. Each object must contain question, options (2–4 distinct strings), correctIndex (zero-based integer), explanation, and evidence')
p.write_text(s);Path('/tmp/syllabus-quiz.js').write_text(max(re.findall(r'<script[^>]*>(.*?)</script>',s,re.S),key=len))
