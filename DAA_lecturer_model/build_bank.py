"""Build DAA_lecturer_model/question_bank.json from the three SE2022 sources.

Every record is one sub-question. Every number, trace and table in `answer`
comes from algos.py (lecture pseudo-code, re-implemented) and is checked here
against an independent brute force where one exists.
Run from the repo root:  python3 -I DAA_lecturer_model/build_bank.py DAA_lecturer_model/question_bank.json
"""
import itertools
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import algos as A  # noqa: E402

OUT = sys.argv[1]

SRC = {
    "T1": {"file": "DAA Model Paper Test 01 (1).pdf", "title": "SE2022 Test 01 Model Paper, Y2S2 2024 (1 h, 2 x 10 marks)", "kind": "test"},
    "FM": {"file": "Final Exam Paper Model Paper (1).pdf", "title": "SE2022 Final Examination Model Paper (2 h; section totals 10/10/14/11/12/20 as printed)", "kind": "final-model"},
    "WB": {"file": "DaaExact.jpeg", "title": "Lecturer's whiteboard: 'this will be kind of the model coming for the paper'", "kind": "lecturer-hint"},
}

# Announced final format (from the notice image the student supplied)
FORMAT = {
    "duration": "2 hours",
    "questions": [
        {"q": "Q1", "marks": 15, "title": "Recursion and Algorithm Design", "lectures": ["L01", "L02", "L03", "L04", "L05"]},
        {"q": "Q2", "marks": 15, "title": "Dynamic Programming (0/1 knapsack, matrix-chain multiplication)", "lectures": ["L09"]},
        {"q": "Q3", "marks": 15, "title": "String Matching Algorithms", "lectures": ["L06"]},
        {"q": "Q4", "marks": 15, "title": "Data Compression Algorithms and Greedy Algorithms", "lectures": ["L08", "L07"]},
    ],
}
LEC_TO_FINAL = {"L01": "Q1", "L02": "Q1", "L03": "Q1", "L04": "Q1", "L05": "Q1",
                "L09": "Q2", "L06": "Q3", "L08": "Q4", "L07": "Q4", "none": None}

R = []


def q(src, qn, part, marks, lec, topic, skill, arche, text, answer,
      trap=None, given=None, repeats=None, note=None):
    R.append({
        "id": f"{src}-{qn}.{part}" if part else f"{src}-{qn}",
        "source": src, "question": qn, "part": part, "marks": marks,
        "lecture": lec, "final_q": LEC_TO_FINAL[lec], "topic": topic,
        "skill": skill, "archetype": arche, "trap": trap, "given": given,
        "text": text, "answer": answer, "repeats": repeats or [], "note": note,
    })


# ------------------------------------------------------------------ computed answers
ins = A.insertion_sort_trace([10, 0, 8, 4])
assert [s["array"] for s in ins] == [[0, 10, 8, 4], [0, 8, 10, 4], [0, 4, 8, 10]]

qs_calls, qs_out = A.quicksort_trace([28, 15, 1, 30, 0, 8])
assert qs_out == sorted([28, 15, 1, 30, 0, 8])

hs = A.heapsort_trace([45, 25, 15, 85, 75, 65, 35, 55])
assert hs["sorted"] == sorted([45, 25, 15, 85, 75, 65, 35, 55])

viol = A.max_heap_violations([23, 17, 14, 6, 13, 10, 1, 5, 7, 12])
assert viol == [{"parent_index": 4, "parent": 6, "child_index": 9, "child": 7}]

ram_a, ram_b = A.fit_linear(A.ram_steps_fragment)
assert (ram_a, ram_b) == (4, 25)


def ks(w, p, c):
    P, rows, x = A.knapsack_table(w, p, c)
    assert P[(1, c)] == A.knapsack_brute(w, p, c)
    optimal_sets = [bits for bits in itertools.product([0, 1], repeat=len(w))
                    if sum(b * v for b, v in zip(bits, w)) <= c
                    and sum(b * v for b, v in zip(bits, p)) == P[(1, c)]]
    return P, rows, x, optimal_sets


fm_P, fm_rows, fm_x, fm_opt = ks([3, 4, 6, 3], [6, 12, 8, 2], 10)
wb_P, wb_rows, wb_x, wb_opt = ks([4, 3, 5, 2], [10, 8, 9, 16], 10)
assert len(fm_opt) == 2 and len(wb_opt) == 1


def mcm(p):
    m, s, working = A.matrix_chain(p)
    n = len(p) - 1
    assert A.unique_minimum(working)
    return m[1][n], A.parens(s, 1, n), A.tables_as_dict(m, s, n), {
        f"{i},{j}": [f"k={k}: {qv}" for k, qv in opts] for (i, j), opts in working.items()}


fm_cost, fm_par, fm_tab, fm_work = mcm([2, 5, 3, 10, 4])
wb_cost, wb_par, wb_tab, wb_work = mcm([2, 3, 4, 5, 10])
clrs_cost, clrs_par, _, _ = mcm([30, 35, 15, 5, 10, 20, 25])
assert (clrs_cost, clrs_par) == (15125, "((A1(A2A3))((A4A5)A6))")  # lecture slide 47

digits = {"0": 121, "1": 50, "2": 203, "3": 401, "4": 8, "5": 195}
hf_codes, hf_bits, hf_merges, hf_ties = A.huffman(digits)
sf_codes, sf_bits, sf_ties = A.shannon_fano(digits)
H, H_total = A.entropy_bits(digits)
assert not hf_ties and not sf_ties
flc_bits = 3 * sum(digits.values())


def dfs(adj, order):
    color = {u: "W" for u in order}
    d, f, parent = {}, {}, {}
    t = [0]

    def visit(u):
        color[u] = "G"
        t[0] += 1
        d[u] = t[0]
        for v in adj[u]:
            if color[v] == "W":
                parent[v] = u
                visit(v)
        color[u] = "B"
        t[0] += 1
        f[u] = t[0]

    for u in order:
        if color[u] == "W":
            visit(u)
    return d, f, parent


fm_graph = {"a": ["b", "e"], "b": ["a", "c", "d"], "c": ["b"], "d": ["b"], "e": ["a", "f"], "f": ["e"]}
dfs_d, dfs_f, dfs_pi = dfs(fm_graph, ["a", "b", "c", "d", "e", "f"])

# ------------------------------------------------------------------ T1: Test 01 model paper
q("T1", "Q1", "1", 2, "L01", "Properties of a good algorithm", "recall", "D11-warm-up-recall",
  "List two properties of good algorithm.",
  "Any two of the lecture's list: be correct; be unambiguous; give the correct solution for all cases; be simple; must terminate.",
  repeats=["FM-Q1.1"],
  note="Flaw: T1 heads Question One '(10 Marks)' but its printed part marks add to 20 (and the paper total is 20).")
q("T1", "Q1", "2", 2, "L01", "Purpose of analysis", "explain", "D11-warm-up-recall",
  "What is the main purpose of analysis of algorithms?",
  "To predict resource usage (mainly running time, also memory) as the input grows, so algorithms can be compared and their growth of run time predicted independently of hardware.",
  repeats=["FM-Q1.2"])
q("T1", "Q1", "3", 3, "L01", "RAM-model step count", "count", "D7-ram-step-count",
  "Analyze the running time of the following program fragment assuming a RAM model of computation.\n  j <- 0\n  for i <- 0 to n\n     while j <= 5\n        j <- j + 1",
  f"With the slide-23 convention (1 step per assignment/comparison/addition; 'for i <- 0 to n' costs (n+2) assignments, (n+2) comparisons, (n+1) additions): j<-0 = 1; for control = 3n+5; while tests = 7 (when i = 0) + n (once per later i) = n+7; body runs 6 times in total = 12. T(n) = {ram_a}n + {ram_b} = O(n).",
  trap="j is set to 0 once, outside the for loop, so the while body runs only while i = 0 (6 times in total); later iterations do one failing test. Students who multiply 6 by (n+1) get the wrong count; the order is still linear.",
  repeats=["FM-Q1.3"], note="Lecture slides 24 and 25 show both versions (j reset inside the loop vs outside): the lecturer tests whether students notice where the initialisation sits.")
q("T1", "Q1", "4", 2, "L02", "Insertion sort best/worst case", "explain", "D5-best-worst-case",
  "What are the best case and worst case running time (in Big O notation) of the insertion sorting algorithm? When do you get such situations?",
  "Best case O(n): input already sorted (the while test fails at once for every j). Worst case O(n^2): input in reverse order (every key is shifted past all earlier elements).",
  repeats=["FM-Q1.4"])
q("T1", "Q1", "5", 3, "L02", "Insertion sort trace", "trace", "D1-illustrate-given-algorithm",
  "Illustrate the operations of the Insertion sort algorithm for A = [10, 0, 8, 4] (assign the values only once to the given algorithm codes, then use a diagrammatic way). INSERTION-SORT pseudo-code is printed with the question.",
  "; ".join(f"j={s['j']}, key={s['key']}, shifts={s['shifts']} -> {s['array']}" for s in ins),
  given={"A": [10, 0, 8, 4], "algorithm": "INSERTION-SORT (lecture, 1-based)"}, repeats=["FM-Q1.5"])
q("T1", "Q1", "6", 2, "L02", "Big-O of a sum of terms", "justify-order", "D6-asymptotic-order",
  "Find the Big oh value for (a) T(n) = log n + n + 100, (b) T(n) = 200n^20 + 100n^10 + 2^n + 3^n + n + 1. Justify your answer.",
  "(a) O(n): n dominates log n and the constant (T(n) <= 3n for n >= 100). (b) O(3^n): 3^n grows faster than 2^n and any polynomial; coefficients 200, 100 are irrelevant (T(n)/3^n -> 1).",
  trap="(b) Students pick n^20 because of the big coefficient, or 2^n because it is the first exponential they see.",
  repeats=["FM-Q1.6"])
q("T1", "Q1", "7a", 6, "L03", "Recursive relation with initial condition", "model-recursion", "D3-model-recursive-definition",
  "pow(x, n) = x^n = x * x^(n-1). Write a recursive relation for pow(x, n) (n non-negative integer). Clearly define the initial condition(s).",
  "pow(x, n) = 1 if n = 0 (initial condition); pow(x, n) = x * pow(x, n-1) if n > 0.",
  repeats=["FM-Q1.7a"], note="7a-7c share one printed total of 6 marks (stored on 7a).")
q("T1", "Q1", "7b", None, "L03", "Recursive pseudo-code", "write-pseudocode", "D3-model-recursive-definition",
  "Write a recursive algorithm in pseudo code for the above recursive relation.",
  "POW(x, n)\n1 if n = 0\n2    then return 1\n3    else return x * POW(x, n - 1)",
  repeats=["FM-Q1.7b"])
q("T1", "Q1", "7c", None, "L03", "Recurrence for running time", "write-recurrence", "D3-model-recursive-definition",
  "Write a recurrence equation that describes the running time T(n) of the part (b) algorithm.",
  "T(0) = c1; T(n) = T(n-1) + c2 for n > 0 (one test, one multiplication, one return per call). Solving by repeated substitution: T(n) = c1 + n*c2 = O(n).",
  repeats=["FM-Q1.7c"])
q("T1", "Q2", "a", 3, "L04", "Quicksort with Lomuto partition trace", "trace", "D1-illustrate-given-algorithm",
  "QUICKSORT / PARTITION (x <- A[r]) are given. Illustrate the operations of QUICKSORT(A, p, r) for A = [28, 15, 1, 30, 0, 8].",
  " | ".join(f"PARTITION(A,{c['p']},{c['r']}) pivot {c['pivot']} -> q={c['q']}, A={c['array']}" for c in qs_calls) + f" | sorted {qs_out}",
  given={"A": [28, 15, 1, 30, 0, 8], "partition": "Lomuto, pivot = A[r]"}, repeats=["FM-Q2.a"],
  trap="The pivot is the LAST element (8), not the first; indices are 1-based. Sub-arrays of size 1 or 0 make no PARTITION call.")
q("T1", "Q2", "b", 2, "L04", "Quicksort best/worst partitioning", "explain", "D5-best-worst-case",
  "What kinds of partitioning generate the best or worst case of quicksort?",
  "Best: every PARTITION splits the array into two halves of (about) n/2 each -> O(n lg n). Worst: every split is 0 and n-1 elements (e.g. already sorted input with pivot = A[r]) -> O(n^2).",
  repeats=["FM-Q2.b"])
q("T1", "Q2", "c", None, "L04", "Best-case recurrence", "write-recurrence", "D3-model-recursive-definition",
  "Write recurrence equations for the best case.",
  "T(1) = c; T(n) = 2T(n/2) + cn for n > 1 (two half-size calls plus linear PARTITION).",
  repeats=["FM-Q2.c"], note="c and d share one printed total of 5 marks (stored on d).")
q("T1", "Q2", "d", 5, "L04", "Repeated substitution", "solve-recurrence", "D4-solve-recurrence",
  "Use the repeated substitution method to solve the best case recurrence equation.",
  "T(n) = 2T(n/2) + cn = 4T(n/4) + 2cn = 8T(n/8) + 3cn = ... = 2^k T(n/2^k) + k*cn. Put n = 2^k (k = lg n): T(n) = nT(1) + cn lg n = cn + cn lg n = O(n lg n).",
  repeats=["FM-Q2.d"])

# ------------------------------------------------------------------ FM: final model paper
# Q1 and Q2 of FM are verbatim copies of T1 (recorded so recycling is visible).
for rec in [r for r in R if r["source"] == "T1"]:
    copy = dict(rec)
    copy["source"] = "FM"
    copy["id"] = "FM-" + rec["id"][3:]
    copy["repeats"] = [rec["id"]]
    copy["note"] = "Verbatim repeat of the Test 01 model paper." + (" " + rec["note"] if rec["note"] else "")
    R.append(copy)

q("FM", "Q3", "1", 2, "L05", "Tree terminology", "define", "D11-warm-up-recall",
  "Briefly describe (a) leaf node, (b) binary tree.",
  "(a) A node with no children. (b) A tree in which every node has at most two children (left and right).",
  note="Question three is printed twice in the paper (once as 'Question One' with items 7-12).")
q("FM", "Q3", "2", 2, "L05", "Full binary tree node count", "prove", "D8-verify-or-prove-property",
  "Prove that for a full binary tree with n nodes and height h, n + 1 = 2^(h+1).",
  "A full binary tree has 2^i nodes on level i (i = 0..h). n = sum_{i=0..h} 2^i = 2^(h+1) - 1 (geometric series), so n + 1 = 2^(h+1).")
q("FM", "Q3", "3", 6, "L05", "Heapsort trace", "trace", "D1-illustrate-given-algorithm",
  "Illustrate the operations of Heap sort for A = [45, 25, 15, 85, 75, 65, 35, 55] (algorithms HEAPSORT, BUILD_HEAP, HEAPIFY at the end of the paper).",
  "BUILD_HEAP (i = 4..1): " + " -> ".join(str(s["array"]) for s in hs["build_steps"]) + f"; heap = {hs['heap']}. Extraction: " + " -> ".join(f"i={s['i']}: {s['array']}" for s in hs["extract_steps"]),
  given={"A": [45, 25, 15, 85, 75, 65, 35, 55]},
  trap="BUILD_HEAP starts at i = floor(n/2) = 4 and goes DOWN to 1; it is not 8 successive insertions. After each exchange heap_size shrinks, so sorted tail elements are never compared again.")
q("FM", "Q3", "4", 2, "L05", "Max-heap check", "verify", "D8-verify-or-prove-property",
  "Is <23, 17, 14, 6, 13, 10, 1, 5, 7, 12> a max heap? Justify your answer.",
  "No. A[4] = 6 has right child A[9] = 7 > 6, violating A[parent(i)] >= A[i]. Every other parent-child pair satisfies the property.",
  trap="The top three levels look perfect; the single violation is at the bottom (index 4 vs 9). Students who only check the root say 'yes'.")
q("FM", "Q3", "5-6", None, "L05", "Priority queue heap type", "justify-choice", "D10-choose-and-justify",
  "CPU scheduling uses a priority queue where a higher number means higher priority. What type of heap should implement it?",
  "A max-heap: the highest-priority (largest number) process is always at the root, so EXTRACT-MAX gives the next process in O(lg n).",
  trap="Students associate 'priority 1 = first' and answer min-heap; the stem says high number = high priority.",
  note="Marks not printed; the statement and the question are split across items 5 and 6.")
q("FM", "Q4", "1", 1, "none", "Draw a directed graph from (V, E)", "draw", "D11-warm-up-recall",
  "Draw the directed graph with V = {1,2,3,4,5}, E = {(1,2),(2,3),(3,4),(3,5),(5,4),(3,2)}.",
  "Arrows 1->2, 2->3, 3->2 (a 2-cycle between 2 and 3), 3->4, 3->5, 5->4.",
  note="Graph representation/DFS is not in the nine lecture decks; graph vocabulary is reused in L07 (spanning trees).")
q("FM", "Q4", "2", 3, "none", "Graph representations", "compare", "D10-choose-and-justify",
  "Briefly explain the two methods to represent a graph. Which suits a sparse graph? Justify.",
  "Adjacency matrix: |V| x |V| array, entry 1 (or the weight) if (u,v) in E; Theta(V^2) space. Adjacency list: an array of |V| lists holding each vertex's neighbours; Theta(V + E) space. Sparse graph (|E| much less than |V|^2): adjacency list, because it stores only existing edges.")
q("FM", "Q4", "3", 6, "none", "DFS trace", "trace", "D1-illustrate-given-algorithm",
  "Illustrate DFS on the given graph (edges a-b, a-e, e-f, b-c, b-d) starting at a, using DFS/DFS-VISIT from the end of the paper.",
  "With alphabetical adjacency lists: " + ", ".join(f"{u} {dfs_d[u]}/{dfs_f[u]}" for u in "abcdef") + "; tree edges " + ", ".join(f"({p},{v})" for v, p in dfs_pi.items()) + ".",
  note="Flaw: adjacency-list order is not stated, so several discovery orders are defensible. Topic is outside the nine lectures.")
q("FM", "C", "1", 2, "L08", "Fixed-length coding", "define", "D11-warm-up-recall",
  "What is meant by fixed length coding in data representation? Give one example.",
  "Every symbol gets a codeword of the same length (ceil(log2 n) bits for n symbols). Examples: ASCII (8 bits), Unicode (16 bits).",
  note="This 12-mark compression section has no question number in the paper; its parts are lettered e-h.")
q("FM", "C", "2", 4, "L08", "Huffman code construction", "trace", "D1-illustrate-given-algorithm",
  "Digits 0-5 have frequencies 121, 50, 203, 401, 8, 195. Construct the codewords with the Huffman algorithm given at the end of the paper.",
  "Merges: " + ", ".join(f"{a}+{b}={c}" for a, b, c in hf_merges) + ". Codes (left/0 = first EXTRACT-MIN): " + ", ".join(f"{k}:{hf_codes[k]}" for k in sorted(hf_codes)) + ".",
  given={"frequencies": digits})
q("FM", "C", "3", 1, "L08", "Total bits", "compute", "D9-read-off-own-construction",
  "How many bits are needed to represent the digits in the file?",
  f"Huffman: sum f*len = {hf_bits} bits (fixed-length would need 3 x {sum(digits.values())} = {flc_bits}; entropy bound {H:.3f} bits/symbol = {H_total:.1f} bits).",
  trap="Students give the bits per codeword, or use the fixed-length total.")
q("FM", "C", "4", 4, "L08", "Shannon-Fano construction", "trace", "D1-illustrate-given-algorithm",
  "Construct the codewords for the same data using the Shannon-Fano algorithm.",
  "Sorted 3,2,5,0,1,4 (401,203,195,121,50,8). Splits: {3}|{2,5,0,1,4} (401 vs 577), {2}|{5,0,1,4}, {5}|{0,1,4}, {0}|{1,4}, {1}|{4}. Codes: " + ", ".join(f"{k}:{sf_codes[k]}" for k in sorted(sf_codes)) + f"; total {sf_bits} bits.",
  note="Flaw: the paper says the Shannon-Fano algorithm is 'at the end of the paper (page 16)' but the appendix does not contain it.")
q("FM", "C", "5", 1, "L08", "Which code is optimal", "justify-choice", "D9-read-off-own-construction",
  "Which codeword is optimal out of the codewords constructed by Huffman and Shannon-Fano?",
  f"Both cost {hf_bits} bits for this file, so both are optimal here. In general only Huffman is guaranteed optimal; Shannon-Fano can be worse.",
  trap="Students answer 'Huffman' without computing; for this data the two totals are equal.")
q("FM", "Q5", "1", 1, "L09", "Optimal substructure", "define", "D11-warm-up-recall",
  "What is meant by optimal substructure in Dynamic Programming?",
  "A problem has optimal substructure when an optimal solution contains within it optimal solutions to its sub-problems.")
q("FM", "Q5", "2", 8, "L09", "0/1 knapsack table from P(i,k)", "fill-table", "D2-dp-table-from-given-recurrence",
  "Construct a table for the 0/1 knapsack problem n = 4, c = 10, w = [3, 4, 6, 3], p = [6, 12, 8, 2] using the recursive solution given at the end of the paper.",
  "Rows i = 4..1, columns k = 0..10: " + "; ".join(f"i={i}: {fm_rows[i]}" for i in fm_rows) + f". P(1,10) = {fm_P[(1, 10)]}.",
  given={"n": 4, "c": 10, "w": [3, 4, 6, 3], "p": [6, 12, 8, 2]})
q("FM", "Q5", "3", 2, "L09", "Read P(i,k) values", "read-off", "D9-read-off-own-construction",
  "Find P(3,9) and P(1,10) using the recursive equations.",
  f"P(3,9) = max(P(4,9), 8 + P(4,3)) = max(2, 8 + 2) = {fm_P[(3, 9)]}. P(1,10) = max(P(2,10), 6 + P(2,7)) = max({fm_P[(2, 10)]}, 6 + {fm_P[(2, 7)]}) = {fm_P[(1, 10)]}.",
  trap="P(i,k) uses items i..n (the suffix). P(3,9) may use only items 3 and 4; students who use items 1..3 get 18.")
q("FM", "Q5", "4", 2, "L09", "Trace back the chosen items", "explain", "D9-read-off-own-construction",
  "Briefly explain how you achieved the final solution.",
  "Start at P(1,10); for each i, if P(i,k) = P(i+1,k) item i is left out, otherwise it is taken and k drops by w_i. Optimal subsets: " + "; ".join(str([i + 1 for i, b in enumerate(s) if b]) for s in fm_opt) + f" (both profit {fm_P[(1, 10)]}).",
  note="Flaw: this instance has TWO optimal subsets because P(1,10) ties (20 = 6 + 14). A mock instance must have a unique optimum.")
q("FM", "Q5", "5", 7, "L09", "Matrix-chain m and s tables", "fill-table", "D2-dp-table-from-given-recurrence",
  "A1..A4 have dimensions 2x5, 5x3, 3x10, 10x4. Draw the m and s tables, then give the optimal parenthesization and the optimal number of scalar multiplications.",
  f"p = [2,5,3,10,4]. m: {fm_tab['m']}; s: {fm_tab['s']}. Optimal {fm_par} with {fm_cost} scalar multiplications.",
  given={"p": [2, 5, 3, 10, 4]},
  trap="The cost term is p(i-1)*p(k)*p(j); using p(i) shifts every product. s[i,j] stores the k of the minimum, not the minimum.")

# ------------------------------------------------------------------ WB: whiteboard
q("WB", "1", "", None, "L09", "Matrix-chain optimal parenthesization", "fill-table", "D2-dp-table-from-given-recurrence",
  "Find the optimal parenthesization for p0 = 2, p1 = 3, p2 = 4, p3 = 5, p4 = 10 using dynamic programming.",
  f"m: {wb_tab['m']}; s: {wb_tab['s']}. Optimal {wb_par}, {wb_cost} scalar multiplications. Working: {wb_work}.",
  given={"p": [2, 3, 4, 5, 10]}, repeats=["FM-Q5.5"],
  note="The lecturer's own signal for the exam: dimensions given directly as p0..p4, not as matrix sizes.")
q("WB", "2", "", None, "L09", "0/1 knapsack by DP", "fill-table", "D2-dp-table-from-given-recurrence",
  "0/1 knapsack: W = [4, 3, 5, 2], P = [10, 8, 9, 16], capacity = 10.",
  "Rows i = 4..1, columns k = 0..10: " + "; ".join(f"i={i}: {wb_rows[i]}" for i in wb_rows) + f". P(1,10) = {wb_P[(1, 10)]}; take items " + str([i + 1 for i, b in enumerate(wb_x) if b]) + " (weight 9, profit 34; unique optimum).",
  given={"w": [4, 3, 5, 2], "p": [10, 8, 9, 16], "c": 10}, repeats=["FM-Q5.2"])

# ------------------------------------------------------------------ checks and summary
ids = [r["id"] for r in R]
assert len(ids) == len(set(ids)), "duplicate ids"
for r in R:
    for rid in r["repeats"]:
        assert rid in ids, (r["id"], rid)

final_like = [r for r in R if r["source"] == "FM" and r["marks"]]
summary = {
    "records": len(R),
    "by_source": dict(Counter(r["source"] for r in R)),
    "by_lecture": dict(sorted(Counter(r["lecture"] for r in R).items())),
    "by_final_q": dict(Counter(str(r["final_q"]) for r in R)),
    "by_archetype": dict(sorted(Counter(r["archetype"] for r in R).items())),
    "by_skill": dict(Counter(r["skill"] for r in R).most_common()),
    "fm_marks_by_lecture": dict(sorted(Counter({k: 0 for k in []}).items())),
    "traps": sum(1 for r in R if r["trap"]),
}
marks = Counter()
for r in final_like:
    marks[r["lecture"]] += r["marks"]
summary["fm_marks_by_lecture"] = dict(sorted(marks.items()))
summary["fm_marks_total"] = sum(marks.values())

doc = {
    "module": "SE2022 Design and Analysis of Algorithms",
    "lecturer_model": "see LECTURER_PROFILE.md in the same folder",
    "sources": SRC,
    "announced_final_format": FORMAT,
    "fields": ["id", "source", "question", "part", "marks", "lecture", "final_q", "topic", "skill",
               "archetype", "trap", "given", "text", "answer", "repeats", "note"],
    "summary": summary,
    "questions": R,
}
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(doc, fh, indent=1, ensure_ascii=False)
print(json.dumps(summary, indent=1))
