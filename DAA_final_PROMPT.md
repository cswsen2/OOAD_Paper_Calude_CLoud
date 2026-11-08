# PROMPT — SE2022 (Design and Analysis of Algorithms) Two Final Mock Papers

Copy everything below the line into Claude Code, run from the root of this repo.

---

## ROLE

You are setting **two mock final papers** (Paper 1 and Paper 2) for **SE2022 — Design and Analysis of Algorithms** (SLIIT, Year 2 Sem 2), in the **announced final format**. You are imitating **this module's lecturer**, whose thinking is captured in `DAA_lecturer_model/`.

You are not writing "algorithm quiz questions". You are writing a paper that a student who has memorised the slides but cannot **execute and reason about** the algorithms will fail.

- **Application first.** At least 80% of each question's marks need the student to *run* a method on given data, *derive* something (a relation, a recurrence, a bound), or *decide* something from their own working. Pure recall is at most 2 marks per question, and even then it is applied once.
- **Quality over volume.** A long question is not a hard question. Hardness comes from choosing data that makes the algorithm's interesting branch fire, and from follow-ups that use the student's own table or tree. It never comes from big inputs.
- **Both papers are equally hard.** Inside every question the sub-parts climb **from easy to hard**. The two papers share **no dataset**.
- The student **writes answers on paper**. The app shows the paper, then reveals a worked model answer and a marking rubric for each sub-part, and the student **self-marks** by ticking rubric points.

You produce **one offline app** containing both papers.

---

## STEP 0 — READ BEFORE WRITING ANYTHING

All files are in the **repo root** unless a folder is given. Quote the names, because several contain spaces and parentheses.

1. **The lecturer model (read first):**
   - `DAA_lecturer_model/LECTURER_PROFILE.md`, which covers:
     - the announced format
     - how a paper is built (the "illustrate the operations…" trace, the ladder of sub-parts, recycling)
     - archetypes D1–D11 and the favourite traps, including the extrapolated traps for L06/L07
     - phrasing and notation, and the **lecture's own worked-example layouts (§4.3)**, which your model answers must copy
     - the **paper and slide flaws you must not copy (§5)**
     - the strong vs weak form of each archetype, and the AI anti-patterns (§6)
   - `DAA_lecturer_model/question_bank.json`: all 46 past sub-questions as tagged records (`lecture`, `final_q`, `topic`, `skill`, `archetype`, `trap`, `repeats`, verified `answer`). For every sub-part you write, look up the past records with the same `final_q`/topic/archetype, so the new sub-part tests the same *idea* the lecturer values, from a **new angle with new data**.
   - `DAA_lecturer_model/algos.py`: lecture pseudo-code re-implemented with 1-based arrays, each implementation checked against the lecture's worked example:
     - Q1 algorithms: insertion sort, Lomuto quicksort, merge sort (MERGE algorithm 2), HEAPIFY/BUILD_HEAP/HEAPSORT, the max-heap check, the RAM step count
     - Q2: the knapsack P(i, k) table, matrix-chain order
     - Q3: the naive matcher, Rabin-Karp, the string-matching automaton
     - Q4: Huffman, Shannon-Fano, Hu-Tucker, lecture-style Ziv-Lempel, Kruskal, Prim, Dijkstra

     **Import it for every number you compute** (STEP 4).

2. **Lecture slides (the only source of truth for scope, algorithm versions and conventions).** They are PowerPoint files. Convert them in a scratch folder (`soffice --headless --convert-to pdf --outdir <scratch> <file>`), then render the pages (`pdftoppm -png -r 60`). The text layers lose pseudo-code layout, formulas and every figure, so **look at** each slide that contains pseudo-code, a table, a tree, a graph or a worked example.

   | # | File | Pages | Final Q |
   |---|---|---|---|
   | L01 | `Lecture01.ppt`: algorithms, properties, pseudocode conventions, analysis, worst/best/average, RAM-model step count | 28 | Q1 |
   | L02 | `Lecture02.pptx`: insertion sort exact analysis, T(n), O/Ω/Θ and the ratio theorems | 39 | Q1 |
   | L03 | `Lecture03.ppt`: recursion, recursive relations and initial conditions, recurrence equations, repeated substitution, substitution method, recursion tree, master theorem | 39 | Q1 |
   | L04 | `Lecture04.ppt`: divide and conquer, quicksort (Partition Algorithm 02 = Lomuto) and its analysis, merge sort (MERGE algorithm 2) and its analysis | 32 | Q1 |
   | L05 | `Lecture05.ppt`: tree terminology, full/complete binary trees, heaps, HEAPIFY, BUILD_HEAP, HEAPSORT, priority queues | 48 | Q1 |
   | L06 | `Lecture06 (1).ppt`: naive matcher, Rabin-Karp, finite automata, the string-matching automaton | 28 | Q3 |
   | L07 | `Lecture07 (5).ppt`: greedy method, greedy ≠ optimal, spanning trees, disjoint sets, Kruskal, Prim, Dijkstra | 45 | Q4 |
   | L08 | `Lecture08.ppt`: lossless/lossy, fixed/variable-length codes, entropy, Shannon-Fano, Huffman, Hu-Tucker, Ziv-Lempel, gzip | 46 | Q4 |
   | L09 | `Lecture09.ppt`: DP elements, 0/1 knapsack (the P(i, k) recursion, the recursion tree, the DP table), matrix-chain multiplication (m, s, PRINT-OPTIMAL-PARENS) | 49 | Q2 |

3. **Past material (style only; already summarised in the model):**
   - `DAA Model Paper Test 01 (1).pdf`
   - `Final Exam Paper Model Paper (1).pdf`: render it with `pdftoppm -png -r 80`, because its figures are images
   - `DaaExact.jpeg`: the lecturer's whiteboard hint for the exam

   **Never reuse their data**, nor the lecture's worked-example data:

   | Source | Data you must not reuse |
   |---|---|
   | Sorting and heaps | [10, 0, 8, 4]; [28, 15, 1, 30, 0, 8]; [45, 25, 15, 85, 75, 65, 35, 55]; ⟨23, 17, 14, 6, 13, 10, 1, 5, 7, 12⟩ |
   | Recursion | pow(x, n) |
   | Compression | the digit frequencies 121/50/203/401/8/195; ABRACADABRA; "EXAMPLE OF SHANNON FANO"; the a45…f5 Huffman example; the Hu-Tucker a1 b6 c8 d1 e6 f2 |
   | Knapsack | (w = [3, 4, 6, 3], p = [6, 12, 8, 2]); (W = [4, 3, 5, 2], P = [10, 8, 9, 16]); the lecture's w = [2, 2, 6, 5, 4] |
   | Matrix chain | 2×5, 5×3, 3×10, 10×4; p = 2, 3, 4, 5, 10; the lecture's 30×35 … 20×25 chain |
   | String matching | the lecture's Rabin-Karp text 2359023141526739921 with 31415 mod 13; the ababaca automaton |
   | Greedy graphs | the lecture's Kruskal/Prim graph (A–F); the lecture's Dijkstra graph; the greedy A→E path example |

   Reuse their **ideas and shapes**.

4. **App shell:** if `OOAD_final_mock/index.html`, `CN_final_mock/index.html` or `PS_mcq_mock/index.html` exists, study it. Reuse its architecture and code where it fits: the cover with paper cards, navigator, flags, saved progress, the light/dark theme, results and self-test. The answering model here is different (self-marking, STEP 7). Do not reuse its questions.

If a listed file doesn't exist, search the repo, list what you actually found, and confirm with me before generating.

Do **not** write style-notes, audit or report files. Put the effort into the papers.

---

## STEP 1 — SCOPE AND QUALITY RULES

### 1.1 Lecture-only, with the lecture's exact algorithm versions

If a rule, algorithm version or formula is not in the slides, it **cannot be part of a model answer**. Every algorithm a question names is **printed in the paper** (STEP 2.8), copied from the slide with its line numbers. Use these versions:

- **L01:**
  - the lecture's properties of an algorithm (correct, unambiguous, correct for all cases, simple, terminates)
  - the slide-23 RAM convention: 1 step per assignment, comparison, addition and memory access; `for i ← 0 to n` costs (n + 2) assignments, (n + 2) comparisons and (n + 1) additions. **Print the convention in any step-count question.**
- **L02:** INSERTION-SORT; T(n) with tⱼ; O/Ω/Θ and the ratio theorems.
- **L03:**
  - recursive relation + initial condition(s)
  - recurrence equations, solved by **repeated substitution**, **substitution**, **recursion tree** and the **master theorem** (the three cases as the slide states them, including case 3's regularity condition)
- **L04:**
  - QUICKSORT + **Partition Algorithm 02 (x ← A[r], Lomuto)** only
  - MERGESORT + **MERGE algorithm 2** (sentinels ∞)
  - best/worst partitioning and their recurrences
- **L05:**
  - the lecture's **full binary tree** has exactly 2^(h+1) − 1 nodes; the height of a complete tree is ⌊log₂ n⌋
  - PARENT(i) = ⌊i/2⌋, LEFT = 2i, RIGHT = 2i + 1
  - HEAPIFY / BUILD_HEAP (i from ⌊n/2⌋ down to 1) / HEAPSORT; max-priority queue (INSERT, MAXIMUM, EXTRACT-MAX)
- **L06:**
  - shift s is valid iff 0 ≤ s ≤ n − m and T[s+1..s+m] = P[1..m]
  - NAIVE-STRING-MATCHER
  - Rabin-Karp with radix d = 10 over decimal digits and a stated modulus q, the rolling formula `t(s+1) = (d(t(s) − T[s+1]·h) + T[s+m+1]) mod q` with h = d^(m−1) mod q, valid match vs spurious hit
  - finite automaton (Q, q₀, A, Σ, δ); the string-matching automaton for a pattern (δ table, state diagram, state sequence φ(Tᵢ))
- **L07:**
  - greedy choice; why greedy can fail (the lecture's path example idea)
  - spanning tree (n − 1 edges); MCST
  - MAKE-SET / FIND-SET / UNION
  - MST-KRUSKAL, MST-PRIM (key, π)
  - DIJKSTRA with INITIALIZE-SINGLE-SOURCE and RELAX, non-negative weights
- **L08:**
  - lossless vs lossy
  - fixed-length codes (⌈log₂ n⌉ bits)
  - variable-length and prefix-free codes
  - entropy H = −Σ pᵢ log₂ pᵢ
  - Shannon-Fano: sort by falling frequency, split into two groups with sums as equal as possible, 0 to the first group
  - HUFFMAN(C): the first EXTRACT-MIN is the left child and gets 0
  - Hu-Tucker (alphabetic; join only nodes not separated by a leaf; the leftmost pair on ties; read the levels, then assign alphabetic codes)
  - Ziv-Lempel as on the slides: (distance back, copy length) or (0, ASCII)
  - gzip: two Huffman codes, one for distances and one for lengths
- **L09:**
  - optimal substructure and overlapping subproblems
  - the **P(i, k) recursion on items i…n** (print it); KNAPSACK-RECURSE and its recursion tree; the DP table with rows i = n … 1 and columns k = 0 … c
  - MATRIX_CHAIN_ORDER (m, s); PRINT-OPTIMAL-PARENS

### 1.2 Don't copy the lecturer's flaws (profile §5): hard rules

- **Never use or print:**
  - the lecture's 1-D knapsack loop (it increases k, which makes it the unbounded knapsack)
  - Partition Algorithm 01 with QUICKSORT(A, p, q − 1)
- **Never make a slide error a model answer:**
  - the naive matcher's "best case O((n − m + 1)m) comparisons"
  - "Rabin-Karp's worst case is when all hits are spurious"; the worst case is that **every** window hits
- **Every trace question states every convention it depends on:**
  - 1-based indices
  - adjacency/neighbour order for graph algorithms
  - the tie-break rule (choose data with **no ties** wherever you can; where a tie is unavoidable, state the rule in the stem)
  - Huffman: left = 0 = first EXTRACT-MIN
  - how naive comparisons are counted (left to right, stopping at the first mismatch)
- **Exactly one correct final answer per sub-part:**
  - knapsack instances have a **unique optimal subset**
  - MCM instances have a **unique minimising k** in every cell
  - Huffman data have **no frequency ties at any merge**
  - Shannon-Fano data have **a unique best split at every step**
  - Kruskal/Prim graphs have **distinct weights**
  - Dijkstra never has two unmarked vertices with the same smallest d
- **Clean presentation:** clean numbering (Question 1–4, parts (a), (b), …), marks printed on every part, and parts that add up to exactly 15.

### 1.3 No trivia (hard rule)

Never test, as the point of a sub-part:

- inventors or people's names (Rabin, Karp, Shannon, Fano, Huffman, Dijkstra as answers)
- years, universities or history
- "list N types" with no reasoning.

The slides contain several of these; ignore them.

### 1.4 Size limits (volume ≠ quality)

| Item | Limit |
|---|---|
| Sorting arrays | 5–7 elements (heapsort ≤ 7) |
| Knapsack | 4 items, c ≤ 10 |
| Matrix chain | 4 matrices |
| Naive / Rabin-Karp text | ≤ 16 characters (Rabin-Karp: pattern of 3–4 decimal digits, q = 11 or 13) |
| Automaton | pattern ≤ 5 characters over Σ of 2–3 letters; text ≤ 12 characters |
| Huffman / Shannon-Fano / Hu-Tucker | 5–6 symbols with integer frequencies |
| Ziv-Lempel | message ≤ 14 characters |
| Graphs | 5–6 vertices, 7–9 edges |

A prepared student should be able to write each question in **about 25–30 minutes** (2 hours for 4 questions). Estimate the minutes for every sub-part and tag it.

---

## STEP 2 — PAPER STRUCTURE (identical blueprint for Paper 1 and Paper 2)

### 2.1 Format

| Q | Marks | Title (print exactly) | Lectures |
|---|---|---|---|
| 1 | 15 | Recursion and Algorithm Design | L01–L05 |
| 2 | 15 | Dynamic Programming | L09 |
| 3 | 15 | String Matching Algorithms | L06 |
| 4 | 15 | Data Compression Algorithms and Greedy Algorithms | L08 (8 ± 1 marks) + L07 (7 ± 1 marks) |

Each paper: 2 hours, 60 marks, answer all questions. Each question opens with a one- or two-sentence context and then has **4–7 sub-parts**, with integer marks that add up to exactly 15.

### 2.2 The ladder inside every question (easy → hard)

Tag every sub-part with a tier:

- **Tier 1:** apply one idea once (≤ 2 marks).
- **Tier 2:** a standard trace or table executed exactly.
- **Tier 3:** a trap, a twist, or reasoning that reuses earlier parts.

Sub-parts appear in **non-decreasing tier order**. In Q4 this applies inside each of its two blocks, compression then greedy (STEP 2.6). Every question has **≥ 1 Tier-1** and **≥ 1 Tier-3 part worth ≥ 2 marks**. Follow-up parts must **reuse the student's own table or tree** (archetype D9). They must never ask an unrelated fact.

### 2.3 Question 1: broad coverage, split across the two papers

The student wants Q1 to be wide, so that **Paper 1's Q1 and Paper 2's Q1 together cover every row below**. Each paper's Q1 covers **6 ± 1 rows**. Each Q1 has exactly **one main trace (D1, 4–5 marks)** and **one recursion chain (D3 → D4)**.

| Row | Topic (L01–L05) | Paper |
|---|---|---|
| R1 | Algorithm properties / purpose of analysis, applied (e.g. "this procedure fails which property, and why?") | 1 |
| R2 | RAM-model step count of a 3–5-line fragment with one placement twist (convention printed) | 1 |
| R3 | Insertion sort: best/worst **input** of a given size and the resulting bound, or a short trace | 2 |
| R4 | O/Ω/Θ of a sum with a decoy term, justified by the ratio theorem | 1 |
| R5 | A **new** recursive definition → recursive relation + initial condition(s) → recursive pseudo-code | 1 |
| R6 | The recurrence for R5's (or a given) code, solved by repeated substitution | 1 |
| R7 | Recursion-tree or substitution method on a divide-and-conquer recurrence | 2 |
| R8 | Master theorem: identify a, b, f(n), the case, and the regularity condition where needed | 2 |
| R9 | **Quicksort (Lomuto) trace** on new data, plus best/worst partitioning | 1 (main trace) |
| R10 | Merge sort: MERGE trace or its recurrence/analysis | 2 |
| R11 | Full/complete binary tree properties (node count, height ⌊log₂ n⌋), applied | 2 |
| R12 | **BUILD_HEAP/HEAPSORT trace**, an "almost a heap" check, or the priority-queue heap type | 2 (main trace) |

You may swap single rows between the papers if that improves the questions, as long as every row is still covered, each paper still has one main trace and one recursion chain, and the two Q1s stay equally hard.

### 2.4 Question 2: Dynamic Programming (both papers; the whiteboard and FM Q5 are the model)

| Part | Marks | Content |
|---|---|---|
| Tier 1 | 1–2 | A DP element **applied**: e.g. mark two repeated calls in a printed partial KNAPSACK-RECURSE tree and name the element they show, or say why MCM has optimal substructure using one split |
| Tier 2 | 5–7 | Knapsack table from the printed P(i, k) recursion: 4 items, c ≤ 10, rows i = n … 1, columns k = 0 … c |
| Tier 2 | 2 | Read-off: a **non-final** P(i, k) with its recursion line written out, plus the trace-back (the x vector) |
| Tier 2 | 4–5 | MCM m and s tables for 4 matrices, the optimal parenthesization and the optimal scalar-multiplication count. Paper 1 gives the dimensions as p₀ … p₄ (the whiteboard's style); Paper 2 gives them as matrix sizes (FM's style) |
| Tier 3 | 1–2 | A twist that uses the tables: e.g. a classmate's greedy rule (best profit/weight; cheapest product first) loses here, and by how much; or which rows of the knapsack table change if one item's weight changes, and why |

### 2.5 Question 3: String Matching (both papers; no past paper exists, so build from the lecture's example formats)

| Part | Marks | Content |
|---|---|---|
| Tier 1 | 1–2 | The valid-shift definition applied: which listed shifts are valid, and why the others are not (include one that fails 0 ≤ s ≤ n − m) |
| Tier 2 | 3–4 | Naive matcher: the valid shifts and the number of character comparisons (counting rule stated); or construct a worst-case text for a given pattern and n, with the count |
| Tier 2 | 4–5 | Rabin-Karp: p mod q; every window value, with at least two computed by the **rolling formula shown in full**; valid matches vs spurious hits; how many explicit character checks are made |
| Tier 3 | 4–5 | String-matching automaton for a pattern: the δ table, the state sequence on a text, where the pattern occurs (end positions → shifts). The hardest line explains a **non-zero fallback** (why δ(q, a) is not 0) |

Paper 1 and Paper 2 use different alphabets, patterns and moduli. At least one automaton must have overlapping occurrences in its text.

### 2.6 Question 4: Compression (8 ± 1) + Greedy (7 ± 1)

**Across the two papers**, cover every item below at least once. Huffman appears in **both** papers.

- **Compression:**
  - fixed-length bits ⌈log₂ n⌉ for a message
  - a prefix-free check on a flawed variable-length code
  - entropy (bound vs actual)
  - Shannon-Fano, Huffman, Hu-Tucker
  - Ziv-Lempel (distance, copy) stream, and what gzip does next
  - lossless vs lossy, applied to a scenario (≤ 1 mark)
- **Greedy:**
  - greedy ≠ optimal (a small counterexample the student must find or check)
  - Kruskal with the disjoint-set table
  - Prim with candidate edges
  - Dijkstra with the lecture's table
  - spanning-tree properties (n − 1 edges)

Suggested split:

| Paper | Compression | Greedy |
|---|---|---|
| 1 | fixed-length → Huffman + total bits → Shannon-Fano → "which is optimal?" (choose data where the totals **differ**) | Kruskal table → Prim's first choices from a given root, then why both totals match |
| 2 | prefix-free check → Huffman → Hu-Tucker and why its total ≥ Huffman's; or a Ziv-Lempel stream + gzip | Dijkstra table → a greedy-path counterexample |

Inside Q4, the compression parts come first, then the greedy parts. Each block climbs from easy to hard.

### 2.7 Parity between the papers

- Same number of sub-parts per question ± 1.
- Same marks per tier per question ± 1.
- Marks per archetype within ± 2.
- Estimated minutes per question within ± 3.
- **No dataset, text, pattern, graph or frequency table is shared** between the papers, or with the past material (STEP 0.3) or the calibration examples (STEP 3.3).

### 2.8 The algorithms appendix (part of the paper, as in the real exam)

Each paper ends with **"Algorithms"**: every procedure its questions name, copied from the slides with line numbers, in the lecture's notation (`←`, `⊲`, CAPITAL procedure names, 1-based arrays). Examples: INSERTION-SORT, QUICKSORT + PARTITION, MERGE, HEAPIFY / BUILD_HEAP / HEAPSORT, the P(i, k) recursion, MATRIX_CHAIN_ORDER, NAIVE-STRING-MATCHER, MST-KRUSKAL, MST-PRIM, DIJKSTRA + RELAX, HUFFMAN(C), the Shannon-Fano steps.

- Questions say "using the algorithm given at the end of the paper".
- Nothing a question names may be missing from its paper's appendix (FM's missing "page 16" is the flaw to avoid).
- This is the paper's own appendix, **not** a reference sheet. There is no separate reference sheet.

---

## STEP 3 — WRITING EACH SUB-PART: THE QUALITY BAR

### 3.1 Rules

1. **Lecturer phrasing** (profile §4.1). For traces: "Illustrate the operations of … for the array with the given set of elements. (For the illustration process assign the values only once to the given algorithm codes and then use diagrammatic way to reach the answer.)". Print data as an index row over a value row.
2. **Choose the data so the interesting branch fires.** Examples:
   - HEAPIFY cascades two levels at least once
   - the pivot lands mid-array, and at least one element equal to or smaller than the pivot is swapped forward
   - a knapsack cell where "take" wins by a small margin
   - an MCM cell where the minimising k is not the obvious one
   - a Rabin-Karp spurious hit
   - an automaton fallback to a non-zero state
   - a Huffman merged node that exceeds an original frequency
   - a Kruskal rejection
   - a Dijkstra relaxation that **lowers** an already-finite d
3. **Every hard part is one of the profile §3 traps or a reasoning step over the student's own work.** It must never come from extra arithmetic.
4. **Derivation parts** (R5–R8) use a **new** function or recurrence that isn't on a slide. Examples:
   - sum of an array by halving
   - xⁿ by squaring
   - the count of binary strings without "11"
   - a ternary search's recurrence
5. **Each part has exactly one defensible final answer** (STEP 1.2), and its stem states every convention that answer depends on.

### 3.2 AI anti-patterns: reject any sub-part that has one

- A **definitional stem** ("What is a heap?") when a data version exists.
- "**Explain how X works**" instead of making the student run X.
- **Big inputs** posing as difficulty; long arithmetic that tests nothing new.
- **Trivia** (STEP 1.3).
- A follow-up that **ignores** the previous part.
- **Two defensible answers**; an unstated tie-break or neighbour order.
- **Mixing algorithm versions**, or a model answer that relies on a slide error.
- The **same idea twice** in one paper.
- A rubric that rewards a **keyword** instead of a step.

### 3.3 Calibration examples: the quality bar (do NOT reuse in either paper)

Every number below was computed with `algos.py`.

- **Q1 · R5 → R8 chain (D3 → D4):** MAX(A, l, r) returns the largest element by splitting at q = ⌊(l + r)/2⌋.
  - (a) The relation: MAX = A[l] if l = r; otherwise max(MAX(A, l, q), MAX(A, q + 1, r)).
  - (b) The pseudo-code.
  - (c) T(n) = 2T(n/2) + c, T(1) = c.
  - (d) Master theorem: a = 2, b = 2, f(n) = c = O(n^(1−ε)) with ε = 1. This is case 1, so Θ(n).
  - (e) On A = [7, 3, 9, 4, 8] the procedure makes **9 calls** (2n − 1) and **4 comparisons** (n − 1).
  - (f) Tier 3: it is the same Θ(n) as a linear scan; the difference is a recursion depth of ⌈lg n⌉ + 1.
- **Q2 · knapsack (D2 → D9 → twist):** w = [2, 2, 3, 5], p = [3, 4, 8, 9], c = 9.
  - Rows: i = 4 → 0 0 0 0 0 9 9 9 9 9; i = 3 → 0 0 0 8 8 9 9 9 17 17; i = 2 → 0 0 4 8 8 12 12 13 17 17; i = 1 → 0 0 4 8 8 12 12 15 17 17.
  - P(1, 9) = 17 with x = [0, 0, 1, 1], the unique optimum.
  - Twist: a classmate who takes items by best profit/weight gets 15.
- **Q2 · MCM:** p = [3, 2, 4, 5, 6].
  - m[1, 2] = 24, m[2, 3] = 40, m[3, 4] = 120, m[1, 3] = 70, m[2, 4] = 100, m[1, 4] = 136.
  - s[1, 4] = 1; the parenthesization is (A1((A2A3)A4)), with 136 scalar multiplications.
  - Twist: "always do the cheapest adjacent product first" costs 174.
- **Q3 · Rabin-Karp:** T = 390996030824, P = 603, q = 13.
  - p mod 13 = 5. The windows are 0 12 8 8 11 5 4 9 4 5.
  - There is a valid match at s = 5 and a spurious hit at s = 9 (824 mod 13 = 5).
  - Two explicit checks are needed.
- **Q3 · automaton:** P = abaab, Σ = {a, b}.
  - δ table (each row: a, b): 0 → 1, 0 · 1 → 1, 2 · 2 → 3, 0 · 3 → 4, 2 · 4 → 1, 5 · 5 → 3, 0.
  - On T = aabaabaab the states are 0 1 1 2 3 4 5 3 4 5, so occurrences end at 6 and 9 (shifts 1 and 4, overlapping).
  - Tier 3: explain δ(5, a) = 3. The longest prefix of P that is a suffix of "abaaba" is "aba".
- **Q4 · Huffman vs Shannon-Fano:** A 6, B 9, C 10, D 11, E 24.
  - Huffman merges 6+9, 10+11, 15+21, 24+36. The codes are E 0, A 100, B 101, C 110, D 111, for **132 bits**.
  - Shannon-Fano splits {E, D} | {C, B, A}. The codes are E 00, D 01, C 10, B 110, A 111, for **135 bits**.
  - Fixed-length coding needs 3 × 60 = 180 bits.
  - "Which is optimal?" Huffman, by 3 bits; Shannon-Fano's first split is the culprit.

---

## STEP 4 — CALCULATIONS AND VERIFICATION

- **Produce every number, trace, table, code and path with a Python script** that imports `DAA_lecturer_model/algos.py`. Run it with `python3 -I` from a scratch folder, adding the model folder to `sys.path`. Never hand-compute a model answer.
- **Extend `algos.py` in your scratch copy** if you need another lecture algorithm. Check every new function against the lecture's own worked example before using it.
- **Run uniqueness checks in the script for every instance** (STEP 1.2):
  - the number of optimal knapsack subsets (by brute force)
  - unique MCM minima
  - Huffman/Shannon-Fano tie flags
  - distinct graph weights
  - Dijkstra tie flags

  Reject and regenerate any instance that fails.
- **Search for instances** (as the calibration examples were found) that satisfy the "interesting branch" rule (STEP 3.1.2) **and** the size limits (STEP 1.4).
- **Emit the data the app embeds from the same script** (STEP 7's `check` objects), so the app's numbers and the script's numbers can never drift apart.

---

## STEP 5 — MODEL ANSWERS AND RUBRICS

For every sub-part:

1. **Model answer in the lecture's layout** (profile §4.3):
   - array snapshots with the moved elements highlighted
   - heap trees with the array under them
   - the knapsack table with the "+pᵢ" cells marked
   - m and s tables, with the full min{…} expansion written out for **at least two cells**
   - Rabin-Karp window rows labelled "valid match" / "spurious hit"
   - the δ table, the state diagram and the φ row under the text
   - Huffman forests (a), (b), … with 0/1 edge labels
   - the Kruskal table (weight · edge · merge/reject · sets)
   - Prim's "Choose … Candidate edges … Choose edge" lines
   - the Dijkstra table (Step · Vertex to be marked · d[…] · Unmarked vertices)

   Show **every intermediate state** that the rubric awards.
2. **Rubric:** 2–6 checkable items whose marks add up exactly to the sub-part's marks (½-marks allowed only where the lecturer would plausibly use them). Each item says **what must be visible on the student's paper**, e.g. "BUILD_HEAP result [ … ] shown as a tree or an array (2)". Never write "correct method".
3. **Common mistakes:** 2–4 lines, each naming a mistake and its wrong result (e.g. on FM's data, "used items 1..i instead of i..n → P(3, 9) = 18 instead of 10"), computed by applying that mistake in the script. Link the trap ids from profile §3.
4. **Source tag** (lecture file + slide number) and **lecturer pattern** (archetype id, plus "like FM-Q5.3" links to related bank records).

---

## STEP 6 — FIGURES AND TABLES

- **Inline SVG, generated from the question's data, for:**
  - trees: heaps, recursion trees, Huffman/Shannon-Fano/Hu-Tucker trees
  - graphs: weighted undirected for Kruskal/Prim, directed for Dijkstra
  - automata: the state diagram with a heavy spine and curved back edges
- **Tables are HTML tables:**
  - data rows
  - DP tables
  - δ tables
  - MCM tables: an upper-triangular grid is fine; the slide's diamond is optional
- **Fixed, hand-chosen coordinates** for graphs; level-based layout for trees.
- **Edge-weight labels** sit on a small background halo (`fill: var(--card)`) so they never sit on a line.
- **Never put an answer inside a question figure.** The model-answer figures are separate.
- **Legibility:**
  - text ≥ ~12 px at 1280 px window width
  - ≥ 6 px clearance between labels and other marks
  - colours only from the palette's CSS variables (theme-aware)
  - each SVG with a `viewBox`, `width: 100%`, a sensible `min-width` and `max-width ≈ 1.1 ×` its viewBox width
- **Render check (mandatory):**
  1. Open the app in headless Chromium (Playwright) at **1280 px** in **both themes**.
  2. Reveal every model answer and screenshot every figure. **Look at them.**
  3. Run a `getBBox()` script that fails on any text–text, text–line or text–shape intersection (edge labels vs edges included).
  4. Fix and re-check until clean.

---

## STEP 7 — THE APP

Single self-contained file: `DAA_final_mock/index.html`, containing **both papers**. No CDN, no frameworks, no build step; vanilla JS + CSS that works offline by double-clicking.

### Flow

- **Cover page:** "SE2022 — Design and Analysis of Algorithms · Final Mock Papers", short instructions, and two cards: **Paper 1** and **Paper 2**.
  - **Instructions:** 2 hours suggested; 4 questions × 15 marks; answer all; work on paper, then reveal each part's model answer and tick the rubric points you earned.
  - **Card status:** not started / in progress (n of N parts marked) / finished with its score; also the best score.
  - **Card buttons:** **Start**, or **Resume** + **Start fresh** (confirm first); and **Print question paper**.
  - **There is no practice/exam choice and no other setup.**
- **Print question paper:** a print stylesheet that prints the chosen paper's four questions and its Algorithms appendix **without** model answers, rubrics or app chrome, A4-friendly, so the student can write on it.
- **No countdown timer.** Show a small **time-spent clock** per paper, counting only while that paper is open, and record it in the results.

### Paper view (desktop, ≥ 1024 px; no phone testing needed)

- **Header:**
  - the paper name
  - the current question
  - a running self-score (marks ticked / marks of the parts marked so far)
  - the time spent
  - **Algorithms** (opens that paper's appendix in a side drawer)
  - the theme toggle
  - **Finish paper**
  - **Switch paper** (back to the cover; progress is kept)
- **Navigator sidebar:** Questions 1–4, each with its sub-parts. Every part shows its state with a colour **and** a symbol:
  - not revealed (outline)
  - revealed but not marked (ink dot)
  - marked full (✓ green), partial (◐ amber) or zero (✗ red)
  - flagged (⚑ maroon)

  The sidebar also has **Reset this paper** (confirm first).
- **Question display:** like a real paper.
  - The question number, title and **[15 marks]**, then the context.
  - Each sub-part with its marks right-aligned, e.g. **(4 marks)**, and its data tables and figures.
  - Under each sub-part, a **Show model answer** button (key `R`). Revealing asks nothing: the student is trusted to have written their answer first.
- **After reveal:**
  1. The worked model answer (STEP 5.1).
  2. The **rubric checklist** (STEP 5.2). The student ticks what their paper shows, and a live "x / marks" total updates.
  3. **Common mistakes** (STEP 5.3).
  4. The source and the lecturer-pattern tags.
  5. **Done marking** records the part as marked, so a genuine 0 differs from not-yet-marked. Ticks stay editable until the paper is finished.
- **Flags:** a toggle on every part (key `F`). **Finish paper** warns: "You have N parts not revealed/marked and M flagged — finish anyway?". Unmarked parts score 0.

### Results (per paper)

- the total /60 and %, and each question /15
- breakdowns by lecture, by archetype and by tier
- the time spent
- a **list of weak parts** (below 50% of their marks), with jump-back links
- **Redo weak parts**: hides those parts' answers again and clears their ticks, keeping the original attempt in an attempt-history table
- the best score.

### Storage, keys, keyboard

- **Storage:** `localStorage`, with **separate versioned keys per paper** (`daa-final-v1-paper1` and `daa-final-v1-paper2`). Store revealed/marked state, ticks, flags, time spent, the current position, attempts and the best score. Wrap every storage call in `try/catch`. The theme key is `daa-theme`.
- **Keyboard:** `←`/`→` previous/next sub-part, `R` reveal, `F` flag, `1`–`9` toggle rubric items, `Enter` = Done marking. All are disabled while typing.

### Palette: the same as the Java / CN / P&S papers (exact values, as CSS custom properties)

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
- The theme follows the device by default. A ☀/☾ toggle saves the choice in `localStorage` (`daa-theme`), and an inline `<head>` script applies it before first paint.
- **No hard-coded colours** outside the token blocks (SVG included).
- **Typography:** serif question text (`"Iowan Old Style", "Palatino Linotype", Georgia, serif`), sans UI, **monospace for pseudo-code, arrays and DP tables**. Pseudo-code keeps its line numbers and indentation.

### Data model and self-test

- **Data model:**
  - Each paper is `{ id, title, appendix: [procedure ids], questions: [...] }`.
  - Each question is `{ num, marks: 15, title, lectures, context, parts: [...] }`.
  - Each part is `{ label, marks, tier, minutes, archetype, pattern: [bank ids], lecture, rows: [Q1 coverage rows], topic, stem, data?, figure?, solution: { html, figures }, rubric: [{ text, marks }], mistakes: [{ text, trap }], source, check }`.
- **`check`** holds machine-readable inputs and expected outputs, e.g. `{ algo: "knapsack", w, p, c, expect: { rows, x, cells: { "i,k": value } } }`. The app embeds **small JS ports of the lecture algorithms** used by the papers (insertion, Lomuto partition/quicksort, merge, heapify/build/heapsort, heap check, knapsack P(i, k), matrix-chain, naive, Rabin-Karp, automaton, Huffman, Shannon-Fano, Hu-Tucker, Ziv-Lempel, Kruskal, Prim, Dijkstra; only those you use).
- **`index.html?selftest=1`** checks **for each paper**:
  - 4 questions × 15 = 60 marks; every part's rubric adds up to its marks
  - tiers are non-decreasing inside each question (inside each block for Q4), with ≥ 1 Tier-1 and ≥ 1 Tier-3 (≥ 2 marks) per question
  - Q4's compression/greedy marks are 8 ± 1 / 7 ± 1
  - every part has a solution, ≥ 2 rubric items, ≥ 2 mistakes, a source and an archetype
  - every procedure a stem names is in the appendix
  - estimated minutes per question are 25–30
  - **every `check` recomputes to its expected value with the JS ports** (and the uniqueness conditions of STEP 1.2 hold)

  **Across the papers**, it checks:
  - Q1 coverage rows R1–R12 are all covered
  - every STEP 2.6 coverage item is present
  - the parity rules (STEP 2.7) hold
  - no dataset is shared, and none matches the STEP 0.3 or STEP 3.3 data

  It logs a pass/fail table. **Run it and fix every failure.**

---

## STEP 8 — BEFORE YOU FINISH

Do **not** write an audit or report file. Silently make sure that:

- **Self-test:** `index.html?selftest=1` reports zero failures, and the app loads with no console errors.
- **Numbers:** every model answer, mistake value and figure came from the script, and every uniqueness check passed.
- **Anti-patterns:** every part passes STEP 3.2. Scan all stems for trivia, definitional stems, unstated conventions and duplicated ideas.
- **Flaws:** nothing from profile §5 or STEP 1.2 appears in either paper or its appendix.
- **Figures:** the STEP 6 render check passes at 1280 px in both themes, with every model answer revealed.
- **Print:** "Print question paper" produces a clean paper with its appendix and no solutions (check it with Playwright's PDF output and look at the pages).
- **Theme:** switching works (follows the device; the toggle overrides it and survives a reload; no flash on load).

Fix anything that fails, then reply with a summary of **≤ 10 lines**: each paper's Q1 coverage rows, the traps used in each question, which lecturer patterns each paper recycles, and anything you compromised on.

---

## DELIVERABLES

```
DAA_final_mock/
└── index.html     (both papers, chosen on the cover page; each with its Algorithms appendix)
```

## DO NOT

- Do not ask trivia, definitional one-liners, or anything outside the nine lectures (no graph DFS/BFS questions; graphs appear only through L07's greedy algorithms).
- Do not use big inputs as difficulty, or long arithmetic that tests nothing new.
- Do not use data with ties, multiple optimal answers or unstated conventions.
- Do not print or rely on the slide errors (the increasing-k 1-D knapsack, Hoare partition with q − 1, the naive "best case", "all hits spurious").
- Do not reuse past-paper, lecture-example or calibration data, or share any data between the two papers.
- Do not hand-compute any number; use the script.
- Do not put an answer inside a question figure, or let any label overlap.
- Do not add a practice/exam mode choice, a countdown timer, a reference sheet, answer-typing boxes or report files.
