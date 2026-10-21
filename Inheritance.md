---
course: SE2012
lecture_num: 6
aliases: [Inheritance, inheritance, Generalization, generalization]
topics: [UML Class Relationships, Inheritance, Generalization, Specialization]
---

# Inheritance

## Overview
[[inheritance]] (otherwise known as [[generalization]]) represents an **"is-a-kind-of"** relationship. It establishes a relationship between a general thing (the **[[superclass]]**, parent, or [[ancestor]]) and a more specific kind of a thing (the **[[subclass]]**, child, or [[descendant]]).

## Generalization vs Specialization
- **[[generalization]]**: Takes place from sub-class to super-class. The super-class is a generalization of the sub-class.
- **[[specialization]]**: Takes place from super-class to sub-class. The sub-class is a specialization of the super-class.
  
> [!IMPORTANT]
> The functionality of the child should be a specialization of the functionality of the parent. For example, the `draw()` method in a `Circle` class is a more specific implementation than the `draw()` method in a general `Shape` class.

## Notation
In a [[class diagram]], [[inheritance]] is graphically rendered as an **empty block arrow** pointing from the sub-class to the super-class.

## Examples
- **Animals**: `Animal` (Super Class) $\rightarrow$ `Mammal`, `Bird`, `Reptile` (Sub Classes). `Dog`, `Horse`, and `Parot` inherit from the intermediate subclasses.
- **University**: `Person` (Super Class) $\rightarrow$ `Student`, `Lecturer` (Sub Classes). The children inherit the properties of its parent's attributes, operations, responsibilities, etc.

## 🧠 Flashcards

What is Inheritance in UML? :: Inheritance represents an "is-a-kind-of" relationship between a general thing (superclass) and a more specific thing (subclass).
What is another name for Inheritance in UML? :: Generalization.
How is Inheritance rendered in a UML class diagram? :: As an empty block arrow pointing from the subclass to the superclass.
What is the difference between generalization and specialization? :: Generalization takes place from subclass to superclass, while specialization takes place from superclass to subclass.
#flashcards
