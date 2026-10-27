# PROMPT — IE2004 (Computer Networks) Final Exam Mock, Real-Exam Format (v2)

Copy everything below the line into Claude Code, run from the root of this repo.

---

## ROLE

You are setting a **mock final exam** for **IE2004 — Computer Networks** (SLIIT, Year 2 Sem 1) in the **format the lecturer announced for the real final**:

> **MCQ:** each question has **TWO correct answers**, with negative marks for incorrect answers. Topics: **all the lessons not covered in the midterm**.
> **Essay / short answer:** **15 questions carrying 2–5 marks each**. Topics: the **entire syllabus**, including the midterm lessons.

This mock doubles the MCQ count to **50** and is **theory-heavy**. The module is theory-based, so most questions must test understanding of how and why networks work: mechanisms, trade-offs, cause and effect, consequences, diagnosis. Some questions still need thinking through a figure, a trace or a short calculation. You are writing questions that a student who has read the slides but not *understood* them will get wrong.

The paper must be **harder than the reference paper in this repo**, but stay strictly within the lecture slides. You produce **one full 100-mark paper** as a single offline exam app.

---

## STEP 0 — READ BEFORE WRITING ANYTHING

All files are in the **repo root** (flat). Quote the names, because they contain spaces and parentheses.

1. **Lecture slides (the only source of truth for scope and rules):**

   | # | File | Pages | In the MCQ section? |
   |---|---|---|---|
   | L01 | `01-Introduction (2).pdf` | 56 | no (midterm) — essays only |
   | L02 | `02-Protocol-architecture.pdf` | 40 | no (midterm) — essays only |
   | L03 | `03-Physical-layer.pdf` | 54 | **yes** |
   | L04 | `04-LANs (3).pdf` | 106 | **yes** |
   | L05 | `05-IP (2).pdf` | 84 | **yes** |
   | L05A | `05A-IPv6 (2).pdf` | 41 | **yes** |
   | L06 | `06-Routing (2).pdf` | 31 | **yes** (listed as "07 - Routing" on the course page) |
   | L07 | `07-Transport (5).pdf` | 92 | no (midterm) — essays only |
   | L08 | `08-Application (4).pdf` | 73 | no (midterm) — essays only |
   | L09 | `09-Network-Programming.pdf` | 28 | **yes** |

   - Extract the text with `pdftotext -layout`, but **do not rely on the text alone**. Much of the teaching is inside slide images: waveforms, timing diagrams, header formats, tables, formulas, worked examples. Render every slide to PNG (`pdftoppm -png -r 60`) and **look at** each slide whose text layer is thin, or that contains a figure, table or worked example. You need them to imitate the lecture style (STEP 6) and to learn the exact conventions (STEP 1).
   - **Everything taught is in scope**, including the WLAN security slides (RSN, PSK, SAE, 802.1X/EAP, 4-way handshake) that come after Lecture 04's References slide. Ignore purely administrative slides (attendance, audience Q&A, "slides prepared by", reference lists).

2. **Reference paper:** `IE2004-Computer Networks (1) (1).pdf`. It is a **scan with no text layer**: render its pages with `pdftoppm -png -r 80` and read the images. It is a real past final (all written questions with lettered sub-parts and marks). It is **too easy**, and it predates the announced MCQ format.
   - **Borrow** for the essay section: the framing (a figure such as a topology or a switched network, followed by sub-parts that each test one step); the kinds of parts it asks (MAC tables after frames, VLAN port configuration, subnet allocation, ARP fields, traceroute, socket counts, TCP sequence/ack numbers, DHCP and DNS exchanges, Python socket code); and marks shown per sub-part.
   - **Do not borrow** its scenarios or numbers: the A–S1–R–S2–B chain; the four-host three-switch tree; 192.168.12.0/22 with 500/200/100 hosts; the 192.168.8.10 / 192.168.8.20 ARP pair; the echo server on port 2000 with ISNs 10000/20000; www.example.com resolved iteratively. Do not reuse lecture exercises verbatim either (e.g. the 223.4.8.0/21 or 172.16.0.0/12 campus exercise, the 2001:db8:1::/48 campus table, "C sends to I" on the multi-switch slide). **New scenarios and new numbers only.**

3. **App shell:** if `OOAD_final_mock/index.html` (or `CN_final_mock/index.html`) exists in the repo, study it. It is a finished exam app built to almost the same spec (navigator, flags, timer, keyword auto-marking with tick overrides, results, retry-missed, saved progress, light/dark theme, self-test). **Reuse its architecture and code**, adapted to this spec. Do not reuse its questions.

If a listed file doesn't exist, search the repo, list what you actually found, and confirm with me before generating.

Do **not** write style-notes, audit or report files. Put the effort into the paper.

---

## STEP 1 — SCOPE AND QUALITY RULES

### 1.1 Lecture-only, using the lectures' own conventions

- If a rule, value, formula or behaviour does not appear in the slides, it **cannot be the correct answer**. It may appear as a distractor, and the explanation must say it is outside the lectures.
- **Use the lectures' own conventions, not textbook variants.** Check each of these in the slides (including the images) before writing questions on it, and follow the slides exactly:
  - **L01–L02:** the four delay components and how the slides compute them; throughput and bottleneck links; circuit vs packet switching (datagram vs VC); topologies; PDU names per layer; which layers each device processes; why layering helps; TCP/IP vs OSI
  - **L03:** bit period and bit rate; the **Manchester convention exactly as the slides draw it**; attenuation and NEXT; UTP vs STP and why twisting/shielding helps; SMF vs MMF and dispersion; fibre vs copper; wireless attenuation, multipath and antennas
  - **L04:** the Ethernet frame and MAC addresses; the CSMA/CD steps and binary exponential backoff as listed; collision domains with hubs vs switches; half/full duplex and auto-negotiation; switch self-learning and flooding; VLAN access/trunk ports, the 802.1Q tag, router-on-a-stick; 802.11 BSS/ESS and channels; CSMA/CA, the IFS ordering and values shown, RTS/CTS and the hidden terminal; the four address cases (To DS / From DS); the client state machine, passive vs active scanning, authentication/association; RSN security (what PSK, SAE and 802.1X/EAP each protect against, and the 4-way handshake)
  - **L05:** network-layer functions; the IPv4 header fields; fragmentation (offset = first byte ÷ 8, the MF flag, lengths); subnet arithmetic (usable hosts = 2^h − 2), netmask/prefix, reserved and private ranges, directed vs limited broadcast; the slides' subnet allocation method (largest subnet first); NAT; ICMP and traceroute (TTL); the DHCP message sequence and relay; ARP table and message fields
  - **L05A:** the IPv6 header and what was removed or changed from IPv4 and why; extension headers; no fragmentation by routers; the zero-compression rules; address types and prefixes; global unicast structure; link-local addresses; modified EUI-64 (insert `fffe`, flip the bit) exactly as the slides show; autoconfiguration; the EUI-64 privacy concern and the pseudo-random interface ID; the slides' nibble-based IPv6 subnetting scheme
  - **L06:** routing vs forwarding; routing to another subnet; routing tables; longest prefix match; static vs dynamic routing; autonomous systems
  - **L07:** sockets, port numbers, UDP vs TCP demultiplexing (which tuple identifies a socket); UDP and the Internet checksum (1's complement with wraparound) and why it is weak; TCP sequence/ack numbering, the 3-way handshake, closing, the states, the ACK-generation table, retransmission scenarios, fast retransmit (3 duplicate ACKs), flow control (rwnd), slow start, AIMD, ssthresh, and the Tahoe vs Reno reactions as the slides show
  - **L08:** client-server vs P2P; the transport needs of applications; DNS hierarchy, iterative vs recursive resolution, caching, record types; HTTP non-persistent vs persistent response time in RTTs; HTTP/2 head-of-line blocking; QUIC; message formats and status codes; cookies; web caches
  - **L09:** the Python socket API exactly as Lecture 09 uses it (UDP and TCP clients and servers, `settimeout` and `try/except`)
- Where the slides themselves say something "depends" (e.g. whether a DHCP ACK is broadcast or unicast), **never make that the deciding fact** of a question.

### 1.2 No trivia (hard rule)

The student explicitly does **not** want questions that just test memory of facts that don't help them understand networking. **Never** ask:

- **dates, years or history** ("when was HTTP created", how the Internet evolved, which version came first)
- **names of people, companies or organisations** as the tested point ("which company/body controls IP addresses", who invented Ethernet, which body publishes 802.11)
- **"name the X" lists** with no reasoning ("name the WLAN security methods", "list the 802.11 frame types", "list the ICMP message types")
- **pure lookup values** as the tested point: RFC numbers, standard amendment letters, cable-category speed tables, frequency-band tables, well-known port numbers on their own.

If a question needs such a value to reason with, **give it in the stem**.

Every question must test understanding (why / how / what happens if / what is wrong / which is better here and why), or application (compute, trace, diagnose, design). "WLAN security" is fine as *"which method stops an attacker who captured the 4-way handshake from guessing the passphrase offline, and why"*. It is not fine as *"name the three methods"*.

### 1.3 Theory-heavy balance

- **MCQs:** at least **36 of 50** are **concept** questions (mechanisms, trade-offs, cause and effect, comparing two techniques, consequences of a design choice), each posed through a situation or claims to evaluate, never "what is the definition of". At most **14** are **applied** (a figure to interpret, a trace, or a calculation), and of those **no more than 8** involve arithmetic.
- **Essays:** most marks are for explanation and reasoning. Apart from the two subnetting questions and the code question, at most **6 sub-parts** in the whole essay section may be calculations or traces.

---

## STEP 2 — SECTION A: MCQs (50 questions, 45 marks)

### 2.1 Format and marking (as the real exam)

- Every MCQ has **5 options**, of which **exactly TWO are correct**. The stem says **"Select TWO"**. Inputs are checkboxes.
- Every MCQ is worth **0.9 marks** (50 × 0.9 = 45).
- **Negative marking:** each correct tick earns **+0.45**, and each incorrect tick costs **−0.45**. The question score is clamped to the range **0 to 0.9**. The student may tick any number of options. Ticking a third option shows an inline warning ("Exactly two options are correct — each extra wrong tick costs 0.45"), but the tick is allowed.
- Only the six non-midterm lectures (L03, L04, L05, L05A, L06, L09) appear in this section.

### 2.2 Lecture allocation (exact, weighted by lecture size)

| Lecture | MCQs | Shapes to use (illustrations, not a checklist) |
|---|---|---|
| L03 Physical layer | 8 | Why a higher bit rate shrinks the bit period, and what that does to the signal. Decode a waveform figure under the slides' Manchester convention (this is applied). Why twisting reduces NEXT, and what shielding adds. Choosing UTP, STP, SMF or MMF for a described situation and why. Dispersion as a distance limit. Multipath and attenuation effects on wireless. |
| L04 LANs | 15 | What happens on a collision under CSMA/CD and why backoff grows. Collision domains on a hub/switch figure. A switch's flood/forward decision and table update for a given frame on a figure. Half vs full duplex consequences. What a VLAN isolates and why inter-VLAN traffic needs a router. Access vs trunk and the 802.1Q tag. Router-on-a-stick trade-offs. Why 802.11 avoids rather than detects collisions. Why SIFS is shorter than DIFS. RTS/CTS and the hidden terminal. Which addresses an 802.11 frame carries in a DS case (figure). Passive vs active scanning trade-offs. What PSK, SAE and 802.1X each defend against, and what the 4-way handshake establishes. |
| L05 IPv4 | 12 | Which header fields change per hop and why (TTL and checksum). What happens when TTL reaches 0. Fragmentation consequences: where reassembly happens and what is lost if one fragment is lost. Netmask/prefix effects. Directed vs limited broadcast reach. Why private addresses need NAT, and what NAT breaks. How traceroute learns each hop. The DHCP sequence and why the first messages are broadcast. What a relay agent solves. When ARP is used (same vs different subnet) and which MAC goes where. |
| L05A IPv6 | 6 | Why IPv6 removed the header checksum or fragmentation fields from routers, and the consequences. Valid vs invalid zero compression. Address type from its prefix. Link-local vs global use. Why EUI-64 harms privacy and what replaces it. What autoconfiguration needs from the router. |
| L06 Routing | 5 | Routing vs forwarding (which is per-packet and which builds tables). Longest prefix match on a given table (this is applied). Static vs dynamic trade-offs in a described network. What happens to traffic when no route matches and there is no default. Intra- vs inter-AS reasoning. |
| L09 Network programming | 4 | Read or trace Python socket code: what it prints or does, which line is wrong, what happens on timeout. Why a TCP server uses the socket that `accept()` returns. Why UDP code uses `sendto`/`recvfrom` but TCP code doesn't. What `bind` does on a server vs a client. |

### 2.3 Required forms (spread across the 50, not extra questions)

- ≥ **10** MCQs include a **figure** (STEP 6).
- **5–8** involve a calculation (fragment values, address/broadcast values, bit period/rate, longest-prefix-match decisions). Give every constant needed.
- ≥ **2** contain **Python socket code** (L09).
- ≥ **8** are negated ("Which TWO statements are NOT true", "Which TWO would FAIL", "Which TWO do NOT change").
- ≥ **4** are "**claims by classmates**": five students' statements about a scenario, of which exactly two are correct.
- ≥ **6** combine two of the six MCQ lectures (e.g. ARP + IP forwarding, VLAN + routing, DHCP + IPv4 broadcast, socket code + IP/port addressing, IPv6 autoconfiguration + routing).

### 2.4 Option-design rules (the most important part of Section A)

Earlier attempts failed because the correct answers were the longest, most detailed options and the distractors were throwaways. That is a fatal defect.

1. **Length parity.** Within a question, the longest option is **≤ 1.25×** the shortest (in characters).
2. **Length tell.** Across the 50, the longest option is one of the two correct options in **at most 18**, and the shortest option is one of the two correct options in **at least 18**.
3. **Parallel structure.** All five options share grammatical shape and specificity. If one gives a number, all do; if one gives a reason, all do.
4. **Every distractor is a diagnosed mistake.** Each of the three wrong options is exactly what a student produces after one nameable error. Examples:
   - reads the Manchester transition with the opposite convention
   - forgets the switch floods when its table has no entry
   - thinks a switch separates broadcast domains
   - divides by 1 instead of 8 for the fragment offset
   - counts the network and broadcast addresses as usable
   - thinks a router reassembles fragments
   - thinks ARP resolves the remote host's MAC across a router
   - puts the AP's MAC in the wrong 802.11 address field
   - thinks SAE still allows offline dictionary attacks
   - thinks a UDP server needs `listen()`

   If you can't name the error, rewrite the option.
5. **Two-correct integrity.** Exactly two options are true, independently of each other. The two correct options must not paraphrase each other, and must not be complementary halves of one fact (so picking one doesn't give away the other). A partially true statement is **false**, and its explanation names the false part.
6. **No free eliminations.** No two wrong options may be ruled out by the same single observation, and no option may paraphrase another.
7. **Banned:** "All of the above", "None of the above", "Both A and C".
8. **No absolute-word tell.** Spread "always/never/only/must" and hedges across correct and incorrect options.
9. **No keyword matching.** A question must not be answerable by matching a distinctive stem word to the same word in an option.
10. **Runtime shuffle.** The app shuffles options, so explanations reference **option text, never letters**.

### 2.5 Difficulty

| Tier | Definition | Count |
|---|---|---|
| 1 — Recall-plus | One idea, applied directly, < 40 s (still never trivia, STEP 1.2) | 10 |
| 2 — Applied | 2–3 reasoning steps | 20 |
| 3 — Hard | 4+ steps, two concepts interacting, 1.5–3 min | 20 |

Twist deliberately. Some examples:

- a frame whose destination the switch has already learned on the *same* port it arrived on
- a host on a different VLAN that the student expects to receive a broadcast
- a fragment whose offset looks right but whose MF flag is wrong
- a /26 that fits 62 hosts but not 63
- a NAT box behind a second NAT
- an IPv6 address compressed with `::` in two places
- an RTS/CTS exchange where the hidden station hears only the CTS
- socket code that calls `recv` on the listening socket instead of the accepted one.

Never ask the plain definitional form when an applied one exists.

---

## STEP 3 — SECTION B: Essay / short answer (15 questions, 55 marks)

Fifteen **substantial** questions covering **all 10 lectures** (midterm lessons included), worth **2–5 marks each**: **four × 5 marks, five × 4 marks, three × 3 marks, three × 2 marks** = 55.

- Each question gives a scenario and/or a **figure**, then lettered sub-parts with marks shown (`(2 marks)`), in the reference paper's format.
- Even a 2-mark question must need a reasoned answer (explain + justify, or compare + conclude), **never a one-line definition**.
- Every question has a **final sub-part at Tier 3** (design, diagnose, or predict the effect of a change).
- Volume is not quality: every sub-part tests a distinct idea, and the section is **theory-first** (STEP 1.3).

| Q | Lecture(s) | Marks | Must cover (new scenarios) |
|---|---|---|---|
| **B1** | L01 | 3 | Circuit vs packet switching (datagram vs VC) for a described traffic pattern, with one short delay/throughput reasoning part. |
| **B2** | L02 | 3 | Encapsulation along a **figure path** (host – switch – router – host): which headers exist on each link, which each device reads, and why layering makes this possible. |
| **B3** | L03 | 4 | Medium selection for a described site (attenuation, NEXT, dispersion, interference reasoning), plus one **waveform figure** to read under the slides' Manchester convention. |
| **B4** | L04 | 5 | **Multi-switch self-learning** tables and flood/forward decisions for a given frame order on a figure, then a **VLAN** redesign: access/trunk ports, allowed VLANs, and why inter-VLAN traffic now needs a router. |
| **B5** | L04 | 4 | 802.11: why CSMA/CA, the hidden-terminal problem and RTS/CTS on a figure, the address fields for a DS case, and what a chosen security method (PSK / SAE / 802.1X) defends against. |
| **B6** | L05 | **5** | **IPv4 subnetting** (STEP 4.1). |
| **B7** | L05 | 4 | How a newly connected host gets working (DHCP, then ARP, then an off-subnet ping): which frames are broadcast, the MAC and IP addresses in each, plus **one fragmentation or NAT** part. |
| **B8** | L05A | **5** | **IPv6 subnetting** (STEP 4.2). |
| **B9** | L05A | 2 | Why the IPv6 header drops or moves IPv4 fields (checksum, fragmentation, options), and one consequence for routers or end hosts. |
| **B10** | L06 | 3 | **Longest prefix match** on a router table (figure plus table) for given destinations, and static vs dynamic routing for the scenario. |
| **B11** | L07 | 4 | A **TCP timing diagram** for a given exchange with exact sequence/ack numbers and flags (new ISNs and payload sizes), plus UDP vs TCP demultiplexing reasoning. |
| **B12** | L07 | 4 | Congestion and flow control theory (why slow start, why AIMD, what rwnd protects, Tahoe vs Reno reactions) with **one** short cwnd/ssthresh trace. |
| **B13** | L08 | 2 | DNS iterative vs recursive resolution and the effect of caching, on a figure of servers. |
| **B14** | L08 | 2 | Non-persistent vs persistent HTTP, or HTTP/2 / QUIC and head-of-line blocking: an explanation with a short RTT comparison. |
| **B15** | L09 | **5** | **Write Python socket code** (STEP 5): a TCP or UDP client or server with a stated behaviour, including a timeout and `try/except` or a loop, as Lecture 09 shows. Plus one sub-part explaining a design choice (e.g. why UDP needs the timeout). |

### Answer input types

- **Text** answers (explanations and code) use the **keyword auto-check** (STEP 8.1).
- **Field** answers (any single exact value: a number, an address, a prefix, a flag value, a sequence number, a table cell) use **typed input boxes marked exactly** (STEP 8.2). For example, a MAC-table question gives one box per table entry, and a TCP diagram gives one box per seq/ack value. Use fields wherever the answer is precise; use text only when it is genuinely prose.

---

## STEP 4 — THE TWO SUBNETTING QUESTIONS

Both are in the lectures' campus style: an organisation with several **buildings and functions**, shown on a **campus topology figure** (core router, border router, buildings; STEP 6). Each has an **exact-marked fill-in table** plus **short written parts** (keyword auto-check).

### 4.1 B6 — IPv4 VLSM (5 marks)

- A given address block (aligned on its prefix boundary) and **6–7 subnets** with different host counts and functions. For example: Engineering lab, Library, Admin, Hostel, Staff Wi-Fi, CCTV, and a point-to-point router link.
- Include **boundary traps**: one subnet needing exactly 2^n − 2 hosts (fits exactly) and one needing 2^n − 1 (needs the next size up).
- State the **allocation rule explicitly**, so the answer is unique: as in the slides, *largest subnet first, smallest prefix that fits, allocated contiguously from the first address after the reserved core block; ties in the order listed*. Say what is reserved first.
- **Table** (one row per subnet): prefix length · network address · first usable · last usable · broadcast, about 3.5 marks in total.
- **Short part** (about 1.5 marks): e.g. the first free block left, why largest-first avoids wasted gaps, or which subnet could grow to N hosts without renumbering.

### 4.2 B8 — IPv6 subnetting (5 marks)

- A **/48** from the documentation range (`2001:db8:…`). A **nibble-based scheme** in the subnet-ID hextet, as in the slides (e.g. site · building · function · LAN nibbles). The first **/56 is reserved for the network core**. One **/64 per LAN**, whatever its host count.
- **Table:** the /64 prefix for each listed building/function LAN, exactly marked (about 3 marks).
- **Short parts** (about 2 marks), chosen from:
  - decide which compressed forms of an address are valid and give the correct one
  - derive the **modified EUI-64 interface ID** from a given MAC, exactly as the slides do
  - how many /64s the scheme allows per building
  - why EUI-64 is a privacy concern.

### Verification

Compute every answer with Python's `ipaddress` module. Confirm that the allocation is **unique** under the stated rule, that no subnets overlap, and that everything fits inside the block. Field marking must accept **every valid equivalent notation**: IPv6 compressed or expanded, upper or lower case, leading zeros or not. A prefix may be typed as `/26` or `26`.

---

## STEP 5 — CALCULATIONS AND CODE

- **Every numeric answer is computed by a script** (Python) before it goes into the paper: fragment fields, subnet values, bit periods, delays, checksums, sequence/ack numbers, cwnd sequences, HTTP RTT totals. Keep units explicit.
- **Python socket code** (Lecture 09 style): `socket(AF_INET, SOCK_DGRAM / SOCK_STREAM)`, `bind`, `listen`, `accept`, `connect`, `send`/`sendall`, `recv`, `sendto`/`recvfrom`, `settimeout` with `try/except socket.timeout`, `encode`/`decode`. Only use API calls the lecture shows.
  - **Run every code snippet and model answer** with `python3` against a real local peer (start a matching client or server on `127.0.0.1` in the same test script). Confirm each stated output **byte-for-byte**. Clean up afterwards.
  - MCQ code is 8–25 lines, with numbered lines when a question refers to one. 4-space indent, ≤ 80 characters per line.
- In the HTML, escape `<`, `>` and `&`, and render code in `<pre><code>` with a non-selectable line-number gutter. Long lines scroll horizontally inside the block, never wrapped or clipped.

---

## STEP 6 — FIGURES (lecture style, redrawn)

Figures are **redrawn as inline SVG in the style of the lecture slides**. Do not crop images out of the PDFs.

- **Imitate the slides' visual language.** Use a consistent icon set modelled on the lectures:
  - desktop/laptop host, server tower, switch (flat box with crossing arrows), router (cylinder/disc with arrows), wireless AP with antenna waves
  - cloud for the Internet; building blocks for campus figures
  - labelled links, with port numbers next to switch ports.

  Build each icon once as a reusable drawing helper so every figure is consistent. Other figure types:
  - **Timing diagrams:** vertical time lines per host, slanted arrows, labels beside the arrows.
  - **Header/frame layouts:** field boxes with bit widths.
  - **Waveforms:** a bit-cell grid with signal levels.
  - **Campus topologies** for the subnetting questions.
- **Tables** (routing, MAC, NAT, ARP) are HTML tables, not images.
- **Never put the answer in the figure.** Don't label the field, address or entry being asked for. Every figure must carry information the question needs.
- **No overlaps, ever.** Lay figures out on a grid with orthogonal connectors where possible. Size every box from its text with ≥ 6 px padding. Keep ≥ 6 px clearance between any label and any line, icon, arrowhead or other label. Labels sit beside lines, never on top of them.
- **Theme-aware:** strokes, text and fills use the palette's CSS variables (`var(--text)`, `var(--card)`, `var(--primary)`), never hard-coded hex. Hollow shapes are filled with `var(--card)`.
- **Size:** text at least ~12 px at 1280 px window width. Each SVG has a `viewBox`, `width: 100%`, a `min-width` of about 600 px, and a `max-width` of about 1.1 × its viewBox width. It sits inside a horizontally scrollable figure.
- **Render check (mandatory):** open the app in a headless browser (Playwright/Chromium if available) at **1280 px**, in **both themes**. Screenshot every figure and **look at the screenshots**. Also run a script that compares the `getBBox()` of every SVG text against every other text, every line, every icon/shape and its containing box. It must fail on any intersection, on a line passing through a label, and on a connector crossing a shape it doesn't connect to. Fix and re-check until clean.

---

## STEP 7 — EXPLANATIONS AND MARKING DATA

**Section A, every question:**
1. **Verdict line:** the two correct options and the single idea being tested.
2. **Reasoning:** 3–8 sentences, or a **worked table** for calculations and traces (step | what happens | values).
3. **Per-option note:** all five options get one line saying why each is true or false. For wrong options, name the mistake that leads to it.
4. **Source tag:** lecture file and slide number (e.g. `04-LANs, slide 4-33`).

**Section B, every sub-part:** model answer · rubric (points of 0.5–2 marks, summing to the sub-part's marks) · auto-check spec per point · 2–4 common mistakes, each naming the point it loses · source tag. For field answers, also give the accepted forms.

---

## STEP 8 — AUTO-MARKING

### 8.1 Text answers: keyword auto-check

- Each rubric point is `{ text, marks, auto, check }`, where `check = { all: [regex…], any: [regex…], none: [regex…], ci: true|false }`. A point passes when every `all` pattern matches, at least one `any` pattern matches (if given), and no `none` pattern matches.
- **Code answers:** strip `#` comments outside string literals before checking. **Never collapse whitespace**; write `\s*`-tolerant patterns instead. Prose checks are case-insensitive. Code checks are case-sensitive.
- Write tolerant but meaningful patterns, using proximity or line-anchored patterns for "X is Y" claims so that a sentence saying the opposite doesn't match.
- After submitting, the app pre-ticks passing points with an **"auto"** badge. Points that can't be keyword-checked are `auto: false`, start unticked, and show a hint. The student can **override any tick** (shown with an **"edited"** badge), and the marks update live.
- **Verdict:** full marks = Correct, 0 = Wrong, otherwise Partial.

### 8.2 Field answers: exact marking

- Each field is `{ label, marks, type, accept }`. The type is one of `int`, `number` (with an explicit tolerance), `ipv4`, `cidr4`, `ipv6`, `cidr6`, `prefix`, `mac`, `text-set` (a list of accepted words).
- **Normalise before comparing:** trim, ignore case, IPv6 to its canonical form (compare 128-bit values), MAC with `:`/`-` and case ignored, prefix with or without `/`, numbers with optional units stripped.
- After submitting, each cell shows ✓ or ✗ with the accepted answer beside it. The student can override a cell's verdict (marked "edited").

### 8.3 Built-in self-test

`index.html?selftest=1` checks:

- every MCQ count, quota and length rule, and that every MCQ has exactly two correct options
- that the essay marks are 4×5 + 5×4 + 3×3 + 3×2 = 55
- every text sub-part: the model answer scores full marks on all auto points, 1–2 plausible wrong answers score less than full, and an empty answer scores 0
- every field: the model answer is correct, each listed alternative notation is correct, and a near-miss is wrong.

It logs a pass/fail table. **Run it and fix every failure before finishing.**

---

## STEP 9 — THE APP

Single self-contained file: `CN_final_mock_v2/index.html`. No CDN, no frameworks, no build step; vanilla JS + CSS that works offline by double-clicking.

### Flow (no mode choice)

- **Cover page:** "IE2004 — Computer Networks · Final Examination (Mock, real-exam format) · Duration: 3 Hours · Total: 100 marks · 65 questions". It gives the instructions (calculators allowed; answer in the boxes provided), the section/marks table (Section A 50 MCQs = 45; Section B 15 questions = 55), and the marking rules ("each MCQ has exactly TWO correct answers; +0.45 per correct tick, −0.45 per wrong tick, minimum 0"; exact fields; keyword auto-check with overrides).
- The cover has **one button**: **Start the paper**, or **Resume saved attempt** plus **Start fresh** if a saved attempt exists. **There is no practice/exam choice.**
- **Feedback after each answer:** when a question or sub-part is submitted, the verdict, the correct answer(s) and the explanation appear immediately below it.

### Layout and features (desktop, ≥ 1024 px; no phone testing needed)

- **Header:** the section and "Question n of 65", a running score (marks earned / marks of submitted questions), the 3-hour countdown, the theme toggle, and **Finish**.
- **Navigator sidebar:** Section A as a 10-column grid (1–50) and Section B (51–65). It shows each question's state: unanswered (outline), answered (ink fill), flagged (maroon outline + flag), and correct/partial/wrong (state colour + ✓ ◐ ✗, so colour is never the only signal). It also has a "Show flagged only" toggle and **Reset attempt** (confirm first).
- **Section A:** checkboxes labelled "Select TWO — negative marking applies". **Submit answer** locks the question. The feedback marks every option: ticked & correct (green ✓ +0.45), ticked & wrong (red ✗ −0.45), **not ticked but correct (amber "missed")**, not ticked & wrong (neutral). The verdict banner shows the maths (e.g. "0.45 / 0.9 — 2 correct ticks +0.90, 1 wrong tick −0.45"). The explanation then opens.
- **Section B:**
  - Text sub-parts use plain monospace textareas (no syntax highlighting, spellcheck off; Tab inserts 4 spaces, Shift+Tab outdents) with a line/character counter.
  - Field sub-parts use inline inputs in tables.
  - Every sub-part has its own **Submit answer**. The feedback below it shows the verdict, then the rubric with auto ticks and overrides, or the field ✓/✗ with accepted answers, then the model answer, common mistakes and source.
- **Flags:** a toggle on every question (key `F`). Finish warns: "You have N flagged and M unanswered questions — finish anyway?" Unsubmitted answers are marked at finish.
- **Timer:** a 3-hour countdown that survives refresh (store the start timestamp). Banners appear at **15** and **5 minutes** left. At 0, the student can carry on: the timer turns into a red overtime count-up, and the overtime is recorded.
- **Results:**
  - total /100 and %, plus per-section scores (A /45, B /55)
  - per-lecture breakdown and per-tier breakdown (MCQs); marks lost to negative marking; time used and overtime
  - a **list of missed questions** (wrong *and* partial) with jump-back links
  - **Retry missed only** (resets just those questions and keeps the original attempt in an attempt-history table) and a best-score record.
- **Save progress:** `localStorage` with a versioned key (`cn-final-v2-…`) holds answers, submitted state, rubric/field overrides, flags, the option-shuffle seed, the timer start, the current question, attempts and best score. Wrap every storage call in `try/catch`.
- **Keyboard:** `1`–`5` toggle options, `Enter` submits, `←`/`→` navigate, `F` flags. All are disabled while typing.

### Palette: the same as the Java paper (exact values, as CSS custom properties)

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
- The theme follows the device by default. A ☀/☾ toggle saves the choice in `localStorage` (key `cn-theme`), and an inline `<head>` script applies it before first paint.
- **No hard-coded colours** outside the two token blocks.
- Typography: serif stems (`"Iowan Old Style", "Palatino Linotype", Georgia, serif`), sans UI, monospace code.

---

## STEP 10 — BEFORE YOU FINISH

Do **not** write an audit or report file. Silently make sure that:

- **Totals:** marks are exactly 100 (45 / 55). There are 50 MCQs, each with 5 options and exactly 2 correct, using only L03/L04/L05/L05A/L06/L09 in the STEP 2.2 counts. The tiers are 10/20/20, with the theory/applied limits of STEP 1.3 and every STEP 2.3 form count. The essay section has 15 questions (4×5, 5×4, 3×3, 3×2) covering all 10 lectures, as in the STEP 3 table.
- **Option rules:** every STEP 2.4 rule holds, with length parity and the length-tell counts actually measured.
- **No trivia:** scan every stem and option for years/dates, people's names, organisation/company names, RFC or standard numbers, and "name the …" stems. Rewrite anything that violates STEP 1.2.
- **Numbers and code:** every number was produced by a script. Every subnet answer was verified with `ipaddress` and is unique. Every Python snippet and model answer ran and matched byte-for-byte.
- **Self-test and loading:** `index.html?selftest=1` reports zero failures, and the app loads with no console errors.
- **Figures and layout:** the STEP 6 render check passes at 1280 px in both themes, and the page never scrolls sideways.
- **Theme:** switching works (follows the device; the toggle overrides it and survives a reload; no flash on load).

Fix anything that fails, then reply with a summary of **≤ 10 lines**: what was generated, the essay scenarios (especially the subnetting and code questions), and anything you compromised on.

---

## DELIVERABLES

```
CN_final_mock_v2/
└── index.html     (the exam app — 50 MCQs + 15 essay questions embedded)
```

## DO NOT

- Do not ask trivia: dates, history, people, organisations, RFC/standard numbers, or "name the …" lists.
- Do not use midterm lectures (L01, L02, L07, L08) in the MCQ section.
- Do not give any MCQ more or fewer than exactly two correct options.
- Do not make the correct answers the longest or most detailed options by habit.
- Do not write one-line definition questions in the essay section; every question needs reasoning.
- Do not reuse reference-paper scenarios or numbers, or lecture exercises verbatim.
- Do not put the answer inside a figure, and never let a figure have overlapping labels or lines.
- Do not use a rule, value or convention that isn't in the slides, and never make an "it depends" behaviour the deciding fact.
- Do not state a number, subnet or code output that you haven't computed or run.
- Do not add a practice/exam mode choice, a reference sheet, or report files.
