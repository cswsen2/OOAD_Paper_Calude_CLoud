---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 05d
aliases: [CRC Cards, CRC cards]
topics:
  - CRC cards
  - responsibilities and collaborators
  - object-oriented analysis
  - analysis classes
  - entity boundary control classes
---

# CRC Cards — Class Responsibility Collaboration

> **Source**: SE2012 OOAD — Lecture 05d (Lecture 10) | Prof. Nuwan Kodagoda & Mr. Jeewaka Perera
> **Developed by**: Kent Beck and Ward Cunningham (1989)

## Overview

**CRC Cards** (Class-Responsibility-Collaboration) are a lightweight [[object-oriented analysis]] technique used to **explore relationships between classes** in a particular [[use case]] scenario. They complement [[noun-verb analysis]] by helping resolve ambiguity about **which class should own which responsibility**.

CRC cards are physical or drawn cards — typically 4×6 inches — used in **collaborative workshops** where team members "role-play" the classes to simulate system behavior.

---

## What are CRC Cards?

A CRC card is a **4×6 inch card divided into three sections**:

```
┌─────────────────────────────────────────┐
│              CLASS NAME                 │
├──────────────────────┬──────────────────┤
│  RESPONSIBILITIES    │  COLLABORATORS   │
│  (What it does)      │  (Who it needs)  │
│                      │                  │
│  - Responsibility 1  │  - ClassA        │
│  - Responsibility 2  │  - ClassB        │
│  - Responsibility 3  │                  │
└──────────────────────┴──────────────────┘
```

| Section | Location | Content |
|---|---|---|
| **Class Name** | Top of card | The name of the class being described |
| **Responsibilities** | Left side | What this class is responsible for doing |
| **Collaborators** | Right side | Other classes this class needs help from |

---

## The Three Sections in Detail

### Class Name

The name identifies the concept being modeled. Comes from the [[noun-verb analysis]] step — surviving noun candidates become class names on CRC cards.

### Responsibilities

**Responsibilities relate to actions** — they are identified by selecting **verbs** from the requirements summary.

> ⚠️ **Important distinction**: The list of responsibilities on a CRC card is **NOT** the list of methods in the class.

A single **responsibility** may require **several methods** to implement:

```
Responsibility: "Store Details of Item"
    → Methods needed: addItems(), updateItems(), deleteItems()
```

Think of responsibilities as **high-level obligations** of the class, not low-level implementation details.

### Collaborators

**Collaborators** are other classes that a class needs to interact with in order to fulfill its responsibilities.

A class may **not be able to act upon a responsibility alone** — it may need help from other classes. These "helper classes" are the collaborators.

```
Responsibility: "Produce a list of Items which need reordering"
    → ItemReport class collaborates with → Item class
      (needs Item's data to generate the report)
```

**To identify collaborations**: Study the responsibilities. For each one, ask: *"Can this class fulfill this responsibility entirely on its own? If not, what other class(es) does it need?"*

---

## Why Use CRC Cards?

CRC cards are most useful when:

1. **Method ownership is unclear**: You've done [[noun-verb analysis]] and found verbs, but it's not obvious which class should own the method
2. **Exploring class interactions**: You want to trace through a [[use case]] scenario to see how objects collaborate
3. **Early design workshops**: Lightweight technique — no UML tools needed, just index cards
4. **Role-playing scenarios**: Team members each hold a card and "act out" the scenario, discovering missing responsibilities and collaborations organically

---

## Identifying Responsibilities — Step by Step

1. Gather the **requirements** or use case scenario
2. Identify **verbs** (action words) from the requirements text
3. Assign each verb to the most appropriate class as a **responsibility**
4. If a class **cannot fulfill a responsibility alone**, identify which other classes it needs → those become **collaborators**

---

## Worked Example 1 — Email CV Scenario

### Scenario

> "You (the student) should e-mail your CV to my (Lecturer's) boss."

### Step 1 — Identify Initial Classes

From the nouns: `Student`, `CV`, `Boss`, `Lecturer`

### Step 2 — Identify the Core Verb

> "send an e-mail with CV" → Responsibility of **`Student`**

### Step 3 — Identify Collaborators

Can `Student` fulfill "send an e-mail with CV" alone?

- **No** — needs to **attach the CV** → Student collaborates with `CV`
- **No** — needs to **find Boss's email address** → Student collaborates with `Lecturer` (who knows the boss)

### Resulting CRC Cards (Slide 10)

```
┌──────────────────────────────────────────────┐
│                   Student                    │
├──────────────────────────┬───────────────────┤
│  Responsibility          │  Collaborators    │
│  e-mail CV to a given    │  CV               │
│      e-mail address      │                   │
│  find e-mail address     │  lecturer         │
└──────────────────────────┴───────────────────┘

┌──────────────────────────────────────────────┐
│                  Lecturer                    │
├──────────────────────────┬───────────────────┤
│  Responsibility          │  Collaborators    │
│  Know boss's e-mail      │                   │
│      address             │                   │
└──────────────────────────┴───────────────────┘

┌──────────────────────────┐   ┌───────────────────────────┐
│            CV            │   │            Boss           │
├────────────┬─────────────┤   ├─────────────┬─────────────┤
│ (no resp.) │ (no collab) │   │ (no resp.)  │ (no collab) │
└────────────┴─────────────┘   └─────────────┴─────────────┘
```

In the role-play, the **Student** can't complete the task alone: it needs the **CV** (to attach) and the **Lecturer** (who *knows the boss's e-mail address*) as collaborators.

---

## Worked Example 2 — DVD Rental Store

### Problem

> In a DVD rental store there are two types of users, a registered member can borrow up to 3 DVDs at a time. These members have already paid a deposit and only need to pay 50/= per DVD. Unregistered members can also borrow DVDs at the rate of 75/= per DVD. They are required to provide their id card for this purpose. Members can keep the DVD for three days and when they are returned appropriate fines may be calculated.

### Classes (from [[noun-verb analysis]])

`DVD`, `Registered Member`, `Unregistered Member` (see [[OO_Analysis_Noun_Verb]] — *Member* is redundant and *Fine* is an attribute, not a class).

### Activity 2 Solution — CRC Cards (Slide 13)

```
┌──────────────────────────┐  ┌──────────────────────────────┐  ┌────────────────────────────────┐
│        DVD Class         │  │   Registered Member Class    │  │   Unregistered Member Class    │
├──────────────┬───────────┤  ├──────────────┬───────────────┤  ├──────────────┬─────────────────┤
│ Responsib.   │ Collab.   │  │ Responsib.   │ Collab.       │  │ Responsib.   │ Collab.         │
│ Store        │           │  │ Pay Deposit  │               │  │ Borrow DVD   │ DVD             │
│  Details of  │           │  │ Borrow DVD   │ DVD           │  │ Return DVD   │ DVD             │
│  DVDs        │           │  │ Return DVD   │ DVD           │  │ Pay Fine     │                 │
│              │           │  │ Pay Fine     │               │  │              │                 │
└──────────────┴───────────┘  └──────────────┴───────────────┘  └──────────────┴─────────────────┘
```

Both member classes **collaborate with `DVD`** to borrow and return. The `DVD` class only stores details and has no collaborators.

---

## Worked Example 3 — Online Order System

### Classes (from prior analysis)

`Customer`, `Order`, `Item`, `Payment`

> [!OUTSIDE] This information was not present in the original lecture material.
> The lecture (Slide 19) only states *"Step 2 — Identify Responsibilities For each Class"* and leaves the actual responsibilities/collaborators as an exercise. The tables below are a **worked-out answer**, not taken directly from the slides.

### Step 1 — Assign Responsibilities (from verbs)

| Class | Responsibilities |
|---|---|
| `Customer` | Register, Confirm order |
| `Order` | Place an order, Show order status, List previous orders |
| `Item` | Add item, Restock item, Update inventory |
| `Payment` | Validate payment |

### Step 2 — Identify Collaborators

| Class | Needs Help From |
|---|---|
| `Customer` | `Order` (to place/see orders), `Payment` (to specify payment) |
| `Order` | `Customer` (who placed it), `Item` (what's in it), `Payment` (how it's paid) |
| `Item` | *(can manage itself)* |
| `Payment` | `Order` (which order it's for) |

---

## Analysis Classes — Types

Beyond entity classes, OOA recognizes three types of analysis classes (each with its own UML stereotype and icon, Slide 14):

| Type | Stereotype / Icon | Description | Quantity Guideline |
|---|---|---|---|
| **Entity Classes** | `«entity»` — circle with an underline (*system information*) | Domain objects — the classes we've been identifying up to now | As many as the domain needs |
| **Boundary Classes** | `«boundary»` — circle with a side bar (*system boundary*) | Interaction classes: forms, reports, UI screens | One per **Actor** |
| **Control Classes** | `«control»` — circle with a curved arrow (*use-case behavior coordination*) | Represent complex use case logic as a class | One per complex **Use Case** |

### Boundary Classes

Boundary classes represent the **interface between the actor and the system**. Examples:
- A login form (boundary between User actor and the system)
- A printed report (boundary between Manager actor and the system)

### Control Classes

In a complex use case, the use case logic itself becomes a class. This prevents entity classes from becoming overloaded with coordination logic.

---

## Actors as Entity Classes — A Special Case

**Actors** from a [[use case]] diagram are normally **outside** the system. However, if an actor's data is **directly relevant to the application domain**, then that actor becomes an **entity class** too.

| Actor Type | Becomes a Class? |
|---|---|
| Actor with only login credentials | ❌ No (user accounts only → not a domain class) |
| Actor whose data is stored in the domain | ✅ Yes |

### Example

> A **Customer** in an Online Store must register and provide shipping address, billing address, contact details.

Since customer data is directly part of the application domain → **`Customer` is both an Actor AND a Class**.

---

## Role-Playing CRC Cards

A powerful technique is **role-playing CRC cards** in a team:
1. Each team member holds one or more CRC cards
2. A facilitator reads a scenario step-by-step
3. The person holding the relevant card "acts" out the class's responsibility
4. When a class needs a collaborator, it "asks" the person holding that card
5. Missing responsibilities and collaborations become obvious through the role-play

---

## Relationship Map

[[CRC cards]] ← used after → [[noun-verb analysis]]
[[CRC cards]] → clarifies → [[class diagram]] relationships
[[CRC cards]] → based on → [[use case]] scenarios
[[responsibilities]] → implemented by → [[method|methods]]
[[collaborators]] → become → [[association|associations]] in [[class diagram]]
[[entity classes]] ↔ [[boundary classes]] ↔ [[control classes]] (three types of analysis classes)
[[object-oriented analysis]] → uses → [[CRC cards]] and [[noun-verb analysis]]

---

## 📅 Tasks

- [ ] Write CRC cards for the Online Order System (Customer, Order, Item, Payment) [due:: 2026-07-05] #p1
- [ ] Role-play the DVD Rental Store scenario using CRC cards with peers [due:: 2026-07-07] #p1
- [ ] Identify which classes in the Online Order System are Entity vs Boundary vs Control [due:: 2026-07-07] #p2
- [ ] Determine if the Administrator actor in the Online Order System should be a class [due:: 2026-07-10] #p3

---

## 🧠 Flashcards

What are CRC Cards? :: **Class-Responsibility-Collaboration** cards. A 4×6 inch card divided into 3 sections: class name (top), responsibilities (left), collaborators (right). Used in OOA to explore class relationships in a use case scenario.

Who invented CRC Cards and when? :: **Kent Beck and Ward Cunningham** in **1989**.

What are the three sections of a CRC Card? :: 1. **Class Name** (top) — the class being modeled. 2. **Responsibilities** (left) — what the class is responsible for doing. 3. **Collaborators** (right) — other classes this class needs to fulfill its responsibilities.

Are responsibilities the same as methods? :: **No.** Responsibilities are high-level obligations. One responsibility may require **several methods** to implement. E.g., "Store Details of Item" → `addItems()`, `updateItems()`, `deleteItems()`.

What are collaborators? :: Other classes that a class needs to interact with in order to fulfill its responsibilities. Classes that "help" the current class — its helper classes.

How do you identify collaborators? :: Study each responsibility and ask: "Can this class fulfill this responsibility alone?" If not, identify which other class(es) it needs — those are the collaborators.

How do you identify responsibilities? :: By selecting **verbs** from the requirements/use case scenario text. Each verb becomes a candidate responsibility for the most appropriate class.

When should you use CRC Cards (vs Noun/Verb analysis)? :: Use CRC cards when it's **unclear which class should own which method/responsibility**. They complement [[noun-verb analysis]] by resolving ambiguity through scenario-based exploration.

What are the three types of Analysis Classes? :: 1. **Entity Classes** — domain objects (the main classes). 2. **Boundary Classes** — interaction classes (forms, reports) — one per Actor. 3. **Control Classes** — represent complex use case logic — one per complex Use Case.

What is a Boundary Class? :: A class that represents the **interaction between an actor and the system** — forms, reports, UI screens. There is typically one boundary class per actor.

What is a Control Class? :: In a complex use case, the use case logic itself is represented as a class. This prevents entity classes from being overloaded with coordination logic. Typically one per complex use case.

When does an Actor become an Entity Class? :: When the actor's data is **directly relevant to the application domain**. E.g., a Customer who must register and provide shipping/billing details → becomes both an actor AND a `Customer` class. An actor who only has login credentials → NOT a class.

What is the Role-Playing technique for CRC Cards? :: Team members each hold a CRC card. A facilitator reads the scenario step-by-step. Each person "acts" their class's responsibility and "asks" collaborators for help when needed. Missing responsibilities and collaborations are discovered naturally.

In the Email CV scenario, why does Student need Lecturer as a collaborator? :: Student needs to find the Boss's email address. Student doesn't know the Boss directly — it must ask Lecturer (who knows the Boss) for that information.

What is the key insight behind CRC Cards in OOA? :: They make **class collaborations visible** by forcing you to trace through a specific scenario step-by-step, asking "who needs to talk to whom?" at each step. This naturally reveals the interaction network between classes.

What is the difference between a responsibility and a method in OOA? :: A **responsibility** is a high-level obligation (e.g., "Store Details of Item"). A **method** is a specific implementation unit. One responsibility often maps to multiple methods (`addItems()`, `updateItems()`, `deleteItems()`).

What do collaborators in CRC cards correspond to in a class diagram? :: **Associations** (or dependencies) between classes. A collaborator relationship means one class depends on or communicates with another.

In the DVD rental CRC solution, what are the three classes and their collaborators? :: DVD (stores DVD details, no collaborators), Registered Member and Unregistered Member (both borrow/return DVDs and pay fines, collaborating with DVD).

What are the UML stereotypes for the three analysis class types? :: «entity» (system information), «boundary» (system boundary), and «control» (use-case behavior coordination).

#flashcards
