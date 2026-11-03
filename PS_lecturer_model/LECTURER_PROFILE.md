# IE2024 Probability & Statistics — Lecturer Thinking-Pattern Profile

A reusable model of **how this lecturer sets questions**, built from every question in the three available papers. Use it together with `question_bank.json` (same folder), which stores each past question as a tagged record. Before writing any IE2024 question, read this file, then look up the related past questions in the bank.

| Source | File | Kind | Records |
|---|---|---|---|
| F2024 | `1st.pdf` | Final, Oct 2024 — 2 h, 4 × 25 marks, essay | 22 |
| F2025 | `2nd Batch Paper.pdf` | Final, May 2025 — 2 h, 4 × 25 marks, essay | 25 |
| MOCK | `Mock_Questions_IE2024.pdf` | Lecturer-issued practice set, 15 × 3 sub-questions, no marks | 45 |

> The mock states that **the final exam also has MCQs covering the full syllabus**, and that the mock gives no hint of the exam's content. All three papers are essay-type, so this profile describes the lecturer's *thinking*, which MCQs should then test in MCQ form.

---

## 1. How a paper is built

- **The four finals questions have a fixed template**, in the same order every time:
  - Q1: sampling + descriptive statistics
  - Q2: probability + distributions
  - Q3: inference
  - Q4: linear regression
- **Every question opens with a context paragraph** that restates the topic ("Sampling is the process of…", "Probability theory is a branch of…"). It carries no data; the data is in the sub-parts.
- **Sub-parts escalate in this order:** compare/explain, then show-that (a proof), then a calculation, then an interpretation or critical evaluation.
- **Critical values are always given in brackets** (`t2.5%,5 = 2.57`, `z95% = 1.645`, `F-table = 3.89`, `χ²0.05,2 = 5.991`, `z0.90 = 1.282`). Students are never expected to look anything up.
- **Non-programmable calculators are allowed**, so the arithmetic is light, with friendly numbers (TSS = 1000).

### Marks by lecture across both finals (200 marks)

| Lecture | Marks | Share | Notes |
|---|---|---|---|
| L1 Sampling | 10 | 5% | Always "probability vs non-probability" or "stratified vs cluster" |
| L2 Descriptive | 44 | 22% | Proofs about IQR and variance, skewness from histograms, correlation ≠ causation, scatter plots |
| L3 Probability & distributions | 55 | 28% | Event properties, Bernoulli/Poisson/exponential, a PDF worked end-to-end |
| L4 Inference | 45 | 23% | Estimator properties, Type I/II, pooled-t CI, two-sample z, ANOVA table |
| L5 Regression | 46 | 23% | Assumptions, dummy variables, R² = 1 − SSE/TSS, slope/intercept meaning |
| L6 Time series | 0 | 0% | Only in the mock (additive vs multiplicative, T×S×C×I), but on the syllabus |

---

## 2. Question archetypes (A1–A10)

The `archetype` field in `question_bank.json` uses these ids. The counts cover all 92 records.

| Id | Archetype | Count | What he is really testing | Example |
|---|---|---|---|---|
| **A1** | Compare & contrast / "briefly explain" a pair | 19 | That the student knows the **distinguishing property**, not just two definitions | probability vs non-probability sampling; stratified vs cluster; Type I vs II; point vs interval estimator; unbiased vs efficient; variance vs SD; independent vs mutually exclusive; prior vs conditional; additive vs multiplicative |
| **A2** | "Show that" proof | 5 | Fluency with **definitions turned into algebra** | IQR = (b − a)/4 from the 1.5×IQR fences; n = a/(a − b) from the n − 1 vs n divisors; Bernoulli E(X) = p; E(X̄) = μ; V(X) = E(X²) − E(X)² |
| **A3** | Check a property from numbers | 3 | Using the **formal test** instead of intuition | independence via P(A∩B) = P(A)P(B); mutual exclusivity impossible when P(A) + P(B) > 1 |
| **A4** | Model the scenario, then compute | 24 | Choosing the **right distribution and parameter** for a story | Poisson with a rate rescaled to the interval; binomial n, p; normal percentile; CLT standard error; least-squares coefficients; PDF constant/E/Var/CDF |
| **A5** | Trap | 4 | Whether the student **thinks before calculating** | P(X = exactly 2) for a continuous variable = 0; irrelevant details (Jenny's birthday range, unknown year gives 1/7); memoryless "given 7 days already"; the base-rate effect in Bayes |
| **A6** | Inference procedure | 12 | Selecting the **correct test or interval** and stating H0/H1 properly | pooled-variance t CI; two-sample z (one-tailed); one-sample z; ANOVA table completion; chi-square independence |
| **A7** | Interpret a result or figure | 15 | Turning a number into a **correct sentence** | CI meaning; slope/intercept in context; R² as "% of variation explained"; residual sign; skew from mean/median/mode; scatter-plot strength |
| **A8** | Critically evaluate a statement | 3 | **Correlation ≠ causation** (in both finals), and judging a biased sample allocation | "Critically analyze 'Correlation does not imply causation'" |
| **A9** | Regression practice | 6 | Assumptions (linearity, independence, homoscedasticity, normal errors) and **k − 1 dummy variables** | Gender (2 categories) gives 1 dummy; a 3-category variable gives 2 dummies |
| **A10** | Set up, don't solve | 1 | Writing the **correct integral/limits** without evaluating | P(2 < X < 4) = ∫₂⁴ (1/3)e^(−x/3) dx |

---

## 3. His favourite traps (use them, in MCQ form)

1. **Continuous point probability.** He asks for P(X = exactly a) for an exponential/normal variable; the answer is 0, and students who plug a into the PDF lose the marks.
2. **Rate scaling (Poisson).** The rate is given "per minute" and the window is 4 minutes, so λ = 16. Students who use λ = 4 are wrong. This exact question is in **both** finals.
3. **Sum of probabilities > 1.** P(A) = 0.8 and P(B) = 0.9 can't be mutually exclusive.
4. **Irrelevant precision.** A date range plus an unknown year makes the weekday uniform, so the answer is 1/7. Extra detail is a decoy.
5. **n − 1 vs n.** Sample vs population variance (a full 7-mark proof in F2025, and the mock asks for *sample* variance).
6. **Memorylessness.** "Given it has already run 7 days…": the conditional probability equals the unconditional one.
7. **Base rate in Bayes.** A positive test with a rare condition: the posterior is far below the sensitivity.
8. **Extrapolated intercept.** The intercept at x = 0 is often meaningless (0 m², 0 study hours).
9. **Correlation ≠ causation** and **R² ≠ causation**.
10. **The CI misconception**, taught explicitly on the L4 slide: "95% confident" is about the method's long-run success rate, **not** "a 95% chance μ is in this interval".

---

## 4. Phrasing and notation habits

- **Verbs:** "Compare and contrast", "Briefly explain", "Show that", "Critically analyze / discuss / evaluate", "Interpret", "Analyze", "Write the Null & Alternative hypotheses".
- **Critical values** are written as `t2.5%,5`, `z95%`, `F-table`, `χ²0.05,2`, and **rounded** (t = 2.57, not 2.571).
- **Regression vocabulary:** "Total Sum of Squares (TSS)", "Sum of Squares of Error (SSE)", "Coefficient of Determination", "GPA-hat = b0 + b1 × Study_Hours".
- **ANOVA table layout:** Source of variation | Degrees of freedom | Sum of Squares | Mean Sum of Squares | F-statistic, with Between Groups and Within Groups rows.
- **Descriptive conventions (mock):** IQR by the **median-of-halves** method; outliers by the **1.5 × IQR** rule; *sample* variance with n − 1.
- **Time series (mock and L6):** additive Y = T + S + C + I; multiplicative Y = T × S × C × I; multiplicative when the seasonal swings grow with the trend.
- **Recycling:** the Poisson rat question, the pooled-t CI (4 males / 3 females, 72/132 vs 60/100) and the whole regression question (TSS = 1000; GPA on Study_Hours) appear **in both finals with only the numbers changed**. These are high-probability exam ideas.

## 5. Flaws in his papers (do NOT imitate)

- **Ambiguity:** F2025-Q1d, the energy-per-star ratio, has two defensible readings (a ratio of totals gives 118 stars; a mean of the daily ratios gives about 154). A mock question must have exactly one defensible answer.
- **Terminology slips:** "Cumulative Density Function" (it should be cumulative *distribution* function).
- **Rounded critical values** without saying so (2.57). In a mock, state the value used and compute with exactly that value.

---

## 6. Turning his thinking into MCQs

Every archetype has an MCQ form. Write MCQs in these forms, not as "What is the definition of …".

| Archetype | MCQ form that keeps his thinking |
|---|---|
| A1 compare | "Which statements correctly distinguish X from Y?": options mix true distinguishing properties with properties *shared* by both, or swapped |
| A2 show-that | "A student's derivation of … is below. Which step is the first wrong one?", or "Which identity is used between step 2 and step 3?" |
| A3 check property | Give P(A), P(B), P(A∪B); options claim independent / exclusive / both / neither, with reasons |
| A4 compute | A numeric best-answer whose distractors are the results of named mistakes (λ not rescaled, n instead of n − 1, z instead of t, SD instead of SE) |
| A5 trap | Options include the "plug-in" answer next to the correct trap answer (e.g. 0 vs f(2)) |
| A6 procedure | "Which test or interval is appropriate here, and why?"; "Which H1 matches 'males performed better'?"; a partially filled ANOVA table where the student picks the missing values |
| A7 interpret | **True/false sets about a given result**, e.g. a computed CI, R², slope, residual or p-value decision: "Which statements are TRUE?" |
| A8 evaluate | Classmates' claims about a correlation or a sampling plan: "Who is correct and why?" |
| A9 regression | How many dummies, what the baseline means, which assumption a residual plot violates |
| A10 set up | Choose the correct integral, limits or expression without evaluating it |

### Anti-patterns that mark a question as weak or AI-generated

- definitional stems ("What is a sample space?") when a scenario version exists
- the correct option is the longest and most qualified
- "All/None of the above"
- numeric distractors that aren't produced by any real mistake
- a slide sentence lightly reworded as the correct option
- the answer can be found by matching a word in the stem
- unrealistic or ugly numbers
- trivia (names of methods' inventors, history, years)
- two defensible answers.

---

## 7. Using the bank (for future sessions)

```python
import json
bank = json.load(open("PS_lecturer_model/question_bank.json"))["questions"]
traps      = [q for q in bank if q["trap"]]                          # all trap questions
recycled   = [q for q in bank if q["repeats"]]                       # asked in more than one paper
inference  = [q for q in bank if q["lecture"] == "L4"]
interprets = [q for q in bank if q["archetype"].startswith("A7")]
```

Every record has `id, source, question, part, marks, lecture, topic, skill, archetype, trap, given, text, answer, repeats, note`. Every number in `answer` was computed by a script. To add a new past paper, append records in the same shape, then update the counts in sections 1–2.
