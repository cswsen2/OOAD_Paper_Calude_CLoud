---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: "04 & 05a"
aliases: [OOP Fundamentals, object-oriented programming, OOP, classes and objects]
topics:
  - object-oriented programming
  - classes and objects
  - abstraction
  - encapsulation
  - information hiding
---

# OOP Fundamentals — Classes, Objects, Abstraction, and Encapsulation

> **Source**: SE2012 OOAD — Lecture 04 & Lecture 05a | Prof. Jagath Samarabandu & Mr. Jeewaka Perera
> **Reference**: Grady Booch et al. (2008), Object-Oriented Analysis and Design with Applications, 3rd Edition

## Overview

[[object-oriented programming]] (OOP) is a method of implementation in which programs are organized as a **collection of objects** which cooperate to solve a problem. It allows solving more complex problems by breaking them into manageable, reusable units.

This page covers the **core conceptual pillars** that underpin all of OOP:
- [[object]] and [[class]] relationship
- [[abstraction]]
- [[encapsulation]] and information hiding

---

## Why Object-Oriented Programming?

A complex system is developed using **smaller sub-systems**. These sub-systems are:
- **Independent units** containing their own data and functions
- **Reusable** — the same unit can solve many different problems

The analogy: just as a building is assembled from individual blocks, an OO program is assembled from objects. Each block (object) is manufactured using a mould (class).

---

## Objects

> [!NOTE] Object — general (dictionary) meaning
> *object (noun): a material thing that can be seen and touched* — "he was dragging a large object." Synonyms: thing, article, item, piece, device, gadget, entity, body.

An **object** is a real-world entity that has both:
- **State** (properties/data/attributes) — *what it knows*
- **Behaviour** (functions/methods) — *what it can do*

### Objects in the Real World

Everything around us is an object. The lecture illustrates this with a table of scattered everyday items (cutlery, glasses, pens, blocks, a football) and then shows **grouping related things together** — the intuitive basis for classifying objects into classes. Examples:
- A specific student (e.g., *Manoj* in SIS)
- A specific book (e.g., *my copy of Learning UML 2.0*)
- A specific lecturer (e.g., *Mr. Jeewaka*)

An **object** is a **specific instance** (variable) of a data type ([[class]]).

---

## Classes

A **class** is the **blueprint/mould** from which objects are created. Classes are **concepts** — they classify objects by focusing on their essential properties.

> "A class is a blue print of an object."

### The Mould Analogy (LEGO)

```
Mould (Class)  →  used to manufacture →  Blocks (Objects)
```

You can make as many objects as you want from a single class, just like manufacturing many LEGO blocks from one mould — or building many houses from one architectural blueprint.

### The House Blueprint Analogy

```
House Plan / Blueprint  (Class)
         ↓
    Contractor builds
         ↓
  Your Dream House  (Object)
```

From **one blueprint**, a contractor can build **many houses** (multiple objects from one class).

### Formal Definition

> An object is a **specific instance (variable)** of the data type (**class**).

---

## Identifying Objects and Classes — Activity Examples

### Activity 1 — Classify These

| Item | Object or Class? |
|---|---|
| Mr. Jeewaka | **Object** (specific individual → Lecturer class) |
| *Learning UML 2.0* (O'Reilly book) | **Class** (the concept "textbook") |
| My copy of Learning UML 2.0 | **Object** (specific instance of Book) |
| A student | **Class** |
| A student at SLIIT | **Object** (specific enough) |
| The person sitting next to you | **Object** |

### Activity 2 — Properties of Student Class

What do we need to store to describe a student?
- Name
- Age
- Student ID
- Department
- Year / Semester
- GPA
- ... *(domain-specific)*

### Activity 3 — Payroll System: Employee Class Properties

Example properties for an `Employee` class:
- Employee ID
- Name
- Department
- Salary
- Designation
- Hours Worked
- Leave Balance

---

## Abstraction

[[abstraction]] is the process of **removing non-essential characteristics** from something in order to reduce it to a set of **essential characteristics** needed for a particular system.

### Three Steps of Abstraction:

1. **Distinguish** between different objects
2. **Classify** objects into concepts (classes)
3. **Focus** on the common, essential properties (ignoring the irrelevant)

### Formal Definition (Grady Booch)

> "An abstraction denotes the essential characteristics of an object that distinguish it from all other kinds of objects and thus provide crisply defined conceptual boundaries, **relative to perspective of the viewer**."
> — Grady Booch et al. (2008), OOAD with Applications, 3rd Ed., p. 44

### Key Insight — Perspective Matters (the Cat metaphor)

> [!QUESTION] The same cat, two abstractions (Slide 15)
> The lecture uses a cartoon of a cat on a table viewed by two people:
> - A **pet-loving lady** abstracts the cat as *"purr, fuzz, cute, food"* — the affectionate essentials.
> - A **veterinary surgeon** abstracts the same cat as *anatomy* — kidney, stomach, heart, lung, liver, bladder, intestine.
>
> *"Abstraction focuses on the essential characteristics of some object, relative to the perspective of the viewer."* The two viewers keep entirely different essential characteristics for the **same** object.

The **classify-into-concepts** idea is also shown with a *Dog Class* (two different dogs) and a *Cat Class* — different individual objects sharing the common properties of their class.

### What Abstraction Achieves

- Allows complex systems to be modeled at the right level of detail.
- Creates **crisply defined conceptual boundaries** between classes, relative to the viewer's perspective.

---

## Encapsulation

[[encapsulation]] is the process of **grouping related attributes and methods together**, giving the unit a name, and providing a **public interface** for outsiders to interact with it.

### Formal Definition (Grady Booch)

> "Encapsulation is the process of compartmentalizing the elements of an abstraction that constitute its structure and behavior; encapsulation serves to **separate the contractual interface of an abstraction and its implementation**."
> — Grady Booch et al. (2008), p. 52

### Why Encapsulation? — The Jewelry Shop Analogy

In a jewelry shop:
- The **jewelry** (data/attributes) is locked in a display case (private)
- You can only access the jewelry **through a sales person** (public interface/methods)
- You cannot directly grab the jewelry yourself

This models the OOP principle: **all properties and some functions are private**; they can only be accessed through **public functions** (the interface).

### The TV Remote Analogy

You can control an OLED, LCD, Plasma, or CRT TV using the **same remote control commands** (interface), even though the internal implementation differs completely. The implementation is **hidden from you** — only the interface matters.

```
TV Implementation (Hidden)   ←→   Remote Control (Public Interface)
  OLED/LCD/CRT internals            ON, OFF, Volume, Channel
```

### The Car Interface Analogy (Slide 30)

You interact with an object only through its **interfaces** (steering wheel, gear stick, pedals). Your car can be **Gasoline, Hybrid, or Electric**, but you drive it the same way — the implementation under the hood is hidden behind a stable public interface.

---

## Information Hiding

[[information hiding]] is the principle of hiding implementation details that are **internal to the encapsulation structure (class)**.

- The **only** way to access an object is through its **public interface** (public functions)
- `public` → anyone can access/see it
- `private` → no one except the class itself can see/use it

### Why Is This Necessary?

> The lecture poses *"Why is this necessary?"* and answers it with the **jewelry shop** example above — controlled access through a trusted interface.

> [!OUTSIDE] This information was not present in the original lecture material.
> Expanding on *why* controlled access matters: without information hiding, external code can directly modify internal state (data corruption), implementation changes break external code (tight coupling), and no validation is possible before values are set. With it, data integrity is enforced through setter methods, the implementation can change freely, and the class controls how its data is accessed.

---

## Classes Capture Both Properties AND Behaviour

A **concept (class)** has both:
1. **Properties** (attributes) — what the object *knows/stores*
2. **Behaviour** (methods/functions) — what the object *can do*

Grouping both **properties and functions together** is called **[[encapsulation]]**.

### Example — Dog and Cat Classes (Slide 18)

The lecture contrasts two classes to show that behaviour is captured as functions:

```
┌─────────────────────┐      ┌─────────────────────┐
│      Dog Class      │      │      Cat Class      │
├─────────────────────┤      ├─────────────────────┤
│ name                │      │ name                │
│ owner               │      │ owner               │
│ breed               │      │ breed               │
│ work (e.g. police   │      │                     │
│        dog)         │      │                     │
├─────────────────────┤      ├─────────────────────┤
│ Bark()              │      │ Meow()              │
│ Fetch()             │      │ Purr()              │
└─────────────────────┘      └─────────────────────┘
```

> *Grouping properties and functions together is called **[[encapsulation]]**.*

### Example — Rectangle Class (Slide 19)

```
┌──────────────────────┐
│      Rectangle       │  ← Class Name
├──────────────────────┤
│ length               │  ← Properties (Attributes)
│ width                │
├──────────────────────┤
│ calcArea()           │  ← Functions (Methods / Behaviour)
│ calcPerimeter()      │
│ getLength()          │
│ getWidth()           │
│ setLength()          │
│ setWidth()           │
└──────────────────────┘
```

### Example — Employee Class (Slide 20)

```
┌──────────────────────────┐
│        Employee          │  ← Class name
├──────────────────────────┤
│ EmpNo                    │  ← Attributes / Properties / Data Members
│ Name                     │
│ Address                  │
│ BasicSalary              │
│ OtHrs                    │
│ OtRate                   │
├──────────────────────────┤
│ CalculateOTAmount()      │  ← Methods / Behaviors / member functions
│ CalculateNetSalary()     │
│ PrintPaySlip()           │
└──────────────────────────┘
```

### Example — JewelleryShop Class (Demonstrating Information Hiding, Slide 24)

```
┌──────────────────────────┐
│   JewelleryShop Class    │
├──────────────────────────┤
│ gems                     │  ← Private (Restricted)
│ jewellery                │
├──────────────────────────┤
│ viewJewellery()          │  ← Public (the Salesman does this)
│ buyJewellery()           │
└──────────────────────────┘
```

---

## Assembling Objects — The Final Product

Once objects are created from classes, they are **assembled together** to build the final solution — just like LEGO blocks assembled into a complete model.

In a real system like a **Student Information System (SIS)**:
- `Course` objects (OOC, IWT) + `Student` objects (Manoj, Gayani) cooperate to represent the full system

---

## Relationship to Other OOP Pillars

[[abstraction]] → identifies what properties/methods a class needs
[[encapsulation]] → bundles those properties/methods together with access control
[[inheritance]] → allows one class to acquire properties/behaviour of another
[[polymorphism]] → allows different objects to be treated uniformly through their interface

All four are enabled by the [[class]]/[[object]] model established in this lecture.

---

## Related Concepts

- [[object-oriented analysis]] — uses these concepts to discover classes
- [[class diagram]] — visually represents classes and their relationships
- [[noun-verb analysis]] — technique to identify classes from requirements
- [[CRC cards]] — technique to identify class responsibilities
- [[information hiding]] — principle behind encapsulation
- [[access modifiers]] — Java/C++ keywords (public, private, protected) that enforce encapsulation

---

## 📅 Tasks

- [ ] Draw the Rectangle class diagram with all attributes and methods [due:: 2026-07-05] #p1
- [ ] Identify classes and properties for the Payroll System Employee class [due:: 2026-07-05] #p1
- [ ] Practice distinguishing Objects from Classes using everyday examples [due:: 2026-07-07] #p2
- [ ] Explain the TV remote analogy for encapsulation to a peer [due:: 2026-07-10] #p3

---

## 🧠 Flashcards

What is Object-Oriented Programming? :: A method of implementation where programs are organized as a collection of **objects** that cooperate to solve a problem. Complex systems are built from independent, reusable sub-systems.

What is an Object? :: A specific **instance** of a class (data type). It has both **state** (attributes) and **behaviour** (methods). Example: *Manoj* is an object of the *Student* class.

What is a Class? :: A **blueprint or mould** for creating objects. It defines the structure (attributes) and behaviour (methods) that all objects of that type will have. A class is a **concept**.

What is the "mould and block" analogy for classes and objects? :: A **mould (class)** is used to manufacture multiple **blocks (objects)**. From one mould, you can create as many identical-structured blocks as needed — just as from one class, you create many objects.

What is Abstraction in OOP? :: The process of removing non-essential characteristics from a real-world thing to reduce it to the **essential characteristics needed for a particular system**. It focuses on what matters for the context, ignoring the rest.

What are the three steps of abstraction? :: 1. Distinguish between different objects. 2. Classify objects into concepts (classes). 3. Focus on common, essential properties.

What does "relative to perspective of the viewer" mean in abstraction? :: The same real-world object can be abstracted differently depending on the system. A person becomes an Employee (Payroll), Patient (Hospital), or Member (Library) based on what properties are relevant.

What is Encapsulation? :: The process of grouping related attributes and methods together, giving the unit a name, and providing a public interface for outside communication. It **separates contractual interface from implementation**.

What is Information Hiding? :: The principle that internal implementation details of a class should be hidden. The ONLY way to access an object is through its public interface (public methods).

What is `private` in the context of OOP? :: A access level meaning no one except the class itself can see or use that attribute/method directly. Enforces information hiding and data integrity.

What is `public` in the context of OOP? :: An access level meaning anyone (any external code or class) can access that attribute or method — these form the **public interface** of a class.

What does "grouping properties and functions together is called...?" :: **Encapsulation**

Give the Jewelry Shop analogy for encapsulation. :: Jewelry (private data) is in a locked display. You can only access it **through a sales person** (public methods). You cannot grab it directly — encapsulation enforces this controlled access.

Give the TV Remote analogy for encapsulation. :: The TV's internal implementation (OLED/LCD/CRT) is hidden. The remote control is the public interface — you use the same commands regardless of internal implementation. The interface is stable; the implementation can change.

What does a class capture beyond properties/attributes? :: **Behaviour** — encoded as methods/functions. A class captures BOTH what an object knows (attributes) AND what it can do (methods).

What is the difference between an object and a class in a real-world example? :: "A student" = **Class** (concept). "The person sitting next to you" = **Object** (specific instance). "My copy of Learning UML 2.0" = **Object**. "A textbook" = **Class**.

How does Grady Booch define Abstraction? :: "An abstraction denotes the essential characteristics of an object that distinguish it from all other kinds of objects and thus provide crisply defined conceptual boundaries, relative to perspective of the viewer."

How does Grady Booch define Encapsulation? :: "The process of compartmentalizing the elements of an abstraction that constitute its structure and behavior; encapsulation serves to separate the contractual interface of an abstraction and its implementation."

What are the four pillars of OOP? :: [[abstraction]], [[encapsulation]], [[inheritance]], [[polymorphism]]

Why must properties of a class generally be private? :: Without private access, external code can directly modify internal state (causing corruption), implementation changes break external code, and no validation is possible before values are set. Private access enforces controlled, validated access through public methods.

What metaphor does the lecture use to show abstraction depends on perspective? :: A cat on a table — a pet-loving lady abstracts it as "purr/fuzz/cute", while a vet abstracts it as anatomy (heart, liver, kidney). Same object, different essential characteristics.

In the lecture's Dog vs Cat class example, what behaviours does each define? :: Dog Class: Bark(), Fetch(); Cat Class: Meow(), Purr(). Both share properties name, owner, breed (Dog adds work).

#flashcards
