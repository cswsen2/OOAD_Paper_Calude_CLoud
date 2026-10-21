---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 2
aliases: [Requirements Engineering, requirements engineering]
topics:
  - requirements engineering
  - functional requirements
  - non-functional requirements
  - stakeholders
  - scenarios
  - user stories
  - use cases
  - actors
---

# Requirements Engineering

> **Source**: SE2012 OOAD — Lecture 02 | Prof. Jagath Samarabandu & Mr. Jeewaka Perera
> **Textbook**: Requirements Engineering for Software and Systems, 4th Edition — Chapter 1

## Overview

[[requirements engineering]] is the branch of engineering concerned with the real-world **goals, functions, and constraints** on systems. It involves:

- **Defining** requirements
- **Documenting** requirements
- **Maintaining** requirements

Every software system begins with requirements. Without understanding requirements, no [[object-oriented programming]] solution can be designed effectively. This is why requirements form the **first serious output** of any [[software development life cycle]].

---

## What are Requirements?

Requirements specify **what is expected from the solution** to a problem. They can range from:

- High-level, abstract statements
- Back-of-the-napkin sketches
- Formal (mathematically rigorous) specifications

The diversity in form exists because [[stakeholders]] operate at different abstraction levels and have varying abilities to articulate needs (e.g., a business customer vs. a design engineer).

---

## Requirements vs. Features vs. Goals

These three terms are often confused:

| Concept | Definition |
|---|---|
| **Goal** | High-level objective of a business, organization, or system |
| **Feature** | A set of logically related requirements allowing a user to satisfy a goal |
| **Requirement** | Specifies how a goal should be accomplished by a proposed system |

### Example — Smart Home System

- **Goal**: Automate tasks that don't need human interaction, so occupants can enjoy other activities
- **Feature**: Automated water purification
- **Requirements**: Specific descriptions of *how* the water purification mechanism works (more granular, implementation-minded)

---

## Requirement Classification

Requirements can be classified by two main criteria:

### By Level
| Level | Description |
|---|---|
| **User Requirements** | Abstract statements in natural language (or informal diagrams) specifying services and constraints the system should provide. Often captured as a **Concept of Operations (ConOps)** document. [[user stories]] can serve as user requirements. |
| **System Requirements** | Detailed, structured, and precise descriptions of services and constraints. Collected in a **Systems Requirements Specification (SRS)**. [[use cases]] can play this role. |
| **Design Specifications** | Emerge from analysis and design documentation, derived directly from the SRS; used as basis for implementation. |

### By Type
| Type | Description |
|---|---|
| **[[functional requirements]]** | Describe services the system should provide and how it reacts to inputs |
| **[[non-functional requirements]]** | Describe system quality attributes (security, reliability, performance, etc.) |
| **Domain Requirements** | Derived from the application domain; reflect characteristics and constraints of the domain |

> [!QUESTION] Example — The three levels in a Point-of-Sale system (Slide 10)
> - **User requirement**: *"The system shall accurately compute sale totals including discounts, taxes, refunds, and rebates; print an accurate receipt; and update inventory counts accordingly."*
> - **System requirements** (derived & precise): each sale shall be assigned a sales ID; each sale may have one or more sales items; each sale may have one or more rebates; each sale may have only one receipt printed.
> - **Software specifications** (numbered, design-ready): *1.2 — The system shall assign a unique sales ID to each sale transaction. 1.2.1 — Each sales ID may have zero or more sales items, but each sales item must be assigned to exactly one sales ID…*

---

## Functional Requirements (FRs)

[[functional requirements]] describe the **services the system should provide** and how it will react to its inputs.

Key characteristics:
- Must explicitly state certain behaviors the system **should NOT do**
- Can be high-level (user requirements) or detailed (system requirements expressing inputs, outputs, exceptions)

---

## Non-Functional Requirements (NFRs)

[[non-functional requirements]] characterize system behavior quality. In competitive markets, NFRs become the differentiator between functionally equivalent products.

Common NFRs:
- **Security**
- **Reliability**
- **Maintainability**
- **Performance**
- **Usability**
- **Testability**
- **Interoperability**
- **Constraints**: design, implementation, financial, resource constraints

---

## The Requirements Engineering Process

The full [[requirements engineering]] process consists of five activities:

```
1. Requirements Elicitation / Discovery
        ↓
2. Requirements Analysis and Reconciliation
        ↓
3. Requirements Representation / Modeling
        ↓
4. Requirements Verification and Validation
        ↓
5. Requirements Management
```

### 1. Requirements Elicitation / Discovery

Involves **uncovering what the customer needs and wants**. Includes:

- Discovering who the [[stakeholders]] are (including hidden stakeholders)
- Determining [[non-functional requirements]] (often overlooked)
- Some requirements are obvious; many need to be extricated through structured approaches

#### Obstacles in Requirements Elicitation

| Obstacle | Problem | Solution |
|---|---|---|
| **New Project Domain** | Requirements engineer lacks domain knowledge | Engage a domain expert |
| **Unclear Project Vision** | Stakeholders don't know what functionality they need | Create a clear mission statement or ConOps |
| **Limited Access to Documentation** | Can't access docs, or evaluating current state takes too long | Use disciplined document/change management systems |
| **Focusing on Solution Instead of Requirements** | Customer describes architectural tactics, not requirements | Active expectation management |
| **Fixation on Specific Functionalities** | Stakeholders insist on certain features | Expectation management; refocus on mission statement |
| **Contradictory Requirements** | Wide range of stakeholders with conflicting needs | Reconciliation through negotiation |

#### Gathering Requirements — Identifying Stakeholders

[[stakeholders]] are people or entities with different desires (desiderata) from a system. There may be various sub-groups.

**Steps in Gathering Requirements:**
1. Identify **all** customers and stakeholders
2. Partition them into classes (by interests, scope, authorization)
3. Select a **champion or representative** for each class
4. Select appropriate elicitation **techniques** for each class/group

#### Example — Point-of-Sale (POS) System Stakeholders

| Stakeholder Group |
|---|
| Cashiers |
| Managers |
| System maintenance personnel |
| Store customers |
| Inventory/warehouse personnel |
| Accountants (tax information) |
| Sales department (pricing, discounting) |

#### Techniques for Gathering Requirements

The lecture lists many elicitation techniques (Slide 24). The three highlighted below are explored in depth in this lecture (and feed directly into [[object-oriented analysis]]):

| | | |
|---|---|---|
| Brainstorming | Goal-based approaches | Quality function deployment (QFD) |
| Card sorting | Group work | Questionnaires |
| Crowdsourcing | Interviews | Repertory grids |
| Designer as apprentice | Introspection | Reverse engineering |
| Domain analysis | Joint application development (JAD) | **[[scenarios|Scenarios]]** |
| Ethnographic observation | Laddering | Task analysis |
| Protocol analysis | Prototyping | **[[use cases|Use cases]]** |
| **[[user stories|User stories]]** | Viewpoints | Workshops |

### 2. Requirements Analysis and Reconciliation

After collection, requirements in their **"raw" form** have several problems — they:

- don't always make sense;
- may **contradict** one another (not always obviously);
- may be **inconsistent**;
- may be **incomplete**;
- may be **vague or just wrong**;
- may **interact** and be dependent on each other.

Many elicitation techniques (and **formal methods**) are intended to avoid or alleviate these problems.

### 3. Requirements Representation / Modeling

Converting the processed requirements into a *model* (usually natural language, mathematics, and visualizations). Proper representations facilitate communication and conversion into a system architecture and design. Techniques are:

| Representation | Meaning |
|---|---|
| **Informal** | natural language, sketches, diagrams |
| **Formal** | mathematically sound representations |
| **Semiformal** | convertible to a sound representation, or made fully formal by adding a semantic framework |

Usually some **combination** of these is employed.

### 4. Requirements Verification and Validation

**Validation** determines if the specification is a *correct representation of the customers' needs* — it answers the question:

> [!QUESTION] "Am I building the right product?"

It involves semiformal and formal methods, text-based tools, visualizations, and inspections.

### 5. Requirements Management

One of the **most overlooked** aspects of [[requirements engineering]]. It involves:

- managing the realities of **changing requirements** over time;
- fostering **traceability** through aggregation and subordination of requirements;
- communicating changes to those who need to know;
- learning to intelligently **push back when scope creep** ensues.

Using tools to track changes and maintain traceability significantly eases the burden.

---

## Scenarios

A **scenario** is a narrative description of a system in use in a particular context. Scenarios are realistic and concrete — they tell a story of how the system is actually used.

### Example — POS System Scenario

> A customer arrives at the checkout with several items. The cashier asks if the customer has a loyalty card. If so, the cashier swipes it, authenticating the customer. The cashier scans products using a bar code reader. Each scan updates the inventory and computes the sale. Upon completion, a subtotal is computed, coupons and discounts are entered, taxes are added, a receipt is printed, and the customer pays using cash, credit card, debit card, or check.

Scenarios highlight real-world edge cases (like loyalty card authentication) that pure requirement lists might miss.

---

## User Stories

[[user stories]] are an extension of scenarios narrated from the **perspective of a user**. They are:

- Short, simple descriptions of a feature told from the user's perspective
- Used in [[agile development]] to capture user needs quickly
- Well-structured using the **Who, What, Why** template

### User Story Format

```
As a [user], I want [goal] so that [benefit].
```

| Field | Description |
|---|---|
| **User** | Who is using the feature |
| **Goal** | What the user wants to achieve |
| **Benefit** | Why the user wants to achieve this goal |

### Example

> **As a** library member, **I want** to renew a borrowed book online, **so that** I don't have to visit the library in person.

---

## Use Cases

[[use cases]] capture and document **functional requirements** by describing interactions between a user (or [[actor]]) and the system to achieve a specific goal.

### Core Properties of Use Cases

- Provide a **measurable result** to a user or external system
- Describe requirements strictly from the **outside looking in**
- Specify the **value** the system delivers to users
- Are the **first serious output** from your model after a project starts
- Are at the **heart of the model** — they affect and guide all other design elements

### Why Use Cases Are Central to OOD

Use cases are usually the best **starting point** for the [[object-oriented analysis]] and design process because:
- You cannot design a system without knowing what it must do
- They bring requirement gaps to the forefront early
- When a gap is found, go back to [[stakeholders]] — they may realize the requirement has little value

### Advantages of Use Cases

1. **Priority and Risk Management**: Assign priorities and risks to each use case; manage project workload
2. **Team Assignment**: Use cases can be assigned to teams or individuals
3. **Progress Tracking**: Track project progress by use cases delivered
4. **Scope Control**: Use cases can be delayed or dropped to deliver highest value first
5. **Test Construction**: Precisely capture success criteria for testing

---

## Constructing a Use Case

### Step 1: Identify Actors

**[[actor|Actors]]** are things that interact with the system.

Key facts about actors:
- Actors do NOT need to be people — they can be **external systems**
- Actors are like a **black box**: you cannot change them; you are not interested in how they work
- Actors may not be limited to direct users — includes **auditors, installers, maintainers, upgraders**

**Representations of an actor:**
- A "stick man" (UML standard)
- A stereotyped box with `«actor»` label

#### Terminology in Requirements

| Term | Meaning |
|---|---|
| **shall** | The requirement MUST be fulfilled; if absent, system fails the requirement |
| **should** | The requirement is desirable but not critical; sacrificed first under pressure |

#### Example — CMS Weblog Actors

From requirement: *"The CMS shall allow an administrator to create a new blog account, provided personal details are verified using the author credentials database."*

- **Administrator**: Interacts with the system → is an **actor**
- **Authors**: Also actors
- **Users**: Also actors

Some actors are related — Administrator and Author are both special kinds of system users. This relationship is shown using a **generalization arrow** (Administrator can do everything a User can, plus more).

### Step 2: Identify Use Cases

Find cases where the system is being used to **complete a specific job for an actor**. Use cases:
- Can be identified from user requirements
- Distill wordy, blurry requirement definitions into clear system jobs
- Must have clear **pass/fail criteria**

**Representing a Use Case:**
- An **oval shape** with text inside naming the use case

### Step 3: Connect Actors to Use Cases

A **communication line** connects an actor to a use case it participates in.

---

## Relationships Between Concepts

[[requirements engineering]] → feeds into → [[use cases]]
[[use cases]] → guide → [[object-oriented analysis]]
[[object-oriented analysis]] → produces → [[class diagram]]
[[user stories]] → equivalent to → user requirements
[[functional requirements]] ↔ [[non-functional requirements]] (complementary)
[[stakeholders]] → provide → [[functional requirements]] and [[non-functional requirements]]
[[actor]] → participates in → [[use cases]]
[[agile development]] → uses → [[user stories]]

---

## 📅 Tasks

- [ ] Practice writing use case scenarios for the Baggage Handling System [due:: 2026-07-01] #p1
- [ ] Construct use cases for the CMS Weblog requirement [due:: 2026-07-01] #p1
- [ ] Identify stakeholders for the Point-of-Sale system and classify them [due:: 2026-07-07] #p2
- [ ] Write user stories for a given system following the Who/What/Why format [due:: 2026-07-07] #p2

---

## 🧠 Flashcards

What is the difference between a Goal, a Feature, and a Requirement? :: A **Goal** is a high-level business objective. A **Feature** is a set of logically related requirements that helps satisfy a goal. A **Requirement** specifies exactly how the system should accomplish the goal — more granular and implementation-focused.

What are the three levels of requirements? :: **User Requirements** (abstract, natural language), **System Requirements** (detailed, precise — SRS document), **Design Specifications** (emerge from system requirements analysis, used for implementation)

What is the difference between Functional and Non-Functional Requirements? :: **Functional Requirements (FRs)** describe services the system provides and how it reacts to inputs. **Non-Functional Requirements (NFRs)** describe quality attributes like security, reliability, performance, usability, and maintainability.

What are the five steps of the Requirements Engineering Process? :: 1. Elicitation/Discovery → 2. Analysis and Reconciliation → 3. Representation/Modeling → 4. Verification and Validation → 5. Management

What is requirements elicitation? :: The process of uncovering what the customer needs and wants, discovering stakeholders (including hidden ones), and determining both functional and non-functional requirements.

What does "shall" mean in requirements terminology vs "should"? :: **Shall** = MUST be fulfilled; if not present in the final system, the system fails this requirement. **Should** = Desirable but not critical; often sacrificed first if there are delivery delays.

What is a Use Case? :: A way to capture and document functional requirements by describing interactions between an actor and the system to achieve a specific, measurable goal.

What is an Actor in a use case? :: Anything that interacts with the system. Does NOT have to be a person — can be an external system. Actors are like a black box: you cannot change them and don't care how they work internally.

How is an actor represented in a Use Case Diagram? :: Either as a "stick man" (UML standard) or a stereotyped box with the «actor» label.

How do you identify use cases? :: Look for cases where the system is used to complete a specific job for an actor. Distill wordy requirement definitions into clear, pass/fail system jobs.

What is the format of a User Story? :: "As a [user], I want [goal] so that [benefit]." — captures Who, What, and Why.

What is a Scenario in requirements engineering? :: A realistic, narrative description of a system being used in a specific context. It tells a concrete story of a system interaction, helping to uncover edge cases and real-world usage patterns.

Why are use cases the "heart of the model" in OOD? :: Because they affect and guide ALL other design elements. You cannot design anything until you know what the system must do. They also surface requirement gaps early — before costly implementation begins.

What is a Concept of Operations (ConOps) document? :: A document that collects user requirements in natural language. User stories can play the role of ConOps content.

Name 5 common Non-Functional Requirements. :: Security, Reliability, Maintainability, Performance, Usability (also: Testability, Interoperability, Constraints)

What is a generalization arrow in a use case diagram (for actors)? :: An arrow showing that one actor type is a specialization of another. E.g., Administrator and Author are both specializations of User — Administrator can do everything a User can, plus more.

What is the difference between a user story and a use case? :: A **user story** is a short, informal description of a feature from a user's perspective (Who/What/Why). A **use case** is a more structured, detailed description of the full interaction sequence between an actor and the system, with pass/fail criteria.

What are the steps in gathering requirements? :: 1. Identify all stakeholders → 2. Partition stakeholders into classes → 3. Select a champion/representative per class → 4. Choose elicitation techniques per class

What obstacle occurs when a customer focuses on architectural solutions instead of requirements? :: "Focusing on the Solution Instead of Requirements" — resolved through active expectation management.

What problems do requirements have in their "raw" form (analysis & reconciliation)? :: They may not make sense, contradict one another, be inconsistent, incomplete, vague or wrong, and interact/depend on each other.

What are the three types of requirements representation? :: Informal (natural language, sketches, diagrams), formal (mathematically sound), and semiformal (convertible to a formal representation).

What question does requirements validation answer? :: "Am I building the right product?" — whether the specification correctly represents the customers' needs.

What does requirements management deal with? :: Managing changing requirements over time, fostering traceability, communicating changes, and pushing back against scope creep.

Name three techniques for gathering requirements. :: Examples include brainstorming, interviews, questionnaires, prototyping, JAD, scenarios, use cases, and user stories.

#flashcards
