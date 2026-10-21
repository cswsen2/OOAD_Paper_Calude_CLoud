---
course: SE2012
lecture_num: 6
aliases: [Association, association]
topics: [UML Class Relationships, Association, Association Class, Multiplicity]
---

# Association

## Overview
An [[association]] defines a **"has a"** relationship between two classes. It connects one instance of a class with an instance of another class, indicating that objects at one end of the association "recognize" objects at the other end and may send messages to them.

## Types of Association
1. **Uni-directional (One Way)**: 
   - Rendered as a simple connecting line with an **arrowhead**.
   - Class A is associated with Class B. Class A uses and contains an instance of Class B, but B does not know about it.
   - Example: A `Department` has a `Manager`.
2. **Bi-directional (Two Way)**: 
   - Rendered as a **simple connecting line** (no arrowheads).
   - Both classes know about each other.
   - Example: A `Person` is associated with a `Dog`, and the `Dog` is associated with the `Person`. A `Customer` owns 1 or more `Accounts`, and `Account` belongs to only one `Customer`. A `University` class has 1 or more students and a `Student` is attached to only one university.

## Properties of an Association
- **Association Name**: An association can be given a name to clarify the relationship (e.g., "owns", "works for").
- **Association Role**: When a class participates in an [[association]], it plays a specific role. A role is the "face" the class presents to the other end. For example, a `Person` playing the role of *employee* is associated with a `Company` playing the role of *employer*.
- **Association Multiplicity**: Defines the number of objects associated with an instance of the association. This "How many" is the multiplicity of an association's role.

### Multiplicity Format Table
| Format | Meaning |
|---|---|
| `1` | Exactly one |
| `n` | Exactly n |
| `0..1` | Zero or one |
| `n..m` | Between n and m (inclusive) |
| `0..*` | Zero or more |
| `1..*` | One or more |
| `0..1, 3..5` | Zero or one, or between 3 and 5 inclusive |

## Association Class
An [[association]] can be promoted to an **Association Class** to hold additional information pertaining to the relationship itself. The responsibility for maintaining information is placed with the ownership class.
- Example: If an `Employee` works for more than one `Project`, and a `Project` is assigned to more than one `Employee`, the additional information (like number of hours each employee spends on a project) can be stored in a `Works ON` association class.

## Java Implementation

### Uni-directional
In an Association relationship, the dependent class defines an instance of the associated class.
```java
class Manager { 
    public Manager() {} 
}

class Department {
    private Manager mgr; // Department knows about Manager
    public Department() {}
}
```

### Bi-directional
```java
class Customer {
    private static final int SIZE = 10;
    private String name;
    private String address;
    private Order[] orders;
    private int noOfOrders;
    
    public Customer() {
        orders = new Order[SIZE];
        noOfOrders = 0;
    }
    
    public Customer(String pname, String paddress) {
        this();
        this.name = pname;
        this.address = paddress;
    }
    
    public void addOrder(Order o) {
        if(noOfOrders < SIZE) {
            orders[noOfOrders] = o;
            noOfOrders++;
        }
    }
    
    public void displayCustomer() {
        System.out.println("Customer Name = " + name);
        System.out.println("Customer Address = " + address);
        for(int i=0; i<noOfOrders; i++) {
            orders[i].displayOrders();
        }
    }
}

class Order {
    private String orderID;
    private Customer customer;
    
    public Order(String porderID, Customer pCustomer) {
        this.orderID = porderID;
        this.customer = pCustomer;
        pCustomer.addOrder(this); // Bi-directional link established
    }
    
    public void displayOrders() {
        System.out.println("Order ID = " + orderID);
    }
}
```

## 🧠 Flashcards

What does an Association represent in UML? :: A "has a" relationship where objects of one class recognize objects of another class.
What is a Uni-directional Association? :: A relationship where Class A knows about Class B, but Class B does not know about Class A. Rendered with an arrowhead.
What is a Bi-directional Association? :: A relationship where both classes know about each other. Rendered with a simple line.
What is an Association Role? :: The specific face or identity a class presents to the other class in an association relationship (e.g., employer/employee).
What is an Association Class? :: A class that is part of an association relationship between two other classes, used to store additional information about the relationship itself.
#flashcards
