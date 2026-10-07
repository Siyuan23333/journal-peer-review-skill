# Report template with sentence patterns

This is the skeleton of a review the user approved (a medical-imaging AI classification paper). The patterns are generalized. Replace everything in <angle brackets>. If the user has earlier finished reviews on this machine, read one locally for style. Never copy review text into this skill or any shared file, because peer-review material is confidential.

```markdown
# Reviewer Comments to the Authors

*Manuscript <ID>: “<title>”*

*Page numbers refer to the manuscript pages (page 1 begins with the Abstract), and line numbers to the margin numbering. Line numbers restart on each page; “top of page” means the unnumbered lines above line 1.*

The authors compare <methods, in the reviewer's framing> for <task> on <data type>. <Models / pipeline in one sentence>. The data are <n> <images> from <a single center>: <class counts>. The models are trained separately for each of the <k> tasks — <task list> — and evaluated on <split / validation design, hedged if unstated>. In this setting, <what works>, whereas <what does not, in words, no exact metrics>, and <the headline comparison in words>.

The clinical question is relevant, since <reason>. Strengths of the manuscript include <A>, <B>, and <C>. However, several issues need to be addressed before the conclusions can be fully assessed. My main concerns are <topic 1>, <topic 2>, <topic 3>, <topic 4>, and <topic 5>.

## Major Comments

**1. <Topic title, not a verdict>.** I could not find the following anywhere in the manuscript, including Section <x>: (a) <…>; (b) <…>; (c) <…>. This information would help readers judge whether <risk 1>, which would <consequence>, whether <risk 2>, and how <risk 3>, given <the manuscript's own statement> (p. <n>, lines <a–b>).

<Direct question about the key missing fact>? If <condition>, I would suggest <fix> and <repeating the evaluation>. It would also be helpful to describe <details>; if <confirmation> is not available, stating <it> as a limitation would be sufficient. Please also add the other items listed above, using, for example, <specific test> for item (<x>).

**2. <Possible problem>.** The example images suggest that <hedged observation>. <Specific observation with Fig. and panel labels>. <Second observation>. This would be expected if <mechanism>. These observations are based on a few small example images and may not hold for the whole dataset. However, if <condition>, <consequence>, and the results might not generalize to clinical practice. In an earlier <comparable> study, <evidence> (<Author> et al., <year>).

As an essential step, I would suggest <tabulating …>. <Targeted re-analysis> would be particularly informative. If <it is infeasible>, please discuss this as a limitation.

**3. <Performance problem>.** <Metric as counts n/N, with Fig./Table>. <Second fact; the authors' CI includes chance, or "only modestly above the <baseline>">. As the authors note, <why it matters clinically>, so <consequence>. Although study designs differ, several studies reviewed in Section 2 report <better result> (e.g., <n/N> in <Author> et al. [<ref>], <key qualifier>, and <n/N> in <Author> et al. [<ref>]). Given this performance, describing <results> as “<quoted claim>” (p. <n>, lines <a–b>) seems too strong.

I would suggest reporting <per-class metrics with CIs>, giving <key metric> in the Abstract, and analyzing <the failures>. <Secondary test>: it would also be helpful to test whether <…>. Please also explain why <…> (p. <n>, lines <a–b>).

**4. <Claimed superiority>.** The Abstract states that <method> “<claim>” (p. 1, lines <a–b>), and the Conclusion repeats this claim (p. <n>, lines <a–b>). However, in <Task/Table A> <observation>. In <Task B>, <observation> (Table <x>). In <Task C>, <observation> (Table <y>). I appreciate <what the authors did well> and the authors’ own note that “<their caution, quoted>” (p. <n>, line <m>). However, <why that is not enough>.

Please compare <…> with <named paired tests>. Unless these tests show a clear advantage, I would suggest tempering the claim in the Abstract and Conclusion, for example by stating that <accurate wording>.

**5. <Untested components>.** The contributions present <component> as <claimed benefit> “<quote>” (p. <n>, lines <a–b>), but <it is never compared with the stated alternative>. Likewise, the contributions credit <components> with “<quote>” (p. <n>, lines <a–b>), but neither is compared with the same pipeline without it. These comparisons would help readers judge whether each component is worth its added complexity, which is not clear. For example, <concrete reason for doubt> and <evidence from cited literature, accurately qualified>.

I would suggest an ablation study in which the authors (a) <…>, (b) <…>, and (c) <…>. All three comparisons are needed to support the stated contributions.

**6. <Interpretation of explainability maps>.** Section <x> states that <…> “<quote>” (p. <n>, lines <a–b>), and the Conclusion links them to “<quote>” (p. <n>, line <m>). It is commendable that <…>, but the manuscript does not analyze them. Each Results section refers to its figure in a single general sentence (e.g., “<quote>”, p. <n>, line <m>), and <no quantitative assessment>. <Specific observation>. As a result, the claims that <…> do not yet seem to be supported by the evidence presented, particularly for <…>.

It would be helpful to quantify <…>, for example as <operational definition>. Such an analysis would also help test <link to another Major comment>. Alternatively, <the softer option>. Please also <…>.

**7. <Framing and novelty>.** The Title, Abstract, and first contribution (p. <n>, lines <a–b>) describe <framing>. However, <quoted fact contradicting it> (p. <n>, top of page). <Consequence>. Because readers are likely to expect <…> from the term “<…>”, the current wording may overstate the methodological contribution. The gap statement that “<quote>” (p. <n>, line <m>) also seems inconsistent with several studies reviewed in Section 2. For example, <counter-examples with [refs]>.

The study should be described as <accurate description>. Alternatively, the authors should consider <stronger experiment>. Please also clarify how the present work differs from <Author> et al. [<ref>], who <shared elements, fairly stated>. I would also suggest discussing the study by <Author> et al. (<year>), “<full title>”, which <what it evaluated>.

**8. Discussion, limitations, and clinical claims.** The manuscript moves directly from the Results (Section <x>) to the Conclusion (Section <y>). As a result, <what is missing>. Some statements in the Conclusion also overstate what was evaluated. Describing the framework as “<quote>” (p. <n>, lines <a–b>) seems too strong, given <…>. Similarly, the claim of “<quote>” (p. <n>, lines <a–b>) is not convincing, since <…> (Major comments <i> and <j>). The expectation that the framework will “<quote>” (p. <n>, lines <a–b>) would also require <evidence>, neither of which was performed.

Please add a Discussion section that compares the results with the studies in Section 2, discusses <…>, and states the limitations. If the additional analyses suggested above are not performed, the limitations should cover <…> (Major comment <i>), <…> (Major comment <j>), and <…> (Major comment <k>). The Conclusion claims quoted above should also be toned down, with the clinical benefits presented as hypotheses for prospective evaluation.

## Minor Comments

Minor comments are listed in page order.

1. Page 1, lines <a–b> (Abstract): Please consider adding <…>.

2. Pages <a–b> (<Section>): <observation>. <suggestion> would be easier to follow.

3. Page <n>, line <m>: “<wrong text>” should be replaced with “<correct text>”.

4. Page <n>, lines <a–b>; Fig. <x>; page <n2>, lines <c–d>: <inconsistency described with quotes>. A single consistent description would help.

5. Page <n>, lines <a–b> and <c–d>: The whole passage beginning “<…>…” (lines <a–b>) is repeated word for word at lines <c–d>.

6. Page <n>, lines <a–b>: <items> are said to have been examined, but <what is actually shown>. Please add them, for example as supplementary material, or remove the statements.

7. Page <n>, lines <a–b>, and Table <x>: <content> would be better placed in the Methods.

8. Page <n>, lines <a–b>: The text appears inconsistent with <Fig./Table>. <What the figure shows, with counts>, whereas the text gives <…>. Please correct this, as <why it matters>.

## References

- <Author> <Initials>, et al. <Title>. <Journal>. <Year>;<vol>:<page>. doi:<…>
```

Not every review needs eight Major comments. Choose the topics with the user and order them by importance. The skeleton shows which sentence patterns go with which kind of problem.
