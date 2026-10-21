---
course: SE2012
lecture_num: 7
aliases: [Java Collections Framework, Java Collection Framework, Collections Framework]
topics: [Java Collection Framework, ArrayList, Stack, Queue, Set, Map]
---

# Java Collections Framework

## Overview
The [[Java Collections Framework]] is a sophisticated hierarchy of interfaces and classes that provide state-of-the-art technology for managing groups of objects. 

### Advantages of the Framework
- Reduces programming effort
- Increases performance
- Provides interoperability between unrelated APIs
- Reduces the effort required to learn APIs
- Reduces the effort required to design and implement APIs
- Fosters software reuse
- [[Generics]] make Collections type-safe. Before generics, collections stored Object references; they could store any type of object, which often led to run-time mismatch errors.

---

## Hierarchy of the Collections Framework

The `java.util` package contains all the classes and interfaces for the Collection framework. The hierarchy (Slide 4) is:

```
Iterable «interface»
   └── Collection «interface»
         ├── List «interface»   ──implemented by──► ArrayList, LinkedList, Vector ──► Stack (extends Vector)
         ├── Queue «interface»  ──implemented by──► PriorityQueue
         │         └── Deque «interface» ──► ArrayDeque
         └── Set «interface»    ──implemented by──► HashSet, LinkedHashSet
                   └── SortedSet «interface» ──► TreeSet
```

- The three core sub-interfaces of `Collection` are **[[List]]**, **[[Queue]]**, and **[[Set]]**.
- `Stack` extends `Vector`; `Deque` extends `Queue`; `SortedSet` extends `Set`.
- **[[Map]]** (and its classes) is part of the framework but does **not** extend `Collection` (covered separately below).

---

## 1. The Collection Interface
`Collection` is the foundation upon which the Collection Framework is built on. 

**Declaration**:
`Interface Collection <E>` (where `E` specifies the type of objects that the collection will hold).

### Collection Interface Methods
The `Collection` interface defines several methods that must be implemented by any child class:

| Method | Description |
|---|---|
| `public boolean add(Object element)` | is used to insert an element in this collection. |
| `public boolean addAll(Collection c)` | is used to insert the specified collection elements in the invoking collection. |
| `public boolean remove(Object element)` | is used to delete an element from this collection. |
| `public boolean removeAll(Collection c)` | is used to delete all the elements of specified collection from the invoking collection. |
| `public boolean retainAll(Collection c)` | is used to delete all the elements of invoking collection except the specified collection. |
| `public int size()` | return the total number of elements in the collection. |
| `public void clear()` | removes the total no of element from the collection. |
| `public boolean contains(Object element)` | is used to search an element. |
| `public boolean containsAll(Collection c)` | is used to search the specified collection in this collection. |
| `public Iterator iterator()` | returns an iterator. |
| `public Object[] toArray()` | converts collection into array. |
| `public boolean isEmpty()` | checks if collection is empty. |
| `public boolean equals(Object element)` | matches two collection. |
| `public int hashCode()` | returns the hashcode number for collection. |

---

## 2. List Interface
`java.util.List` is a child interface of `Collection`.
- **Characteristics**: It is an ordered collection of objects in which **duplicate values can be stored**. Since `List` preserves the insertion order, it allows positional access and insertion of elements.
- **Implementations**: `ArrayList`, `LinkedList`, `Vector`, and `Stack` classes.

### Case Study: School Management Application
> [!NOTE] Problem Scenario
> Think of a School management application. You have a list of students stored in a Database. To display those names on the user interface, you have to make a call to the database, store these elements, and populate those list elements on UI. **Is an Array the best approach?**

**Why Arrays fail here:**
- Arrays are of fixed length. You cannot change the size of the arrays once they are created.
- You cannot accommodate an extra element in an array after they are created.
- Memory is allocated to an array during its creation only, much before the actual elements are added to it.

### ArrayList Class
`ArrayList` class extends the `AbstractList` class and implements the `List` interface.
- Supports **dynamic arrays** (can increase and decrease size dynamically).
- Elements can be inserted at or deleted from a particular position.
- If generics are not used, `ArrayList` can hold any type of objects.

**ArrayList Code Example:**
```java
import java.util.*;

class ArrayListDemo {
    public static void main(String args[]) {
        // Create an array list
        ArrayList<String> al = new ArrayList<String>();

        System.out.println("Initial size of al: " + al.size());

        // Add elements to the array list
        al.add("C");
        al.add("A");
        al.add("E");
        al.add("B");
        al.add("D");
        al.add("F");
        al.add(1, "A2");

        System.out.println("Size of al after additions: " + al.size());

        // Display the array list
        System.out.println("Contents of al: " + al);

        // Remove elements from the array list
        al.remove("F");
        al.remove(2);

        System.out.println("Size of al after deletions: " + al.size());
        System.out.println("Contents of al: " + al);
    }
}
```

### Obtaining Array from an ArrayList
Reasons for converting an array to an `ArrayList` (or vice versa):
- To obtain faster processing time for certain operations.
- To pass an array to a method that is not overloaded to accept a collection.
- To integrate collection-based code with legacy code that doesn't understand collections.

**ArrayList to Array Code Example:**
```java
import java.util.*;

class ArrayListToArray {
    public static void main(String args[]) {
        // Create an array list
        ArrayList<Integer> al = new ArrayList<Integer>();

        // Add elements to the array list
        al.add(1);
        al.add(2);
        al.add(3);
        al.add(4);

        System.out.println("Contents of al: " + al);

        // Get the array
        Integer ia[] = new Integer[al.size()];
        ia = al.toArray(ia);

        int sum = 0;

        // Sum the array
        for(int i = 0; i < ia.length; i++) {
            sum += ia[i];
        }

        System.out.println("Sum is: " + sum);
    }
}
```

### The forEach Loop
You can use the `forEach` loop to cleanly iterate over collections.
```java
import java.util.ArrayList;

public class ForEachExample {
    public static void main(String[] args) {
        ArrayList<String> items = new ArrayList<>();
        items.add("A");
        items.add("B");
        items.add("C");
        items.add("D");
        items.add("E");

        for (String item : items) {
            System.out.println(item);
        }
    }
}
```

---

## 3. Stack Class

### Case Study: Canteen Plates
> [!NOTE] Problem Scenario
> Think of a scenario where plates are stacked over one another in a canteen. The plate which is at the top is the first one to be removed, i.e., the plate which has been placed at the bottommost position remains in the stack for the longest period of time. **Is an ArrayList the best approach?**

**Why ArrayList fails here:**
In `ArrayList`, elements can be inserted at or deleted from a particular position. If we remove a middle plate from the stack, it breaks the physical rules of plate stacking. 

**Solution: Stack Class**
`Stack` is a subclass of `Vector`. Stacks are dynamic data structures that follow the **Last In First Out (LIFO)** principle.

**Stack Code Example:**
```java
import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();
        stack.push("aaaaaaa");
        stack.push("bbbbbbb");
        stack.push("ccccccc");
        stack.push("ddddddd");
        stack.push("eeeeeee");
        stack.add("ffffffff");

        System.out.println(stack);
        
        // Remove last item
        System.out.println("Stack pop = " + stack.pop() + "\n");
        System.out.println(stack);

        // Add elements
        System.out.println("Stack add = " + stack.add("1111111") + "\n");
        System.out.println("Stack add = " + stack.add("2222222") + "\n");
        
        System.out.println(stack);
    }
}
```

---

## 4. Queue Interface

### Case Study: Bank Line
> [!NOTE] Problem Scenario
> Think of a scenario of a Bank line where people who come first will do their transaction first. What is the best approach?

**Solution: Queue Interface**
The `Queue` interface extends `Collection`. It defines a queue data structure which is normally **First-In-First-Out (FIFO)**.
- Elements are added from one end and deleted from another end.
- Most common implementations: `PriorityQueue` and `LinkedList`.
- In a `PriorityQueue`, elements are removed from one end, but they are added according to the order defined by the supplied comparator (not strictly FIFO).

**PriorityQueue Code Example:**
```java
import java.util.PriorityQueue;

public class PriorityQueueExample {
    public static void main(String[] args) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<Integer>();
        priorityQueue.add(11);
        priorityQueue.add(22);
        priorityQueue.add(22);
        priorityQueue.add(44);
        priorityQueue.add(33);
        priorityQueue.add(55);
        priorityQueue.add(66);
        priorityQueue.add(77);
        priorityQueue.add(88);

        System.out.println("=======Before=======================");
        System.out.println(priorityQueue);

        // Show first element
        System.out.println("Queue Peek = " + priorityQueue.peek());
        // Poll delete the first element
        System.out.println("Queue Poll = " + priorityQueue.poll());
        // Poll delete the second element
        System.out.println("Queue Poll = " + priorityQueue.poll());

        System.out.println("=======After========================");
        System.out.println(priorityQueue);
    }
}
```

---

## 5. Set Interface

### Case Study: Unique User IDs
> [!NOTE] Problem Scenario
> Think of an application that requires a unique User ID as an input. What is the best approach?

**Solution: Set Interface**
The `java.util.Set` interface is a subtype of `Collection`. A Set is a collection that **cannot contain duplicate elements**. It models the mathematical set abstraction.
- Implemented by `SortedSet` interface, and `HashSet` and `LinkedHashSet` classes.
- `SortedSet` declares the behavior of a set sorted in ascending order (implemented by `TreeSet` class).
- `HashSet` class stores elements using a mechanism called hashing.

### HashSet Class & The Pizza Scenario
> [!NOTE] Problem Scenario
> Think of a scenario where you are ordering a 3-topping pizza. Whether you say "Pepperoni, mushrooms, and onions, please" or "Yoo hoo! Make that mushrooms, pepperoni, and onions", the result is exactly the same unordered combination.

**HashSet Class**
`HashSet` extends `AbstractSet` and implements `Set`. 
- Creates a collection that uses a hash table for storage. 
- **No duplication and unordered**.
- In hashing, the informational content of a key is used to determine a unique value (hash code), which is used as the index to store the data.

**HashSet Code Example:**
```java
import java.util.HashSet;
import java.util.Set;

public class HashSetDemo {
    public static void main(String args[]) {
        // Create a hash set
        Set<Integer> set = new HashSet<Integer>();
        
        // Add elements to the hash set
        set.add(10);
        set.add(20);
        set.add(50);
        set.add(50); // Duplicate, will be ignored
        set.add(20); // Duplicate, will be ignored
        set.add(10); // Duplicate, will be ignored
        
        for (Integer value : set) {
            System.out.println(value);
        }
        
        // Example with Strings
        HashSet<String> hs = new HashSet<String>();
        hs.add("Beta");
        hs.add("Alpha");
        hs.add("Eta");
        hs.add("Gamma");
        hs.add("Epsilon");
        hs.add("Omega");
        
        System.out.println(hs);
    }
}
```

### TreeSet Class & Student Marks
> [!NOTE] Problem Scenario
> Think of a scenario where you store student details including ID and the marks. What is the best approach to keep them sorted?

**TreeSet Class**
`TreeSet` extends `AbstractSet` and implements the `NavigableSet` interface. Objects are stored in **sorted, ascending order**.

---

## 6. Map Interfaces (Key/Value Pairs)

### Case Study: Recent State Cache
> [!NOTE] Problem Scenario
> Think of a cache, where if new data comes in we overwrite the existing record using the key. So basically, the cache would be used to store the most recent state.

**Solution: Maps**
A map is an object that stores associations between keys and values (key/value pairs). Given a key, you can find its value.
- Both keys and values are objects. The keys must be unique, but the values may be duplicated.
- Map is useful if you have to search, update, or delete elements on the basis of a key.
> [!IMPORTANT]
> Maps are **not** part of the `Collection` Interface, though they are part of the Collections Framework.

### Map Implementation Classes
Several classes provide implementations of the map interfaces:

| Class | Description |
|---|---|
| `AbstractMap` | Implements most of the `Map` interface. |
| `EnumMap` | Extends `AbstractMap` for use with `enum` keys. |
| `HashMap` | Extends `AbstractMap` to use a hash table. |
| `TreeMap` | Extends `AbstractMap` to use a tree. |
| `WeakHashMap` | Extends `AbstractMap` to use a hash table with weak keys. |
| `LinkedHashMap` | Extends `HashMap` to allow insertion-order iterations. |
| `IdentityHashMap` | Extends `AbstractMap` and uses reference equality when comparing documents. |

### HashMap Class
The `HashMap` class extends `AbstractMap` and implements the `Map` interface.
- Values in hash map are not ordered or sorted.
- Removes duplicates in the key.
- Declaration: `class HashMap< K, V >` (where `K` specifies the type of keys, and `V` specifies the type of values).

**HashMap Code Example:**
```java
import java.util.HashMap;
import java.util.Set;
import java.util.Map;

public class HashMapDemo {
    public static void main(String args[]) {
        // Create a hash map
        HashMap<String, Double> hm = new HashMap<String, Double>();
        
        // Put elements to the map
        hm.put("John Doe", new Double(3434.34));
        hm.put("Tom Smith", new Double(123.22));
        hm.put("Jane Baker", new Double(1378.00));
        hm.put("Tod Hall", new Double(99.22));
        hm.put("Ralph Smith", new Double(-19.08));
        
        // Get a set of the entries
        Set<Map.Entry<String, Double>> set = hm.entrySet();
        
        // Display the set
        for (Map.Entry<String, Double> me : set) {
            System.out.print(me.getKey() + ": ");
            System.out.println(me.getValue());
        }
        
        // Deposit 1000 into John Doe's account
        double balance = hm.get("John Doe");
        hm.put("John Doe", balance + 1000);
        
        System.out.println("John Doe's new balance: " + hm.get("John Doe"));
    }
}
```

### Other Maps
- **LinkedHashMap**: `HashMap` with an additional feature that maintains insertion order. Contains values based on the key, removes duplicate keys. When displayed, the order is guaranteed based on insertion.
- **TreeMap**: Contains values based on the key. Contains only unique elements. Maintains ascending orders. Provides an efficient means of storing key-value pairs in sorted order.

---

## 🧠 Flashcards

What is the primary foundation interface of the Java Collections Framework? :: The Collection interface.
What method in the Collection interface returns the total number of elements? :: public int size()
What method in the Collection interface checks if the collection has zero elements? :: public boolean isEmpty()
Why might an Array be a bad choice for a School management system UI compared to an ArrayList? :: Arrays are fixed-length, memory is allocated beforehand, and they cannot accommodate extra elements once created.
What is the primary difference between a List and a Set? :: A List allows duplicate values and preserves insertion order, while a Set cannot contain duplicate elements.
Which Java Collection class implements a dynamic array? :: ArrayList
Which Collection class should be used to simulate a stack of plates in a canteen? :: Stack (it follows LIFO).
Which Collection interface should be used to simulate a bank line? :: Queue (it follows FIFO).
What is the difference between Queue and PriorityQueue? :: Queue is strictly FIFO, while PriorityQueue removes elements based on a supplied comparator order.
Which Collection should be used to store unique User IDs? :: Set (e.g., HashSet).
Does a HashSet maintain insertion order? :: No, it is unordered and uses a hash table for storage.
Which Set implementation stores elements in ascending order? :: TreeSet.
Are Maps part of the `Collection` interface? :: No, Maps are part of the Collections Framework but do not extend the `Collection` interface.
What is the primary characteristic of a Map? :: It stores associations between keys and values, where keys must be unique.
What is the difference between HashMap and LinkedHashMap? :: HashMap is unordered, while LinkedHashMap maintains insertion order.
What is the difference between HashMap and TreeMap? :: HashMap is unordered, while TreeMap maintains keys in ascending order.
#flashcards
