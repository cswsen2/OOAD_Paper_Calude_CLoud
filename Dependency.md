---
course: SE2012
lecture_num: 6
aliases: [Dependency, dependency]
topics: [UML Class Relationships, Dependency]
---

# Dependency

## Overview
[[dependency]] is a **weaker form of relationship** which indicates that one class depends on another because it **uses** it at some point in time. It implies that a change to the depended-on class may affect the dependent class, but not vice versa.

## Characteristics
- **"Uses" Relationship**: Class A uses Class B, but Class A does *not* contain an instance of Class B as part of its own state/attributes.
- Typically, the depended-on object is passed as a **parameter** to a method of the dependent class.

## Notation
In a [[class diagram]], [[dependency]] is graphically rendered as a **dashed directed line** pointing to the thing being depended on.

## Examples
- **Person and Dog**: A `Person` object uses a `Dog` object somewhere as a parameter in one of its methods: `void Person::walk(Dog dog)`. Changes to the `Dog` class may affect the `Person` class, but not vice versa.
- **Player and Dice**: `void Player::ThrowDice(Dice mydice);` (The ThrowDice method has a parameter of the Dice Class).
- **SalesPerson and Product**: A `SalesPerson` class depends on a `Product` class because the `Product` class is used as a parameter for an add operation in the `SalesPerson` class.

## Java Implementation
In Java, a [[dependency]] is seen when a class appears in method signatures (as parameters) or as local variables, rather than as instance variables.

```java
class Product {
    private double price;
    public Product(double price) { this.price = price; }
    public double getPrice() { return price; }
}

class SalesPerson {
    private String name;
    private double salesAmount;
    
    public SalesPerson(String pname) { 
        this.name = pname; 
        this.salesAmount = 0;
    }
    
    // Dependency: Product is used as a parameter, not stored as a class field
    public void addSales(int qty, Product p) {
        this.salesAmount += qty * p.getPrice();
    }
    
    public void display() {
        System.out.println("Name = " + name);
        System.out.println("Sales Amount = " + salesAmount);
    }
}
```

## 🧠 Flashcards

What is a Dependency relationship in UML? :: A weak "uses" relationship where one class depends on another (e.g., as a method parameter), but doesn't store it as an attribute.
How is a Dependency rendered in a class diagram? :: As a dashed directed line pointing to the depended-on class.
What is the key difference between Dependency and Association? :: Association implies a "has a" relationship where one object is stored as a field/attribute, whereas Dependency implies a "uses" relationship where the object is typically just passed as a method parameter.
How is Dependency typically implemented in Java? :: The depended-on class appears only in method parameters, return types, or local variables, rather than as instance fields.
#flashcards
