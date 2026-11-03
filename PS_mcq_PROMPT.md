# PROMPT — IE2024 (Probability & Statistics) Two 50-MCQ Mock Papers

Copy everything below the line into Claude Code, run from the root of this repo.

---

## ROLE

You are setting **two mock MCQ papers** (Paper 1 and Paper 2, **50 MCQs each**) for **IE2024 — Probability and Statistics** (SLIIT, Year 2 Sem 1). You are imitating **this module's lecturer**, whose thinking is captured in `PS_lecturer_model/`. Your job is not to write "quiz questions about statistics". You are writing questions that a student who has memorised the slides but not *understood* them will get wrong.

The papers are **theory-first** (about 75% theory, 25% calculation). Theory here means interpreting results, distinguishing concepts, spotting misconceptions and judging claims, never reciting definitions. Difficulty runs from easy to hard, mixed through each paper. Both papers are **equally hard** and **share no scenarios**.

The student specifically wants to avoid the weak, low-thought question types that AI generators produce (STEP 3.2). Quality beats volume.

You produce **one offline exam app** containing both papers.

---

## STEP 0 — READ BEFORE WRITING ANYTHING

All files are in the **repo root** unless a folder is given. Quote the names, because they contain spaces, parentheses and an en dash.

1. **The lecturer model (read first):**
   - `PS_lecturer_model/LECTURER_PROFILE.md`: how the lecturer sets questions (archetypes A1–A10, favourite traps, phrasing, marks by lecture, flaws not to copy, MCQ forms per archetype, AI anti-patterns).
   - `PS_lecturer_model/question_bank.json`: all 92 past sub-questions as tagged records (`lecture`, `topic`, `skill`, `archetype`, `trap`, `repeats`, verified `answer`). Filter it while writing: for every MCQ, look up the past questions on the same topic and archetype, so the new question tests the same *idea* the lecturer values, from a **new angle with new numbers**.

2. **Lecture slides (the only source of truth for scope and rules):**

   | # | File | Pages |
   |---|---|---|
   | L1 | `L1 - Introduction to Data Analytics and Sampling.pdf` | 29 |
   | L2 | `L2 - Descriptive Statistics.pdf` | 35 |
   | L3 | `L3 - Probability Theory and Distributions (1).pdf` | 79 |
   | L4 | `L4 – Statistical Inference (2).pdf` | 80 |
   | L5 | `L5 - Linear Regression (1).pdf` | 11 |
   | L6 | `L6 - Time Series Analysis.pdf` | 23 |

   The text layers are thin. **Formulas, worked examples and charts are mostly images**, and several L6 slides have no text at all. Render every slide (`pdftoppm -png -r 60`) and **look at** each one that contains a formula, table, chart or worked example. You need the slides' exact formulas and conventions (STEP 1.1).

3. **Past papers (style only; already summarised in the model):** `1st.pdf` and `2nd Batch Paper.pdf` are scans; render them with `pdftoppm -png -r 80` and read the images. `Mock_Questions_IE2024.pdf` has a text layer. They are all essay-type. **Never reuse their scenarios or numbers** (the rat lever, 4 males / 3 females with 72/132 and 60/100, GPA = b0 + b1 × Study_Hours with TSS = 1000, Jenny's birthday, the energy-per-star ratio, the mock's 15 scenarios). Reuse their *ideas*.

4. **App shell:** if `CN_final_mock/index.html` or `OOAD_final_mock/index.html` exists, study it. It is a finished exam app built to almost the same spec (navigator, flags, multi-answer negative marking, feedback, results, retry-missed, saved progress, light/dark theme, self-test). **Reuse its architecture and code**, adapted to this spec. Do not reuse its questions.

If a listed file doesn't exist, search the repo, list what you actually found, and confirm with me before generating.

Do **not** write style-notes, audit or report files. Put the effort into the papers.

---

## STEP 1 — SCOPE AND QUALITY RULES

### 1.1 Lecture-only, using the slides' own formulas and conventions

If a rule, formula or value is not in the slides, it **cannot be the correct answer**. It may appear as a distractor, and the explanation must say it is outside the lectures.

Check each of these in the slides (images included) and follow the slides exactly:

- **L1:** primary vs secondary data; variable types; the four domains of data analytics; population vs sample; sampling frame; the probability methods (simple random, stratified, cluster); the non-probability methods (convenience, voluntary response, purposive/judgement, snowball); sample size and the Krejcie & Morgan table (only if a question supplies the table)
- **L2:**
  - mean/median/mode
  - quartiles: use the **median-of-halves** method, as the mock does, unless the slides show a different one; if so, state the method in the stem
  - range and IQR; outliers by **1.5 × IQR**
  - **sample variance with n − 1** vs population variance with n; standard deviation
  - skewness and kurtosis; how mean, median and mode sit under skew
  - boxplot reading; choosing a chart (line, histogram, bar, pie, multiple/stacked bar, side-by-side boxplots, scatter)
  - covariance vs correlation
- **L3:**
  - experiment, trial, sample space; mutually exclusive / collectively exhaustive / independent events
  - classical probability and its properties; joint, conditional and total probability; Bayes' theorem
  - random variables, pmf/pdf, moments, and the properties of E(X) and V(X)
  - discrete uniform, Bernoulli, binomial, Poisson, normal, standard normal (Z table), exponential (memoryless)
  - the sampling distribution of the mean (CLT)
- **L4:**
  - unbiased and most efficient estimators; interval estimation; CIs for μ with σ known (z) and unknown (t)
  - **the slide's CI interpretation and misconception**
  - hypothesis-testing steps; Type I/II errors; the significance level; z and t tests
  - two population means (pooled CI; unpaired vs paired)
  - one-way ANOVA (the table and F test) and post-hoc ideas
  - chi-square (two proportions, several proportions, independence) and the "Important Facts About Chi Square Test" slide (Z² = χ² with 1 df, expected counts ≥ 5, chi-square can't test a direction)
- **L5:** simple vs multiple linear regression, least squares, interpreting slope and intercept, dummy variables (k − 1), R² = 1 − SSE/TSS, and the assumptions as the slides list them
- **L6:** the components T, S, C, I; additive Y = T + S + C + I vs multiplicative Y = T × S × C × I and when to use each; forecasting and the forecasting models the slides describe

### 1.2 No trivia (hard rule)

Never test any of these as the point of a question:

- dates or history ("when was…")
- people's names ("who proposed…", including "Krejcie and Morgan" as an answer)
- organisations
- "name the N types/methods" lists with no reasoning.

If a question needs a name or a table value to reason with, give it in the stem. "The four domains of data analytics" is fine as *"a team that predicts next quarter's demand is doing which kind of analytics, and why"*. It is not fine as *"list the four domains"*.

### 1.3 Don't copy the lecturer's flaws

Profile §5: no ambiguous wording (every question must have **exactly one defensible answer set**), no terminology slips, and **state every critical value you use** and compute with exactly that value.

---

## STEP 2 — PAPER STRUCTURE (identical blueprint for Paper 1 and Paper 2)

### 2.1 Questions and marking

| Type | Count per paper | Input | Options | Marking (2 marks per question) |
|---|---|---|---|---|
| **Multi-answer** | 30 | checkboxes | 5 | the number of correct options is **hidden** ("Select all that apply"); with *k* correct options, each correct tick earns **+2/k** and each wrong tick costs **−2/k**; the score is clamped to **0 to 2** |
| **Best-answer** | 20 | radio | 4 | 2 or 0, no negative marking |

- **Per paper:** 50 questions × 2 = **100 marks**.
- **Multi-answer correct-counts per paper:** exactly **4 with 1 correct, 9 with 2, 10 with 3, 7 with 4**.
- At least **6** best-answer questions per paper have a **defensible runner-up** that only loses by the slides' rule, and the explanation says why it loses.

### 2.2 Lecture allocation per paper (by lecture size)

| Lecture | Per paper | Must include across the two papers (new angles, never the past numbers) |
|---|---|---|
| L1 Sampling & data | 5 | choosing/identifying a sampling method from a scenario; stratified vs cluster (what makes each valid); bias from non-probability methods; proportionate allocation; variable types in context |
| L2 Descriptive | 7 | skew from mean/median/mode (and a histogram figure); a robust vs sensitive measure when an outlier is present; the 1.5×IQR fences; n − 1 vs n; boxplot reading; covariance vs correlation; choosing a chart for a purpose |
| L3 Probability & distributions | 15 | independent vs mutually exclusive (with numbers); conditional probability and Bayes (base rate); the complement rule; choosing a distribution and parameter for a story (binomial / Poisson with **rate scaling** / normal / exponential); the **continuous point-probability trap**; memorylessness; E/V properties (E(aX + b), V(aX + b)); PDF constant/probability; the CLT and standard error |
| L4 Inference | 15 | **CI interpretation true/false sets** (≥ 2 per paper); what changes a CI's width; z vs t choice; setting H0/H1 (one- vs two-tailed); Type I/II and α/β trade-offs; reading a test decision; pooled vs paired comparison; reading or completing an ANOVA table; what an ANOVA rejection does and doesn't say; chi-square facts (expected ≥ 5, no direction, Z² = χ²); unbiased vs efficient |
| L5 Regression | 3 | interpreting slope/intercept (including the extrapolation trap); R² meaning and its limits (causation); k − 1 dummies and the baseline; the assumptions |
| L6 Time series | 5 | identifying a component from a description or plot; additive vs multiplicative choice from a plot; computing a multiplicative or additive value; what a seasonal index below or above 1 means; forecasting-model choice as the slides describe |

### 2.3 Theory vs calculation (per paper)

- **38 theory questions:** interpretation, distinction, misconception-spotting, choosing a method, judging claims. They may *read* given numbers, but must not need arithmetic beyond a one-step comparison.
- **12 calculation questions:** the answer needs real computation. Most should end in an interpretation, e.g. "compute the interval, then which statements about it are TRUE".
- Tag each question `kind: "theory" | "calculation"`.

### 2.4 Lecturer archetypes per paper (from the profile)

| Archetype | Per paper |
|---|---|
| A1 compare / distinguish | ≥ 8 |
| A2 show-that → "which step is wrong / which identity is used" | ≥ 3 |
| A3 check a property from numbers | ≥ 2 |
| A4 model & compute | ≥ 7 |
| A5 trap | ≥ 5, and the two papers together cover **all 10** traps in profile §3 |
| A6 inference procedure | ≥ 6 |
| A7 interpret a result/figure (true/false statement sets) | ≥ 8 |
| A8 judge a claim (classmates' statements) | ≥ 3 |
| A9 regression practice | ≥ 2 |
| A10 set up, don't solve | ≥ 1 |

Tag each question with its archetype and the related past-paper ids from the bank (e.g. `pattern: ["A5", "F2024-Q2d.ii"]`).

### 2.5 Difficulty and order

- **Tiers per paper:** Tier 1 (one idea, < 40 s) **10** · Tier 2 (2–3 steps) **20** · Tier 3 (4+ steps or two concepts interacting, 1.5–3 min) **20**. The two papers must match on tier counts, theory/calculation counts and archetype counts. The average tier per lecture must not differ by more than 0.3 between the papers.
- **Mixed order:** within each paper, never put 3 consecutive questions from the same tier or the same lecture. Every block of 10 questions contains 2 ± 1 Tier-1, 4 ± 1 Tier-2 and 4 ± 1 Tier-3 questions. The question order is fixed (only the options are shuffled at run time).

### 2.6 Required forms (per paper, spread across the 50)

- ≥ **6** questions with a **figure** (STEP 5).
- ≥ **8** negated ("Which is NOT…", "Which statements are FALSE…", "LEAST appropriate").
- ≥ **4** "Student A says X, Student B says Y — who is correct and why?" (best-answer; every option pairs a verdict with a reason).
- ≥ **5** combine two lectures (e.g. CLT + CI width, Bayes + binomial, outlier + regression slope, sampling bias + inference, seasonality + forecasting).
- The two papers share **no scenario, dataset or number set**.

---

## STEP 3 — OPTION DESIGN AND THE QUALITY BAR

### 3.1 Option-design rules (the most important part)

1. **Length parity.** Within a question, the longest option is **≤ 1.25×** the shortest (in characters). Numeric options use the same number of decimal places.
2. **Length tell (per paper).** The longest option is a correct one in **at most 20** questions, and the shortest is a correct one in **at least 18**.
3. **Parallel structure.** All options share grammatical shape and specificity. If one gives a reason, all do.
4. **Every distractor is a diagnosed mistake.** Each wrong option is exactly what a student produces after one nameable error. Examples:
   - λ not rescaled to the interval
   - n instead of n − 1
   - σ instead of σ/√n
   - z instead of t
   - a two-tailed instead of a one-tailed critical value
   - reporting P(B | A) instead of P(A | B)
   - ignoring the base rate
   - treating "mutually exclusive" as "independent"
   - reading a CI as P(μ in interval) = 0.95
   - causation from R²
   - an extrapolated intercept
   - an additive model where the swings grow with the trend

   **Compute every numeric distractor in a script by applying its named mistake.** No invented numbers.
5. **Multi-answer integrity.** Each option is independently true or false. A partially true statement is **false**, and its explanation names the false part.
6. **No free eliminations.** No two options may be ruled out by the same observation, and none may paraphrase another.
7. **Banned:** "All of the above", "None of the above", "Both A and C".
8. **No absolute-word tell.** Spread "always/never/only/must" and hedges across correct and incorrect options.
9. **No keyword matching** between the stem and the correct option.
10. **Runtime shuffle.** Options are shuffled, so explanations reference **option text, never letters**.

### 3.2 AI anti-patterns: reject any question that has one

- **Definitional stems** ("What is a sample space?") when a scenario version exists.
- **A slide sentence lightly reworded** as the correct option.
- **Distractors that are obviously absurd**, off-topic, or produced by no real mistake.
- **Ugly or unrealistic numbers**, or arithmetic that is long without testing understanding.
- A question **answerable without reading its stem or figure**.
- **Two defensible answers**, or an answer that depends on an unstated convention.
- **Trivia** (STEP 1.2).
- **The same idea twice** in one paper (two questions that differ only in numbers).

### 3.3 Calibration examples: the quality bar (do NOT reuse these in either paper)

The student has already seen these and their answers. Match their quality; don't copy their content.

- **Theory · L4 · multi-answer:** given a 95% CI (18.2, 19.8) hours for mean battery life, which are TRUE? Repeated sampling gives about 95% of intervals covering μ ✓ · "95% probability μ lies in this interval" ✗ (the slide's misconception) · a 99% CI from the same sample is wider ✓ · "95% of batteries last 18.2–19.8 h" ✗ (data spread vs the mean) · a larger n gives a narrower interval ✓.
- **Theory · L3 · best-answer:** P(A) = 0.5, P(B) = 0.4, mutually exclusive, so they **cannot be independent**: P(A∩B) = 0 ≠ 0.2. The distractors treat exclusive as independent, use the addition rule as a test, or confuse independence with long-run frequency.
- **Theory · L1 · best-answer:** whole districts that each mirror the population are randomly picked and fully surveyed, which is **cluster sampling** (cost trade-off). The distractors name stratified ("divided into districts"), simple random ("districts chosen randomly") and non-probability ("not every customer can be chosen").
- **Theory · L5 · multi-answer:** Price = 2.1 + 0.18 × Area, R² = 0.81. The slope meaning ✓ and "81% of the variation explained" ✓; the distractors are causation from R², an extrapolated intercept, and an exact prediction for one apartment.
- **Calculation · L3 · best-answer (Bayes):** base rate 2%, sensitivity 90%, false-positive rate 5%: P(fraud | flag) = **0.269**. The distractors are 0.900 (inverted conditional), 0.018 (the joint, not divided) and 0.067 (P(flag)).
- **Calculation · L3 · multi-answer (Poisson, λ = 3/min):** P(0 in 1 min) ≈ 0.050 ✓; the mean in 20 s is 1 ✓; P(2 in 2 min) ≈ 0.045 ✓. The distractors are a variance of √3 (variance vs SD) and "2 × P(1 in 1 min)" (scaling the probability instead of the rate).
- **Calculation · L4 · best-answer (t CI):** n = 16, x̄ = 50, s = 8, t0.025,15 = 2.131 gives **(45.74, 54.26)**. The distractors use s instead of s/√n, z = 1.96, and divide by n.
- **Calculation · L2 · multi-answer:** for 4, 7, 7, 9, 13: mean > median suggests a right skew ✓; s² = 11 ✓; "s² = 8.8" ✗ (n vs n − 1); changing 13 to 30 leaves the median unchanged ✓; "adding 5 raises the SD by 5" ✗.

---

## STEP 4 — CALCULATIONS

- **Every number is produced by a Python script**: answers, distractors (each by applying its named mistake), and figure data. Use `scipy.stats` if it is installed; otherwise use `math` (`erf` for the normal) and **give every t, χ² and F critical value in the stem**, as the lecturer does. Use the stated value in the computation.
- **Non-programmable-calculator-friendly numbers.** State the rounding rule in the stem ("to 3 decimal places") when it matters.
- No question may need a table that isn't printed in the question.

---

## STEP 5 — FORMULAS AND FIGURES

- **Formulas:** use native **MathML** (`<math>`, no library, no CDN) for fractions, roots, sums, integrals, hats and bars. Use plain Unicode (x̄, μ, σ, ≤, ≠, ∩, ∪) inline where it reads clearly. Check that every formula renders in Chromium.
- **Figures are inline SVG generated from the question's data**, so the picture and the numbers always agree:
  - histograms (with bin edges and frequencies)
  - boxplots (whiskers, the median line, outlier dots; the method stated in the stem)
  - scatter plots (≥ 12 points)
  - time-series line charts (labelled periods, with trend/seasonality visible)
  - normal / exponential / PDF curves with a shaded region and labelled bounds.

  Data tables (contingency tables, ANOVA tables, frequency tables) are **HTML tables**, not images.
- **Never put the answer in the figure** (don't label the median if the question asks for it).
- **Clean and legible:**
  - axis labels and ticks, with text ≥ ~12 px at 1280 px window width
  - ≥ 6 px clearance between any label and any line, bar, point or other label
  - **no overlaps**
  - colours from the palette's CSS variables only (theme-aware)
  - each SVG with a `viewBox`, `width: 100%`, a `min-width` of about 560 px and a `max-width` of about 1.1 × its viewBox width.
- **Render check (mandatory):** open the app in a headless browser (Playwright/Chromium if available) at **1280 px**, in **both themes**. Screenshot every figure and formula-heavy question and **look at them**. Run a `getBBox()` script that fails on any text–text, text–line or text–shape intersection. Fix and re-check until clean.

---

## STEP 6 — EXPLANATIONS

Every question has:

1. **Verdict line:** the correct option(s) and the single idea being tested.
2. **Worked reasoning:** 3–8 sentences, or a **step table** (step | formula | value) for calculations.
3. **Per-option notes:** every option gets one line saying why it is true or false. For a wrong option, **name the mistake** that produces it.
4. **Source tag:** lecture file and slide number.
5. **Lecturer pattern:** the archetype id, with "like F2024-Q2d.ii" links to the related past questions, so the student sees what the lecturer has asked before.

---

## STEP 7 — THE APP

Single self-contained file: `PS_mcq_mock/index.html`, containing **both papers**. No CDN, no frameworks, no build step; vanilla JS + CSS that works offline by double-clicking.

### Flow

- **Cover page:** "IE2024 — Probability and Statistics · MCQ Mock Papers", short instructions (calculators allowed; multi-answer negative marking explained; each paper 50 questions / 100 marks), and **two cards: Paper 1 and Paper 2**. Each card shows its status (not started / in progress n of 50 / finished with score) and best score, with buttons **Start**, or **Resume** + **Start fresh** (confirm first). **There is no practice/exam choice and no other setup.**
- **Feedback after each answer:** when a question is submitted, the verdict, the correct option(s), every option marked, and the explanation appear immediately below it.
- **No countdown timer.** Show a small **time-spent clock** per paper, counting only while that paper is open, and record it in the results.

### Layout and features (desktop, ≥ 1024 px; no phone testing needed)

- **Header:** the paper name, "Question n of 50", a running score (marks earned / marks of submitted questions), the time spent, the theme toggle, **Finish paper**, and **Switch paper** (back to the cover; progress is kept).
- **Navigator sidebar:** a 10-column grid (1–50) showing each question's state: unanswered (outline), answered (ink fill), flagged (maroon outline + flag), and correct/partial/wrong (state colour + ✓ ◐ ✗, so colour is never the only signal). It also has a "Show flagged only" toggle and **Reset this paper** (confirm first).
- **Questions:** radio buttons (best-answer) or checkboxes (multi-answer), labelled "Select the BEST answer" or "Select all that apply — negative marking applies". **Submit answer** locks the question. The feedback marks every option: ticked & correct (green ✓), ticked & wrong (red ✗ with its penalty), **not ticked but correct (amber "missed")**, not ticked & wrong (neutral). The verdict banner shows the maths (e.g. "1.33 / 2 — 2 correct ticks +1.33, 1 wrong tick −0.67"). The explanation then opens.
- **Flags:** a toggle on every question (key `F`). Finish warns: "You have N flagged and M unanswered questions — finish anyway?" Unsubmitted questions are marked at finish.
- **Results (per paper):**
  - total /100 and %
  - breakdown by lecture, by tier, theory vs calculation, best-answer vs multi-answer, and by archetype
  - marks lost to negative marking; time spent
  - a **list of missed questions** (wrong *and* partial) with jump-back links
  - **Retry missed only** (resets just those questions and keeps the original attempt in an attempt-history table) and a best-score record.
- **Save progress:** `localStorage`, with **separate versioned keys per paper** (`ps-mcq-v1-paper1` and `ps-mcq-v1-paper2`). Store answers, submitted state, flags, the option-shuffle seed, the time spent, the current question, attempts and best score. Wrap every storage call in `try/catch`.
- **Keyboard:** `1`–`5` toggle options, `Enter` submits, `←`/`→` navigate, `F` flags. All are disabled while typing.

### Palette: the same as the Java / CN papers (exact values, as CSS custom properties)

```
token            LIGHT "Ink & Paper"   DARK "Night Ink"
--bg             #FAF7F0               #1B1814
--card           #FFFDF8               #24201B
--heading        #7A1E2C               #E39AA5
--primary        #2B3A55               #A9BCE0
--border         #E3DCCB               #3A342C
--text           #1F1F1F               #ECE6DA
--code-bg        #F1ECE1               #2B2620
--code-text      #2B2B2B               #E8E1D3
--correct        #2E7D32               #7CC47F
--wrong          #B3261E               #F08A80
--partial        #B7791F               #E3B25A
--on-primary     #FFFFFF               #1B1814
--correct-text   #276E2B               #7CC47F
--partial-text   #8A5A12               #E3B25A
--muted          rgba(31,31,31,.68)    rgba(236,230,218,.68)
--correct-tint   #E6EEE0               #323A2B
--wrong-tint     #F6E3DE               #45312B
--partial-tint   #F6EDDE               #433725
--primary-tint   #E6E6E4               #39393B
```

- Light tokens go on `:root` with `color-scheme: light`. Dark tokens go under `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {…} }` **and** under `:root[data-theme="dark"] {…}`, with `color-scheme: dark`.
- The theme follows the device by default. A ☀/☾ toggle saves the choice in `localStorage` (key `ps-theme`), and an inline `<head>` script applies it before first paint.
- **No hard-coded colours** outside the token blocks (SVG and MathML included).
- Typography: serif stems (`"Iowan Old Style", "Palatino Linotype", Georgia, serif`), sans UI, monospace for numeric tables if helpful.

### Data model and self-test

- Each question is `{ id, paper, num, type: "best"|"multi", marks: 2, lecture, kind, tier, archetype, pattern: [past ids], topic, stem, figure?, table?, options: [{ text, correct, note }], explanation: { verdict, reasoning, source } }`.
- `index.html?selftest=1` checks, **for each paper**: 50 questions and 100 marks; the 30/20 type split; the correct-count distribution 4/9/10/7; the lecture allocation 5/7/15/15/3/5; theory/calculation 38/12; tiers 10/20/20 and the ordering rules; the archetype minimums; length parity and the length-tell counts; every option has a note; the required-form counts. **Across the papers**, it checks the parity rules and that all 10 profile traps are covered. It logs a pass/fail table. **Run it and fix every failure.**

---

## STEP 8 — BEFORE YOU FINISH

Do **not** write an audit or report file. Silently make sure that:

- **Self-test:** `index.html?selftest=1` reports zero failures, and the app loads with no console errors.
- **Numbers:** every answer and numeric distractor was produced by a script, and the stated critical values were used.
- **Anti-patterns:** every question passes STEP 3.2. Scan all stems and options for trivia (years, people's names, organisations), definitional stems, and duplicated ideas within a paper.
- **No overlap with past material:** neither paper reuses a past-paper or calibration scenario or number set, and the two papers share none.
- **Figures and formulas:** the STEP 5 render check passes at 1280 px in both themes, and every MathML formula renders.
- **Theme:** switching works (follows the device; the toggle overrides it and survives a reload; no flash on load).

Fix anything that fails, then reply with a summary of **≤ 10 lines**: the two papers' topic spread, which traps and recycled lecturer ideas each paper uses, and anything you compromised on.

---

## DELIVERABLES

```
PS_mcq_mock/
└── index.html     (both papers: 2 × 50 MCQs embedded, chosen on the cover page)
```

## DO NOT

- Do not ask trivia, definitional one-liners, or anything outside the six lectures.
- Do not make the correct answer the longest or most detailed option by habit.
- Do not reveal how many options are correct in a multi-answer question.
- Do not reuse past-paper or calibration scenarios/numbers, or share any scenario between the two papers.
- Do not invent a distractor value; compute it from a named mistake.
- Do not put the answer inside a figure, or let any figure label overlap.
- Do not add a practice/exam mode choice, a countdown timer, a reference sheet, or report files.
