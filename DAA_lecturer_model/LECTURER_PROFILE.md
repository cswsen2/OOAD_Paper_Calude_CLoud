# SE2022 Design and Analysis of Algorithms — Lecturer Thinking-Pattern Profile

A reusable model of **how this lecturer sets questions**, built from every question in the three available sources. Use it with `question_bank.json` (same folder), which stores each past sub-question as a tagged record whose answer was computed by script. Before writing any SE2022 question, read this file, then look up the related past questions in the bank.

| Source | File | Kind | Records |
|---|---|---|---|
| T1 | `DAA Model Paper Test 01 (1).pdf` | Test 01 model paper, Y2S2 2024, 1 h, 20 marks | 13 |
| FM | `Final Exam Paper Model Paper (1).pdf` | Final exam model paper, 2 h | 31 (13 are verbatim T1 repeats) |
| WB | `DaaExact.jpeg` | Lecturer's whiteboard: "this will be kind of the model coming for the paper" | 2 |

### The announced final (from the exam notice)

2 hours, 4 questions × 15 marks = 60 marks.

| Q | Marks | Title | Lectures |
|---|---|---|---|
| Q1 | 15 | Recursion and Algorithm Design | L01–L05 (analysis, insertion sort, asymptotics, recursion and recurrences, divide and conquer, trees and heaps) |
| Q2 | 15 | Dynamic Programming: 0/1 knapsack and matrix-chain multiplication | L09 |
| Q3 | 15 | String Matching Algorithms | L06 |
| Q4 | 15 | Data Compression Algorithms and Greedy Algorithms | L08 + L07 |

**L06 (string matching) and L07 (greedy) have never appeared in any past paper**, yet together they carry about 22 of the 60 marks. Questions on them must be built from the lecturer's general habits (§1–§4) and the lecture's own worked-example formats (§4.3), not from memory of other universities' exams.

---

## 1. How a paper is built

- **The signature instruction:** *"Illustrate the operations of [ALGORITHM] for the array with the given set of elements. (For the illustration process assign the values only once to the given algorithm codes and then use diagrammatic way to reach the answer.)"* It appears in 6 of the 8 trace questions (the two coding traces say "Construct the codeword … using the … Algorithm given at the end of the paper"). The lecturer prints the pseudo-code (with the question, or in an **"Algorithms" appendix at the end of the paper**) and marks how faithfully the student *executes* it. Students never have to recall pseudo-code.
- **Every long question climbs the same ladder:**
  1. a 1–2 mark recall opener ("List two properties…", "What is meant by optimal substructure?")
  2. the big trace or table (6–8 marks)
  3. a follow-up that **reads a result off the student's own work** ("Find P(3,9) and P(1,10)", "How many bits are needed?", "Hence find the optimal parenthesizing")
  4. a reasoning part (best/worst case and *when* it happens, a recurrence and its solution, "which is optimal").
- **Small, friendly data:** 4–8 array elements, 4 knapsack items with capacity 10, 4 matrices with single-digit/ten dimensions, 6 symbols with integer frequencies. Calculators are allowed, but the arithmetic is light. The difficulty lies in executing the method exactly.
- **1-based arrays**, shown as an index row above a value row.
- **Recycling is heavy:** the whole of Test 01 reappears word for word as Q1–Q2 of the final model paper. The whiteboard hint is FM Question Five (MCM + knapsack) with new numbers. Expect **the same question shapes with new numbers**.

### Marks by lecture in the final model paper (84 printed marks)

| Lecture | Marks | Share | What was asked |
|---|---|---|---|
| L01 Intro & analysis | 7 | 8% | properties of a good algorithm; purpose of analysis; RAM step count of a 4-line fragment |
| L02 Insertion sort & asymptotics | 7 | 8% | best/worst case and when; insertion-sort trace; Big-O of two sums |
| L03 Recursion & recurrences | 6 | 7% | pow(x, n): recursive relation + initial condition, pseudo-code, recurrence T(n) |
| L04 Divide & conquer | 10 | 12% | quicksort (Lomuto) trace; best/worst partitioning; best-case recurrence solved by repeated substitution |
| L05 Trees & heaps | 12 | 14% | leaf/binary tree; prove n + 1 = 2^(h+1); heapsort trace; max-heap check; heap type for a priority queue |
| L08 Compression | 12 | 14% | fixed-length coding; Huffman; total bits; Shannon-Fano; which code is optimal |
| L09 Dynamic programming | 20 | 24% | optimal substructure; knapsack table; P(3,9), P(1,10); trace-back; MCM m/s tables + parenthesization |
| Graphs/DFS (not in the nine decks) | 10 | 12% | draw a digraph; matrix vs list; DFS trace |
| L06, L07 | 0 | 0% | never examined so far, but they are in the announced final |

---

## 2. Question archetypes (D1–D11)

The `archetype` field in `question_bank.json` uses these ids. The counts cover all 46 records (T1 repeats inside FM are counted twice, because they were asked twice).

| Id | Archetype | Count | What he is really testing | Past examples |
|---|---|---|---|---|
| **D1** | Illustrate a **given** algorithm on given data | 8 | Executing printed pseudo-code **exactly**: indices, loop bounds, which element is the pivot, when HEAPIFY recurses, which node gets 0 | insertion sort [10, 0, 8, 4]; Lomuto quicksort [28, 15, 1, 30, 0, 8]; heapsort [45, 25, 15, 85, 75, 65, 35, 55]; DFS; Huffman and Shannon-Fano on digit frequencies |
| **D2** | Build a DP table from the **given** recurrence | 4 | Filling P(i, k) or m[i, j]/s[i, j] in the right order from the printed recurrence | knapsack w = [3, 4, 6, 3], p = [6, 12, 8, 2], c = 10; MCM 2×5, 5×3, 3×10, 10×4; whiteboard: p = 2, 3, 4, 5, 10 and W = [4, 3, 5, 2], P = [10, 8, 9, 16], c = 10 |
| **D3** | Model a recursive definition | 8 | Turning a definition into (a) a recursive relation **with the initial condition**, (b) recursive pseudo-code, (c) a recurrence for T(n) | pow(x, n) = x · pow(x, n − 1); quicksort best case T(n) = 2T(n/2) + cn |
| **D4** | Solve a recurrence by a **named** method | 2 | Carrying the method through, not quoting the answer | repeated substitution for T(n) = 2T(n/2) + cn → O(n lg n) |
| **D5** | Best/worst case **and when it happens** | 4 | Linking a bound to the **input that causes it** | insertion sort (sorted / reverse sorted); quicksort (balanced / 0 : n − 1 splits) |
| **D6** | Asymptotic order with justification | 2 | Picking the dominant term **and saying why** | log n + n + 100 → O(n); 200n²⁰ + 100n¹⁰ + 2ⁿ + 3ⁿ + n + 1 → O(3ⁿ) |
| **D7** | RAM-model step count | 2 | Counting with the lecture's convention, and noticing **where a variable is initialised** | `j ← 0; for i ← 0 to n; while j ≤ 5; j ← j + 1` → 4n + 25 = O(n) |
| **D8** | Verify or prove a structural property | 2 | Checking **every** parent–child pair; a short proof from the definition | is ⟨23, 17, 14, 6, 13, 10, 1, 5, 7, 12⟩ a max-heap (no: 6 < 7 at indices 4/9); n + 1 = 2^(h+1) |
| **D9** | Read a result off your own construction | 4 | Using the table or tree just built: a single cell, the chosen items, total bits, which code wins | P(3, 9) and P(1, 10); "explain how you achieved the final solution"; total bits; Huffman vs Shannon-Fano |
| **D10** | Choose and justify | 2 | A design decision derived from the problem statement | max-heap when a higher number means higher priority; adjacency list for a sparse graph |
| **D11** | Warm-up recall (1–2 marks) | 8 | One precise sentence, or a definition applied once | properties of a good algorithm; purpose of analysis; leaf node, binary tree; fixed-length coding + example; optimal substructure |

---

## 3. His favourite traps (use them as the hard sub-parts)

1. **Initialisation outside the loop.** `j ← 0` sits before the `for`, so the inner `while` runs only during the first outer iteration. The fragment is linear (4n + 25 steps), not "6 × (n + 1)". Lecture slides 24/25 show both versions on purpose.
2. **The dominant term, not the biggest coefficient.** 3ⁿ beats 2ⁿ and 200n²⁰; log n loses to n.
3. **The deep heap violation.** The top levels are perfect; the one failing pair is at the bottom (A[4] = 6 < A[9] = 7).
4. **Read the stem for the heap type.** "Higher number means higher priority" gives a **max**-heap.
5. **Lomuto's pivot is the last element** (x ← A[r]), with 1-based indices, and size-0/1 sub-arrays make no PARTITION call.
6. **BUILD_HEAP starts at ⌊n/2⌋ and goes down to 1.** It is not n insertions, and heap_size shrinks after every exchange in HEAPSORT.
7. **P(i, k) is defined on the suffix i…n.** P(3, 9) may use only items 3..n. Students who use items 1..3 get a different (wrong) value.
8. **MCM's cost term is p_{i−1} · p_k · p_j.** Off-by-one dimension indices give every entry wrong; s[i, j] stores the **k**, not the cost.
9. **"Which code is optimal?" needs the totals.** In FM both Huffman and Shannon-Fano cost 2166 bits, so the reflex answer "Huffman" is incomplete.
10. **Bits per codeword ≠ bits for the file.** Total bits = Σ frequency × codeword length; fixed-length uses ⌈log₂ n⌉ bits per symbol.

For the never-examined lectures, these traps follow the same thinking and are fair game:

- **L06:** a Rabin-Karp hit is not a match (spurious hits must be checked character by character); window values come from the rolling formula, not from re-dividing each window; a shift s is valid only if 0 ≤ s ≤ n − m; in the matching automaton, a mismatch does **not** always return to state 0.
- **L07:** greedy shortest path ≠ optimal (the lecture's A→E example, greedy 10 vs optimal 6); Kruskal rejects an edge whose ends are already in the same set; Prim's candidate edges change after every choice; in Dijkstra, a vertex is final only once it is marked.

---

## 4. Phrasing and notation habits

### 4.1 Verbs and stems

- "Illustrate the operations of … (assign the values only once to the given algorithm codes and then use diagrammatic way to reach the answer)"
- "List two …", "What is meant by …", "Briefly describe/explain …", "Give one example …"
- "Prove that …", "Is … a max heap? **Justify your answer.**", "Find the Big oh value … **Justify your answer.**"
- "Write a recursive relation … **Clearly define the initial condition(s).**", "Write a recursive algorithm in pseudo code …", "Write a recurrence equation that describes the running time T(n) …", "Use the repeated substitution method to solve …"
- "Construct a table … using Dynamic Programming with the recursive solution given at the end of the paper", "Find P(3,9) and P(1,10) …", "Briefly explain how you achieved the final solution"
- "Draw the m and s table …", "**Hence** find the optimal parenthesizing and optimal number of scalar multiplications"
- "Construct the codeword … using Huffman Algorithm given at the end of the paper", "How many bits are needed …", "Which codeword is optimal …"

### 4.2 Notation

- `←` for assignment, `⊲` for comments, `A[1..n]`, procedure names in CAPITALS (HEAPIFY, BUILD_HEAP, PARTITION, DFS-VISIT).
- Matrix A_i has dimension p_{i−1} × p_i. Tables are m[i, j] and s[i, j]; the knapsack function is P(i, k); running time is T(n); "Big oh".
- The lecture's **full binary tree** is the one with exactly 2^(h+1) − 1 nodes. The height of a complete binary tree with n nodes is ⌊log₂ n⌋.

### 4.3 The lecture's own worked-example formats (copy these layouts)

| Topic | Lecture layout |
|---|---|
| Insertion sort | array snapshots (a)–(f) after each j, with the key shaded |
| Quicksort | PARTITION snapshots with i and j positions, and the pivot boxed |
| Heapsort | tree + array after each HEAPIFY of BUILD_HEAP, then after each exchange/HEAPIFY |
| Knapsack | table with header `i\k`, **rows i = n down to 1**, columns k = 0..c; the "+p_i" annotation shows which cell was added; the solution vector x = [ … ] |
| MCM | m and s tables (CLRS diamond on the slide; an upper-triangular grid is equivalent), with the full min{ … } expansion written for a cell such as m[2, 5] |
| Naive matching | text with index row 1..n, the pattern written under each shift |
| Rabin-Karp | text digits in boxes, pattern value mod q, a row of window values mod q with "valid match" and "spurious hit" labels, and the rolling step `14152 ≡ (31415 − 3·10000)·10 + 2 (mod 13)` |
| Finite automaton | state-transition diagram, δ table (state × input, with the pattern letter beside each row), and the state sequence φ(T_i) under the text |
| Greedy path | step-by-step picture of the greedy choice, then the optimal path for comparison |
| Kruskal | table: weight · edge · merge/reject · the disjoint sets after the step |
| Prim | "Choose vertex A, V = {…}; Candidate edges = …; Choose edge (A, D)", repeated |
| Dijkstra | table: Step # · Vertex to be marked · d[u] d[a] … · Unmarked vertices |
| Fixed/variable length | codeword table and the encoded message with its bit count; a comparison table (ASCII · binary · VLC · entropy) |
| Entropy | H = −Σ p_i log₂ p_i, and total = n·H (ABRACADABRA: H = 2.04, 22.44 bits) |
| Huffman | forest snapshots (a)…(f), left edge 0 / right edge 1, the first EXTRACT-MIN as the left child |
| Shannon-Fano | sorted list, a split tree with group frequency sums, codeword table |
| Hu-Tucker | leaves kept in alphabetical order; join only nodes not separated by a leaf; the leftmost pair on ties; read the lengths, then assign alphabetic codes |
| Ziv-Lempel / gzip | table of the growing prefix · distance back · number to copy or ASCII code, then the (distance, length) symbol stream and two Huffman codes |

---

## 5. Flaws in his papers and slides (do NOT imitate)

**Paper flaws**

- **Messy numbering.** Question three is printed twice (once as "Question One", items 7–12). The compression section has no question number and its parts run e–h. The statement and the question are split across items 5 and 6.
- **Marks that don't add up.** T1 heads Question One "(10 Marks)" but its parts total 20. Several FM parts have no marks.
- **Missing appendix.** FM says the Shannon-Fano algorithm is "at the end of the paper (page 16)", but the appendix doesn't contain it.
- **Under-specified trace.** The DFS question never states the adjacency-list order, so several discovery orders are defensible. Graphs/DFS are also outside the nine decks.
- **Two optimal answers.** The FM knapsack instance (w = [3, 4, 6, 3], p = [6, 12, 8, 2], c = 10) has two optimal subsets, {2, 3} and {1, 2, 4}, both worth 20, so "explain how you achieved the final solution" has two answers.

**Slide flaws to avoid when writing questions**

- **The 1-D knapsack DP iterates k upward** ("for k ← w_i to C"). That computes the *unbounded* knapsack. Use only the P(i, k) recursion for 0/1 questions.
- **Inconsistent examples:**
  - The knapsack profits change from [6, 3, 5, 4, 6] to [2, 3, 5, 4, 6] mid-lecture.
  - Hu-Tucker's f has frequency 2 in the tree but 1 in the table.
  - The FLC slide labels "DBADCBEA" but encodes ABRACADABRA.
- **Shannon-Fano ties are broken inconsistently** (13|10 in one split, 2|3 in another).
- **Partition Algorithm 01 (Hoare, returns j) is shown with QUICKSORT(A, p, q − 1)**. That pairing is incorrect. Use only Algorithm 02 (Lomuto), as both papers do.
- **The naive-matcher "best case" slide** says O((n − m + 1)m) comparisons next to an example that needs only n − m + 1.
- **"Rabin-Karp worst case = all hits spurious"** is loose. The real worst case is that *every* window hits (valid or spurious), giving Θ((n − m + 1)m).

**Rules that follow:**

- Number questions cleanly, and give every part its marks.
- Print every algorithm the question names.
- State every convention a trace depends on (adjacency order, tie-breaks, which child gets 0, how comparisons are counted).
- Choose data with **no ties** where the lecture's tie-break is unclear.
- Make sure every part has **exactly one correct final answer**.
- Never make a slide error the correct answer.

---

## 6. Turning his thinking into new questions

Each archetype has a strong form and a weak (AI-looking) form. Write the strong form.

| Archetype | Strong form (his thinking) | Weak form to avoid |
|---|---|---|
| D1 trace | New data chosen so the **interesting branch fires**: HEAPIFY cascades two levels, a partition puts the pivot mid-array, a Huffman merge creates a node larger than an original symbol, an automaton mismatch falls back to a non-zero state | "Explain how heapsort works"; data where nothing interesting happens; 12+ elements (volume ≠ quality) |
| D2 DP table | A 4-item or 4-matrix instance with a **unique optimum** and at least one cell where the "take" branch wins narrowly | a 6-matrix chain (hours of arithmetic, nothing new learned) |
| D3 model recursion | A fresh recursive definition (sum of digits, a^n by halving, the number of moves of a recursive process) → relation + initial condition → pseudo-code → T(n) | asking for a recursive definition already on a slide (factorial, Fibonacci) |
| D4 solve | A recurrence that comes from the student's own D3 answer, solved by the method named in the stem | quoting the master theorem result without the case check |
| D5 best/worst | "Give an input of size 5 that makes … take its worst case, and say why" | "What is the worst case of X?" alone |
| D6 order | A sum with a decoy (a large coefficient on a smaller term, or 2ⁿ next to 3ⁿ or n!) and a one-line justification | ordering textbook functions with no decoy |
| D7 step count | A 3–5 line fragment where one initialisation or bound changes the count | a fragment with no twist |
| D8 verify/prove | An array that is *almost* a heap; a short proof from the slide's definition | "Define a heap" |
| D9 read-off | A value that **reuses the table/tree** (P(i, k) for a non-final cell, the chosen items, total bits vs fixed length vs entropy) | a follow-up that ignores the previous part |
| D10 choose | A design scenario where the stem decides the answer (max vs min heap; Kruskal vs Prim stated as equivalent but asked for the *first* edge each picks) | "Which is better, A or B?" with no data |
| D11 recall | One precise sentence **applied once** ("give a fixed-length code for these 5 symbols and its total length") | lists of names, dates or inventors |

### Anti-patterns that mark a question as weak or AI-generated

- **Trivia:** who invented Rabin-Karp, the year of Dijkstra's paper, Shannon 1948, university names. The slides contain these, so the temptation is real. **Never ask them.**
- Definitional stems when a data version exists.
- **Large inputs as fake difficulty.** Ten-element heapsorts and six-matrix chains are long, not hard.
- **Asking for a result the slides state wrongly** (§5).
- **Mixing algorithm versions**: Hoare's partition with Lomuto's QUICKSORT, CLRS DIJKSTRA with a "visited list" variant.
- **Ambiguous data**: tied frequencies, tied Shannon-Fano splits, multiple optimal knapsack subsets, unordered adjacency.
- Follow-ups that don't reuse the previous part.
- Marking schemes that reward a keyword instead of a step.
- Ugly numbers, or numbers that make one branch never fire.

---

## 7. Using the bank (for future sessions)

```python
import json
bank = json.load(open("DAA_lecturer_model/question_bank.json"))["questions"]
traps    = [q for q in bank if q["trap"]]                       # all trap sub-questions
traces   = [q for q in bank if q["archetype"].startswith("D1")]  # "illustrate the operations"
dp       = [q for q in bank if q["final_q"] == "Q2"]             # what the final's Q2 looks like
recycled = [q for q in bank if q["repeats"]]                     # asked in more than one source
```

Every record has these fields: `id, source, question, part, marks, lecture, final_q, topic, skill, archetype, trap, given, text, answer, repeats, note`. `final_q` maps the record onto the announced final (Q1–Q4, or null for the off-syllabus graph questions).

When a part's marks were printed as one total for several parts, the first part carries the total and the others have `marks: null`.

Every number, trace and table in `answer` was produced by `algos.py` (same folder: the lecture pseudo-code re-implemented, with 1-based arrays) and checked against brute force. Two checks confirm it:

- The lecture's 6-matrix MCM example reproduces 15125 and ((A1(A2A3))((A4A5)A6)).
- Both knapsack instances match an exhaustive search.

`algos.py` also holds implementations for the topics no past paper has used yet. Each one reproduces the lecture's own worked example exactly:

| Function | Lecture's worked example it reproduces |
|---|---|
| `mergesort_trace` | — (merge sort; no worked example listed here) |
| `naive_match` | shifts 3 and 9 |
| `rabin_karp` | windows 8 9 3 11 0 1 7 8 4 5 10 11 7 9 11, valid shift 6, spurious shift 12 |
| `fa_table` / `fa_run` | the ababaca δ table and the run on abababacaba |
| `kruskal` | the lecture graph, total 9 |
| `prim` | the lecture graph, total 9 |
| `dijkstra` | — (Dijkstra; no worked example listed here) |
| `hu_tucker` | a1 b6 c8 d1 e6 f2 → 000, 001, 01, 100, 101, 11 |
| `lz_lecture` | ABRACADABRA → (0,65)(0,66)(0,82)(3,1)(0,67)(2,1)(0,68)(7,4) |

Rebuild the bank with `python3 -I DAA_lecturer_model/build_bank.py DAA_lecturer_model/question_bank.json`. To add a past paper, append records in the same shape, then update the counts in §1–§2.
