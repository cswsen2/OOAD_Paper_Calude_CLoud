---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 0
topics:
  - module overview
  - learning outcomes
  - assessment
  - object orientation
  - evolution of programming languages
  - history of oop
aliases:
  - OOAD Module Overview
  - Introduction to the Unit
  - Object Orientation
  - object orientation
---

# OOAD Module Overview & Introduction to Object Orientation

> **Source**: SE2012 OOAD — Lecture 00: *Introduction to the Unit*

This lecture introduces the **delivery, objectives, contents, and assessment** of the Object Oriented Analysis and Design module, and then opens the conceptual story of why software moved toward **[[object orientation]]**. It is the map for everything that follows — [[Java]], [[UML]], [[Requirements Engineering]], the [[UML Class Relationships|class relationships]], behavioural modelling, [[Java Collections Framework|collections]], [[Java Generics|generics]], [[Threads|concurrency]], the [[SOLID principles]], and finally the [[design patterns]].

> [!NOTE] Lesson objectives
> At the end of the lesson, you should be able to:
> - Understand the **delivery** of the module.
> - Explain the **objectives** of the module.
> - Gain a basic understanding of the **contents** of the module.
> - Understand the **assessment criteria** of the module.

---

## Module Details and Delivery

| Item | Value |
| --- | --- |
| **Credits** | 4 |
| **Lecture** | 3 Hours |
| **Practical** | 2 Hours |

> [!IMPORTANT] Independent study expectation
> You are expected to put in **at least 2 hours for each hour you spend in lectures** to study the concepts in depth, work on assessments, and carry out independent study.

---

## Module Objectives (Learning Outcomes)

| Code | Learning Outcome |
| --- | --- |
| **LO1** | Apply the object-oriented concepts to design and implement [[UML]] diagrams using [[Java]] and vice-versa. |
| **LO2** | Apply **concurrency programming** in application development. |
| **LO3** | Analyze the application of object-oriented concepts in **[[design patterns]]**. |
| **LO4** | Design a complete **[[Requirements Engineering|requirements engineering]]** process through object-oriented analysis using **[[Use Case Diagrams]]** and **[[Activity Diagrams]]**. |
| **LO5** | Design the **behaviour of a system** through interaction and state chart diagrams. |

---

## Module Contents (Week-by-Week)

This is the full delivery plan for the module. Each entry links to its dedicated concept page where one exists in the vault.

### Week 01 — Lecture 01: Introduction to the Module & Introduction to [[Java]]
- Brief Introduction to [[Java]]
- [[Java Development Kit]] (JDK), [[Java Virtual Machine]] (JVM), [[Java Runtime Environment]] (JRE)
- Java Doc
- [[Java]] Classes
- [[Java]] Data Types
- [[access modifiers|Access Modifiers]]
- [[Java]] Control Structures

> See **[[Java Programming]]** for the full treatment of this week.

### Week 02 — Lecture 02: Introduction to [[UML]] 2.0 & [[Requirements Engineering]]
- What is [[UML]]
- Why [[UML]] is needed
- [[UML]] Tools
- What is [[Requirements Engineering]]?
- Importance of [[Requirements Engineering]]
- **Stakeholders** in [[Requirements Engineering]]
- Techniques for **Gathering Requirements**
- **Documenting Requirements**

### Week 03 — Lecture 03: [[Use Case Diagrams]] and Use Case Scenarios
- [[Use Case Diagrams]] and Use Case Scenarios
- **User Stories**

### Week 04 — Lecture 04: Object-Oriented Design Principles with [[UML]]
- Classes and Objects
- Class Diagrams: Basics
- Identifying Classes: **[[OO Analysis Noun Verb|Verb-Noun Analysis]]**
- **[[CRC Cards|Class Responsibility Collaboration (CRC) Cards]]**
- Relationships between Classes
- **Boundary, Entity, and Control Classes**
- Implementation of Classes and Objects in [[Java]]

> See **[[OOP Fundamentals]]**, **[[OO Analysis Noun Verb]]**, and **[[CRC Cards]]**.

### Week 05 — Lecture 05: Object-Oriented Design Principles
- [[abstraction|Abstraction]]
- [[interface|Interfaces]]
- [[encapsulation|Encapsulation]]
- [[inheritance|Inheritance]]: Superclasses and Subclasses
- [[polymorphism|Polymorphism]]
- [[composition|Composition]] and [[aggregation|Aggregation]]

> See **[[OOP Fundamentals]]** and **[[UML Class Relationships]]**.

### Week 06 — Lecture 06: Behavioral Modeling using [[Java]] and [[UML]] Diagrams
- **Interaction Diagrams**: Sequence and Communication Diagrams
- **State Chart Diagrams**
- **[[Activity Diagrams]]** with Swim lanes
- Modeling System Behavior

### Week 08 — Lecture 07: [[Java]] Exception Handling & Collections/Generics
- Error Handling in [[Java]]
- Exceptions: Try-Catch-Finally
- **Custom Exceptions**
- Introduction to [[Java Collections Framework]]
- Types of Collections: [[List]], [[Set]], [[Map]]
- Using [[Java Generics|Generics]] in [[Java]]
- Iterating through Collections
- Best Practices for Collections and Generics

> See **[[Errors and Exceptions]]**, **[[Java Collections Framework]]**, and **[[Java Generics]]**.

### Week 09 — Lecture 08: Concurrency in [[Java]]
- Introduction to **Concurrency**
- **Thread** Creation and Manipulation
- **Multithreading** in [[Java]]
- **Synchronized** Methods and Blocks
- **Locks and Semaphores**
- Best Practices for Concurrent Programming

> See **[[Threads]]**.

### Week 10 — Lecture 09: [[SOLID principles|SOLID Principles]] in Object-Oriented Design (Part 1)
- **Single Responsibility Principle (SRP)**
- **Open/Closed Principle (OCP)**

### Week 11 — Lecture 10: [[SOLID principles|SOLID Principles]] (Part 2)
- **Liskov Substitution Principle (LSP)**
- **Interface Segregation Principle (ISP)**
- **Dependency Inversion Principle (DIP)**

> The **[[dependency inversion principle]]** is explored in depth in the **[[Factory Pattern]]** lecture.

### Week 12 — Lecture 11: Introduction to [[design patterns|Design Patterns]]
- What are [[design patterns|Design Patterns]]?
- Relationship between OOP Concepts and Design Patterns
- **Gang of Four (GoF)** Design Patterns
- **Creational Patterns**

> See **[[Design Patterns]]**, plus the deep-dives: **[[Singleton Pattern]]**, **[[Factory Pattern]]**, **[[Command Pattern]]**.

### Week 13 — Lecture 12: Structural & Behavioral Patterns
- **Structural Patterns**
- **Behavioral Patterns**

---

## Assessment and Passing Criteria

> [!IMPORTANT] To pass the module
> You need to **both**:
> - Obtain a passing mark for the **CA (Continuous Assessment)**, **and**
> - Obtain a passing mark for the **Final exam**.

### Assessment Breakdown

| Weight | Maps to LOs | Component |
| --- | --- | --- |
| **20%** | LO1, LO4, LO5 | Mid-Semester Examination |
| **5%** | LO1 – LO5 | Laboratory Submissions |
| **25%** | LO1 – LO5 | Group Project |
| **50%** | LO1 – LO5 | End of Semester Examination |

The assessed components are:
- **Mid-Semester examination**
- **Laboratory Submissions**
- **Group Project**
- **End of Semester Examination**

---

## Introduction to Object Orientation

### Evolution of Programming Languages

The lecture frames object orientation as the answer to limitations that earlier paradigms could not solve.

**Early Programming Languages:**

| Era | Language Level | Description |
| --- | --- | --- |
| 1940s–1950s | **Machine Language** | Binary code directly executed by the computer. |
| 1950s–1960s | **Assembly Language** | Low-level code with symbolic representations. |
| 1960s–1970s | **High-Level Languages** | FORTRAN, COBOL, BASIC — abstracted machine details. |

**Procedural Programming:**
- Focus on **procedure calls and routines** (e.g., C, Pascal).
- Code organized into **functions**, with a **separation of data and behavior**.

### Necessity for Object Orientation

> [!QUESTION] Why did we need a new paradigm?
> **Challenges with Procedural Programming:**
> - Difficult to manage **large codebases**.
> - Code **reusability** issues.
> - **Maintenance and scalability** problems.
>
> **Emergence of Object Orientation:**
> - Addresses procedural programming limitations.
> - Emphasizes **modularity, reusability, and abstraction**.

### Key Concepts of Object Orientation

| Concept | Meaning |
| --- | --- |
| **Modularity** | Breaking down complex systems into manageable, reusable pieces. |
| **Reusability** | Promoting code reuse through [[inheritance]] and [[polymorphism]]. |
| **Maintenance** | Simplifying code maintenance by [[encapsulation|encapsulating]] changes within objects. |
| **Scalability** | Enabling easier expansion and adaptation of software systems. |

> These four concepts are the through-line of the whole module — [[encapsulation]] underlies the [[command pattern]]'s "encapsulate a request", [[inheritance]] drives the [[factory method pattern]], and [[modularity]] is what the [[SOLID principles]] formalize.

### History of Object Orientation

A clean timeline of how OO concepts accumulated, language by language.

| Decade | Language | Creator(s) | Contribution to OO |
| --- | --- | --- | --- |
| **1960s** | **Simula** | Ole-Johan Dahl & Kristen Nygaard | Introduced **classes and objects**, **inheritance**, and **dynamic binding**. |
| **1970s** | **Smalltalk** | Alan Kay and others at Xerox PARC | Fully realized OOP concepts such as **encapsulation, inheritance, and polymorphism**. |
| **1980s** | **Ada** | U.S. Department of Defense | Incorporated **strong typing, modularity**, and some OOP features like **packages**. |
| **1980s** | **C++** | Bjarne Stroustrup | Extended C with **classes, inheritance, and polymorphism**, bringing OOP to a broader audience. |
| **1990s** | **[[Java]]** | Sun Microsystems | Brought **"write once, run anywhere"** capability with a strong emphasis on OOP. |
| **2000s** | **Modern OOP Languages** | — | Languages like C#, [[Python]], and Ruby emphasized and expanded OOP principles. |

> [!NOTE] Where the rest of the vault picks up
> The four pillars introduced here — encapsulation, inheritance, polymorphism, and abstraction — are detailed in **[[OOP Fundamentals]]**. This module then layers analysis ([[Requirements Engineering]], [[CRC Cards]], [[OO Analysis Noun Verb|noun-verb analysis]]), modelling ([[Use Case Diagrams]], [[Activity Diagrams]], [[UML Class Relationships]]), advanced Java ([[Java Collections Framework]], [[Java Generics]], [[Errors and Exceptions]], [[Threads]]), and finally [[design patterns]].

---

## 📅 Tasks

- [ ] Review the full module syllabus and map each week to its vault note [due:: 2026-07-02] #p3
- [ ] Confirm Mid-Semester examination scope (covers LO1, LO4, LO5 = 20%) [due:: 2026-07-09] #p2
- [ ] Track Laboratory Submissions (5%) and Group Project (25%) deliverables across the semester [due:: 2026-07-09] #p2

---

## 🧠 Flashcards

How many credits is the SE2012 OOAD module worth? :: 4 credits (3 hours lecture, 2 hours practical per week).

What is the expected independent-study ratio for the module? :: At least 2 hours of self-study for every 1 hour spent in lectures.

What does Learning Outcome LO1 require? :: Apply object-oriented concepts to design and implement UML diagrams using Java and vice-versa.

What does Learning Outcome LO2 require? :: Apply concurrency programming in application development.

What does Learning Outcome LO3 require? :: Analyze the application of object-oriented concepts in design patterns.

What does Learning Outcome LO4 require? :: Design a complete requirements engineering process through OO analysis using Use Case Diagrams and Activity Diagrams.

What does Learning Outcome LO5 require? :: Design the behaviour of a system through interaction and state chart diagrams.

What are the two conditions to pass the OOAD module? :: Obtain a passing mark for the CA (Continuous Assessment) AND a passing mark for the Final exam.

What is the assessment breakdown for OOAD? :: Mid-Semester exam 20% (LO1,LO4,LO5), Lab Submissions 5%, Group Project 25%, End of Semester exam 50%.

What were the three eras of early programming languages? :: Machine Language (1940s–50s, binary), Assembly Language (1950s–60s, symbolic), and High-Level Languages (1960s–70s, e.g. FORTRAN/COBOL/BASIC).

What characterizes procedural programming? :: A focus on procedure calls and routines (e.g. C, Pascal), with code organized into functions and a separation of data and behavior.

What three problems with procedural programming motivated object orientation? :: Difficulty managing large codebases, code reusability issues, and maintenance/scalability problems.

What are the four key concepts of object orientation? :: Modularity, Reusability, Maintenance, and Scalability.

Which language first introduced classes, objects, inheritance, and dynamic binding? :: Simula (1960s), by Ole-Johan Dahl and Kristen Nygaard.

Which language fully realized encapsulation, inheritance, and polymorphism? :: Smalltalk (1970s), developed by Alan Kay and others at Xerox PARC.

Who created C++ and what did it contribute? :: Bjarne Stroustrup; it extended C with classes, inheritance, and polymorphism, bringing OOP to a broad audience.

What capability did Java (1990s, Sun Microsystems) bring? :: "Write once, run anywhere" with a strong emphasis on OOP.

#flashcards
