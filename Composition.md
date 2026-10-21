---
course: SE2012
lecture_num: 6
aliases: [Composition, composition]
topics: [UML Class Relationships, Composition, Whole-Part Relationship]
---

# Composition

## Overview
[[composition]] is a **strong form of whole-part relationship**. It implies that the **"part cannot exist without the whole"**. In this relationship, the objects have coincident lifetimes.

## Characteristics
- If the parent (whole) object is deleted, then all of its child (part) objects will also be deleted automatically.
- Child objects are typically created within the parent class.

## Notation
In a [[class diagram]], [[composition]] is graphically rendered as a **filled diamond arrow** pointing to the "whole" class. 
- Multiplicity: [[composition]] should have a relationship with a multiplicity of `1..` at the whole end.

## Examples
- **Book and Page**: A `Book` (Whole) has `Page`s (Part). A page cannot exist without the book.
- **University and Room**: A `University` is composed of at least one `Room`. If there are no rooms, there is no university. If the `University` object is deleted, the class room objects will get deleted automatically.

## Java Implementation
In Java, [[composition]] is implemented by having the whole class create instances of the part class within its own constructors, meaning the whole class tightly controls the lifecycle of the parts.

```java
class ClassRoom {
    private int roomno;
    public ClassRoom() {}
    public ClassRoom(int no) { this.roomno = no; }
    public void display() { System.out.println("Class Room " + roomno); }
}

class University {
    private static final int SIZE = 2; // Assuming SIZE is 2 based on the code
    private ClassRoom[] room;
    
    public University() {
        // The University strictly controls the creation of ClassRooms
        room = new ClassRoom[SIZE];
        room[0] = new ClassRoom(101);
        room[1] = new ClassRoom(102);
    }
    
    public University(int no1, int no2) {
        room = new ClassRoom[SIZE];
        room[0] = new ClassRoom(no1);
        room[1] = new ClassRoom(no2);
    }
    
    public void displayClassRooms() {
        for(int i=0; i<SIZE; i++) {
            room[i].display();
        }
    }
    
    public void shutDown() {
        System.out.println("University shutting down");
        for(int i=0; i<SIZE; i++) {
            room[i] = null; // Nullify the reference for garbage collection
        }
        System.out.println("The End");
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an instance of University
        University myUniversity = new University(501, 502);

        // Call the method to display classroom details
        myUniversity.displayClassRooms();

        // Optionally, call shutDown if needed for cleanup
        myUniversity.shutDown();
    }
}
```

> [!WARNING] Outside Knowledge
> In Java, object destruction is handled by the Garbage Collector. Explicit deletion (like `delete` in C++) is not necessary. Nullifying references as seen in `shutDown()` is a pattern to help the GC reclaim memory, simulating the deterministic destruction found in C++ composition.

## 🧠 Flashcards

What is Composition in UML? :: A strong form of whole-part relationship where the part cannot exist without the whole.
How is Composition rendered in a class diagram? :: As a filled diamond arrow pointing to the whole class.
What happens to the child objects in Composition when the parent is deleted? :: They are also deleted (they have coincident lifetimes).
How is Composition typically implemented in Java? :: The parent class instantiates the child objects directly (e.g., inside its constructor), tightly controlling their lifecycle.
#flashcards
