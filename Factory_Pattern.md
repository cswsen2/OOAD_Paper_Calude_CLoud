---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 11
topics:
  - factory pattern
  - simple factory
  - factory method pattern
  - abstract factory pattern
  - creational patterns
  - dependency inversion principle
aliases:
  - factory pattern
  - Factory Pattern
  - simple factory
  - Simple Factory
  - factory method pattern
  - Factory Method Pattern
  - abstract factory pattern
  - Abstract Factory Pattern
  - dependency inversion principle
  - Dependency Inversion Principle
---

# Factory Pattern

> **Source**: SE2012 OOAD — *Head First Design Patterns*, Chapter 4: *Baking with OO Goodness* (used as the lecture deck).

Get ready to bake some **loosely coupled** OO designs. There is more to making objects than just using the **`new`** operator. **Instantiation** is an activity that shouldn't always be done in public — it can often lead to **coupling problems**. The **factory** [[design patterns]] help save you from embarrassing dependencies.

This chapter covers **three** things that are easy to confuse:
1. **Simple Factory** — a programming idiom (not a true pattern).
2. **[[factory method pattern|Factory Method Pattern]]** — relies on **[[inheritance]]**.
3. **[[abstract factory pattern|Abstract Factory Pattern]]** — relies on **[[composition]]**.

It also introduces a new OO design principle: the **[[dependency inversion principle|Dependency Inversion Principle]]**.

---

## What's wrong with `new`?

> [!IMPORTANT] When you see `new`, think "concrete"
> When you use the `new` operator you are instantiating a **concrete class** — that's an implementation, not an interface. Tying your code to a concrete class makes it **more fragile and less flexible**.

When we have a whole set of related concrete classes, we often end up writing code that decides **which to instantiate at runtime**, depending on conditions:

```java
Duck duck;
if (picnic) {
    duck = new MallardDuck();
} else if (hunting) {
    duck = new DecoyDuck();
} else if (inBathTub) {
    duck = new RubberDuck();
}
```

When it comes time for changes or extensions, you'll have to **reopen this code** and examine what to add or delete. This kind of code often ends up in **several parts** of the application, making maintenance error-prone.

> [!NOTE] The real culprit is CHANGE
> Technically there's nothing wrong with `new` — it's fundamental to OO languages. The problem is **change**. By **coding to an interface**, you insulate yourself from changes: your code works with **any** new class implementing that interface, via **[[polymorphism]]**. Code that uses lots of **concrete classes** is not *"closed for modification"* — to extend it with new concrete types, you must reopen it. (Remember: designs should be **"open for extension but closed for modification"** — the **Open/Closed Principle**.)

> [!NOTE] Brain Power
> How might you take all the parts of your application that **instantiate concrete classes** and **separate or encapsulate** them from the rest of your application? (Answer: a Factory.)

---

## Identifying What Varies: The Pizza Store

> [!QUESTION] The problem scenario — a cutting-edge pizza store
> As a pizza store owner in Objectville, you start with simple ordering code. But you need **more than one type** of pizza, so you add code to pick the right type — and then competitors add **Clam** and **Veggie** pizzas while **Greek** stops selling. Every menu change forces you to edit `orderPizza()`. The `new` calls are **messing up `orderPizza()` and preventing it from being closed for modification.**

The starting point — one kind of pizza:

```java
Pizza orderPizza() {
    Pizza pizza = new Pizza();

    pizza.prepare();
    pizza.bake();
    pizza.cut();
    pizza.box();
    return pizza;
}
```

Adding a type parameter so we can make different pizzas:

```java
Pizza orderPizza(String type) {
    Pizza pizza;

    if (type.equals("cheese")) {
        pizza = new CheesePizza();
    } else if (type.equals("greek")) {
        pizza = new GreekPizza();
    } else if (type.equals("pepperoni")) {
        pizza = new PepperoniPizza();
    }

    pizza.prepare();
    pizza.bake();
    pizza.cut();
    pizza.box();
    return pizza;
}
```

Now the menu changes (add Clam & Veggie, remove Greek). The part that **varies** is the instantiation block; the part that **stays the same** is `prepare/bake/cut/box`:

```java
Pizza orderPizza(String type) {
    Pizza pizza;

    if (type.equals("cheese")) {
        pizza = new CheesePizza();
    } else if (type.equals("clam")) {        // added — keeping up with competitors
        pizza = new ClamPizza();
    } else if (type.equals("veggie")) {      // added
        pizza = new VeggiePizza();
    } else if (type.equals("pepperoni")) {
        pizza = new PepperoniPizza();
    }
    // GreekPizza removed — wasn't selling

    pizza.prepare();                         // this part does NOT change
    pizza.bake();
    pizza.cut();
    pizza.box();
    return pizza;
}
```

---

## Simple Factory

We move the object creation **out** of `orderPizza()` and into another object that is **only concerned with creating pizzas** — a **Factory**.

```java
public class SimplePizzaFactory {
    public Pizza createPizza(String type) {
        Pizza pizza = null;

        if (type.equals("cheese")) {
            pizza = new CheesePizza();
        } else if (type.equals("pepperoni")) {
            pizza = new PepperoniPizza();
        } else if (type.equals("clam")) {
            pizza = new ClamPizza();
        } else if (type.equals("veggie")) {
            pizza = new VeggiePizza();
        }
        return pizza;
    }
}
```

Reworked `PizzaStore` — it is **composed** with a factory and becomes a **client** of it:

```java
public class PizzaStore {
    SimplePizzaFactory factory;

    public PizzaStore(SimplePizzaFactory factory) {     // factory passed in
        this.factory = factory;
    }

    public Pizza orderPizza(String type) {
        Pizza pizza;

        pizza = factory.createPizza(type);              // ask the factory; no more `new`
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();
        return pizza;
    }
}
```

> [!QUESTION] Aren't we just pushing the problem to another object?
> The `SimplePizzaFactory` may have **many clients** — `orderPizza()`, a `PizzaShopMenu` for descriptions/prices, a `HomeDelivery` class, etc. By encapsulating creation in **one class**, we now have **only one place** to make changes when implementations change.

> [!NOTE] Static Factory
> A simple factory is sometimes defined as a **static method** (a *static factory*). The advantage: you don't need to instantiate an object to use the create method. The disadvantage: you **can't subclass** and change the behavior of the create method.

> [!IMPORTANT] Simple Factory is NOT a real Design Pattern
> It's more of a **programming idiom** (a "Head First Pattern Honorable Mention"). Some developers mistake it for the Factory Pattern. Think of Simple Factory as a **warm-up** for the two heavy-duty factory patterns that follow.

> [!NOTE] "Implement an interface" — a clarification
> In design patterns, *"implement an interface"* does **not** always mean writing a class with Java's `implements` keyword. In the general sense, a concrete class implementing a method from a **supertype** (whether an **abstract class OR an interface**) is still "implementing the interface" of that supertype.

---

## Factory Method Pattern

> [!QUESTION] Franchising the pizza store
> Your store does so well that everyone wants a franchise. But **regional differences** matter — New York wants thin crust, Chicago wants deep dish, California wants cracker-thin. One approach is three separate factories (`NYPizzaFactory`, `ChicagoPizzaFactory`, `CaliforniaPizzaFactory`) composed into the store. But the franchises started **employing their own home-grown procedures** for the rest of the process — baking differently, forgetting to cut, using third-party boxes. You want a **framework that ties the store and pizza creation together yet stays flexible**.

The solution: put `createPizza()` **back into `PizzaStore`**, but as an **abstract method**, and create a **subclass for each region**.

```java
public abstract class PizzaStore {

    public Pizza orderPizza(String type) {
        Pizza pizza;

        pizza = createPizza(type);            // calls the subclass's factory method
        pizza.prepare();                      // the well-tuned, consistent order process
        pizza.bake();
        pizza.cut();
        pizza.box();
        return pizza;
    }

    // The "factory method" — abstract, so subclasses decide which concrete Pizza to make
    abstract Pizza createPizza(String type);
}
```

Each region subclasses `PizzaStore` and implements `createPizza()` — deciding **which concrete pizza** to make:

```java
public class NYPizzaStore extends PizzaStore {

    Pizza createPizza(String item) {
        if (item.equals("cheese")) {
            return new NYStyleCheesePizza();
        } else if (item.equals("veggie")) {
            return new NYStyleVeggiePizza();
        } else if (item.equals("clam")) {
            return new NYStyleClamPizza();
        } else if (item.equals("pepperoni")) {
            return new NYStylePepperoniPizza();
        } else return null;
    }
}
```

```java
public class ChicagoPizzaStore extends PizzaStore {

    Pizza createPizza(String item) {
        if (item.equals("cheese")) {
            return new ChicagoStyleCheesePizza();
        } else if (item.equals("veggie")) {
            return new ChicagoStyleVeggiePizza();
        } else if (item.equals("clam")) {
            return new ChicagoStyleClamPizza();
        } else if (item.equals("pepperoni")) {
            return new ChicagoStylePepperoniPizza();
        } else return null;
    }
}
```

> [!NOTE] Who "decides" which class to instantiate?
> The `orderPizza()` method in the abstract `PizzaStore` has **no clue** which concrete pizza is created — it just knows it can `prepare/bake/cut/box` it: it's **decoupled**. We say *"the subclass decides"* not because the subclass makes a runtime choice, but because **the decision comes down to which subclass you chose** (NY vs. Chicago store).

### The Product classes

The pizzas themselves. The abstract `Pizza`:

```java
import java.util.ArrayList;

public abstract class Pizza {
    String name;
    String dough;
    String sauce;
    ArrayList<String> toppings = new ArrayList<String>();

    void prepare() {
        System.out.println("Preparing " + name);
        System.out.println("Tossing dough...");
        System.out.println("Adding sauce...");
        System.out.println("Adding toppings: ");
        for (String topping : toppings) {
            System.out.println("   " + topping);
        }
    }

    void bake() {
        System.out.println("Bake for 25 minutes at 350");
    }

    void cut() {
        System.out.println("Cutting the pizza into diagonal slices");
    }

    void box() {
        System.out.println("Place pizza in official PizzaStore box");
    }

    public String getName() {
        return name;
    }
}
```

A concrete NY-style cheese pizza (sets its own ingredients in the constructor):

```java
public class NYStyleCheesePizza extends Pizza {

    public NYStyleCheesePizza() {
        name = "NY Style Sauce and Cheese Pizza";
        dough = "Thin Crust Dough";
        sauce = "Marinara Sauce";

        toppings.add("Grated Reggiano Cheese");
    }
}
```

A concrete Chicago-style cheese pizza — note it **overrides `cut()`** because Chicago cuts square slices:

```java
public class ChicagoStyleCheesePizza extends Pizza {

    public ChicagoStyleCheesePizza() {
        name = "Chicago Style Deep Dish Cheese Pizza";
        dough = "Extra Thick Crust Dough";
        sauce = "Plum Tomato Sauce";

        toppings.add("Shredded Mozzarella Cheese");
    }

    void cut() {
        System.out.println("Cutting the pizza into square slices");
    }
}
```

Ordering pizzas (Ethan orders NY, Joel orders Chicago):

```java
public class PizzaTestDrive {

    public static void main(String[] args) {
        PizzaStore nyStore = new NYPizzaStore();
        PizzaStore chicagoStore = new ChicagoPizzaStore();

        Pizza pizza = nyStore.orderPizza("cheese");
        System.out.println("Ethan ordered a " + pizza.getName() + "\n");

        pizza = chicagoStore.orderPizza("cheese");
        System.out.println("Joel ordered a " + pizza.getName() + "\n");
    }
}
```

> [!NOTE] How ordering works (step by step)
> 1. Joel needs a `ChicagoPizzaStore`; Ethan needs a `NYPizzaStore`.
> 2. With a store in hand, both call `orderPizza()` passing the type (cheese, veggie, ...).
> 3. `createPizza()` — defined in the **subclass** — instantiates the regional pizza and returns it to `orderPizza()`.
> 4. `orderPizza()` has **no idea** what kind of pizza was created, but it `prepare/bake/cut/box`es it anyway.

### Factory Method Pattern defined

> [!NOTE] Official definition
> **The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.**

- The abstract **Creator** gives you an interface with a method (the **factory method**) for creating objects. Other methods in the Creator operate on the products the factory method produces.
- Only **subclasses** actually implement the factory method and create products.
- **Creator** and **Product** classes form **parallel class hierarchies** — for every concrete Creator there's a set of products it creates.

> [!QUESTION] There Are No Dumb Questions
> - **Advantage with only one ConcreteCreator?** Still useful — you **decouple** the product's implementation from its use, so changing/adding products won't affect the Creator.
> - **Are NY/Chicago stores just Simple Factory?** Similar, but different: the concrete stores **extend** a class that defines `createPizza()` as **abstract**; in Simple Factory the factory is a **separate object composed** into the store.
> - **Are the factory method and Creator always abstract?** No — you can define a **default** factory method producing a concrete product, so you can create products even with no subclasses.
> - **Do all concrete creators make multiple products?** Our `createPizza(String)` is a **parameterized factory method** (makes more than one product based on a parameter). Often a factory just produces **one** object and is not parameterized. Both are valid.
> - **Is `String type` type-safe?** No — asking for a `"CalmPizza"` causes a **runtime error**. You can make it safer with parameter objects, **static constants**, or **enums**.

---

## Looking at Object Dependencies & the Dependency Inversion Principle

> [!QUESTION] The "very dependent" PizzaStore
> A version of `PizzaStore` that instantiates all the pizzas **itself** (no factory) is **dependent on every concrete pizza class**. If you draw it, the high-level `PizzaStore` depends on a large number of low-level concrete pizza classes. Reducing those dependencies is clearly a "good thing".

> [!IMPORTANT] The Dependency Inversion Principle
> **Depend upon abstractions. Do not depend upon concrete classes.**
>
> This sounds like *"program to an interface, not an implementation,"* but it makes a **stronger** statement: **high-level components should not depend on low-level components — both should depend on abstractions.**

> [!NOTE] High-level vs. low-level components
> A **"high-level" component** is a class whose behavior is defined in terms of other, **"low-level"** components. `PizzaStore` is high-level because its behavior is defined in terms of pizzas (it creates, prepares, bakes, cuts, boxes them); the pizzas are the low-level components.

**Applying it:** the problem with the very-dependent `PizzaStore` is that it **instantiates concrete pizzas** in `orderPizza()`. Applying the **[[factory method pattern]]** gets those instantiations out, so that **both** the high-level `PizzaStore` **and** the low-level pizzas now depend on the **abstraction `Pizza`**.

> [!NOTE] Where's the "inversion"?
> It **inverts** the typical top-down thinking. Normally you start at the top (`PizzaStore`) and follow down to concrete pizza classes. Instead, **start at the Pizzas and think about what you can abstract** (`Pizza`), then design the store against that abstraction. Now **both high-level and low-level modules depend on the abstraction** — the dependency chart has flipped.

### Guidelines to follow the principle

| Guideline | Note |
| --- | --- |
| **No variable should hold a reference to a concrete class.** | If you use `new`, you're holding a reference to a concrete class — use a factory to get around it. |
| **No class should derive from a concrete class.** | Derive from an **abstraction** (an interface or abstract class) instead. |
| **No method should override an implemented method of any of its base classes.** | If you override an implemented method, the base class wasn't really an abstraction to start with. |

> [!WARNING] These are guidelines, not absolute rules
> Every Java program ever written **violates** these guidelines! They are something to **strive for**, not follow all the time. If a class **isn't likely to change** (like `String`), it's fine to instantiate it directly — we create `String` objects all the time. Reserve the effort (e.g., Factory Method) for classes that **are** likely to change.

---

## Abstract Factory Pattern

> [!QUESTION] Ensuring consistent ingredients
> Your franchises follow the framework, but some are **substituting inferior ingredients** to cut costs — hurting the Objectville brand. Solution: **build a factory that produces the ingredients** and ships them to franchises. But ingredients are **regional** — "red sauce" in New York isn't "red sauce" in Chicago. You must handle **families of ingredients** (each region implements a complete family: dough, sauce, cheese, veggies, meats...).

Define an interface for a factory that creates a **whole family** of ingredients:

```java
public interface PizzaIngredientFactory {
    public Dough createDough();
    public Sauce createSauce();
    public Cheese createCheese();
    public Veggies[] createVeggies();
    public Pepperoni createPepperoni();
    public Clams createClam();
}
```

The plan:
1. Build a factory for **each region** (a subclass implementing each `create` method).
2. Implement the **ingredient classes** (`ReggianoCheese`, `RedPeppers`, `ThickCrustDough`...), shared among regions where appropriate.
3. Hook the new ingredient factories into the existing `PizzaStore` code.

The New York ingredient factory — specializes in marinara, Reggiano, fresh clams, etc.:

```java
public class NYPizzaIngredientFactory implements PizzaIngredientFactory {

    public Dough createDough() {
        return new ThinCrustDough();
    }

    public Sauce createSauce() {
        return new MarinaraSauce();
    }

    public Cheese createCheese() {
        return new ReggianoCheese();
    }

    public Veggies[] createVeggies() {
        Veggies veggies[] = { new Garlic(), new Onion(), new Mushroom(), new RedPepper() };
        return veggies;
    }

    public Pepperoni createPepperoni() {
        return new SlicedPepperoni();
    }

    public Clams createClam() {
        return new FreshClams();
    }
}
```

The Chicago ingredient factory (the "Sharpen Your Pencil" solution) — note **thick crust**, **plum tomato sauce**, **mozzarella**, and **frozen clams**:

```java
public class ChicagoPizzaIngredientFactory implements PizzaIngredientFactory {

    public Dough createDough() {
        return new ThickCrustDough();
    }

    public Sauce createSauce() {
        return new PlumTomatoSauce();
    }

    public Cheese createCheese() {
        return new MozzarellaCheese();
    }

    public Veggies[] createVeggies() {
        Veggies veggies[] = { new BlackOlives(), new Spinach(), new Eggplant() };
        return veggies;
    }

    public Pepperoni createPepperoni() {
        return new SlicedPepperoni();
    }

    public Clams createClam() {
        return new FrozenClams();
    }
}
```

### Reworking the Pizzas to use ingredient factories

The abstract `Pizza` now holds **ingredient objects** (not strings) and `prepare()` becomes **abstract** — each pizza collects its ingredients from the factory:

```java
public abstract class Pizza {
    String name;

    Dough dough;
    Sauce sauce;
    Veggies veggies[];
    Cheese cheese;
    Pepperoni pepperoni;
    Clams clam;

    abstract void prepare();                 // now abstract — uses the ingredient factory

    void bake() {
        System.out.println("Bake for 25 minutes at 350");
    }

    void cut() {
        System.out.println("Cutting the pizza into diagonal slices");
    }

    void box() {
        System.out.println("Place pizza in official PizzaStore box");
    }

    void setName(String name) {
        this.name = name;
    }

    String getName() {
        return name;
    }

    public String toString() {
        StringBuffer result = new StringBuffer();
        result.append("---- " + name + " ----\n");
        if (dough != null) {
            result.append(dough);
            result.append("\n");
        }
        if (sauce != null) {
            result.append(sauce);
            result.append("\n");
        }
        if (cheese != null) {
            result.append(cheese);
            result.append("\n");
        }
        if (veggies != null) {
            for (int i = 0; i < veggies.length; i++) {
                result.append(veggies[i]);
                if (i < veggies.length - 1) {
                    result.append(", ");
                }
            }
            result.append("\n");
        }
        if (clam != null) {
            result.append(clam);
            result.append("\n");
        }
        if (pepperoni != null) {
            result.append(pepperoni);
            result.append("\n");
        }
        return result.toString();
    }
}
```

Because the **factory** now handles regional differences, we no longer need separate `NYCheesePizza` / `ChicagoCheesePizza` classes — **one `CheesePizza`** works everywhere; it just pulls ingredients from whichever factory it was composed with:

```java
public class CheesePizza extends Pizza {
    PizzaIngredientFactory ingredientFactory;

    public CheesePizza(PizzaIngredientFactory ingredientFactory) {
        this.ingredientFactory = ingredientFactory;
    }

    void prepare() {
        System.out.println("Preparing " + name);
        dough = ingredientFactory.createDough();
        sauce = ingredientFactory.createSauce();
        cheese = ingredientFactory.createCheese();
    }
}
```

```java
public class ClamPizza extends Pizza {
    PizzaIngredientFactory ingredientFactory;

    public ClamPizza(PizzaIngredientFactory ingredientFactory) {
        this.ingredientFactory = ingredientFactory;
    }

    void prepare() {
        System.out.println("Preparing " + name);
        dough = ingredientFactory.createDough();
        sauce = ingredientFactory.createSauce();
        cheese = ingredientFactory.createCheese();
        clam = ingredientFactory.createClam();       // NY → FreshClams, Chicago → FrozenClams
    }
}
```

### Revisiting the pizza stores

Each store gives its pizzas a reference to its **local ingredient factory**:

```java
public class NYPizzaStore extends PizzaStore {

    protected Pizza createPizza(String item) {
        Pizza pizza = null;
        PizzaIngredientFactory ingredientFactory =
            new NYPizzaIngredientFactory();           // the regional ingredient factory

        if (item.equals("cheese")) {
            pizza = new CheesePizza(ingredientFactory);
            pizza.setName("New York Style Cheese Pizza");
        } else if (item.equals("veggie")) {
            pizza = new VeggiePizza(ingredientFactory);
            pizza.setName("New York Style Veggie Pizza");
        } else if (item.equals("clam")) {
            pizza = new ClamPizza(ingredientFactory);
            pizza.setName("New York Style Clam Pizza");
        } else if (item.equals("pepperoni")) {
            pizza = new PepperoniPizza(ingredientFactory);
            pizza.setName("New York Style Pepperoni Pizza");
        }
        return pizza;
    }
}
```

### Abstract Factory Pattern defined

> [!NOTE] Official definition
> **The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.**

- An Abstract Factory gives an **interface for a family of products** (everything to make a pizza: dough, sauce, cheese, meats, veggies).
- From it we derive **concrete factories** that produce the same products with **different implementations**.
- Client code is written against the **interface**, so passing in different factories yields different product implementations while the **client code stays the same**.

> [!NOTE] Is there a Factory Method lurking inside the Abstract Factory?
> **Yes** — often the methods of an Abstract Factory are implemented as **factory methods**. Each method in the interface is responsible for creating a concrete product, and a subclass supplies the implementation. So factory methods are a natural way to implement the product methods inside abstract factories.

---

## Factory Method vs. Abstract Factory

> [!QUESTION] Patterns Exposed — the interview
> Both patterns **encapsulate object creation** and **decouple clients from concrete types**, but they do it differently:
> - **Factory Method** creates objects through **[[inheritance]]** — you **extend a class and override a factory method**. It creates **one** product, so it needs only **one method**.
> - **Abstract Factory** creates objects through **object [[composition]]** — you **instantiate a factory and pass it** into code written against the abstract type. It creates **families** of products, so it needs a **bigger interface**.
> - **Downside of Abstract Factory:** if you need to **add a new product** to the family, you must **change the interface** — which means changing **every** subclass that implements it.

| Aspect | Factory Method | Abstract Factory |
| --- | --- | --- |
| **Mechanism** | Inheritance (subclass overrides the factory method) | Object composition (factory instantiated and passed in) |
| **Creates** | One product | Families of related products |
| **Interface size** | One method | Larger interface (one method per product) |
| **Intent** | Let a class **defer instantiation to subclasses** | Create **families of related objects** without depending on their concrete classes |
| **Cost of adding a product** | Add/override in the subclass | Must change the factory interface and **all** implementing subclasses |

---

## Key Points (Bullet Points)

- **All factories encapsulate object creation.**
- **Simple Factory**, while not a bona fide design pattern, is a simple way to decouple clients from concrete classes.
- **Factory Method** relies on **inheritance**: object creation is delegated to **subclasses** that implement the factory method.
- **Abstract Factory** relies on **object composition**: object creation is implemented in methods exposed in the factory **interface**.
- All factory patterns promote **loose coupling** by reducing dependency on concrete classes.
- The intent of **Factory Method** is to allow a class to **defer instantiation to its subclasses**.
- The intent of **Abstract Factory** is to **create families of related objects** without depending on their concrete classes.
- The **[[dependency inversion principle]]** guides us to avoid dependencies on concrete types and strive for **abstractions**.

> Both factory patterns are **creational** [[design patterns]] (alongside the **[[singleton pattern]]** — see **[[Singleton Pattern]]**). They lean on [[inheritance]] and [[composition]] (compare the **[[UML Class Relationships]]**), [[abstraction]], and [[polymorphism]] from **[[OOP Fundamentals]]**. The parameterized `ArrayList<String> toppings` ties into **[[Java Collections Framework]]** and **[[Java Generics]]**. The overview lives in **[[Design Patterns]]**; the contrasting **behavioral** intent is shown by the **[[command pattern]]** (see **[[Command Pattern]]**).

---

## 🧠 Flashcards

What problem does using `new` directly cause? :: It ties your code to a concrete class (an implementation), making it fragile, less flexible, and not "closed for modification" when new concrete types are added.

What is a Simple Factory and is it a real design pattern? :: A class (or static method) that encapsulates object creation behind a createPizza()-style method; it is NOT a real design pattern — it's a programming idiom/honorable mention.

What is a static factory and its trade-off? :: A simple factory defined as a static method — you can call it without instantiating the factory, but you cannot subclass it to change the create method's behavior.

What is the official definition of the [[factory method pattern]]? :: It defines an interface for creating an object but lets subclasses decide which class to instantiate — letting a class defer instantiation to subclasses.

How does the abstract PizzaStore use the factory method? :: orderPizza() (concrete, in the superclass) calls the abstract createPizza() (the factory method), which each regional subclass implements to return its own concrete pizza.

In what sense do subclasses "decide" which class to instantiate in Factory Method? :: Not by a runtime choice — the decision comes down to which subclass (e.g. NYPizzaStore vs ChicagoPizzaStore) you instantiate.

What is a parameterized factory method? :: A factory method that creates more than one kind of product based on a parameter passed in (e.g. createPizza("cheese") vs createPizza("veggie")).

What are parallel class hierarchies in Factory Method? :: The Creator hierarchy (PizzaStore subclasses) runs parallel to the Product hierarchy (Pizza subclasses) — each concrete creator produces a corresponding set of products.

What is the Dependency Inversion Principle? :: Depend upon abstractions; do not depend upon concrete classes — and high-level components should not depend on low-level ones; both should depend on abstractions.

Where is the "inversion" in the Dependency Inversion Principle? :: It flips top-down thinking: instead of the high-level PizzaStore depending on concrete pizzas, you start from the Pizza abstraction so both high-level and low-level modules depend on it.

Name the three guidelines for following the Dependency Inversion Principle. :: No variable should hold a reference to a concrete class; no class should derive from a concrete class; no method should override an implemented method of a base class.

Why are the Dependency Inversion guidelines treated as guidelines, not rules? :: Every Java program violates them; you only need to apply them to classes likely to change — instantiating stable classes like String directly is fine.

What is the official definition of the [[abstract factory pattern]]? :: It provides an interface for creating families of related or dependent objects without specifying their concrete classes.

How does Abstract Factory let one CheesePizza class serve all regions? :: The pizza is composed with a PizzaIngredientFactory and pulls its ingredients from that factory in prepare(), so the factory supplies the regional differences.

How does Factory Method differ from Abstract Factory in mechanism? :: Factory Method creates objects through inheritance (override a factory method); Abstract Factory creates objects through composition (instantiate a factory and pass it in).

What is the main downside of the Abstract Factory Pattern? :: Adding a new product to the family changes the factory interface, forcing changes in every concrete factory that implements it.

What is the intent of Factory Method vs Abstract Factory? :: Factory Method: let a class defer instantiation to its subclasses. Abstract Factory: create families of related objects without depending on their concrete classes.

#flashcards
