"""Reference implementations that follow the SE2022 lecture pseudo-code exactly.

Every function returns a trace so the bank can show *how* an answer is reached,
not only the final value. Arrays are handled 1-based internally (index 0 unused)
to match the lecture algorithms.
"""
import heapq
import itertools
import math


# ---------- L02 insertion sort (lecture pseudo-code, 1-based) ----------
def insertion_sort_trace(a):
    A = [None] + list(a)
    states = []
    for j in range(2, len(A)):
        key = A[j]
        i = j - 1
        shifts = 0
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
            shifts += 1
        A[i + 1] = key
        states.append({"j": j, "key": key, "shifts": shifts, "array": A[1:]})
    return states


# ---------- L04 quicksort with Lomuto PARTITION (x <- A[r]) ----------
def quicksort_trace(a):
    A = [None] + list(a)
    calls = []

    def partition(p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def qs(p, r):
        if p < r:
            pivot = A[r]
            q = partition(p, r)
            calls.append({"p": p, "r": r, "pivot": pivot, "q": q, "array": A[1:]})
            qs(p, q - 1)
            qs(q + 1, r)

    qs(1, len(A) - 1)
    return calls, A[1:]


# ---------- L05 heaps (HEAPIFY / BUILD_HEAP / HEAPSORT, max-heap) ----------
def heapsort_trace(a):
    A = [None] + list(a)
    n = len(a)
    size = [n]
    swaps = []

    def heapify(i):
        l, r = 2 * i, 2 * i + 1
        largest = l if (l <= size[0] and A[l] > A[i]) else i
        if r <= size[0] and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            swaps.append((i, largest))
            heapify(largest)

    build = []
    for i in range(n // 2, 0, -1):
        heapify(i)
        build.append({"i": i, "array": A[1:]})
    heap = A[1:]
    extract = []
    for i in range(n, 1, -1):
        A[1], A[i] = A[i], A[1]
        size[0] -= 1
        heapify(1)
        extract.append({"i": i, "array": A[1:], "heap_size": size[0]})
    return {"build_steps": build, "heap": heap, "extract_steps": extract, "sorted": A[1:]}


def max_heap_violations(seq):
    A = [None] + list(seq)
    n = len(seq)
    bad = []
    for i in range(1, n // 2 + 1):
        for c in (2 * i, 2 * i + 1):
            if c <= n and A[c] > A[i]:
                bad.append({"parent_index": i, "parent": A[i], "child_index": c, "child": A[c]})
    return bad


# ---------- L01 RAM-model step count (lecture convention, slide 23) ----------
def ram_steps_fragment(n):
    """j<-0; for i<-0 to n; while j<=5; j<-j+1.
    Counts as on the lecture slide: 1 step per assignment, comparison, addition;
    a for loop i<-0 to n costs (n+2) assignments, (n+2) comparisons, (n+1) additions."""
    steps = 1  # j <- 0
    steps += (n + 2) + (n + 2) + (n + 1)  # for-loop control
    j = 0
    for _ in range(n + 1):
        while True:
            steps += 1  # comparison j <= 5
            if not j <= 5:
                break
            j += 1
            steps += 2  # addition + assignment
    return steps


def fit_linear(f, ns=(0, 1, 2, 10, 50)):
    a = f(1) - f(0)
    b = f(0)
    assert all(f(n) == a * n + b for n in ns)
    return a, b


# ---------- L09 0/1 knapsack, lecture recursion P(i,k) on items i..n ----------
def knapsack_table(w, p, c):
    n = len(w)
    P = {}
    for i in range(n, 0, -1):
        for k in range(0, c + 1):
            wi, pi = w[i - 1], p[i - 1]
            if i == n:
                P[(i, k)] = 0 if wi > k else pi
            elif wi > k:
                P[(i, k)] = P[(i + 1, k)]
            else:
                P[(i, k)] = max(P[(i + 1, k)], pi + P[(i + 1, k - wi)])
    # trace-back of the chosen items from P(1,c)
    x, k = [], c
    for i in range(1, n + 1):
        if i == n:
            take = 1 if w[i - 1] <= k else 0
        else:
            take = 1 if P[(i, k)] != P[(i + 1, k)] else 0
        x.append(take)
        if take:
            k -= w[i - 1]
    rows = {i: [P[(i, k)] for k in range(c + 1)] for i in range(n, 0, -1)}
    return P, rows, x


def knapsack_brute(w, p, c):
    best = 0
    for bits in itertools.product([0, 1], repeat=len(w)):
        if sum(b * x for b, x in zip(bits, w)) <= c:
            best = max(best, sum(b * x for b, x in zip(bits, p)))
    return best


# ---------- L09 matrix-chain order ----------
def matrix_chain(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    working = {}
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = math.inf
            options = []
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                options.append((k, q))
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
            working[(i, j)] = options
    return m, s, working


def parens(s, i, j):
    if i == j:
        return f"A{i}"
    return "(" + parens(s, i, s[i][j]) + parens(s, s[i][j] + 1, j) + ")"


def tables_as_dict(m, s, n):
    return {
        "m": {f"{i},{j}": m[i][j] for i in range(1, n + 1) for j in range(i, n + 1)},
        "s": {f"{i},{j}": s[i][j] for i in range(1, n + 1) for j in range(i + 1, n + 1)},
    }


def unique_minimum(working):
    """True when every m[i,j] has a single minimising k (so s is unambiguous)."""
    for opts in working.values():
        best = min(q for _, q in opts)
        if sum(1 for _, q in opts if q == best) > 1:
            return False
    return True


# ---------- L08 Huffman (lecture HUFFMAN(C): left = first EXTRACT-MIN = 0) ----------
def huffman(freq):
    counter = itertools.count()
    heap = [(f, next(counter), sym) for sym, f in freq.items()]
    heapq.heapify(heap)
    merges = []
    ties = False
    while len(heap) > 1:
        f1, _, x = heapq.heappop(heap)
        f2, _, y = heapq.heappop(heap)
        if heap and heap[0][0] == f2:
            ties = True
        merges.append((f1, f2, f1 + f2))
        heapq.heappush(heap, (f1 + f2, next(counter), (x, y)))
    codes = {}

    def walk(node, code):
        if isinstance(node, tuple):
            walk(node[0], code + "0")
            walk(node[1], code + "1")
        else:
            codes[node] = code or "0"

    walk(heap[0][2], "")
    total = sum(freq[s] * len(codes[s]) for s in freq)
    return codes, total, merges, ties


# ---------- L08 Shannon-Fano (lecture: sort by falling frequency, split to most equal halves) ----------
def shannon_fano(freq):
    items = sorted(freq.items(), key=lambda kv: -kv[1])
    codes = {s: "" for s, _ in items}
    ties = []

    def split(group):
        if len(group) == 1:
            return
        total = sum(f for _, f in group)
        diffs = []
        run = 0
        for cut in range(1, len(group)):
            run += group[cut - 1][1]
            diffs.append((abs(total - 2 * run), cut))
        best = min(d for d, _ in diffs)
        cuts = [c for d, c in diffs if d == best]
        if len(cuts) > 1:
            ties.append([s for s, _ in group])
        cut = cuts[0]
        for s, _ in group[:cut]:
            codes[s] += "0"
        for s, _ in group[cut:]:
            codes[s] += "1"
        split(group[:cut])
        split(group[cut:])

    split(items)
    total = sum(freq[s] * len(codes[s]) for s in freq)
    return codes, total, ties


def entropy_bits(freq):
    n = sum(freq.values())
    h = -sum(f / n * math.log2(f / n) for f in freq.values())
    return h, h * n


# ---------- L04 merge sort (MERGE algorithm 2, sentinels) ----------
def mergesort_trace(a):
    A = [None] + list(a)
    merges = []

    def merge(p, q, r):
        L = A[p:q + 1] + [math.inf]
        R = A[q + 1:r + 1] + [math.inf]
        i = j = 0
        for k in range(p, r + 1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        merges.append({"p": p, "q": q, "r": r, "array": A[1:]})

    def ms(l, r):
        if l < r:
            q = (l + r) // 2
            ms(l, q)
            ms(q + 1, r)
            merge(l, q, r)

    ms(1, len(a))
    return merges, A[1:]


# ---------- L06 naive matcher (comparisons left to right, stop at first mismatch) ----------
def naive_match(T, P):
    n, m = len(T), len(P)
    valid, comps, per_shift = [], 0, []
    for s in range(0, n - m + 1):
        c = 0
        ok = True
        for i in range(m):
            c += 1
            if T[s + i] != P[i]:
                ok = False
                break
        comps += c
        per_shift.append(c)
        if ok:
            valid.append(s)
    return {"valid_shifts": valid, "comparisons": comps, "per_shift": per_shift,
            "shifts_tried": n - m + 1}


# ---------- L06 Rabin-Karp (radix d, modulus q, rolling hash) ----------
def rabin_karp(T, P, q, d=10):
    n, m = len(T), len(P)
    digits_T = [int(ch) for ch in T]
    digits_P = [int(ch) for ch in P]
    h = pow(d, m - 1, q)
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + digits_P[i]) % q
        t = (d * t + digits_T[i]) % q
    windows, valid, spurious = [], [], []
    for s in range(0, n - m + 1):
        windows.append(t)
        assert t == int(T[s:s + m]) % q
        if t == p:
            (valid if T[s:s + m] == P else spurious).append(s)
        if s < n - m:
            t = (d * (t - digits_T[s] * h) + digits_T[s + m]) % q
    return {"p_mod": p, "h": h, "windows": windows, "valid": valid, "spurious": spurious}


# ---------- L06 string-matching automaton ----------
def fa_table(P, sigma):
    m = len(P)
    delta = {}
    for qs in range(m + 1):
        for a in sigma:
            k = min(m, qs + 1)
            while k > 0 and not (P[:qs] + a).endswith(P[:k]):
                k -= 1
            delta[(qs, a)] = k
    return delta


def fa_run(delta, T, m):
    state, states, ends = 0, [0], []
    for i, a in enumerate(T, start=1):
        state = delta[(state, a)]
        states.append(state)
        if state == m:
            ends.append(i)
    return states, ends


# ---------- L07 greedy graph algorithms (ties broken alphabetically, stated in every question) ----------
def kruskal(vertices, edges):
    """edges: list of (w, u, v) undirected. Ties: by (w, u, v) after sorting u<v."""
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    E = sorted((w, min(u, v), max(u, v)) for w, u, v in edges)
    ties = len({w for w, _, _ in E}) != len(E)
    steps, total = [], 0
    for w, u, v in E:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
            total += w
            action = "merge"
        else:
            action = "reject"
        groups = {}
        for x in vertices:
            groups.setdefault(find(x), []).append(x)
        steps.append({"edge": (u, v), "w": w, "action": action,
                      "sets": sorted(sorted(g) for g in groups.values())})
    return steps, total, ties


def prim(vertices, edges, root):
    adj = {v: {} for v in vertices}
    for w, u, v in edges:
        adj[u][v] = w
        adj[v][u] = w
    in_tree = {root}
    steps, total = [], 0
    while len(in_tree) < len(vertices):
        cands = sorted((w, u, v) for u in in_tree for v, w in adj[u].items() if v not in in_tree)
        best = cands[0]
        tie = len(cands) > 1 and cands[1][0] == best[0]
        in_tree.add(best[2])
        total += best[0]
        steps.append({"candidates": [(u, v, w) for w, u, v in cands], "chosen": (best[1], best[2], best[0]), "tie": tie})
    return steps, total


def dijkstra(vertices, arcs, s):
    """arcs: list of (u, v, w) directed. Returns the lecture's table rows."""
    INF = math.inf
    d = {v: INF for v in vertices}
    pi = {v: None for v in vertices}
    d[s] = 0
    S, rows = [], []
    Q = set(vertices)
    adj = {v: [] for v in vertices}
    for u, v, w in arcs:
        adj[u].append((v, w))
    while Q:
        u = min(sorted(Q), key=lambda x: d[x])
        tie = sum(1 for x in Q if d[x] == d[u]) > 1 and d[u] != INF
        Q.remove(u)
        S.append(u)
        for v, w in adj[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                pi[v] = u
        rows.append({"marked": u, "d": dict(d), "unmarked": sorted(Q), "tie": tie})
    return rows, d, pi


# ---------- L08 Hu-Tucker (lecture rules: join only pairs not separated by a leaf; leftmost on ties) ----------
def hu_tucker(symbols, weights):
    nodes = [{"w": w, "leaf": True, "syms": [s]} for s, w in zip(symbols, weights)]
    depth = {s: 0 for s in symbols}
    joins = []
    while len(nodes) > 1:
        best = None
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                if any(nodes[k]["leaf"] for k in range(i + 1, j)):
                    break
                key = (nodes[i]["w"] + nodes[j]["w"], i, j)
                if best is None or key < best:
                    best = key
        w, i, j = best
        for s in nodes[i]["syms"] + nodes[j]["syms"]:
            depth[s] += 1
        joins.append(("+".join(nodes[i]["syms"]), "+".join(nodes[j]["syms"]), w))
        merged = {"w": w, "leaf": False, "syms": nodes[i]["syms"] + nodes[j]["syms"]}
        nodes = nodes[:i] + [merged] + nodes[i + 1:j] + nodes[j + 1:]
    # alphabetic codes from the levels
    codes, code, prev = {}, None, None
    for s in symbols:
        L = depth[s]
        if code is None:
            code = 0
        else:
            code += 1
            code = code << (L - prev) if L >= prev else code >> (prev - L)
        codes[s] = format(code, f"0{L}b")
        prev = L
    return depth, codes, joins


# ---------- L08 Ziv-Lempel as on the slides: (distance back, copy length) or (0, ASCII) ----------
def lz_lecture(text):
    out, i = [], 0
    while i < len(text):
        best_len, best_dist = 0, 0
        for start in range(i - 1, -1, -1):  # nearest first, so ties keep the smallest distance
            L = 0
            while i + L < len(text) and start + L < i and text[start + L] == text[i + L]:
                L += 1
            if L > best_len:
                best_len, best_dist = L, i - start
        if best_len == 0:
            out.append((0, ord(text[i])))
            i += 1
        else:
            out.append((best_dist, best_len))
            i += best_len
    return out
