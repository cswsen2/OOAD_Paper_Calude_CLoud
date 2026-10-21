---
course: SE2012
lecture_num: 6
aliases: [UML Class Relationships, Class Relationships]
topics: [UML Class Relationships, Dependency, Association, Aggregation, Composition, Inheritance]
---

# UML Class Relationships

## Overview
In Object-Oriented Analysis and Design, classes rarely exist in isolation. They interact and relate to each other to form complex systems. These relationships can be divided into five main categories, ranging from weakest to strongest.

## The Five Relationships
1. **[[dependency]] (Uses)**
   - *Strength*: Weakest
   - *Notation*: Dashed Arrow
   - *Meaning*: When objects of one class work briefly with objects of another class (e.g., as method parameters).
2. **[[association]] (Has a)**
   - *Strength*: Weak
   - *Notation*: Simple Connecting Line (with optional arrowhead for direction)
   - *Meaning*: When objects of one class work with objects of another class on an ongoing basis.
3. **[[aggregation]] (Part of - weak)**
   - *Strength*: Moderate
   - *Notation*: Empty Diamond Arrow
   - *Meaning*: A whole-part relationship where parts **can** exist without the whole.
4. **[[composition]] (Part of - strong)**
   - *Strength*: Strong
   - *Notation*: Filled Diamond Arrow
   - *Meaning*: A whole-part relationship where parts **cannot** exist without the whole.
5. **[[inheritance]] / [[generalization]] (Is a)**
   - *Strength*: Strongest
   - *Notation*: Empty Block Arrow
   - *Meaning*: When one class is a specific type of another class (Subclass $\rightarrow$ Superclass).

## Deciding on Relationships
When modeling a system, use the following rules of thumb to choose the right relationship:
- **Is-A relationship**: $\rightarrow$ [[inheritance]]
- **Part of (Part cannot exist without the whole)**: $\rightarrow$ [[composition]]
  - *e.g., Pages are part of a Book*
- **Part of (Part can exist without the whole)**: $\rightarrow$ [[aggregation]]
  - *e.g., Students are part of a Batch*
- **Has a (Not a direct Part of relationship)**: $\rightarrow$ [[association]]
  - *e.g., Customer has multiple Orders, Airplane can carry Passengers*
- **Uses (An object is used as a parameter of a method)**: $\rightarrow$ [[dependency]]
  - *e.g., `void Player::ThrowDice(Dice mydice);`*

## Class Diagram Elements
A typical [[class diagram]] consists of:
- Classes (with attributes and methods)
- Relationships (the lines connecting classes)
- [[multiplicity]] (how many objects participate in the relationship)
- Roles (the function a class serves in an association)

## Worked Example — Building a Class Diagram (Exam Paper)

> [!QUESTION] The Case (Slide 34)
> *"An Exam Paper has many instructions and has one or more Questions. Each Question has a solution. Here you can assume that Questions can only be in Exam papers."*

Reading the relationships:
- *"Questions can only be in Exam papers"* → a Question **cannot exist without** the Exam Paper → **[[composition]]**.
- An Exam Paper also has many Instructions in the same way → **[[composition]]**.
- *"Each Question has a solution"* → a plain **has-a** → **[[association]]**.

Resulting diagram (Slide 37):

```
                         1..*  ┌──────────┐        ┌──────────┐
            ┌──────────┐◆──────│ Question │────────│ Solution │
            │  Exam    │       └──────────┘  assoc └──────────┘
            │  Paper   │ 1..*  ┌─────────────┐
            └──────────┘◆──────│ Instruction │
                               └─────────────┘
```

- `Exam Paper ◆——— Question` (filled diamond = composition, multiplicity **1..\***)
- `Exam Paper ◆——— Instruction` (filled diamond = composition, multiplicity **1..\***)
- `Question ——— Solution` (association)

## 🧠 Flashcards

List the five UML class relationships from weakest to strongest. :: Dependency, Association, Aggregation, Composition, Inheritance.
Which UML relationship represents an "Is-a" relationship? :: Inheritance.
Which UML relationship represents a strong "Part-of" relationship? :: Composition.
Which UML relationship is used when an object is merely passed as a method parameter? :: Dependency.
Which UML relationship is represented by a filled diamond arrow? :: Composition.
Which UML relationship is represented by an empty diamond arrow? :: Aggregation.
What question should you ask to decide between Aggregation and Composition? :: Can the part exist without the whole? (Yes = Aggregation, No = Composition).

In the Exam Paper case study, what relationship links Exam Paper to Question? :: Composition (filled diamond, 1..*) — because a Question cannot exist outside an Exam Paper.

In the Exam Paper case study, what relationship links Question to Solution? :: A plain association (each Question has a Solution).

#flashcards
