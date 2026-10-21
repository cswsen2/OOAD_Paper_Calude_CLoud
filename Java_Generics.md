---
course: SE2012
lecture_num: 8
aliases: [Java Generics, Generics, generics]
topics: [Java Generics, Wrapper Classes, Autoboxing, Unboxing, Parameterized Types, Type-Safety, Bounded Types, Wildcards]
---

# Java Generics

## Wrapper Classes (Covering Classes)
> [!NOTE] Lecture context
> Before Generics, the lecture introduces **Wrapper classes**, because Generics rely on them — primitive types do **not** support Generics, so their object equivalents (wrappers) must be used instead.

A **[[Wrapper Class]]** (also called a *covering class*) in Java provides the mechanism to convert a **primitive datatype into an object** and an **object back into a primitive type**. For each primitive datatype, there exists a covering class in the `java.lang` package.

### Primitive → Wrapper Class Mapping
| Primitive Type | Wrapper Class |
|---|---|
| `byte` | `Byte` |
| `short` | `Short` |
| `int` | `Integer` |
| `long` | `Long` |
| `float` | `Float` |
| `double` | `Double` |
| `char` | `Character` |
| `boolean` | `Boolean` |

### Autoboxing and Unboxing
- **[[Autoboxing]]**: the **automatic conversion of a primitive type into its wrapper object** (primitive → object).
- **[[Unboxing]]**: the reverse — **automatic conversion of a wrapper object back into a primitive** (object → primitive).
- Since **J2SE 5.0**, the autoboxing and unboxing feature performs these conversions **automatically**, so you do not have to box/unbox manually.

```java
public class WrapperExample {
    public static void main(String[] args) {
        // ---- Autoboxing: primitive -> object ----
        int a = 50;
        Integer autoBoxed = a;                  // automatic autoboxing
        Integer explicitBoxed = Integer.valueOf(a); // explicit boxing

        // ---- Unboxing: object -> primitive ----
        Integer obj = Integer.valueOf(60);
        int autoUnboxed = obj;                  // automatic unboxing
        int explicitUnboxed = obj.intValue();   // explicit unboxing

        System.out.println("Autoboxed value   : " + autoBoxed);
        System.out.println("Auto-unboxed value: " + autoUnboxed);
        System.out.println("Explicit unbox    : " + explicitUnboxed);
    }
}
```

> [!IMPORTANT]
> This is exactly why, later in this note, you will see `Collection<Integer>` instead of `Collection<int>` — primitive types do not support [[generics]], so their wrapper classes are used.

---

## Overview
[[generics]] in Java mean **"parameterized types"**. Many algorithms are the same regardless of the data type that is applied. With [[generics]], you can define an algorithm once independently of any specific type of data, and later use that algorithm with a wide variety of data types without any additional effort.

### Advantages of Generics
1. **Type-Safety**: We can hold only a single type of objects in generics. It doesn't allow storing other types of objects.
2. **Type casting is not required**: There is no need to typecast the object. All type conversions are implicit.
3. **Compile-Time Checking**: It is checked at compile time so problems will not occur at runtime. A good programming strategy says it is far better to handle problems at compile time than at runtime.

---

## 1. Implementation Problem & Scenario
> [!NOTE] Problem Scenario
> When you need to store a list of values, you might use an array (e.g., storing marks of 5 students). However, the size of the array is fixed. If there is a change in the size of the array, you have to modify the code manually. You cannot expand or shrink the array automatically as an element is added.

**Initial Array Approach:**
```java
public class GenExample {
    public static void main(String args[]) {
        int marks[] = new int[5]; // Fixed size
    }
}
```

**Solution: Use Collection Interface**
We can use an `[[ArrayList]]` from the [[Java Collections Framework]] to let the list grow each and every time `add()` is called.

**Raw Collection Approach (No Generics):**
```java
import java.util.ArrayList;
import java.util.Collection;

public class GenExample {
    public static void main(String args[]) {
        Collection value = new ArrayList();
        value.add(10);
        value.add(20);
        value.add(30);
        value.add(40);
        value.add(50);
    }
}
```

> [!WARNING] The Danger of Raw Collections
> The list created above may contain **any** object because we have not specified the data type of the element to be added.

**The Mixed Types Problem:**
```java
import java.util.ArrayList;
import java.util.Collection;

public class GenExample {
    public static void main(String args[]) {
        Collection value = new ArrayList();
        value.add("SLIIT");     // String object
        value.add(145);         // integer
        value.add(23.4578);     // double
        value.add(1.54f);       // float
        value.add('y');         // char
    }
}
```

**The Generics Solution:**
To restrict the collection to store only integers, we make use of [[generics]]. 
> [!IMPORTANT]
> Primitive types do not support Generics. You **must** make use of their Wrapper classes (e.g., `Integer` instead of `int`).

```java
import java.util.ArrayList;
import java.util.Collection;

public class GenExample {
    public static void main(String args[]) {
        Collection<Integer> value = new ArrayList<>();
        
        // value.add("SLIIT");  // Compilation Error
        value.add(145);         // Valid
        // value.add(23.4578);  // Compilation Error
        // value.add(1.54f);    // Compilation Error
        // value.add('y');      // Compilation Error
    }
}
```

---

## 2. Type Parameters
The type parameter naming conventions are as follows:
- **T** - Type
- **E** - Element
- **K** - Key
- **N** - Number
- **V** - Value

---

## 3. Generic Classes
A class that can refer to any type is known as a generic class. The type `T` indicates that it can refer to any type (`Integer`, `Double`, `Employee`, etc.).

**Generic Class Implementation:**
```java
public class MyGen<T> {
    T obj;
    void add(T val) {
        this.obj = val;
    }
    T get() {
        return obj;
    }
}

public class Test {
    public static void main(String args[]) {
        MyGen<Integer> m = new MyGen<>();
        m.add(12);
        System.out.println(m.get());
        
        // Note that there will be a compilation error if you attempt 
        // to add any other type of data other than an integer.
    }
}
```

---

## 4. Generic Methods
Like a generic class, we can create a generic method that can accept any type of argument.

**Generic Method Implementation:**
```java
public class Test {
    public static <E> void printArray(E[] elements) {
        for(E elem : elements) {
            System.out.print(elem + " ");
        }
        System.out.println();
    }
    
    public static void main(String args[]) {
        Integer[] intArray = {12, 15, 45, 78, 92, 56, 72};
        Character[] charArray = {'S', 'L', 'I', 'I', 'T'};
        
        printArray(intArray);
        printArray(charArray);
    }
}
```

---

## 5. Multiple Parameters
A generic class or method can have multiple type parameters.

**Multiple Parameters Implementation:**
```java
public class TwoGen<T, V> {
    T ob1;
    V ob2;
    
    public TwoGen(T ob1, V ob2) {
        this.ob1 = ob1;
        this.ob2 = ob2;
    }
    
    public void ShowType() {
        System.out.println("Type of T is " + ob1.getClass().getName());
        System.out.println("Type of V is " + ob2.getClass().getName());
    }
    
    public T getob1() { return ob1; }
    public V getob2() { return ob2; }
}

public class GenExample {
    public static void main(String args[]) {
        TwoGen<Integer, String> tgOb = new TwoGen<>(123, "Anne");
        tgOb.ShowType();
        
        int v = tgOb.getob1();
        System.out.println("Value is " + v);
        
        String s = tgOb.getob2();
        System.out.println("Value is " + s);
        
        // Although the two type arguments differ above, it is possible for both types to be the same:
        TwoGen<String, String> tgOb2 = new TwoGen<>("BM-1", "Anne");
        tgOb2.ShowType();
        
        String v2 = tgOb2.getob1();
        System.out.println("Value is " + v2);
        
        String s2 = tgOb2.getob2();
        System.out.println("Value is " + s2);
    }
}
```
> [!NOTE] 
> If both type arguments were *always* the same, then having two type parameters would be unnecessary.

---

## 6. Bounded Type Parameters
There may be times when you want to restrict the kind of data types that are allowed to be passed to a type parameter. For example, a method that operates on numbers might only want to accept instances of `Number` or its subclasses.

To declare a bounded type parameter, list the type parameter's name, followed by the `extends` keyword, followed by its upper bound.
**Format**: `<T extends superclass>`
**Example**: `<T extends Number>` (Note: T can only be replaced by the superclass or its subclasses).

**Bounded Type Implementation:**
```java
public class Stats <T extends Number> {
    T[] nums;
    
    Stats(T[] ob) {
        nums = ob;
    }
    
    double average() {
        double sum = 0.0;
        for(int i = 0; i < nums.length; i++) {
            sum += nums[i].doubleValue();
        }
        return sum / nums.length;
    }
}

public class BoundDemo {
    public static void main(String[] args) {
        Integer inums[] = {1, 2, 3, 4, 5};
        Double dnums[] = {1.1, 2.2, 3.3, 4.4, 5.5};
        
        Stats<Integer> ob1 = new Stats<>(inums);
        Stats<Double> ob2 = new Stats<>(dnums);
        
        double i = ob1.average();
        System.out.println("Average of Integer Array: " + i);
        
        double d = ob2.average();
        System.out.println("Average of Double Array: " + d);
        
        // Note that the following code segment will give a compilation error
        // as String is not a subclass of Number.
        /*
        String snum[] = {"1", "2", "3", "4", "5"};
        Stats<String> ob3 = new Stats<>(snum); 
        */
    }
}
```

### Multiple Interface Bounds
In addition to using a class type as a bound, you can also use an interface type too! In fact, you can specify multiple interfaces as bounds.
- A bound can include a class type & one or more interfaces. In this case, the **class type needs to be specified first**.
- When specifying a bound that has a class & an interface, use the `&` operator to connect them.

```java
class TClass {}
interface TInterface {}

// T must extend TClass and implement TInterface
public class MyClass <T extends TClass & TInterface> {
    // code
}
```

---

## 7. Wildcards in Java Generics
The `?` symbol represents the wildcard element. It means **any type** can be matched with the `?` symbol.
If we write `<? extends Number>`, it means any child class of `Number` (e.g., `Integer`, `Double`, `Float`, etc.) can be matched.

**Wildcard Implementation:**
```java
import java.util.List;
import java.util.ArrayList;

class Shape {
    void draw() { System.out.println("Drawing Shape"); }
}

class Rectangle extends Shape {
    @Override
    void draw() { System.out.println("Drawing Rectangle"); }
}

class Circle extends Shape {
    @Override
    void draw() { System.out.println("Drawing Circle"); }
}

public class Test {
    // creating a method that accepts only the child class of Shape
    public static void drawShapes(List<? extends Shape> lists) {
        for(Shape s : lists) {
            s.draw();
        }
    }
    
    public static void main(String args[]) {
        List<Rectangle> list1 = new ArrayList<>();
        list1.add(new Rectangle());
        
        List<Circle> list2 = new ArrayList<>();
        list2.add(new Circle());
        list2.add(new Circle());
        
        drawShapes(list1);
        drawShapes(list2);
    }
}
```

---

## 8. Limitations in Generics
1. **Type parameters cannot be instantiated**: It is not possible to create instances of a type parameter (e.g., `new T()`).
2. **Restriction on static members**: No static member can use a type parameter declared by the enclosing class. Note that you *can* declare static generic methods.
3. **Generic array restriction**: Cannot instantiate an array whose element type is a type parameter. Cannot create an array of type specific references.
4. **Generic exception restriction**: A generic class cannot extend `Throwable`. This means we cannot create generic exception classes.

---

## 🧠 Flashcards

What is a Wrapper class in Java? :: A covering class that converts a primitive datatype into an object and an object back into a primitive type; one exists for each primitive in the java.lang package.

What is the wrapper class for `int` and for `char`? :: Integer and Character.

What is autoboxing? :: The automatic conversion of a primitive type into its wrapper object (primitive to object).

What is unboxing? :: The automatic conversion of a wrapper object back into a primitive type (object to primitive).

Since which Java version are autoboxing and unboxing automatic? :: Since J2SE 5.0.

Why must wrapper classes be used with Generics? :: Because primitive types do not support generics, so their object (wrapper) equivalents like Integer must be used instead of int.

What does "Generics" mean in Java? :: Generics mean "parameterized types", allowing the definition of algorithms independently of specific data types.
What are three main advantages of using Generics? :: 1. Type-safety. 2. Type casting is not required. 3. Compile-time checking.
Why is checking for errors at compile-time better than at run-time? :: A good programming strategy says it is far better to handle problems at compile time before the program executes and potentially crashes.
Can you use a primitive type like `int` with Generics? :: No, primitive types do not support Generics. You must make use of their Wrapper classes (e.g., `Integer`).
What does the type parameter convention `T` stand for? :: Type.
What does the type parameter convention `E` stand for? :: Element.
What does the type parameter convention `K` and `V` stand for? :: Key and Value.
What does the type parameter convention `N` stand for? :: Number.
How do you write a generic method that accepts any type of array argument? :: `public static <E> void printArray(E[] elements) { ... }`
What is a bounded type parameter? :: A type parameter restricted to a specific superclass or its subclasses, defined using the `extends` keyword (e.g., `<T extends Number>`).
If a bounded type parameter includes both a class and an interface, which must come first? :: The class type needs to be specified first.
What operator is used to connect multiple interfaces and classes in a bounded type parameter? :: The `&` operator (e.g., `<T extends ClassName & InterfaceName>`).
What symbol represents a wildcard element in Java generics? :: The `?` symbol.
What does `<? extends Number>` mean in Java generics? :: Any child class of `Number` (like Integer or Double) can be matched with the wildcard.
Can you instantiate a type parameter (e.g., `new T()`)? :: No, type parameters cannot be instantiated.
Can a static member use a type parameter declared by its enclosing class? :: No, but you can declare static generic methods.
Can a generic class extend Throwable? :: No, there is a generic exception restriction preventing the creation of generic exception classes.
Can you instantiate an array whose element type is a generic type parameter? :: No, due to generic array restrictions.
#flashcards
