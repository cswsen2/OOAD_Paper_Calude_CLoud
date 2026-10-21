# PROMPT — SE2012 (OOAD) Final Exam Mock Paper Generator

Copy everything below the line into Claude Code, run from the root of this repo.

---

## ROLE

You are setting a **mock final exam** for **SE2012 — Object Oriented Analysis and Design** (SLIIT, Year 2 Sem 1). The real paper is sat on **NetExam**: no internet, no calculators, no IDE, no external editor. All code is typed straight into a plain answer box. Your job is not to write "quiz questions about Java". You are writing questions that a student who has read the notes but not *understood* them will get wrong. The paper must be **harder than the past papers in this repo**, but stay strictly within the lecture notes.

You produce **one full 100-mark paper**, delivered as an offline exam app, plus a printable A4 reference sheet.

---

## STEP 0 — READ BEFORE WRITING ANYTHING

All files are in the **repo root** (flat, no subfolders). Read in this order:

1. **Lecture notes (the only source of truth for scope and rules)**, all `.md` files in the root:
   - Mid-term material: `OOAD_Module_Overview.md`, `Java_Programming.md`, `Requirements_Engineering.md`, `OOP_Fundamentals.md`, `Function_Overloading_and_Constructors.md`, `OO_Analysis_Noun_Verb.md`, `CRC_Cards.md`, `Use_Case_Diagrams.md`, `UML_Class_Relationships.md`, `Inheritance.md`, `Association.md`, `Aggregation.md`, `Composition.md`, `Dependency.md`
   - Final-only material: `Activity_Diagrams.md`, `Errors_and_Exceptions.md`, `Java_Collections_Framework.md`, `Java_Generics.md`, `Threads.md`, `Design_Patterns.md`, `Singleton_Pattern.md`, `Factory_Pattern.md`, `Command_Pattern.md`
   - `Remebering Stuff OOAD.md` is the student's own memory list (interfaces vs inheritance, `static`, arrays, collections). Its embedded images are not in the repo. Treat it as a list of **known weak spots** that deserve traps, not as a source of rules.
2. **Past papers (style inspiration only, never scope or difficulty)**, all `.pdf` files in the root:
   - `IT2030 -Object Oriented Programming-Version E.pdf`, `IT2030 -Object Oriented Programming-Version F.pdf`, `IT203 0 -Object Oriented Programming.pdf`, `IE2021 -Object Oriented Programming.pdf` have noisy OCR text layers. Read them with `pdftotext -layout`.
   - `IE2021-Object Oriented Programming.pdf` and `IT2030-Object Oriented Programming.pdf` are **scans with no text layer**. Render the pages with `pdftoppm -png -r 80` and read the images.

**Important context about the past papers:** they come from a **different but related module** (IT2030 / IE2021 Object Oriented Programming). They are **easier** and use a **different format**: four lab-style coding questions in Eclipse, keyboard input with `Scanner`, and long "create class X with attributes + `Read()`/`Print()`" busywork. Read them to learn how the setters frame a problem. Then deliberately go beyond them.

- **Borrow**: the scenario-driven framing; the lead line "This question is based on …"; supplying starter code / a partial `main` / an interface to implement; showing a **sample output** the program must reproduce; listing the expected classes as a "package hierarchy"; marks shown per sub-part (`(06 marks)`).
- **Do not borrow**: their difficulty; attribute-plus-getter busywork; `Scanner`-driven input (nothing can be run in NetExam); or **any of their scenarios**. **Banned scenarios**: missile launch / WAR system, vehicle factory (cars/buses), TV/sound-system remote control, `Pair<T, U>`, odd/even printer threads, `ResourceManager` with users acquiring resources, library catalogue, student manager / GPA, username/password validation, warehouse order quantity, employee/manager product numbers, PriorityQueue of book titles, HashMap product inventory. Also do not reuse the worked examples from the lecture notes verbatim (Pizza store, Chocolate Boiler, Home Automation remote, Ceiling Fan, LG/Sony TV, Duck/FlyBehaviour, Beverage). New scenarios only.

If a listed file doesn't exist, search the repo, list what you actually found, and confirm with me before generating.

Do **not** write a style-notes file, an audit file, or any report. Do your analysis in your head and put the effort into the paper.

---

## STEP 1 — SCOPE RULES

- **Section 1 (MCQs)** may draw from **every lecture note** (the exam notice says "all topics discussed in class"), weighted towards final-only material (see STEP 2).
- **Sections 2 and 3** stick to the focus areas the exam notice lists (STEP 3, STEP 4).
- If a rule, keyword, API or notation does not appear in the notes, it **cannot be the correct answer** to anything. It may appear as a distractor, and the explanation must say it is outside the notes.
- **Use the course's own rule sets, not textbook versions.** Examples:
  - Noun/verb analysis uses the course's **five rejection rules**: **Redundant, Meta-language, Event or Operation, Outside scope of system, An attribute**. Do not use the textbook Redundant/Vague/Attribute/Operation/Role set.
  - Singleton thread-safety uses the notes' three options: **synchronize `getInstance()`, eager instantiation, double-checked locking with `volatile`**, plus the **enum Singleton**.
  - Command uses the notes' four roles (**Client, Invoker, Command, Receiver**), `NoCommand` as a null object, undo, and macro commands.
  - Bridge: the notes state it "allows you to vary both the implementation and the abstraction by placing both in separate class hierarchies". The notes place Bridge under **Behavioral**, whereas GoF calls it **structural**. **Never make Bridge's category the deciding fact of a question.**
  - Exceptions use the notes' three kinds (**`Error`, `RuntimeException`, checked `Exception`**) and their handling forms (try-catch, multiple catch, Java SE 7 multi-catch, nested try, `finally`, `throws`, custom exceptions).
  - Threads use the notes' lifecycle states and the notes' exact semantics for `wait()`, `notify()`, `notifyAll()`, `sleep()`, `join()`, `yield()`, synchronized methods and synchronized blocks.
  Check the notes for every such rule set before writing questions on it.
- **Syntax level**: only Java features that appear in the notes. No `var`, records, `switch` expressions, text blocks, streams or `Optional` unless the notes use them. Lambdas only in a Command context, because `Command_Pattern.md` covers them.

---

## STEP 2 — SECTION 1: MCQs (14 questions, 30 marks)

### 2.1 Question types and marks

| Type | Count | Input | Options | Marking |
|---|---|---|---|---|
| **Multi-answer** | 9 | checkboxes | 5 | proportional with negative marking (below) |
| **Best-answer** | 5 | radio | 4 | full marks or 0, no negative marking |

- Marks: **12 questions × 2 marks + 2 questions × 3 marks = 30**. The two 3-mark questions are the two hardest Tier-3 multi-answer questions.
- **Multi-answer negative marking (count hidden):** the stem **never** says how many options are correct ("Select all that apply"). For a question worth *M* with *k* correct options, each correct option ticked earns **+M/k**, and each incorrect option ticked costs **−M/k**. The question score is clamped to the range **0 to M**. Round display to 2 dp.
- **Correct-option counts across the 9 multi-answer questions must vary**: exactly **1 question with 1 correct, 3 with 2, 3 with 3, 2 with 4**. A student must not be able to assume "it's always two".
- Best-answer stems say "Select the BEST answer". At least 2 of the 5 must have more than one *defensible* option, where only one is *best* by the notes' rule, and the explanation must say why the runner-up loses.

### 2.2 Topic allocation (exact)

| # | Topic (notes file) | Count | Shape |
|---|---|---|---|
| 1 | Exceptions (`Errors_and_Exceptions.md`) | 2 | One exact-output trace through try / catch / `finally` / `throws` propagation. One compile-time question: catch-clause order, unreported checked exception, or multi-catch with related types |
| 2 | Threads (`Threads.md`) | 2 | One "which outputs are POSSIBLE" multi-answer over `start()` / `join()` / `synchronized`. One on `wait`/`notify`/`notifyAll`/`sleep` lock semantics or lifecycle state transitions |
| 3 | Collections (`Java_Collections_Framework.md`) | 1 | Trace a program mixing List / Set / Map / Stack / Queue and predict the exact output: duplicates, `TreeSet` ordering, `HashMap` key overwrite, `Stack` pop order, queue order |
| 4 | Generics (`Java_Generics.md`) | 1 | Which statements compile: bounded types, multiple bounds, wildcards, autoboxing, the notes' generics limitations |
| 5 | Design patterns (`Design_Patterns.md`, `Singleton_Pattern.md`, `Factory_Pattern.md`, `Command_Pattern.md`) | 2 | One creational (Singleton thread-safety options, or Factory Method vs Abstract Factory). One from Command / Bridge / Strategy / Template Method: identify the pattern or a participant's role from code or a class diagram |
| 6 | Activity diagrams (`Activity_Diagrams.md`) | 1 | Interpret an SVG activity diagram: fork/join vs decision/merge, swimlanes, which execution trace is valid |
| 7 | UML class relationships (`UML_Class_Relationships.md` + the five relationship files) | 1 | Code ↔ diagram, lifetime ⇒ composition vs aggregation, multiplicity, dependency vs association |
| 8 | Use case diagrams (`Use_Case_Diagrams.md`) | 1 | `<<include>>` vs `<<extend>>`, actor vs system, boundary errors, from a scenario or a supplied diagram |
| 9 | Requirements Engineering (`Requirements_Engineering.md`) | 1 | Applied: FR/NFR classification, defect in a stated requirement, elicitation technique for a situation |
| 10 | OO analysis (`OO_Analysis_Noun_Verb.md`, `CRC_Cards.md`) | 1 | Five rejection rules applied to a scenario, or responsibility/collaborator placement on CRC cards |
| 11 | Java and OOP core (`Java_Programming.md`, `OOP_Fundamentals.md`, `Function_Overloading_and_Constructors.md`) | 1 | Overload resolution, constructor chaining, `static` vs instance, pass-by-value of references, interface vs abstract class |

That gives 9 final-only questions (rows 1–6) and 5 mid-term questions (rows 7–11).

### 2.3 Required forms (spread across the 14, not extra questions)

- ≥ **6** contain a Java code block.
- ≥ **3** contain a diagram (activity diagram, use case or class diagram, pattern structure).
- ≥ **3** are negated (`NOT`, `would FAIL to compile`, `LEAST appropriate`, `IMPOSSIBLE`).
- ≥ **1** "Student A says X, Student B says Y — who is correct and why?" (as best-answer, all four options pairing a verdict with a reason).
- ≥ **2** combine two topics: e.g. Singleton + `synchronized`; a generic class stored in a collection; an exception thrown inside `run()`; a Command invoker holding a `Stack<Command>` for undo; a class diagram whose relationship must be read off constructor code.

### 2.4 Option-design rules (the most important part of Section 1)

Earlier attempts failed because the correct answer was always the longest, most detailed option and the distractors were throwaways. That is a fatal defect.

1. **Length parity.** Within a question, the longest option is **≤ 1.25×** the character length of the shortest.
2. **Length tell.** Across the 14 questions, the longest option is a correct option in **at most 6**, and the shortest option is a correct option in **at least 5**.
3. **Parallel structure.** All options share grammatical shape and specificity. If one cites a line number, all do. If one gives a reason, all do.
4. **Every distractor is a diagnosed mistake.** Each wrong option is exactly what a student produces after one specific, nameable error. Examples: thinks `finally` is skipped when `catch` returns; uses `if` instead of `while` around `wait()`; believes `sleep()` releases the lock; expects `TreeSet` to keep insertion order; thinks `List<Object>` accepts a `List<String>`; puts the `instance` field non-`static`; confuses Invoker with Receiver; uses `<<extend>>` for mandatory behaviour; rejects a noun as an Attribute when the course's rule makes it Meta-language. If you can't name the error, rewrite the option.
5. **Multi-answer integrity.** Each option is independently true or false. No option's truth may depend on another option. A "partially true" statement counts as **false**, and its explanation names the false part.
6. **No free eliminations.** No two options may be ruled out by the same single observation, and no option may paraphrase another.
7. **Banned**: "All of the above", "None of the above", "Both A and C".
8. **No absolute-word tell.** Spread "always/never/must/only" and hedges ("can/may/typically") across both correct and incorrect options.
9. **No keyword matching.** A question must not be answerable by matching a distinctive stem word to the same word in an option.
10. **Runtime shuffle.** The app shuffles options. Explanations reference **option text, never letters**.

### 2.5 Difficulty for Section 1

| Tier | Definition | Count |
|---|---|---|
| 1 — Recall | One fact, < 30 s | 2 |
| 2 — Applied | 2–3 reasoning steps or a short trace | 5 |
| 3 — Hard | 4+ steps, two concepts interacting, needs scratch working, 2–4 min | 7 |

Twist deliberately: add a line that looks decisive but isn't; a `finally` that overwrites a return value; a `catch (Exception e)` placed before `catch (IOException e)`; a thread started with `run()` instead of `start()`; a Singleton whose constructor is accidentally `public`; a generic method whose bound is *almost* satisfied; a diagram with one correct relationship and one wrong multiplicity. Never ask the plain definitional form of a concept when an applied form is available.

---

## STEP 3 — SECTION 2: Structured / Short Answer (4 questions, 30 marks)

Based on the style of the **worksheets and in-class activities** in the notes, e.g. the activities in `OOP_Fundamentals.md`, the worked examples in `OO_Analysis_Noun_Verb.md` / `CRC_Cards.md`, and the case studies in `Java_Collections_Framework.md`. Use **new scenarios**. **No diagram-drawing questions**: diagrams are supplied to *interpret*, never to draw. Each question has a scenario and 2–4 lettered sub-parts with marks shown, like the past papers.

| Q | Focus area (from the exam notice) | Marks | Must include |
|---|---|---|---|
| 2.1 | Identifying classes, objects, fields | 7 | A 120–180-word scenario. (a) List the candidate classes after applying the course's five rejection rules, naming the rule for each rejected noun. (b) Give fields with types and visibility for one class. (c) Separate objects from classes in the scenario, or give one CRC card's responsibilities and collaborators. |
| 2.2 | OOP concepts and class relationships | 8 | An **SVG class diagram to interpret**. Identify relationship types with a lifetime/ownership justification. Write a Java skeleton that correctly implements one composition (the whole creates the part) and one aggregation (the part is passed in). Apply one OOP concept: encapsulation, polymorphism, or abstract class vs interface. |
| 2.3 | Exception handling and threads | 7 | Given code (15–30 lines). (a) Trace the output, or classify exceptions as checked/unchecked and fix a compile error. (b) Identify a race condition or missed notification and explain it using thread states. (c) Write the corrected `synchronized` / `wait`–`notifyAll` fragment. |
| 2.4 | Collections and generics | 8 | A scenario. (a) Choose a collection and justify it by ordering, duplicates or key lookup. (b) **Write a generic class with a bounded type parameter** for the scenario (≤ 25 lines). (c) Say whether three given usages of that class compile, and why (bounds/wildcards). |

Each question's final sub-part is Tier 3: justify, fix or predict, never just recall.

---

## STEP 4 — SECTION 3: Coding Questions (2 problems, 40 marks)

The notice says students "will be provided with a basic code structure to follow". So every problem supplies **starter code**: interfaces, partial classes with `// TODO`, and a partial `main`. It also supplies a **sample output** the finished program must reproduce exactly, and a **class list** in the past papers' "package hierarchy" style. Sub-parts carry marks (`(04 marks)`), and each sub-part gets its **own answer box**.

| P | Focus | Marks |
|---|---|---|
| 3.1 | **Threads** (synchronization, `wait`/`notify`/`notifyAll`) **+ exception handling** (a custom checked exception thrown and handled correctly, plus correct `InterruptedException` handling), using at least one collection | 20 |
| 3.2 | **Design patterns**: exactly two of Abstract Factory / Command / Singleton / Bridge, **plus collections/generics** (e.g. an invoker keeping a `Stack<Command>` history for undo, or a generic registry with a bounded type) | 20 |

Rules:

- **3.2 pattern pair**: at least one of the two must be **Bridge or Abstract Factory**. The pair must **not** be Command + Singleton or Abstract Factory + Singleton, because the past papers already used both. Any of the four patterns not used in Section 3 must be tested in Section 1 or 2.
- **At least one Section 3 problem requires the student to write a generic class or generic method.**
- **Deterministic output.** Thread problem 3.1 must be designed so the correct solution prints **identical output every run** (strict turn-taking through `wait`/`notifyAll`, or `join`-based ordering). Never mark on an interleaving the student can't control.
- **Harder than the past papers.** Each problem has at least one sub-part needing a non-obvious decision, for example: `while` not `if` around `wait()`; `notifyAll` vs `notify` with more than two threads; which object to lock on; where the Singleton's lock goes; which participant holds the Bridge reference; making undo work after a macro command. The starter code should also contain **one planted defect** the student must spot and fix as a marked sub-part, e.g. `t.run()` instead of `t.start()`, a `public` Singleton constructor, or a catch block that swallows `InterruptedException` and loops forever.
- **Hand-writable in time.** No IDE means the student writes at most **~90 lines per problem** beyond the starter code. Budget: MCQs ~45 min, Section 2 ~50 min, Section 3 ~85 min, within the **3-hour** limit.
- Every model solution must be complete, compilable Java whose output matches the sample output **byte-for-byte**.

---

## STEP 5 — JAVA CODE STANDARDS

- Real, compilable Java in the style and syntax level of the notes. 4-space indent, K&R braces, meaningful names, ≤ 80 characters per line.
- MCQ snippets are 8–30 lines, with `class` + `main` whenever output is asked for. Number the lines (`1  public class …`) whenever the question refers to one.
- **Verification is mandatory.** If a JDK is available, write every snippet and every model solution to a temp directory, `javac` + `java` it, and confirm each stated output byte-for-byte, including spaces and newlines. Run each threaded program **at least 20 times** and confirm identical output. For "which outputs are POSSIBLE" questions, justify every possible option with an explicit interleaving and every impossible one with the ordering guarantee (`join`, `synchronized`, `wait`/`notify`) that rules it out. Clean up temp files afterwards. If there is no JDK, hand-trace every snippet twice independently.
- In the HTML, escape `<`, `>` and `&`, and render code in `<pre><code>` so whitespace survives.

---

## STEP 6 — DIAGRAMS

- **Inline SVG** only (`viewBox`, no fixed width, scales on mobile). No external images or base64.
- Use the notation exactly as the notes present it:
  - **Class diagrams**: three-compartment boxes, `+ - #` visibility, `name : type`, method signatures, hollow triangle (inheritance), dashed line with hollow triangle (interface realisation, if the notes use it), filled diamond (composition), hollow diamond (aggregation), plain line (association), dashed open arrow (dependency), multiplicities at both ends.
  - **Use case diagrams**: system boundary with name, stick-figure actors outside, ellipses inside, dashed `<<include>>` / `<<extend>>` arrows in the correct direction.
  - **Activity diagrams**: filled-circle initial node, bullseye final node, rounded action nodes, diamond decision/merge with guards, thick bar fork/join, swimlanes, exactly as in `Activity_Diagrams.md`.
- A diagram must carry information needed for the answer, never decoration. It must stay legible at ~360 px wide, with arrowheads and diamonds clearly distinguishable.
- Diagram strokes and text use the palette's text/ink colours (STEP 9) on the card background.

---

## STEP 7 — EXPLANATIONS AND MARKING DATA

**Section 1, for every question:**
1. **Verdict line**: the correct option(s) and the single idea being tested.
2. **Reasoning**: 3–8 sentences, or a **trace table** (step | statement | state | output so far) for code questions.
3. **Per-option note**: every option (correct and incorrect) gets one line saying why it is true or false. For wrong options, name the mistake that leads a student to pick it.
4. **Source tag**: lecture file + section heading.
5. Anything not in the notes is marked `[beyond notes]` with a justification, but preferably avoid it.

**Sections 2 and 3, for every sub-part:**
1. **Model answer** (prose or code).
2. **Rubric**: a list of marking points, each worth 0.5–2 marks, summing to the sub-part's marks.
3. **Keyword auto-check spec** for each rubric point (see STEP 8).
4. **Common mistakes**: 2–4 bullets, each naming the rubric point it loses.
5. **Source tag**.

---

## STEP 8 — KEYWORD AUTO-CHECK (Sections 2 and 3)

When the student submits a written answer, the app **pre-ticks rubric points automatically** using keyword/regex checks. **The student can override any tick.**

- Each rubric point is `{ text, marks, auto, check }`, where `check = { all: [regex…], any: [regex…], none: [regex…], ci: true|false }`. A point passes when every `all` pattern matches, at least one `any` pattern matches (if `any` is given), and no `none` pattern matches.
- **Preprocessing before checking**: for code answers, strip `//` and `/* */` comments so that keywords in comments don't count, and collapse runs of whitespace to a single space. Prose checks are case-insensitive (`ci: true`). Code checks are case-sensitive.
- **Write tolerant patterns.** Allow flexible whitespace (`\s*`) and modifier order (`(public\s+)?(static\s+)?synchronized`). Use `\w+` where the student picks the name, and exact names only where the question fixes them. Structural checks should be specific enough to mean something, e.g. `wait()` *inside a `while`*: `while\s*\([^)]*\)\s*\{?[^}]*?\bwait\s*\(`.
- Points that can't sensibly be keyword-checked (e.g. a justification's quality) are `auto: false`. They start unticked and show a hint: "Tick if your answer says the part cannot exist without the whole".
- Show auto-ticked points with an **"auto"** badge and overridden ones with an **"edited"** badge.
- **Verdict**: full marks = **Correct**, 0 = **Wrong**, anything else = **Partial**.
- **Built-in self-test**: for each sub-part, the data includes the model answer plus 1–2 **plausible wrong answers** (each embodying a listed common mistake). Opening `index.html?selftest=1` runs every check and logs a pass/fail table to the console. A pass requires the model answer to score full marks on all `auto` points, each wrong answer to score **less** than full, and an empty answer to score 0. **Run it and fix every failure before finishing.**

---

## STEP 9 — THE APP

Single self-contained file: `OOAD_final_mock/index.html`. No CDN, no frameworks, no build step. Vanilla JS + CSS, and it must work offline by double-clicking.

### Palette — "Ink & Paper" (use exactly these as CSS custom properties)

```
--bg:        #FAF7F0   page background (cream paper)
--card:      #FFFDF8   question cards, panels
--heading:   #7A1E2C   headings, section titles (maroon)
--primary:   #2B3A55   buttons, links, selected state (ink blue)
--border:    #E3DCCB   borders, dividers
--text:      #1F1F1F   body text
--code-bg:   #F1ECE1   code blocks and answer boxes
--code-text: #2B2B2B
--correct:   #2E7D32
--wrong:     #B3261E
--partial:   #B7791F   partial credit, missed options
```

Derive tints only from these (e.g. a 10–12 % tint of `--correct` behind a correct option). Text drawn in a state colour must reach **4.5:1** contrast on its background, so darken the shade (same hue) where needed, e.g. for `--partial`. Light theme only. Typography: question stems in a **serif** stack (`"Iowan Old Style", "Palatino Linotype", Georgia, serif`) for the printed-paper feel. UI chrome in the system sans stack. Code in `ui-monospace, Consolas, "Courier New", monospace`.

### Data model

Question data lives in a JS array at the top of the file:

- Section 1: `{ id, section: 1, type: "best"|"multi", marks, topic, notesFile, tier, stem, code?, svg?, options: [{ text, correct, note }], explanation: { verdict, reasoning, source } }`
- Sections 2–3: `{ id, section, marks, topic, notesFile, stem, svg?, starterCode?, sampleOutput?, classList?, parts: [{ label, marks, prompt, modelAnswer, rubric: [{ text, marks, auto, check }], commonMistakes: [], wrongAnswers: [], source }] }`

### Screens and behaviour

- **Cover screen**: styled like an exam cover ("SE2012 — Object Oriented Analysis and Design · Final Examination (Mock) · Duration: 3 Hours · Total: 100 marks"). Instructions mirror the real notice: no internet/calculators/IDEs, one A4 double-sided reference sheet allowed, sections and marks. **Mode choice**:
  - **Practice mode (default)**: **feedback immediately after each answer is submitted** (below).
  - **Exam mode**: no feedback at all until "Finish exam", for a realistic run.
  - The mode is locked for the attempt. Also offer **Resume saved attempt** / **Start fresh**.
- **Layout**: NetExam-like. A header shows the section, "Question n of 20", the countdown timer and marks. A **question navigator grid** (1–20, grouped by section) shows each question's state: unanswered (outline), answered (ink-blue fill), **flagged** (maroon flag icon + maroon outline), and in practice mode after submission correct / partial / wrong (state colour + ✓ / ◐ / ✗ icon, so colour is never the only signal). Previous / Next buttons.
- **Section 1 answering**: radio buttons for best-answer, checkboxes for multi-answer, labelled "Select the BEST answer" or "Select all that apply — negative marking applies". A **Submit answer** button locks the question.
  - **Practice-mode feedback (immediately below the question)**: a verdict banner (**Correct / Partial / Wrong** with the score, e.g. "1.33 / 2 — 2 correct ticks +2.00, 1 wrong tick −0.67"). Every option is marked: ticked & correct (green ✓), ticked & wrong (red ✗ with its penalty), **not ticked but correct (amber "missed")**, not ticked & wrong (neutral). Then the explanation panel opens automatically with verdict, reasoning/trace table, per-option notes and source.
- **Sections 2–3 answering**: starter code / sample output / class list shown read-only above the answer boxes, each with a **Copy** button and an **"Insert starter code"** button for the answer box. Answer boxes are plain monospace `<textarea>`s, **no syntax highlighting**, `spellcheck="false"`, autocorrect and autocapitalise off. Tab inserts 4 spaces, Shift+Tab outdents. Line and character count shown. **Submit answer** locks the sub-part and runs the keyword auto-check.
  - **Practice-mode feedback (immediately below the answer)**: verdict banner (Correct / Partial / Wrong + marks), the rubric with auto-ticks and override checkboxes (the total updates live), the model answer in `<pre><code>`, common mistakes, and source.
- **Flag for review**: a flag toggle on every question (keyboard `F`). Flags are visible in the navigator, filterable ("Show flagged only"), and persisted. **Finish exam** warns: "You have N flagged and M unanswered questions — finish anyway?"
- **Timer**: a **3-hour countdown** that survives refresh (store the start timestamp, not a ticking counter). A warning banner appears at **15 minutes** and **5 minutes** left. At 0, show "Time's up" but **let the student keep going**: the timer switches to a red overtime count-up, and the overtime is recorded in the results.
- **Exam mode at finish**: run all marking, then reveal every question's feedback exactly as practice mode would. The student can still override rubric ticks, and the results update live.
- **Results screen**: total /100 and %, per-section scores (/30, /30, /40), per-topic breakdown, best-answer vs multi-answer accuracy, total marks lost to negative marking, time used and overtime. Then a **list of missed questions** (wrong *and* partial) with jump-back links, a **"Retry missed only"** button (resets just those questions in practice mode and keeps the original attempt's score on record), and a best-score record.
- **Save progress**: `localStorage` with a versioned key stores answers, submitted state, rubric overrides, flags, mode, option-shuffle seed (so option order survives refresh), timer start, current question, and best score. A **Reset attempt** button asks for confirmation. Wrap every storage call in `try/catch` so the app still works with storage blocked.
- **Keyboard**: `1`–`5` toggle options, `Enter` submits, `←`/`→` navigate, `F` flags. All are disabled while typing in a textarea.
- **Mobile-first**: works at 360 px, tap targets ≥ 44 px, visible focus rings, code blocks and wide SVGs scroll horizontally instead of overflowing, generous line height.

---

## STEP 10 — A4 REFERENCE SHEET

The exam allows **one A4 double-sided reference sheet**. Produce `OOAD_final_mock/reference-sheet.html`, a printable sheet that fits **exactly two A4 pages** (`@page { size: A4; margin: 10mm; }`), built **only from the lecture notes**, with no rules the notes don't contain.

- Dense multi-column layout, minimum font size 7.5 pt, clear section headings in `--heading` maroon. When printed: white background, near-black text, readable in greyscale.
- Prioritise what is **hard to memorise and likely to be tested**: the exception hierarchy and checked/unchecked list; try/catch/`finally`/multi-catch rules; thread lifecycle states and what each method does to the lock (`wait`/`notify`/`notifyAll`/`sleep`/`join`/`yield`); synchronized method vs block; a `wait()`-in-`while` template; the collections hierarchy with a "which class for which need" table (ordering, duplicates, nulls, key lookup) and key methods; generics syntax (class, method, bounded, multiple bounds, wildcards, limitations); compact skeletons of Singleton (all variants from the notes), Abstract Factory, Command (roles, `NoCommand`, undo, macro) and Bridge; the UML relationship notation table; `<<include>>` vs `<<extend>>`; activity-diagram symbols; FR vs NFR; the five noun rejection rules; the CRC card layout.
- It must be a **general** sheet. It must not contain answers to this mock's specific questions.
- If a headless browser is available (e.g. Chromium/Playwright), print it to PDF and confirm it is exactly 2 pages. Fix overflow by tightening content, not by shrinking fonts below 7.5 pt.

---

## STEP 11 — BEFORE YOU FINISH

Do **not** write an audit or report file. Silently make sure that:

- Marks total exactly 100 (30 / 30 / 40), and the STEP 2 counts, tiers, correct-count distribution and required forms are all met.
- Every option-design rule in 2.4 holds: check length parity and the length-tell counts by actually measuring.
- Every Java snippet and model solution compiles and produces exactly the stated output (threads: 20 identical runs).
- `index.html?selftest=1` reports zero failures.
- `index.html` loads with no console errors (use a headless browser if available), and every SVG renders.
- The reference sheet is exactly 2 A4 pages.

Fix anything that fails. Then reply with a summary of **≤ 10 lines**: what was generated, the Section 3 scenarios and pattern pair, and anything you had to compromise on.

---

## DELIVERABLES

```
OOAD_final_mock/
├── index.html            (the exam app — all 20 questions embedded)
└── reference-sheet.html  (printable double-sided A4 reference sheet)
```

## DO NOT

- Do not make the correct answer the longest or most detailed option by habit.
- Do not reveal how many options are correct in a multi-answer question.
- Do not reuse any past-paper scenario or a lecture worked example verbatim.
- Do not ask the student to draw a diagram.
- Do not set Section 3 problems that are just "create classes with attributes, getters and a print method".
- Do not mark threaded output that depends on scheduling.
- Do not use generic textbook rule sets where the notes give the course's own.
- Do not use pseudo-Java, unformatted code, or Java features absent from the notes.
- Do not state an output you have not compiled and run (or hand-traced twice).
- Do not produce style-notes, audit or report files.
