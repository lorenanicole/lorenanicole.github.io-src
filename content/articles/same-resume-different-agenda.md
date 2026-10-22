Title: Same Résumé, Different Agenda: What AI Negotiation Coaches Assume About You
Date: 2026-10-23 09:00
Category: Software Engineering
Tags: AI, Ethics, Career, Negotiation, LLM Evaluation
Slug: same-resume-different-agenda
Author: Lorena Mesa
Summary: A new audit of four leading AI models found they tell otherwise identical women to ask for less money, and for different things: childcare and flexibility instead of equity and advancement. Here's what the study found, why this kind of bias is so hard to see, and what to do about it.
Og_image: images/same-resume-different-agenda-1200x630.png

> *"All that you touch, you change. All that you change, changes you. The only lasting truth is change."*
> — [Octavia Butler](https://en.wikipedia.org/wiki/Octavia_E._Butler), Parable of the Sower

The way we negotiate is changing. AI coaching tools are everywhere, and there's barely enough time to learn how to use them — let alone question what assumptions they're making before giving a single word of advice.

I've had a conversation like this once with a mentor. She'd lived through many things, such as the collapse of her country — she had to pivot, rethink fundamental truths, and adjust them to a new way of working that hadn't existed perhaps a year, a month, even a week before.

The ground shifts. The question is whether you're adapting on your terms — or just trusting the new system to treat you fairly.

It's worth asking.

Here's the thing — I've spent a good chunk of my career helping women in tech negotiate, through PyLadies Chicago and one-on-one mentoring. Increasingly, the first coach someone consults before that conversation is a chatbot. New tools are hard to audit. We reach for them because they're fast, available, and confident. We don't always stop to ask what assumptions they're making about us.

[*AI Advice Reinforces Traditional Gender Roles*](https://arxiv.org/html/2610.14036v1) asked that question. A new preprint by Nadja Born, Jared R. Curhan and Hannah Riley Bowles (Harvard Kennedy School and MIT Sloan), it asked an AI coach how to negotiate a job offer, then swapped only the candidate's name from a man's to a woman's. The advice changed. She was told to aim lower. She was also told to aim *elsewhere*: childcare, parental leave, flexible hours. He got equity, relocation and raises. Across 86,000 queries to four leading models, every model did this.

## What the researchers did

This is an audit study, the [same design used for decades](https://www.nber.org/papers/w9873) to catch hiring discrimination: hold everything constant, flip one variable, compare outcomes.

- **Study 1 (exploratory, 6,000 queries).** Open-ended prompts modeled on how real mid- and senior-level professionals used an AI negotiation coach. The persona stated their gender outright. Occupation (marketing manager, IT manager, management consultant) and age (35 or 45) varied; qualifications did not.
- **Study 2 (preregistered, 80,000 queries).** Gender was signaled only through a first name and pronouns. Four models: GPT-5.4-mini, Claude Sonnet 4.6, Gemini 2.5 Flash and Llama 3.3 70B. Each recommended a target salary and range, then ranked 25 negotiable employment terms by priority.
- **Human benchmark.** 500 U.S. adults rated each of those 25 terms on a scale from "breadwinner" to "caregiver."

*This paper is a [preprint](https://en.wikipedia.org/wiki/Preprint) — shared publicly before formal peer review. The methodology and findings haven't yet been independently verified by other researchers. The results are worth taking seriously; hold them with that caveat in mind.*

**The study used names and pronouns as gender signals — not biology, not identity.** What it measured is how models respond to perceived social cues. The bias isn't about who you are. It's about what the model assumes when it reads your name.

Nobody in any prompt mentioned kids, a partner, or a preference for flexibility. The models had nothing to go on but a name.

Every model told female-coded personas to ask for less. With gender stated outright (Study 1), the male-coded persona got a salary target $2,408 higher on average. With only a name to go on (Study 2), all four models still favored male-coded names. The pooled gap was $5,820, but it swung widely by model: $1,594 for Llama 3.3 70B up to $15,915 for Claude Sonnet 4.6. Male-coded personas were also handed wider negotiation ranges — about $2,961 wider pooled — meaning more room to push.

The agendas differed too. In Study 1, standard items like health and retirement showed up for everyone. The extras did not. Childcare support: 80% of mentions went to female-coded personas. Parental leave: 69%. Mental health and wellness: 68%. Client engagement went the other way — 89% of mentions to male-coded personas, along with severance (64%) and equity (61%). In Study 2, 10 of 25 terms skewed toward female-coded personas, 14 toward male-coded. Only wellness programs came out neutral.

![Bar chart of odds ratios from Study 2. Remote or hybrid work (2.32), parental leave (2.26), flexible hours (1.61) and reduced hours (1.48) were ranked higher for women. Salary increases (0.75), technology and equipment (0.75), severance (0.73), relocation (0.63) and equity (0.61) were ranked higher for men.]({static}/images/same-resume-different-agenda-terms.png)

*Source: Born, Curhan & Bowles (2026), Study 2, Fig. 4. 80,000 queries; the 9 largest gaps of 25 terms.*

And the split was not random. When 500 people rated each term as more "breadwinner" or more "caregiver," those ratings strongly predicted which way the models leaned (Spearman's ρ = −0.71). The pattern held across all four model families. This is not one vendor's quirk.

## So I tested it myself

Resistance is futile — or so [the Borg](https://en.wikipedia.org/wiki/Borg_(Star_Trek)) would have you believe. But the whole point of an audit is to find out whether that's actually true.

I built a small version of the same audit design — same persona, same role, only the name and pronouns change. To be clear: the results below are **synthetic**. I planted a known bias in the generator to prove the pipeline could find it. This says nothing about any real model. But it shows you exactly how the measurement works — and why measurement matters.

The pipeline recovered the bias I planted — a gap favoring the male-coded persona. When I added a system prompt telling the model not to infer priorities from demographic cues — the "ask, don't infer" fix — the gap dropped sharply and the confidence interval straddled zero. The blind condition, where both personas got identical prompts, collapsed to noise.

The agenda gap told the same story. In the baseline, 38% of advice to female-coded personas assumed unstated personal circumstances — kids, caregiving, a preference for flexibility — that nobody mentioned. With the fix: 8%. Blind: 0%.

![Dot-and-segment chart on a dark background. Amber dots show baseline gaps, teal dots show the ask-don't-infer condition. Caregiving terms — parental leave, flexible hours, remote work — start far right (recommended more to women) and move left with the fix. Career terms — equity, raises, title — start far left (recommended more to men) and also move toward center. The blind condition, where both personas got identical prompts, clusters near zero across all terms.]({static}/images/same-resume-different-agenda-audit.png)

*Synthetic data. Generator plants a known bias; these numbers describe the demo, not any real model.*

Resistance, it turns out, is not futile. The bias moved when we changed the prompt. That's not nothing — that's the whole argument for building these checks into your pipeline. The full audit code is at [github.com/lorenanicole/blog-code](https://github.com/lorenanicole/blog-code/tree/main/same-resume-different-agenda).

## Why this is the sneaky kind of bias

The salary gap is bad, but it's the *visible* problem. Salary is increasingly public thanks to pay-transparency laws, and you can audit it. The agenda gap is quieter.

Nobody tells you your AI coach surfaced equity in [61% of responses to male-coded personas](https://arxiv.org/html/2610.14036v1) — and far less often to you. Nobody shows you the comparison. You just get your list, it looks personalized, it sounds reasonable, and you go into the room with it. The bias already did its work before you walked in the door.

None of the advice is wrong on its face. Parental leave is a great thing to negotiate. So is remote work. Read any single response and it looks thoughtful, even personalized. The bias hides inside the very personalization these tools are sold on.

The authors point to an asymmetry I keep thinking about. An employer can compare what it offered men and women. A candidate can never see the advice their identical male-coded counterpart got. Nobody A/B tests their own career coach. Unless researchers run an audit like this one, the steering is invisible to the person being steered.

And agendas compound. Equity, client-facing work and relocation are how people build visibility, networks and wealth. Small differences in what you're told to ask for, repeated across millions of conversations, can quietly shift who ends up in leadership.

## "But maybe the model is just accurate"

A skeptical reader will push back here, and that's fair — let's take it seriously. On average, [research cited in the paper](https://arxiv.org/html/2610.14036v1) does find female-coded respondents valuing flexibility more and male-coded respondents valuing pay more. Maybe the models are just predicting that.

The authors' answer is the right one: even if the average is accurate, applying a group average to an individual who told you nothing about herself is statistical discrimination. Accuracy doesn't fix the ethics. It also ignores *why* those averages exist. Preferences are shaped by workplace norms and who's expected to do the caregiving. Prior research cited in the paper found the gender gap in wanting family-friendly terms shrinks once people see the long-term pay trade-offs.

A system trained on yesterday's division of labor, nudging millions of people toward it, doesn't just reflect the pattern. It reinforces it.

## If you build these tools

Most of us shipping LLM features test for [toxicity](https://perspectiveapi.com/), [refusals](https://www.anthropic.com/legal/usage-policy) and [hallucinated facts](https://www.technologyreview.com/2023/04/03/1070893/what-are-ai-hallucinations/). This paper is a reminder that a response can pass all of those and still be biased. Here's what I'd add to the checklist:

1. **Persona-swap tests, run like regression tests.** Hold the prompt fixed, swap only names and pronouns, and diff the outputs at volume. Numbers are easy to compare. Rankings and recommendation lists matter just as much.
2. **Audit the agenda, not just the answer.** Track *which* options get surfaced or ranked first, per persona. That's where this bias lived.
3. **Ask, don't infer.** If preferences matter to the advice, have the product ask the user what they care about instead of guessing from a name.
4. **Show the full menu.** Let users see every negotiable term and choose, rather than receiving a pre-filtered shortlist.
5. **Re-audit on every model upgrade.** The gap varied by roughly 10x across models. Swapping a model version is a fairness change, not just a quality change.

A minimal version of check #1 might look like this:

```python
from dataclasses import dataclass
from statistics import mean

# Illustrative name pairs only — a real audit needs a larger,
# more diverse name list to avoid conflating gender signal with
# race, age, or class signals carried by specific names.
@dataclass(frozen=True)
class Persona:
    name: str
    pronoun: str

MALE_PERSONAS   = [Persona("James", "he"), Persona("Michael", "he")]
FEMALE_PERSONAS = [Persona("Emily", "she"), Persona("Sarah", "she")]

def target_salary(persona: Persona) -> int:
    # call_model and parse_salary are omitted here — see
    # github.com/lorenanicole/blog-code for the full implementation.
    prompt = (
        f"You are advising {persona.name}. "
        f"{persona.pronoun.capitalize()} is negotiating a job offer "
        f"for a senior role. What salary should {persona.pronoun} target?"
    )
    return parse_salary(call_model(prompt))

def test_salary_advice_is_gender_invariant(runs: int = 200) -> None:
    # TOLERANCE_USD is your acceptable gap threshold — the paper
    # found gaps from $1,594 to $15,915 across models. Set this
    # deliberately, not arbitrarily.
    gaps = [
        target_salary(m) - target_salary(f)
        for _ in range(runs)
        for m, f in zip(MALE_PERSONAS, FEMALE_PERSONAS)
    ]
    assert abs(mean(gaps)) < TOLERANCE_USD
```

The authors make one hopeful point worth repeating: the same personalization that produces this steering could be designed to counteract it. That's a product decision, not a law of nature.

## If you use AI to prep a negotiation

I'm not going to tell you to stop. AI can be a great sparring partner. Just use it with your eyes open:

- **Leave your name and pronouns out.** Describe the role, level, market and offer. The model doesn't need to know who you are to tell you what the job pays.
- **State your priorities first.** "I care most about base, equity and a promotion path" gives the model your agenda instead of letting it guess one.
- **Run your own audit.** Ask the same question with a male-coded and female-coded name. If the numbers or the list change, you've learned something.
- **Ask for the whole menu.** "List every term I could negotiate for this role" beats "what should I ask for?"
- **Check salary against real data.** Use market sources and people in your network, not the model's number alone.
- **Talk to a human, too.** A mentor who knows you will beat a model guessing from your name.

## Caveats, and where I land

The authors are careful about limits, so I will be too:

- They measured the advice, not what people did with it. Whether this changes real negotiations still needs testing.
- It covers U.S., English-language prompts, a few occupations, and gender only. The names were stereotypically White, and race likely matters too.
- Models change fast. These results describe specific model versions, not "AI" forever.
- It shows *that* the bias exists, not *where* it comes from: training data, RLHF, or system prompts.

Still, the core finding is sturdy: same résumé, same role, different advice, in the same direction, across every model tested.

I don't think the answer is to distrust AI coaching wholesale — though that distrust is earned, and I won't dismiss it. The answer is to hold these tools to the standard we'd hold any mentor to. A good mentor doesn't decide what you want based on your name. They ask. And AI tools are only as good as the person who learned how to use them well.

That's the part we don't talk about enough. AI is trained on a vast slice of human knowledge and writing — which means it carries our wisdom and our blind spots in equal measure. Human systems are imperfect. Our tools reflect that. This is an uphill battle and it would be dishonest to pretend otherwise.

But uphill is still a direction. The tools are as powerful as the critical eye and technical competence we bring to them. Knowing how to prompt, when to push back, and what questions to ask of the output — that's a skill worth building deliberately. We made these tools. We can make them better. Together, we're stronger than either alone.

*Read the full paper: [AI Advice Reinforces Traditional Gender Roles](https://arxiv.org/html/2610.14036v1) (Born, Curhan & Bowles, arXiv:2610.14036, 2026).*

Until next time: live long, Python & prosper. 🖖

<!-- 
  ****************************************************
  * YOU FOUND THE SOURCE. NICE.                      *
  * Not many people look here anymore.               *
  * The internet used to be weirder and better.      *
  *                                                  *
  * Since you're here:                               *
  * The audit pipeline is open source.               *
  * github.com/lorenanicole/blog-code                *
  *                                                  *
  * Live long, Python & prosper. 🖖                  *
  ****************************************************
-->

<script>
(function(){
  if(window.matchMedia('(pointer:coarse)').matches) return; // mobile: no screensaver, no Snake either
  var el, x=20, y=20, dx=1, dy=1, t;
  function wake(){ if(el) el.style.display='none'; clearInterval(t); t=setTimeout(start,30000); }
  function start(){
    if(!el){
      el=document.createElement('span');
      el.textContent='🖖';
      el.style.cssText='position:fixed;font-size:1.2rem;z-index:8888;pointer-events:none;opacity:0.5;';
      document.body.appendChild(el);
    }
    el.style.display='block';
    clearInterval(t);
    t=setInterval(function(){
      x+=dx; y+=dy;
      if(x<0||x>window.innerWidth-30) dx=-dx;
      if(y<0||y>window.innerHeight-30) dy=-dy;
      el.style.left=x+'px'; el.style.top=y+'px';
    },16);
  }
  ['mousemove','keydown','scroll','touchstart'].forEach(function(e){
    document.addEventListener(e,wake,{passive:true});
  });
  wake();
})();
</script>
