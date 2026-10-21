---
course: SE2012
lecture_num: 6
aliases: [Aggregation, aggregation]
topics: [UML Class Relationships, Aggregation, Whole-Part Relationship]
---

# Aggregation

## Overview
[[aggregation]] is a **weak form of whole-part relationship**. It implies that the **"part can exist without the whole"**. It is a special kind of [[association]].

## Characteristics
- The objects have their own life cycles, but there is ownership involved.
- If the parent (whole) object is deleted, the child (part) objects can still exist independently.
- If the child (part) object is deleted, the parent (whole) object can still exist.

## Notation
In a [[class diagram]], [[aggregation]] is graphically rendered as an **empty diamond arrow** pointing to the "whole" class.
- The same rules for [[multiplicity]] apply. In some situations, [[aggregation]] can also have a multiplicity of `0..*`.

## Examples
- **Batch and Student**: `Batch` (Whole) and `Student` (Part). A batch consists of one or more students. A student can exist without the batch.
- **Department and Employee**: `Department` (Whole) and `Employee` (Part). A department has one or more employees.
- **Sentence, Word, Letter**: A sentence aggregates words, and words aggregate letters.

## Java Implementation
In Java, [[aggregation]] is implemented by passing already-existing objects to the whole class (e.g., via an "add" method). The whole class stores references but does not exclusively manage the lifecycle of the parts.

```java
class Employee {
    private String empID;
    private String name;
    public Employee(String pempID, String pname) {
        this.empID = pempID;
        this.name = pname;
    }
    public void displayEmployee() {
        System.out.println("empID = " + empID);
        System.out.println("name = " + name);
        System.out.println("***********************");
    }
}

class Department {
    private static final int SIZE = 2;
    private Employee[] emp;
    
    public Department() {
        emp = new Employee[SIZE];
    }
    
    // The Department aggregates Employees passed from outside
    public void addEmployee(Employee emp1, Employee emp2) {
        emp[0] = emp1;
        emp[1] = emp2;
    }
    
    public void displayDepartment() {
        for(int i=0; i<SIZE; i++) {
            emp[i].displayEmployee();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Department ABC = new Department();
        
        // Employees are created independently of the Department
        Employee e1 = new Employee("E001", "Nimal");
        Employee e2 = new Employee("E002", "Jagath");
        
        ABC.addEmployee(e1, e2);
        ABC.displayDepartment();
    }
}
```

## 🧠 Flashcards

What is Aggregation in UML? :: A weak form of whole-part relationship where the part can exist without the whole.
How is Aggregation rendered in a class diagram? :: As an empty diamond arrow pointing to the whole class.
What happens to child objects in Aggregation when the parent is deleted? :: They continue to exist independently; they have their own lifecycles.
How is Aggregation typically implemented in Java? :: By passing references of existing child objects into the parent class (e.g., via an add method), rather than the parent creating them.
#flashcards
