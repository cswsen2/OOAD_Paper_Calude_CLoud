---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 05c
aliases: [OO Analysis Noun Verb, noun-verb analysis, Noun-Verb Analysis, object-oriented analysis]
topics:
  - object-oriented analysis
  - noun-verb analysis
  - identifying classes
  - common and proper nouns
  - rejecting nouns
---

# OO Analysis — Noun/Verb Method for Identifying Classes

> **Source**: SE2012 OOAD — Lecture 05c | Prof. Jagath Samarabandu & Mr. Jeewaka Perera
> **References**: Head First OOA&D (Ch. 4), A Student Guide to Object-Oriented Development (Ch. 5)

## Overview

[[object-oriented analysis]] (OOA) is the process of **discovering classes** from a system's requirements. It sits within the [[software development life cycle]] between requirements gathering and design:

```
Requirements Gathering → Describe the Application
        ↓
    Analysis (OOA) ← YOU ARE HERE
        ↓
      Design
        ↓
 Implementation (Coding)
```

Requirements are typically represented as:
- [[use cases]] / [[use case]] diagrams
- [[use case scenarios]]
- [[user stories]]

In OOA, we take these representations and **identify the classes** needed to build the system.

---

## Two Techniques for Discovering Classes

| Technique | Description |
|---|---|
| **[[noun-verb analysis]]** (Noun/Verb Method) | Extract nouns → candidate classes; extract verbs → candidate methods |
| **[[CRC cards]]** | Class-Responsibility-Collaboration cards for exploring class relationships |

This page covers the **Noun/Verb Method** in detail.

---

## OOA is Part of the SDLC

Requirements should describe the **new application to be built**, not how things are done manually. The analysis phase takes those requirements and translates them into an OO model of classes, attributes, and methods.

---

## Noun / Verb Analysis

The **Noun/Verb Method** leverages a key insight from natural language:

> **In general, classes correspond to nouns.**
> **Methods correspond to verbs.**

### Steps

1. **Identify nouns** (and noun phrases) in the requirements/problem statement
2. **Underline** each noun → each becomes a **candidate class or object**
3. **Filter** the candidates using rejection rules
4. **Identify verbs** → each becomes a **candidate method**
5. **Assign** methods to the most appropriate class

---

## Common Nouns vs. Proper Nouns

| Type | Definition | Maps To |
|---|---|---|
| **Common Noun** | A name for a class of beings or things (e.g., *Person*, *Book*) | **Class** |
| **Proper Noun** | A specific named individual (e.g., *Jagath*, *Dehiwala*, *Keels*) | **Object** |

This distinction helps separate **classes** (concepts) from **objects** (specific instances).

---

## Rules for Rejecting Noun Candidates

Not every noun becomes a class. Apply these five rejection rules:

| # | Rule | Explanation | Example |
|---|---|---|---|
| 1 | **Redundant** | Same concept named twice with different words | "Member" and "User" in a library system refer to the same entity |
| 2 | **Meta-language** | Words used to talk *about* the language itself, not domain concepts | "In a library system people who are using library system can be called members" — "library system" is meta-language |
| 3 | **Event or Operation** | Something that happens, not a thing | "Search book" is an operation, not a class |
| 4 | **Outside scope of system** | The concept exists but is not part of the system being built | "University Department (SE/IT)" is outside scope of a library system |
| 5 | **An attribute** | A property of another class, not a class itself | "ISBN" is an attribute of Book, not its own class |

> **Note**: Rules 1 and 2 overlap in many real situations.

---

## Worked Example 1 — Library System

### Problem Description

> In the Library a member can borrow, return **Books**. The people using the library can also search for **Books**. The users of the library from the Faculty of Computing belong to the **Department** of IT/SE/ISE. Each **Book** has an **ISBN**. The **SLIIT Librarian** is Ms Pushpamala Perera.

### Nouns Identified

| Noun | Keep? | Reason |
|---|---|---|
| Library | ❌ | Scope — this IS the system itself |
| Member | ✅ → **Class** | Core domain concept |
| Books | ✅ → **Class** | Core domain concept |
| People / Users | ❌ | Redundant with "Member" |
| Faculty of Computing | ❌ | Outside scope |
| Department (IT/SE/ISE) | ❌ | Outside scope |
| ISBN | ❌ | Attribute of Book |
| SLIIT Librarian | ❌ | Proper noun → Object (specific person) |
| Ms Pushpamala Perera | ❌ | Proper noun → Object (specific person) |

**Resulting Classes**: `Member`, `Book`

---

## Worked Example 2 — DVD Rental Store

### Problem Description

> In a DVD rental store there are two types of users, a **registered member** can borrow up to 3 **DVDs** at a time. These **members** have already paid a **deposit** and only need to pay 50/= per **DVD**. Unregistered **members** can also borrow **DVDs** at the rate of 75/= per **DVD**. They are required to provide their **id card** for this purpose. **Members** can keep the **DVD** for three **days** and when they are returned appropriate **fines** may be calculated.

### After Applying Rejection Rules (Activity 1 Answer — Slide 15)

| Noun | Decision |
|---|---|
| DVD | ✅ → **class** |
| User / Member | ❌ Redundant |
| Unregistered member | ✅ → **class** |
| Registered member | ✅ → **class** |
| ID Card | ❌ — "ID number" is an **attribute** |
| Fine | ❌ — **attribute** |
| Deposit | ❌ — **attribute / operation** |
| Store | ❌ — **out of scope** (the system itself) |
| Rate | ❌ — **attribute** |

**Resulting Classes**: `DVD`, `Registered Member`, `Unregistered Member` (with `ID number` as an attribute of Registered Member).

> [!IMPORTANT] Note the two pitfalls here
> *Member* is **redundant** (covered by Registered/Unregistered member), and *Fine*, *Deposit*, and *Rate* are **attributes**, not classes — a common over-identification mistake.

---

## Worked Example 3 — Online Order System (Full Noun + Verb Analysis)

### Problem Description

> A **customer** in an **online store** needs to first *register* providing details such as **name**, **address**. The **online store administrator** can *add* new **items** to the store, *restock* (increase quantity), *generate* a list of **items** that need to be restocked. A **Customer** can *place* an **Order** from an online store. An **Order** consists of multiple **items**. The **customer** can *see* the status of the **Orders** placed, and *get* a list of previous orders made. The **customer** specifies a **payment method** (credit card, debit card, paypal) for each **order**. Once the **customer** *confirms* the order and the **payment** is *validated* the **order** is placed and **items** are updated.

---

### Step 1 — Noun Analysis (Candidate Classes)

| Noun | Decision | Reason |
|---|---|---|
| customer | ✅ → **`Customer`** | Core class |
| online store | ❌ | The system itself (scope) |
| name, address | ❌ | Attributes of Customer |
| administrator | ❌ | Actor (outside system), not a class with data domain relevance |
| items | ✅ → **`Item`** | Core class |
| list of items | ❌ | Redundant (Item handles this) |
| Order | ✅ → **`Order`** | Core class |
| payment method (credit card, debit card, paypal) | ✅ → **`Payment`** | Core class |
| list of previous orders | ❌ | Redundant (Order handles this) |
| Store | ❌ | The system itself |
| status | ❌ | Attribute of Order |
| paypal, credit card, debit card | ❌ | Subtypes/attributes of Payment |

**Resulting Classes**: `Customer`, `Order`, `Item`, `Payment`

---

### Step 2 — Verb Analysis (Candidate Methods)

After identifying classes, go back and identify **verbs** (action words) → these become **candidate methods**:

| Verb | Assigned To |
|---|---|
| register | `Customer` |
| validated | `Payment` |
| place an Order, see status of Orders, confirm | `Order` |
| add, restock, updated | `Item` |
| generate list of items, list of previous orders | `Report` *(new support class)* |

### Resulting Method Assignments

```
Customer:  register()
Payment:   validate()
Order:     placeOrder(), getStatus(), confirmOrder()
Item:      addItem(), restockItem(), updateItem()
Report:    generateItemList(), getPreviousOrders()
```

> **Note**: Sometimes it's not clear which class should contain which method. In such cases, use **[[CRC cards]]** to resolve the ambiguity.

---

## Full Process Summary

```
Requirements / Problem Statement
        ↓
1. Identify ALL nouns
        ↓
2. Mark common nouns → Candidate Classes
   Mark proper nouns → Candidate Objects (instances)
        ↓
3. Apply rejection rules (redundant, meta, event, scope, attribute)
        ↓
4. Surviving nouns = CLASSES
        ↓
5. Identify verbs → Candidate Methods
        ↓
6. Assign methods to appropriate classes
        ↓
7. Unclear assignments? → Use CRC Cards
```

---

## Connection to the Rest of OOA

[[noun-verb analysis]] → produces candidate [[class|classes]] and [[method|methods]] → refined with [[CRC cards]] → modeled in a [[class diagram]] → implemented in code

- [[requirements engineering]] provides the problem statement used as input
- [[use cases]] and [[user stories]] can also serve as input documents
- [[CRC cards]] complement this method when method ownership is unclear
- [[object-oriented design]] uses the classes found here

---

## 📅 Tasks

- [ ] Apply Noun/Verb analysis to the DVD Rental Store problem [due:: 2026-07-05] #p1
- [ ] Complete Activity 2 (Online Order System) — identify all classes and methods [due:: 2026-07-05] #p1
- [ ] Practice distinguishing attributes from classes in requirements [due:: 2026-07-07] #p2
- [ ] Use Noun analysis on a new system of your choice (e.g., Hospital, Bank) [due:: 2026-07-10] #p3

---

## 🧠 Flashcards

What is Object-Oriented Analysis (OOA)? :: The process of **discovering classes** from a system's requirements. It sits between requirements gathering and design in the SDLC. It answers: "What classes do we need to build this system?"

What does the Noun/Verb Method state about nouns and verbs? :: **Nouns** in requirements → **Candidate Classes** (or objects). **Verbs** in requirements → **Candidate Methods**. Common nouns = classes; proper nouns = objects.

What are the 5 rules for rejecting noun candidates? :: 1. Redundant (same thing named twice), 2. Meta-language (language about language, not domain), 3. Event or operation (a thing that happens, not a thing), 4. Outside scope of system, 5. An attribute of another class.

What is the difference between a Common Noun and a Proper Noun in OOA? :: **Common Noun** (e.g., "Person") → maps to a **Class**. **Proper Noun** (e.g., "Jagath", "Keels") → maps to an **Object** (specific instance).

In the Library System example, why is "ISBN" rejected as a class? :: It is an **attribute** of the Book class — it belongs to Book as a property, not as its own independent class.

In the Library System example, why is "Department (IT/SE/ISE)" rejected? :: It is **outside the scope** of the library system — it belongs to the university infrastructure, not the library domain.

In the Online Order System, why is "Administrator" rejected as a class? :: Administrator is an **Actor** (outside the system) who interacts with the system but does not have domain data relevant to the application. Actors typically don't become classes unless they need their own data in the system.

What are the resulting classes from the Online Order System analysis? :: `Customer`, `Order`, `Item`, `Payment`

What should you do when it's unclear which class a method belongs to? :: Use **[[CRC cards]]** (Class-Responsibility-Collaboration cards) to resolve the ambiguity by exploring collaborations between classes.

Give the steps of Noun/Verb Analysis. :: 1. Extract all nouns → candidate classes/objects. 2. Separate common nouns (classes) from proper nouns (objects). 3. Apply 5 rejection rules. 4. Survivors = classes. 5. Extract verbs → candidate methods. 6. Assign methods to classes.

What verbs map to what classes in the Online Order System? :: Customer → register(). Payment → validate(). Order → placeOrder(), getStatus(), confirmOrder(). Item → addItem(), restockItem(), updateItem(). Report → generateItemList(), getPreviousOrders().

What is OOA's place in the SDLC? :: OOA sits between **Requirements Gathering** and **Design**. It takes requirements (use cases, user stories) and produces a set of candidate classes and methods for the design phase.

Why is "list of previous orders" rejected as a class in the Online Order System? :: It is **redundant** — the `Order` class already handles order data. "List of previous orders" is not a new concept but a query/operation on existing Order data.

What inputs does the Noun/Verb Method use? :: The **requirements/problem statement**, which can come from [[use cases]], [[use case scenarios]], or [[user stories]].

What are the resulting classes in the DVD rental store example? :: DVD, Registered Member, and Unregistered Member. (Member is redundant; Fine, Deposit, and Rate are attributes, not classes.)

In the DVD rental example, why is "Fine" not a class? :: Because it is an attribute (a value calculated for a member), not an independent domain object.

#flashcards
