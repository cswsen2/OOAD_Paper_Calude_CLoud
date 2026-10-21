---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 11
topics:
  - singleton pattern
  - creational patterns
  - lazy instantiation
  - eager instantiation
  - thread safety
  - double-checked locking
  - enum singleton
aliases:
  - singleton pattern
  - Singleton Pattern
  - Singleton
  - one-of-a-kind objects
---

# Singleton Pattern

> **Source**: SE2012 OOAD — *Head First Design Patterns*, Chapter 5: *One-of-a-Kind Objects* (used as the lecture deck).

The **[[singleton pattern]]** is our ticket to creating **one-of-a-kind objects** for which there is only **one instance, ever**. Of all the [[design patterns]], the Singleton is the simplest in terms of its class diagram — the diagram holds just a **single class**. But despite its simplicity from a class-design perspective, it requires some deep object-oriented thinking in its **implementation**: as simple as it sounds, *Singleton code is hard to get right*.

> [!NOTE] Official definition
> **The Singleton Pattern ensures a class has only one instance, and provides a global point of access to it.**

Breaking that definition down:
- We take a class and let **it manage a single instance of itself**, and we prevent any other class from creating a new instance on its own. To get an instance, you've got to go **through the class itself**.
- We provide a **global access point** to the instance: whenever you need it, you query the class and it hands back the single instance. This can be implemented so the Singleton is created in a **lazy** manner, which is especially important for **resource-intensive** objects.

---

## Why do we only need one of something?

> [!QUESTION] The Guru–Developer dialogue: what use is "only one"?
> **Developer:** What use is that?
> **Guru:** There are many objects we only need one of: **thread pools, caches, dialog boxes, objects that handle preferences and registry settings, objects used for logging**, and objects that act as **device drivers** to devices like printers and graphics cards. For many of these, if we instantiate **more than one** we run into all sorts of problems: **incorrect program behavior, overuse of resources, or inconsistent results.**

> [!QUESTION] Can't I just use a global variable or a static variable?
> **Developer:** Can't I do this by convention or with global variables — like a `static` variable in Java?
> **Guru:** In many ways the Singleton *is* a convention for ensuring one and only one object is instantiated. It also gives a **global point of access**, just like a global variable, **but without the downsides**.
> **The downside of a global variable:** if you assign an object to a global variable, that object might be **created when the application begins**. If the object is resource-intensive and the application never ends up using it, you've wasted those resources. With the Singleton Pattern, we can **create the object only when it is needed** (lazy instantiation).

---

## The Little Singleton — building it up step by step

A small Socratic exercise (in the style of *The Little Lisper*) walks through the reasoning that leads to the classic implementation.

| Question | Answer |
| --- | --- |
| How would you create a single object? | `new MyObject();` |
| Could another object call `new` on `MyObject` again? | Yes, of course. |
| So as long as we have a class, can we always instantiate it one or more times? | Yes — well, only if it's a **public** class. |
| And if it's **not** public? | Only classes in the **same package** can instantiate it — but they can still instantiate it **more than once**. |
| Did you know you could do this? `private MyClass() {}` | It's a legal definition — a class that **can't be instantiated** because it has a **private constructor**. |
| Is there *any* object that could use the private constructor? | Only the code **in `MyClass` itself** could call it. |
| Why is that a chicken-and-egg problem? | You'd need an **instance** of the class to call the constructor, but you **can't get an instance** because no other class can instantiate it. |
| What does a `public static MyClass getInstance()` method give us? | A **class method** you can call *without an instance*: `MyClass.getInstance();` |

Putting the pieces together produces a class that can hand out an instance of itself **even though its constructor is private**:

```java
public class MyClass {
    private MyClass() {}                          // private constructor

    public static MyClass getInstance() {
        return new MyClass();                     // only MyClass's own code can call new MyClass()
    }
}
```

The final step is to make sure **only ONE** instance is ever created — leading to the classic implementation below.

---

## The Classic Singleton Implementation

```java
public class Singleton {
    private static Singleton uniqueInstance;      // holds our one instance
    // other useful instance variables here

    private Singleton() {}                         // private — only Singleton can instantiate

    public static Singleton getInstance() {        // global access point
        if (uniqueInstance == null) {              // lazy: create only when first needed
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }

    // other useful methods here
}
```

> [!WARNING] Don't blindly type this in
> The book's *"Watch It!"* warning: this classic implementation **has a few issues later in the chapter** (it is **not thread-safe**). Read on before relying on it.

> [!NOTE] Confessions of a Singleton (interview)
> - *"I'm totally unique; there is just one of me."* The Singleton ensures that at any time there is only one instance.
> - **There is power in ONE.** Example: an object holding **registry settings** — you don't want multiple copies running around; that would lead to chaos. A Singleton ensures every object in the application uses the **same global resource**.
> - Good for managing **pools of resources**, like connection or thread pools.
> - *"How do you know there's only one of you? Can't anyone with `new` create a new you?"* — **No. I have no public constructor; my constructor is declared `private`.** To get hold of a Singleton you **don't instantiate one, you ask for an instance** via the static `getInstance()` method.

---

## Worked Example: The Chocolate Factory

> [!QUESTION] The problem scenario — Choc-O-Holic, Inc.
> Every modern chocolate factory has a **computer-controlled chocolate boiler**. The boiler takes in **chocolate and milk**, brings them to a boil, and passes them on to the next phase. The controller tries to be careful so bad things **don't** happen — like draining 500 gallons of **unboiled** mixture, **filling** the boiler when it's already full, or **boiling an empty** boiler.
>
> **But what if two `ChocolateBoiler` instances get loose?** Some very bad things can happen — e.g., the second instance's `fill()` could start filling a boiler that the first instance has already filled and started boiling.

Here is the original (non-Singleton) controller class:

```java
public class ChocolateBoiler {
    private boolean empty;
    private boolean boiled;

    public ChocolateBoiler() {
        empty = true;       // boiler starts empty...
        boiled = false;     // ...and not boiled
    }

    public void fill() {
        if (isEmpty()) {                 // only fill if empty
            empty = false;
            boiled = false;
            // fill the boiler with a milk/chocolate mixture
        }
    }

    public void drain() {
        if (!isEmpty() && isBoiled()) {  // only drain if full AND boiled
            // drain the boiled milk and chocolate
            empty = true;
        }
    }

    public void boil() {
        if (!isEmpty() && !isBoiled()) { // only boil if full AND not yet boiled
            // bring the contents to a boil
            boiled = true;
        }
    }

    public boolean isEmpty() {
        return empty;
    }

    public boolean isBoiled() {
        return boiled;
    }
}
```

Turning `ChocolateBoiler` into a Singleton (the "Sharpen Your Pencil" solution) — add the private static instance, make the constructor private, and provide `getInstance()`:

```java
public class ChocolateBoiler {
    private boolean empty;
    private boolean boiled;
    private static ChocolateBoiler uniqueInstance;     // the one instance

    private ChocolateBoiler() {                          // private constructor
        empty = true;
        boiled = false;
    }

    public static ChocolateBoiler getInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new ChocolateBoiler();
        }
        return uniqueInstance;
    }

    public void fill() {
        if (isEmpty()) {
            empty = false;
            boiled = false;
            // fill the boiler with a milk/chocolate mixture
        }
    }

    public void drain() {
        if (!isEmpty() && isBoiled()) {
            // drain the boiled milk and chocolate
            empty = true;
        }
    }

    public void boil() {
        if (!isEmpty() && !isBoiled()) {
            // bring the contents to a boil
            boiled = true;
        }
    }

    public boolean isEmpty() {
        return empty;
    }

    public boolean isBoiled() {
        return boiled;
    }
}
```

---

## "Hershey, PA, we have a problem..." — the multithreading bug

> [!IMPORTANT] The race condition
> Despite improving the code with the **classic** Singleton, the boiler's `fill()` method was somehow able to **start filling the boiler even though a batch was already boiling** — 500 gallons of spilled milk and chocolate!
>
> **The cause:** the addition of **[[Threads|threads]]**. Two threads can both enter `getInstance()`, both find `uniqueInstance == null`, and both call `new ChocolateBoiler()` — producing **two different instances**.

### Fix 1 — Synchronize `getInstance()`

The multithreading woes are *almost trivially* fixed by making `getInstance()` a **`synchronized`** method:

```java
public class Singleton {
    private static Singleton uniqueInstance;

    private Singleton() {}

    public static synchronized Singleton getInstance() {   // only one thread at a time
        if (uniqueInstance == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }
}
```

> [!WARNING] The cost of synchronization
> The **only time synchronization is relevant is the first time** through the method. Once `uniqueInstance` is set, synchronizing is **totally unneeded overhead** — and synchronizing a method can **decrease performance by a factor of 100**. See [[Threads]] for how `synchronized` works.

### Can we improve multithreading? Three options

> [!NOTE] Option 1 — Do nothing (if performance isn't critical)
> If calling `getInstance()` isn't causing substantial overhead, **just synchronize it** — it's straightforward and effective. Only reconsider if a **high-traffic** part of your code begins using `getInstance()`.

> [!NOTE] Option 2 — Eagerly created instance (instead of lazy)
> If your application **always** creates and uses the Singleton, or creation overhead isn't onerous, create it **eagerly**. We rely on the **JVM** to create the unique instance when the class is loaded; the JVM **guarantees** the instance is created **before any thread accesses** the static variable.
>
> ```java
> public class Singleton {
>     private static Singleton uniqueInstance = new Singleton();   // created at class load
>
>     private Singleton() {}
>
>     public static Singleton getInstance() {
>         return uniqueInstance;                                   // already created
>     }
> }
> ```

> [!NOTE] Option 3 — Double-Checked Locking
> First check if an instance exists, and **only if it doesn't** do we synchronize. This way we synchronize **only the first time** through — exactly what we want. If performance is an issue, this can **drastically reduce** the overhead.
>
> ```java
> public class Singleton {
>     private volatile static Singleton uniqueInstance;            // volatile ensures correct multithread handling
>
>     private Singleton() {}
>
>     public static Singleton getInstance() {
>         if (uniqueInstance == null) {                            // check 1 (no lock)
>             synchronized (Singleton.class) {                     // lock only if needed
>                 if (uniqueInstance == null) {                    // check 2 (with lock)
>                     uniqueInstance = new Singleton();
>                 }
>             }
>         }
>         return uniqueInstance;
>     }
> }
> ```

> [!WARNING] Double-checked locking doesn't work in Java 1.4 or earlier!
> In Java **1.4 and earlier**, many JVMs contain implementations of the `volatile` keyword that **allow improper synchronization** for double-checked locking. If you must use a JVM earlier than **Java 5**, consider other methods of implementing your Singleton.

### Choosing the fix for the Chocolate Boiler

| Solution | Applicability to the Chocolate Boiler |
| --- | --- |
| **Synchronize `getInstance()`** | A straightforward technique, **guaranteed to work**. We have no performance concerns with the boiler, so this is a **good choice**. |
| **Eager instantiation** | We always instantiate the boiler in our code, so statically initializing it causes **no concerns**. Works as well as the synchronized method, though perhaps **less obvious** to a developer familiar with the standard pattern. |
| **Double-checked locking** | Given we have **no performance concerns**, this seems like **overkill**. We'd also have to ensure we're running at least **Java 5**. |

---

## The Enum Singleton — the simplest of all

Many of the problems discussed — **synchronization, class-loading issues, reflection, and serialization/deserialization** — can **all be solved** by using an **`enum`** to create your Singleton:

```java
public enum Singleton {
    UNIQUE_INSTANCE;
    // more useful fields here
}

public class SingletonClient {
    public static void main(String[] args) {
        Singleton singleton = Singleton.UNIQUE_INSTANCE;
        // use the singleton here
    }
}
```

> [!TIP] Why bother learning the hard way first?
> *"Why did we go through all that earlier with `getInstance()`, synchronizing, and so on?"* — So you **truly understand how Singleton works**. Now you can use `enum` whenever you need a Singleton, and still ace the interview question: **"How do you implement a Singleton *without* using enum?"**

---

## Pitfalls & "There Are No Dumb Questions"

> [!QUESTION] Why not just a class with all `static` methods and variables?
> That can work **if the class is self-contained and doesn't depend on complex initialization**. However, because of how static initializations are handled in Java, it gets **messy** — especially across multiple classes — and can cause **subtle order-of-initialization bugs**. Unless there's a compelling need, stay in the **object world**.

> [!QUESTION] Could two class loaders each end up with their own Singleton?
> **Yes.** Each class loader defines a **namespace**. With two or more class loaders you can load the same class **multiple times** (once per loader), giving **more than one instance** of the Singleton. Workaround: **specify the class loader yourself**.

> [!QUESTION] What about reflection and serialization/deserialization?
> They can **also present problems** with Singletons. Advanced Java users employing reflection, serialization, and deserialization need to keep this in mind (the `enum` approach avoids these issues).

> [!QUESTION] Doesn't a Singleton violate loose coupling?
> Yes — this is a **common criticism**. Every object depending on the Singleton is **tightly coupled** to that one specific object, so a change to the Singleton likely forces changes in every object connected to it. (See [[loose coupling]].)

> [!QUESTION] Doesn't it violate the Single Responsibility Principle?
> Yes — the Singleton is responsible **both** for managing its one instance (and global access) **and** for its main role in the application — arguably **two responsibilities**. Still, there's utility in a class managing its own instance, and it's a widely understood pattern. (See [[SOLID principles]].)

> [!QUESTION] Is it okay to subclass a Singleton?
> Problematic. The **private constructor** can't be extended, so you'd have to make it `public`/`protected` — but then it's **not really a Singleton** anymore. Also, the static instance variable would be **shared** across all subclasses (probably not what you want), so subclassing requires implementing a **registry** in the base class.

> [!QUESTION] Why are global variables worse than a Singleton?
> In Java, global variables are basically **static references** to objects. A global variable can give you **global access** but **not** the guarantee of **one instance** — and globals tend to encourage **polluting the namespace** with many references to small objects. Globals also force **eager** instantiation, losing the lazy benefit.

---

## Key Points (Bullet Points)

- The Singleton Pattern ensures you have **at most one instance** of a class in your application.
- It also provides a **global access point** to that instance.
- Java's implementation uses a **private constructor**, a **static method**, and a **static variable**.
- Examine your **performance and resource constraints** and carefully choose an appropriate implementation for multithreaded applications (**consider all applications multithreaded!**).
- **Beware double-checked locking** — it isn't thread-safe in versions before **Java 5**.
- Be careful with **multiple class loaders** — they can defeat the Singleton and result in multiple instances.
- You can use Java's **`enum`** to simplify your Singleton implementation.

> The classic vs. thread-safe Singletons are also summarized in the **[[Design Patterns]]** overview and connect to the synchronization machinery in **[[Threads]]**. Singleton is one of the **creational** [[design patterns]], alongside the **[[factory method pattern]]** and **[[abstract factory pattern]]** (see **[[Factory Pattern]]**).

---

## 🧠 Flashcards

What does the [[singleton pattern]] ensure? :: That a class has only one instance, ever, and provides a global point of access to it.

What three Java mechanisms make a classic Singleton work? :: A private constructor, a private static instance variable, and a public static getInstance() method.

Why is the Singleton constructor declared private? :: So no other class can use `new` to create additional instances — only the class's own getInstance() can create the single instance.

What is lazy instantiation in a Singleton? :: Creating the instance only when it is first requested (inside getInstance() when uniqueInstance == null), rather than at class-load time — important for resource-intensive objects.

What is the bug in the classic (unsynchronized) Singleton? :: It is not thread-safe — two threads can both see uniqueInstance == null and each create a separate instance.

How does the `synchronized` keyword fix the Singleton, and what is the cost? :: Marking getInstance() synchronized lets only one thread enter at a time, preventing duplicate creation; the cost is that synchronization (only needed the first time) can slow the method by up to ~100x.

What is eager instantiation and why is it thread-safe? :: Creating the instance at class-load time (`private static Singleton uniqueInstance = new Singleton();`); the JVM guarantees the instance exists before any thread accesses the variable.

How does double-checked locking work? :: Check if the instance is null without locking; if null, synchronize on the class and check again inside the lock before creating it — so synchronization happens only on the first call.

Why must the double-checked-locking instance variable be `volatile`, and when does this fail? :: volatile ensures correct cross-thread visibility of the instance; double-checked locking does not work correctly in Java 1.4 or earlier due to flawed volatile implementations.

What is the simplest correct Singleton in Java? :: An enum with a single value (e.g. `public enum Singleton { UNIQUE_INSTANCE; }`), which also solves synchronization, class-loader, reflection, and serialization problems.

Name four kinds of objects you typically only need one of. :: Thread pools, caches, dialog boxes, and objects handling preferences/registry settings (also logging objects and device drivers).

How can multiple class loaders defeat a Singleton? :: Each class loader is its own namespace, so the same Singleton class can be loaded once per loader, yielding multiple instances; you can fix this by specifying the class loader yourself.

Which two design principles does the Singleton arguably violate? :: Loose coupling (dependents are tightly coupled to it) and the Single Responsibility Principle (it manages its instance AND does its main job).

Why is a Singleton better than a global variable? :: A global gives global access but cannot guarantee a single instance, forces eager creation, and encourages namespace pollution; the Singleton guarantees one instance and supports lazy creation.

Why is subclassing a Singleton problematic? :: Its private constructor can't be extended (forcing you to weaken it), and the static instance variable would be shared across subclasses — so it requires a registry in the base class.

#flashcards
