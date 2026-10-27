# PROMPT — IE2004 (Computer Networks) Final Exam Mock Paper Generator

Copy everything below the line into Claude Code, run from the root of this repo.

---

## ROLE

You are setting a **mock final exam** for **IE2004 — Computer Networks** (SLIIT, Year 2 Sem 1). Your job is not to write "quiz questions about networking". You are writing questions that a student who has read the slides but not *understood* them will get wrong. This module is **theory-based**, so the paper must test understanding of how and why networks work: mechanisms, trade-offs, consequences, diagnosis. It also needs **thinking questions**: calculations, traces, scenarios and figures to reason about.

The paper must be **harder than the reference paper in this repo**, but stay strictly within the lecture slides.

You produce **one full 100-mark paper** as a single offline exam app.

---

## STEP 0 — READ BEFORE WRITING ANYTHING

All files are in the **repo root** (flat). Quote the names, because they contain spaces and parentheses.

1. **Lecture slides (the only source of truth for scope and rules):**

   | # | File | Pages |
   |---|---|---|
   | L01 | `01-Introduction (2).pdf` | 56 |
   | L02 | `02-Protocol-architecture.pdf` | 40 |
   | L03 | `03-Physical-layer.pdf` | 54 |
   | L04 | `04-LANs (3).pdf` | 106 |
   | L05 | `05-IP (2).pdf` | 84 |
   | L05A | `05A-IPv6 (2).pdf` | 41 |
   | L06 | `06-Routing (2).pdf` | 31 |
   | L07 | `07-Transport (5).pdf` | 92 |
   | L08 | `08-Application (4).pdf` | 73 |
   | L09 | `09-Network-Programming.pdf` | 28 |

   - Extract the text with `pdftotext -layout`, but **do not rely on the text alone**. Much of the teaching is inside slide images: waveforms, timing diagrams, header formats, tables, formulas, worked examples. Render every slide to PNG (`pdftoppm -png -r 60`) and **look at** each slide whose text layer is thin, or that contains a figure, table or worked example. You need those figures to imitate the lecture style (STEP 6) and to learn the exact conventions (STEP 1).
   - **Everything taught is in scope**, including the WLAN security slides (RSN, PSK, SAE, 802.1X/EAP, 4-way handshake) that come after Lecture 04's References slide. Ignore purely administrative slides (attendance, audience Q&A, "slides prepared by", reference lists).

2. **Reference paper:** `IE2004-Computer Networks (1) (1).pdf`. It is a **scan with no text layer**: render its pages with `pdftoppm -png -r 80` and read the images. It is a real past final: 2 hours, 4 written questions of 25 marks each, every question a scenario or figure with lettered sub-parts and marks. It is **too easy**.
   - **Borrow:** the framing (a figure such as a topology or a switched network, followed by sub-parts that each test one step); calculation and trace parts (full-mesh link counts, MAC tables after frames, VLAN port configuration, subnet allocation, ARP fields, traceroute, socket counts, TCP sequence/ack numbers, DHCP and DNS exchanges, Python socket code); and marks shown per sub-part.
   - **Do not borrow** its scenarios or numbers: the A–S1–R–S2–B chain; the four-host three-switch tree; 192.168.12.0/22 with 500/200/100 hosts; the 192.168.8.10 / 192.168.8.20 ARP pair; the echo server on port 2000 with ISNs 10000/20000; www.example.com resolved iteratively. Do not reuse lecture exercises verbatim either (e.g. the 223.4.8.0/21 or 172.16.0.0/12 campus exercise, the 2001:db8:1::/48 campus table, "C sends to I" on the multi-switch slide). **New scenarios and new numbers only.**

3. **App shell:** if `OOAD_final_mock/index.html` exists in the repo, study it. It is a finished exam app from another module, built to almost the same spec (navigator, flags, timer, keyword auto-marking with tick overrides, results, retry-missed, saved progress, light/dark theme, self-test). **Reuse its architecture and code**, adapted to this spec. Do not reuse its questions.

If a listed file doesn't exist, search the repo, list what you actually found, and confirm with me before generating.

Do **not** write style-notes, audit or report files. Put the effort into the paper.

---

## STEP 1 — SCOPE AND QUALITY RULES

### 1.1 Lecture-only, using the lectures' own conventions

- If a rule, value, formula or behaviour does not appear in the slides, it **cannot be the correct answer**. It may appear as a distractor, and the explanation must say it is outside the lectures.
- **Use the lectures' own conventions, not textbook variants.** Check each of these in the slides (including the images) before writing questions on it, and follow the slides exactly:
  - the four delay components and how the slides compute transmission and propagation delay; throughput and bottleneck links
  - the PDU names at each layer, and which layers each device (host, switch, router) processes
  - the **Manchester encoding convention exactly as the slides draw it** (which transition means 1)
  - the CSMA/CD steps and binary exponential backoff as listed
  - collision domains with hubs vs switches; switch self-learning and flooding
  - VLAN access/trunk ports, the 802.1Q tag, router-on-a-stick
  - 802.11: CSMA/CA, the IFS ordering and values shown, RTS/CTS, the four address cases (To DS / From DS), passive vs active scanning, authentication/association, and the security slides
  - the IPv4 header fields; fragmentation (offset = first byte ÷ 8, the MF flag, lengths)
  - subnet arithmetic (usable hosts = 2^h − 2), reserved and private ranges, directed vs limited broadcast
  - NAT translation, ICMP and traceroute (TTL), the DHCP message sequence, the ARP message fields
  - IPv6: the header and what was removed or changed from IPv4 and why; extension headers; no fragmentation by routers; the zero-compression rules; address types and prefixes; modified EUI-64 (insert `fffe`, flip the bit) exactly as the slides show; autoconfiguration and the EUI-64 privacy concern
  - routing vs forwarding, routing tables, longest prefix match, static vs dynamic routing, autonomous systems
  - UDP vs TCP demultiplexing (which tuple identifies a socket); the Internet checksum (1's complement with wraparound) and why it is weak
  - TCP sequence/ack numbering, the 3-way handshake, closing, the states, the ACK-generation table, retransmission scenarios, fast retransmit (3 duplicate ACKs), flow control (rwnd), slow start, AIMD, ssthresh, and the Tahoe vs Reno reactions exactly as the slides show
  - DNS hierarchy, iterative vs recursive resolution, caching, record types
  - HTTP non-persistent vs persistent response-time reasoning (RTTs), HTTP/2 head-of-line blocking, QUIC, message formats, status codes, cookies, web caches
  - the Python socket API as Lecture 09 uses it
- Where the slides themselves say something "depends" (e.g. whether a DHCP ACK is broadcast or unicast), **never make that the deciding fact** of a question.

### 1.2 No trivia (hard rule)

The student explicitly does **not** want questions that just test memory of facts that don't help them understand networking. **Never** ask:

- **dates, years or history** ("when was HTTP created", how the Internet evolved, which version came first)
- **names of people, companies or organisations** as the tested point ("which company/body controls IP addresses", who invented Ethernet, which body publishes 802.11)
- **"name the X" lists** with no reasoning ("name the WLAN security methods", "list the 802.11 frame types", "list the ICMP message types")
- **pure lookup values** as the tested point: RFC numbers, standard amendment letters, cable-category speed tables, frequency-band tables, well-known port numbers on their own.

If a question needs such a value to reason with, **give it in the stem**.

Every question must test understanding (why / how / what happens if / what is wrong / which is better here and why), or application (compute, trace, diagnose, design). "WLAN security" is fine as *"which method stops an attacker who captured the 4-way handshake from guessing the passphrase offline, and why"*. It is not fine as *"name the three methods"*.

### 1.3 Theory and thinking balance

- About half the MCQs (**≥ 25**) are **concept** questions: mechanisms, trade-offs, cause and effect, comparing two techniques, consequences of a design choice. All of them are asked through a situation or a claim to evaluate, never as "what is the definition of".
- At least **20** are **applied** questions: a calculation, a trace, a figure to interpret, or a scenario to diagnose.
- Every large question mixes both (STEP 3).

---

## STEP 2 — SECTION A: MCQs (50 questions, 40 marks)

### 2.1 Types and marks

| Type | Count | Input | Options | Marking |
|---|---|---|---|---|
| **Multi-answer** | 32 | checkboxes | 5 | proportional, negative marking |
| **Best-answer** | 18 | radio | 4 | full marks or 0, no negative marking |

- Every MCQ is worth **0.8 marks** (50 × 0.8 = 40).
- **Multi-answer negative marking (count hidden):** the stem never says how many options are correct ("Select all that apply"). With *k* correct options, each correct tick earns **+0.8/k** and each incorrect tick costs **−0.8/k**. The score is clamped to the range **0 to 0.8**. Display it to 2 dp.
- **Correct-option counts across the 32 multi-answer questions:** exactly **4 with 1 correct, 10 with 2, 11 with 3, 7 with 4**.
- Best-answer stems say "Select the BEST answer". At least **6** of the 18 must have a defensible runner-up that only loses by the lectures' rule, and the explanation must say why it loses.

### 2.2 Lecture allocation (exact, weighted by lecture size)

| Lecture | MCQs | Shapes to use (illustrations, not a checklist) |
|---|---|---|
| L01 Introduction | 5 | Which delay dominates in a described link (transmission vs propagation, with numbers given). Store-and-forward and queueing loss. Throughput bottleneck on a figure path. Datagram vs virtual-circuit behaviour for a packet sequence. What a topology change does to link count or fault tolerance. |
| L02 Protocol architecture | 3 | Encapsulation through a figure path: which headers each device adds or reads. PDU names. Why layering helps and what it costs. TCP/IP vs OSI mapping in a scenario. |
| L03 Physical layer | 4 | Decode a waveform figure under the slides' Manchester convention. Bit rate vs bit period. Why twisting or shielding reduces NEXT. SMF vs MMF and dispersion consequences. Multipath and attenuation. Choose a medium for a situation. |
| L04 LANs | 9 | CSMA/CD and backoff behaviour. Collision domains on a hub/switch figure. Self-learning tables after given frames on a multi-switch figure. Half vs full duplex. Access/trunk ports and 802.1Q. Router-on-a-stick. Why 802.11 uses CA not CD. IFS priority. RTS/CTS and the hidden terminal. Address fields for an AP/DS figure. Passive vs active scanning. What PSK, SAE or 802.1X each protects against. |
| L05 IPv4 | 7 | Which header fields change per hop and why. Fragmentation numbers. Network, broadcast and usable ranges from an address/prefix. Directed vs limited broadcast. NAT table on a figure, and NAT's limitations. How traceroute uses TTL and ICMP. DHCP sequence (who broadcasts what). ARP request/reply fields on a figure. |
| L05A IPv6 | 3 | Why IPv4 fields were removed or moved. The consequence of no fragmentation at routers. Valid vs invalid zero compression. Identify an address type from its prefix. EUI-64 derivation and its privacy problem. |
| L06 Routing | 3 | Routing vs forwarding. Longest prefix match on a given table. Static vs dynamic trade-offs. Intra- vs inter-AS reasoning. |
| L07 Transport | 8 | UDP vs TCP demultiplexing (which socket gets a segment). Internet checksum computation and its weakness. Sequence/ack numbers across segments. Handshake and close states. ACK-generation rules. Retransmission vs fast retransmit. rwnd. cwnd/ssthresh evolution after given events (Tahoe vs Reno as in the slides). |
| L08 Application | 6 | Client-server vs P2P. Transport needs of applications. Iterative vs recursive DNS with caching on a figure. Record types in a scenario. Non-persistent vs persistent HTTP response time in RTTs. HTTP/2 head-of-line blocking and why QUIC uses UDP. Status codes in a scenario. Cookies. Web-cache effect. |
| L09 Network programming | 2 | **Read or trace Python socket code** (Lecture 09 style): what it prints or does, which line is wrong, what happens on timeout, why a TCP server uses the socket that accept() returns. |

### 2.3 Required forms (spread across the 50, not extra questions)

- ≥ **12** MCQs include a **figure** (STEP 6).
- ≥ **8** involve a **calculation** (delays, throughput, fragmentation, subnet values, checksum, sequence/ack numbers, cwnd, HTTP response time). Give every constant needed, and keep the arithmetic doable with a calculator.
- ≥ **2** contain **Python socket code** (L09).
- ≥ **8** are negated (`NOT`, `would FAIL`, `LEAST appropriate`, `IMPOSSIBLE`, `does NOT change`).
- ≥ **4** use the "Student A says X, Student B says Y — who is correct and why?" form (best-answer, all options pairing a verdict with a reason).
- ≥ **6** combine two lectures (e.g. a frame crossing a switch and a router, so both L02 encapsulation and L04/L05 forwarding matter; ARP + DHCP; NAT + transport ports; DNS + TCP/UDP choice).

### 2.4 Option-design rules (the most important part of Section A)

Earlier attempts failed because the correct answer was always the longest, most detailed option and the distractors were throwaways. That is a fatal defect.

1. **Length parity.** Within a question, the longest option is **≤ 1.25×** the shortest (in characters).
2. **Length tell.** Across the 50, the longest option is a correct option in **at most 20**, and the shortest option is a correct option in **at least 18**.
3. **Parallel structure.** All options share grammatical shape and specificity. If one gives a number, all do; if one gives a reason, all do.
4. **Every distractor is a diagnosed mistake.** Each wrong option is exactly what a student produces after one nameable error. Examples:
   - adds propagation delay once per hop where the slides count it per link
   - forgets the switch floods when its table has no entry
   - divides by 1 instead of 8 for the fragment offset
   - counts the network and broadcast addresses as usable
   - thinks the UDP socket is identified by the 4-tuple
   - thinks a timeout halves cwnd under Tahoe
   - reads the Manchester transition with the opposite convention
   - thinks a router reassembles fragments
   - puts the AP's MAC in the wrong 802.11 address field

   If you can't name the error, rewrite the option.
5. **Multi-answer integrity.** Each option is independently true or false. A partially true statement is **false**, and its explanation names the false part.
6. **No free eliminations.** No two options may be ruled out by the same single observation, and no option may paraphrase another.
7. **Banned:** "All of the above", "None of the above", "Both A and C".
8. **No absolute-word tell.** Spread "always/never/only/must" and hedges across correct and incorrect options.
9. **No keyword matching.** A question must not be answerable by matching a distinctive stem word to the same word in an option.
10. **Runtime shuffle.** The app shuffles options, so explanations reference **option text, never letters**.

### 2.5 Difficulty

| Tier | Definition | Count |
|---|---|---|
| 1 — Recall-plus | One idea, applied directly, < 40 s (still never trivia, STEP 1.2) | 8 |
| 2 — Applied | 2–3 reasoning steps, or a short calculation or trace | 17 |
| 3 — Hard | 4+ steps, two concepts interacting, needs scratch working, 1.5–3 min | 25 |

Twist deliberately. Some examples:

- a link where propagation dominates although the stem stresses the bandwidth
- a frame whose destination the switch has already learned on the *same* port it arrived on
- a fragment whose offset looks right but whose MF flag is wrong
- a /26 that fits 62 hosts but not 63
- a NAT box behind a second NAT
- a duplicate ACK that is caused by reordering, not loss
- a DNS answer served from the local cache, so the root is never asked
- an HTTP page with objects on two different servers.

Never ask the plain definitional form when an applied one exists.

---

## STEP 3 — SECTION B: Large questions (5 questions, 40 marks)

Five questions of **8 marks** each, in the reference paper's format: a scenario and/or a **figure**, then **3–5 lettered sub-parts** with marks shown (`(2 marks)`). Every large question must contain:

- at least one **theory sub-part** (explain, compare, justify)
- at least one sub-part that **uses a figure**
- at least one **calculation or trace** sub-part
- a **final sub-part at Tier 3** (design, diagnose, or predict the effect of a change).

Volume is not quality: every sub-part must test a distinct idea.

| Q | Lectures | Must cover (pick sub-parts from these; new scenarios) |
|---|---|---|
| **B1** | L01–L02 | End-to-end delay over a multi-hop **figure path** (store-and-forward, per-link transmission plus propagation, given lengths and rates). The throughput bottleneck. Circuit vs packet switching (datagram vs VC) for the scenario. Encapsulation: the headers present on each link and which devices read which headers. |
| **B2** | L03–L04 | Decode or encode a **waveform figure** (Manchester as in the slides). Medium choice with attenuation/NEXT/dispersion reasoning. **Multi-switch self-learning** tables and flood/forward decisions for a given frame order on a figure. VLAN design (access/trunk, allowed VLANs, 802.1Q, why inter-VLAN traffic needs a router). An 802.11 scenario (hidden terminal and RTS/CTS, the address fields for a DS case, or what a security method defends against). |
| **B3** | L05–L06 | **Fragmentation** of a given datagram over a smaller MTU (lengths, offsets, MF). **Longest prefix match** on a router table for given destinations (figure plus table). A **NAT** translation table for given flows. The DHCP + ARP sequence when a host joins and pings off-subnet: which frames are broadcast, with the source/destination MAC and IP in each. How traceroute discovers the routers. |
| **B4** | L07 | Socket/demux reasoning for given flows (UDP vs TCP). A **TCP timing diagram** with exact sequence/ack numbers and flags for a given exchange (new ISNs and payload sizes). An **Internet checksum** worked by hand on given 16-bit words. **cwnd/ssthresh per RTT** after given loss events (timeout vs 3 dup ACKs, as the slides define them). One flow-control or retransmission reasoning part. |
| **B5** | L08–L09 | DNS resolution on a **figure of servers** (iterative vs recursive, number of queries, effect of a cached entry). HTTP response time in RTTs for non-persistent vs persistent connections (given object counts). Why HTTP/2 or QUIC fixes head-of-line blocking. **Write Python socket code** (Lecture 09 style; a TCP or UDP client or server meeting a stated behaviour, including a timeout or a loop where the slides cover it). |

### Answer input types for Sections B and C

- **Text** answers (explanations, prose, code) use the **keyword auto-check** (STEP 8).
- **Field** answers (any single exact value: a number, an address, a prefix, a flag value, a sequence number, a table cell) use **typed input boxes that are marked exactly** (STEP 8.2). For example, a fragment table gives one box per length/offset/MF cell, and a MAC-table question gives one box per entry. Use fields wherever the answer is a precise value. Use text only when it is genuinely prose.

---

## STEP 4 — SECTION C: Subnetting (2 questions, 20 marks)

Two questions of **10 marks** each, both in the lectures' campus style: an organisation with several **buildings and functions**, shown on a **campus topology figure** (core router, border router, buildings; STEP 6). Each question has an **exact-marked fill-in table** plus **two short written parts** (keyword auto-check).

### C1 — IPv4 VLSM (10 marks)

- A given address block (aligned on its prefix boundary) and **6–8 subnets** with different host counts and functions. For example: Engineering lab, Library, Admin, Hostel, Staff Wi-Fi, CCTV, a server farm, and point-to-point router links.
- Include **boundary traps**: one subnet needing exactly 2^n − 2 hosts (fits exactly) and one needing 2^n − 1 (needs the next size up). One requirement may say "plus 20% growth" or "plus a gateway address" (state precisely how to count it).
- State the **allocation rule explicitly**, so the answer is unique: as in the slides, *largest subnet first, smallest prefix that fits, allocated contiguously from the first address after the reserved core block; ties in the order listed*. Say what is reserved first (e.g. "reserve the first /27 for the network core").
- **Table** (one row per subnet): prefix length · network address · first usable · last usable · broadcast. Each cell is a field, about 6–7 marks in total.
- **Short parts** (about 3–4 marks), for example:
  - the first free block left and how many addresses remain
  - why largest-first avoids wasted gaps
  - which subnet could grow to N hosts without renumbering, and why
  - what goes wrong if a given (wrong) mask is used on one building.

### C2 — IPv6 subnetting (10 marks)

- A **/48** from the documentation range (`2001:db8:…`). A **nibble-based scheme** in the subnet-ID hextet, as in the slides (e.g. site · building · function · LAN nibbles). The first **/56 is reserved for the network core**. One **/64 per LAN**, whatever its host count.
- **Table:** the /64 prefix for each listed building/function LAN, exactly marked (about 5–6 marks).
- **Short parts** (about 4–5 marks), chosen from:
  - how many /64s the scheme allows per building
  - decide which of several compressed forms of an address are valid (e.g. two `::` is invalid) and give the correct compression
  - derive the **modified EUI-64 interface ID** from a given MAC, exactly as the slides do
  - say why EUI-64 is a privacy concern and what the slides offer instead
  - identify an address type from its prefix.

### Verification for Section C

Compute every answer with Python's `ipaddress` module. Confirm that the allocation is **unique** under the stated rule, that no subnets overlap, and that everything fits inside the block. Field marking must accept **every valid equivalent notation**: IPv6 compressed or expanded, upper or lower case, leading zeros or not. A prefix may be typed as `/26` or `26`, as long as the field asks for a prefix.

---

## STEP 5 — CALCULATIONS AND CODE

- **Every numeric answer is computed by a script** (Python) before it goes into the paper: delays, throughput, fragment fields, subnet values, checksums, sequence/ack numbers, cwnd sequences, HTTP RTT totals. Keep units explicit in stems and explanations.
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
  - **Timing diagrams:** vertical time lines per host, slanted arrows, labels beside the arrows, as the slides draw TCP and delay.
  - **Header/frame layouts:** field boxes with bit widths.
  - **Waveforms:** a bit-cell grid with signal levels.
  - **Campus topologies** for Section C.
- **Tables** (routing tables, MAC tables, NAT tables) are HTML tables, not images.
- **Never put the answer in the figure.** Don't label the field, address or table entry being asked for. Every figure must carry information the question needs.
- **No overlaps, ever.** Lay figures out on a grid with orthogonal connectors where possible. Size every box from its text with ≥ 6 px padding. Keep ≥ 6 px clearance between any label and any line, icon, arrowhead or other label. Labels sit beside lines, never on top of them.
- **Theme-aware:** strokes, text and fills use the palette's CSS variables (`var(--text)`, `var(--card)`, `var(--primary)`), never hard-coded hex, so figures switch with light/dark. Hollow shapes are filled with `var(--card)`.
- **Size:** text at least ~12 px at 1280 px window width. Each SVG has a `viewBox`, `width: 100%`, a `min-width` of about 600 px, and a `max-width` of about 1.1 × its viewBox width (so small figures don't blow up). It sits inside a horizontally scrollable figure.
- **Render check (mandatory):** open the app in a headless browser (Playwright/Chromium if available) at **1280 px**, in **both themes**. Screenshot every figure and **look at the screenshots**. Also run a script that compares the `getBBox()` of every SVG text against every other text, every line, every icon/shape and its containing box. It must fail on any intersection, on a line passing through a label, and on a connector crossing a shape it doesn't connect to. Fix and re-check until clean.

---

## STEP 7 — EXPLANATIONS AND MARKING DATA

**Section A, every question:**
1. **Verdict line:** the correct option(s) and the single idea being tested.
2. **Reasoning:** 3–8 sentences, or a **worked table** for calculations and traces (step | what happens | values).
3. **Per-option note:** every option, correct and incorrect, gets one line saying why it is true or false. For wrong options, name the mistake that leads to it.
4. **Source tag:** lecture file and slide number (e.g. `04-LANs, slide 4-33`).

**Sections B and C, every sub-part:** model answer · rubric (points of 0.5–2 marks, summing to the sub-part's marks) · auto-check spec per point · 2–4 common mistakes, each naming the point it loses · source tag. For field answers, also give the accepted forms.

---

## STEP 8 — AUTO-MARKING

### 8.1 Text answers: keyword auto-check (as in the Java paper)

- Each rubric point is `{ text, marks, auto, check }`, where `check = { all: [regex…], any: [regex…], none: [regex…], ci: true|false }`. A point passes when every `all` pattern matches, at least one `any` pattern matches (if given), and no `none` pattern matches.
- **Code answers:** strip `#` comments outside string literals before checking. **Never collapse whitespace** (it corrupts string literals); write `\s*`-tolerant patterns instead. Prose checks are case-insensitive. Code checks are case-sensitive.
- Write tolerant but meaningful patterns, using proximity or line-anchored patterns for "X is Y" claims so that a sentence saying the opposite doesn't match.
- After submitting, the app pre-ticks passing points with an **"auto"** badge. Points that can't be keyword-checked are `auto: false`, start unticked, and show a hint. The student can **override any tick** (shown with an **"edited"** badge), and the marks update live.
- **Verdict:** full marks = Correct, 0 = Wrong, otherwise Partial.

### 8.2 Field answers: exact marking

- Each field is `{ label, marks, type, accept }`. The type is one of `int`, `number` (with an explicit tolerance), `ipv4`, `cidr4`, `ipv6`, `cidr6`, `prefix`, `mac`, `text-set` (a list of accepted words).
- **Normalise before comparing:** trim, ignore case, IPv6 to its canonical form (expand, then compare 128-bit values), MAC with `:`/`-` and case ignored, prefix with or without `/`, numbers with optional units stripped.
- After submitting, each cell shows ✓ or ✗ with the accepted answer beside it. The student can override a cell's verdict (marked "edited").

### 8.3 Built-in self-test

`index.html?selftest=1` checks every MCQ count, quota and length rule. For every text sub-part it scores the model answer (full marks on all auto points), 1–2 plausible wrong answers (less than full) and an empty answer (0). For every field it scores the model answer (correct), each listed alternative notation (correct), and a near-miss (wrong). It logs a pass/fail table. **Run it and fix every failure before finishing.**

---

## STEP 9 — THE APP

Single self-contained file: `CN_final_mock/index.html`. No CDN, no frameworks, no build step; vanilla JS + CSS that works offline by double-clicking.

### Flow (no mode choice)

- **Cover page:** "IE2004 — Computer Networks · Final Examination (Mock) · Duration: 3 Hours · Total: 100 marks · 57 questions". It gives the instructions (calculators allowed; answer in the boxes provided), the section/marks table, and the marking rules (negative marking for multi-answer; exact fields; keyword auto-check with overrides).
- The cover has **one button**: **Start the paper**, or **Resume saved attempt** plus **Start fresh** if a saved attempt exists. **There is no practice/exam choice.**
- **Feedback after each answer:** when a question or sub-part is submitted, the verdict, the correct answer(s) and the explanation appear immediately below it (the Java paper's "practice mode" behaviour).

### Layout and features (desktop, ≥ 1024 px; no phone testing needed)

- **Header:** the section and "Question n of 57", a running score (marks earned / marks of submitted questions), the 3-hour countdown, the theme toggle, and **Finish**.
- **Navigator sidebar:** Section A as a 10-column grid (1–50), Section B (51–55), Section C (56–57). It shows each question's state: unanswered (outline), answered (ink fill), flagged (maroon outline + flag), and correct/partial/wrong (state colour + ✓ ◐ ✗, so colour is never the only signal). It also has a "Show flagged only" toggle and **Reset attempt** (confirm first).
- **Section A:** radio buttons (best-answer) or checkboxes (multi-answer), labelled "Select the BEST answer" or "Select all that apply — negative marking applies". **Submit answer** locks the question. The feedback marks every option: ticked & correct (green ✓), ticked & wrong (red ✗ with its penalty), **not ticked but correct (amber "missed")**, not ticked & wrong (neutral). The verdict banner shows the maths (e.g. "0.53 / 0.8 — 2 correct ticks +1.07, 1 wrong tick −0.53"). The explanation then opens.
- **Sections B and C:**
  - Text sub-parts use plain monospace textareas (no syntax highlighting, spellcheck off; Tab inserts 4 spaces, Shift+Tab outdents) with a line/character counter.
  - Field sub-parts use inline inputs in tables.
  - Every sub-part has its own **Submit answer**. The feedback below it shows the verdict, then the rubric with auto ticks and overrides, or the field ✓/✗ with accepted answers, then the model answer, common mistakes and source.
- **Flags:** a toggle on every question (key `F`). Finish warns: "You have N flagged and M unanswered questions — finish anyway?" Unsubmitted answers are marked at finish.
- **Timer:** a 3-hour countdown that survives refresh (store the start timestamp). Banners appear at **15** and **5 minutes** left. At 0, the student can carry on: the timer turns into a red overtime count-up, and the overtime is recorded.
- **Results:**
  - total /100 and %, plus per-section scores (A /40, B /40, C /20)
  - per-lecture breakdown and per-tier breakdown; best-answer vs multi-answer accuracy
  - marks lost to negative marking; time used and overtime
  - a **list of missed questions** (wrong *and* partial) with jump-back links
  - **Retry missed only** (resets just those questions and keeps the original attempt in an attempt-history table) and a best-score record.
- **Save progress:** `localStorage` with a versioned key holds answers, submitted state, rubric/field overrides, flags, the option-shuffle seed, the timer start, the current question, attempts and best score. Wrap every storage call in `try/catch`.
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

- **Totals:** marks are exactly 100 (40 / 40 / 20). There are 50 MCQs (32 multi / 18 best; correct-counts 4/10/11/7), the STEP 2.2 per-lecture counts, the tiers 8/17/25, the theory/applied balance, and every STEP 2.3 form count.
- **Option rules:** every STEP 2.4 rule holds, with length parity and the length-tell counts actually measured.
- **No trivia:** scan every stem and option for years/dates, people's names, organisation/company names, RFC or standard numbers, and "name the …" stems. Rewrite anything that violates STEP 1.2.
- **Numbers and code:** every number was produced by a script. Every subnet answer was verified with `ipaddress` and is unique. Every Python snippet and model answer ran and matched byte-for-byte.
- **Self-test and loading:** `index.html?selftest=1` reports zero failures, and the app loads with no console errors.
- **Figures and layout:** the STEP 6 render check passes at 1280 px in both themes, and the page never scrolls sideways.
- **Theme:** switching works (follows the device; the toggle overrides it and survives a reload; no flash on load).

Fix anything that fails, then reply with a summary of **≤ 10 lines**: what was generated, the five large-question scenarios and the two subnetting scenarios, and anything you compromised on.

---

## DELIVERABLES

```
CN_final_mock/
└── index.html     (the exam app — all 57 questions embedded)
```

## DO NOT

- Do not ask trivia: dates, history, people, organisations, RFC/standard numbers, or "name the …" lists.
- Do not make the correct answer the longest or most detailed option by habit.
- Do not reveal how many options are correct in a multi-answer question.
- Do not reuse reference-paper scenarios or numbers, or lecture exercises verbatim.
- Do not put the answer inside a figure, and never let a figure have overlapping labels or lines.
- Do not use a rule, value or convention that isn't in the slides, and never make an "it depends" behaviour the deciding fact.
- Do not state a number, subnet or code output that you haven't computed or run.
- Do not add a practice/exam mode choice, a reference sheet, or report files.
