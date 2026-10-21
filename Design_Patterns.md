---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 13
aliases: [Design Patterns, design patterns, design pattern, GoF patterns]
topics:
  - design patterns
  - singleton
  - factory
  - abstract factory
  - command
  - strategy
  - bridge
  - template method
---

# Design Patterns

> **Source**: SE2012 OOAD — Lecture 13 | Udara Samaratunge

In Software Engineering, a [[design pattern]] is a general repeatable solution to a commonly occurring problem in software design. It is not a finished design that can be transformed directly into code. Rather, it is a description or template for how to solve a problem that can be used in many different situations.

> [!NOTE] Patterns covered in this lecture (Gang of Four)
> - **Creational**: [[singleton pattern|Singleton]], [[factory method pattern|Factory]], [[abstract factory pattern|Abstract Factory]]
> - **Behavioral** (the lecture's grouping): [[command pattern|Command]], [[strategy pattern|Strategy]], [[bridge pattern|Bridge]], [[template method pattern|Template Method]]
>
> (Note: in the classic GoF taxonomy the **Bridge** pattern is actually *structural*; this lecture groups it under Behavioral.)

## Categories of Design Patterns

Design patterns are typically categorized into three main types based on their purpose:

1. **Creational Patterns:** Involve object initialization and provide a way to decouple client from the objects it needs to instantiate.
   - Examples: [[singleton pattern]], [[builder pattern]], [[prototype pattern]], [[abstract factory pattern]], [[factory method pattern]]
2. **Structural Patterns:** Lets you compose classes or objects into larger structures.
   - Examples: [[decorator pattern]], [[composite pattern]], [[flyweight pattern]], [[adapter pattern]], [[proxy pattern]], [[facade pattern]], [[bridge pattern]]
3. **Behavioral Patterns:** Concerned with how classes and objects interact or distribute responsibility.
   - Examples: [[template method pattern]], [[interpreter pattern]], [[chain of responsibility pattern]], [[strategy pattern]], [[visitor pattern]], [[command pattern]], [[iterator pattern]], [[memento pattern]], [[observer pattern]], [[state pattern]], [[mediator pattern]]

---

## Creational Patterns

### Singleton Pattern

The [[singleton pattern]] ensures that **only one object instance is ever created** for a class, and provides a global point of access to it. It needs a **private constructor** (to block multiple instances), a **private static instance**, and a public `getInstance()` method that uses **lazy loading**.

```java
public class Singleton {
    private static Singleton uniqueinstance;   // A static instance

    private Singleton() {}                      // private constructor blocks multiple instances

    public static Singleton getInstance() {
        if (uniqueinstance == null) {           // Lazy Loading
            uniqueinstance = new Singleton();
        }
        return uniqueinstance;
    }
}
```

> [!WARNING] This ensures only one object instance is created — but is good only for a **single-threaded** application.

**Thread-safe Singleton** — adding `synchronized` to `getInstance()` overcomes the multiple-threading issue:

```java
public class Singleton {
    private static Singleton uniqueinstance;

    private Singleton() {}

    public static synchronized Singleton getInstance() {   // overcomes the multi-threading issue
        if (uniqueinstance == null) {
            uniqueinstance = new Singleton();
        }
        return uniqueinstance;
    }
}
```

> However, the synchronization is **a bit expensive** — this approach is good if performance is not an issue. (See also the synchronized-block double-checked version in [[Threads]].)

### Factory Method Pattern

The [[factory method pattern]] encapsulates the object creation by letting subclasses to decide what objects to create. The lecture's steps are: **(1)** create an interface, **(2)** create concrete classes implementing the interface, **(3)** create a Factory to generate the concrete object based on given information, **(4)** use the Factory to get the object by passing information such as a type. The lecture's worked example is the **Shape Factory** below.

> [!OUTSIDE] The Simple-Factory-vs-Factory-Method discussion and the `PizzaStore` example below are from *Head First Design Patterns* — supplementary to the lecture, which uses the Shape Factory example.

#### Simple Factory vs Factory Method
- **Simple Factory:** Does not let you vary the product implementations being created.
- **Factory Method:** Creates a framework that lets the sub classes decide which product implementation will be used.

**The Creator Classes**
Factory objects are created through INHERITANCE. The creator class `PizzaStore` is abstract and contains the "Factory Method" `createPizza()`.

```java
public abstract class PizzaStore {
    abstract Pizza createPizza(String item); // This is the "Factory Method"
    
    public Pizza orderPizza(String type) {
        Pizza pizza = createPizza(type);
        System.out.println("--- Making a " + pizza.getName() + " ---");
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();
        return pizza;
    }
}
```

**Concrete Creators**
Subclasses inherit and implement the factory method.

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

#### Another Example: Shape Factory

```java
public interface Shape {
    void draw();
}

public class Rectangle implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Rectangle::draw() method.");
    }
}

public class Square implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Square::draw() method.");
    }
}

public class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Circle::draw() method.");
    }
}

public class ShapeFactory {
    //use getShape method to get object of type shape
    public Shape getShape(String shapeType){
        if(shapeType == null){
            return null;
        }
        if(shapeType.equalsIgnoreCase("CIRCLE")){
            return new Circle();
        } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
            return new Rectangle();
        } else if(shapeType.equalsIgnoreCase("SQUARE")){
            return new Square();
        }
        return null;
    }
}

public class FactoryPatternDemo {
    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();
        
        //get an object of Circle and call its draw method.
        Shape shape1 = shapeFactory.getShape("CIRCLE");
        //call draw method of Circle
        shape1.draw();
        
        //get an object of Rectangle and call its draw method.
        Shape shape2 = shapeFactory.getShape("RECTANGLE");
        //call draw method of Rectangle
        shape2.draw();
        
        //get an object of Square and call its draw method.
        Shape shape3 = shapeFactory.getShape("SQUARE");
        //call draw method of square
        shape3.draw();
    }
}
```

### Abstract Factory Pattern

The [[abstract factory pattern]] provides an interface for creating families of related or dependent objects without specifying their concrete classes.

- Defines an `AbstractFactory` interface.
- Has concrete factories (e.g. `ShapeFactory`, `ColorFactory`) that extend or implement it.
- Has a `FactoryProducer` that returns the abstract factory.

**Implementation Example:**

```java
package design.pattern.abstractFactory;

public interface Shape {
    void draw();
}

public interface Color {
    void fill();
}
```

```java
public abstract class AbstractFactory {
    abstract Color getColor(String color);
    abstract Shape getShape(String shape);
}
```

```java
public class ShapeFactory extends AbstractFactory {
    @Override
    public Shape getShape(String shapeType) {
        if(shapeType == null){
            return null;
        }
        if(shapeType.equalsIgnoreCase("CIRCLE")){
            return new Circle();
        } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
            return new Rectangle();
        } else if(shapeType.equalsIgnoreCase("SQUARE")){
            return new Square();
        }
        return null;
    }

    @Override
    public Color getColor(String color) {
        return null;
    }
}
```

```java
public class ColorFactory extends AbstractFactory {
    @Override
    public Color getColor(String color) {
        if(color == null){
            return null;
        }
        if(color.equalsIgnoreCase("RED")){
            return new Red();
        } else if(color.equalsIgnoreCase("GREEN")){
            return new Green();
        } else if(color.equalsIgnoreCase("BLUE")){
            return new Blue();
        }
        return null;
    }

    @Override
    public Shape getShape(String shapeType) {
        return null;
    }
}
```

```java
public class FactoryProducer {
    public static AbstractFactory getFactory(String choice) {
        if(choice.equalsIgnoreCase("SHAPE")){
            return new ShapeFactory();
        } else if(choice.equalsIgnoreCase("COLOR")){
            return new ColorFactory();
        }
        return null;
    }
}
```

```java
public class AbstractFactoryPatternDemo {
    private static final String SHAPE = "SHAPE";
    private static final String CIRCLE = "CIRCLE";
    private static final String RECTANGLE = "RECTANGLE";
    private static final String SQUARE = "SQUARE";
    
    private static final String COLOR = "COLOR";
    private static final String RED = "RED";
    private static final String GREEN = "GREEN";
    private static final String BLUE = "BLUE";

    public static void main(String[] args) {
        AbstractFactory shapeFactory = FactoryProducer.getFactory(SHAPE);
        Shape shape = shapeFactory.getShape(CIRCLE);
        shape.draw();
        
        FactoryProducer.getFactory(SHAPE).getShape(RECTANGLE).draw();
        FactoryProducer.getFactory(SHAPE).getShape(SQUARE).draw();
        
        FactoryProducer.getFactory(COLOR).getColor(RED).fill();
        FactoryProducer.getFactory(COLOR).getColor(GREEN).fill();
        FactoryProducer.getFactory(COLOR).getColor(BLUE).fill();
    }
}
```

---

## Behavioral Patterns

### Command Pattern

The [[command pattern]] declares an interface for all commands, providing a simple `execute()` method which asks the **Receiver** of the command to carry out an operation.

**Real World Example:**
- **Customer:** Submits an order.
- **Order:** A command from the customer. This order is queued for the kitchen staff.
- **Waiter (Invoker):** Takes the order and tells the chef a new order has come in. The Invoker holds a command and gets the Command to execute a request by calling the execute method.
- **Chef (Receiver):** Has the knowledge of what to do to carry out the request (cook the meal).

The Client creates **ConcreteCommands** and sets a Receiver for the command.
The ConcreteCommand defines a binding between the action and the receiver.
When the Invoker calls execute, the ConcreteCommand will run one or more actions on the Receiver.

**Implementation Example: Remote Controller**

```java
package design.pattern.command;

public interface Command {
    public void execute();
}
```

```java
public class Light {
    private String location;
    
    public Light(String location) {
        this.location = location;
    }
    
    public void on() {
        System.out.println(location + " light is on.");
    }
    
    public void off() {
        System.out.println(location + " light is off.");
    }
}
```

```java
public class LightOnCommand implements Command {
    Light light;
    
    public LightOnCommand(Light light) {
        this.light = light;
    }
    
    public void execute() {
        light.on();
    }
}

public class LightOffCommand implements Command {
    Light light;
    
    public LightOffCommand(Light light) {
        this.light = light;
    }
    
    public void execute() {
        light.off();
    }
}
```

```java
public class RemoteController {
    Command[] onCommands;
    Command[] offCommands;
    
    public RemoteController() {
        onCommands = new Command[7];
        offCommands = new Command[7];
        
        Command noCommand = new NoCommand();
        for (int i = 0; i < 7; i++) {
            onCommands[i] = noCommand;
            offCommands[i] = noCommand;
        }
    }
    
    public void setCommand(int slot, Command onCommand, Command offCommand) {
        onCommands[slot] = onCommand;
        offCommands[slot] = offCommand;
    }
    
    public void onButtonWasPushed(int slot) {
        onCommands[slot].execute();
    }
    
    public void offButtonWasPushed(int slot) {
        offCommands[slot].execute();
    }
}
```

```java
public class Client {
    public static void main(String[] args) {
        RemoteController remoteController = new RemoteController();
        
        Light livingRoomLight = new Light("Living Room Light");
        Light kitchenLight = new Light("Kitchen Light");
        
        LightOnCommand onLivingRoomLight = new LightOnCommand(livingRoomLight);
        LightOffCommand offLivingRoomLight = new LightOffCommand(livingRoomLight);
        LightOnCommand onKitchenLight = new LightOnCommand(kitchenLight);
        LightOffCommand offKitchenLight = new LightOffCommand(kitchenLight);
        
        remoteController.setCommand(0, onLivingRoomLight, offLivingRoomLight);
        remoteController.setCommand(1, onKitchenLight, offKitchenLight);
        
        remoteController.onButtonWasPushed(0);
        remoteController.offButtonWasPushed(0);
        remoteController.onButtonWasPushed(1);
        remoteController.offButtonWasPushed(1);
    }
}
```

### Strategy Pattern

The [[strategy pattern]] is about setting behavior dynamically. 

**Real World Example:**
- A software developer might be asked to write a piece of code for a UI.
- One developer uses Java with Swing. Another uses C#.
- The details of how to write the UI are left to the developers, and both apply their own **strategy**.
- At any stage, the developer could change their strategy, choosing to use a different language if they feel it's necessary.
- It's all about dynamically changing behaviors.

**Implementation Example: Duck fly behaviours.** A family of `IFlyBehaviour` strategies is defined, and a `Duck` can swap its behaviour at runtime via `setFlyBehaviour()`.

```java
public interface IFlyBehaviour {
    public void fly();
}

public class FlyWithWings implements IFlyBehaviour {
    @Override
    public void fly() {
        System.out.println("I am flying with wings");
    }
}

public class FlyNoWay implements IFlyBehaviour {
    @Override
    public void fly() {
        System.out.println("I can't fly");
    }
}

public class FlyRocketPower implements IFlyBehaviour {
    @Override
    public void fly() {
        System.out.println("I am flying with a rocket");
    }
}
```

Using the strategy (note `setFlyBehaviour` changing the behaviour **dynamically**):

```java
public class TestDuck {
    public static void main(String[] args) {
        System.out.println("Start Mollard Duck");
        System.out.println("==================");
        Duck mollard = new MollardDuck();
        mollard.performFly();          // I am flying with wings
        mollard.performQuack();        // Quack..Quack...

        System.out.println("Start Model Duck");
        System.out.println("==================");
        Duck model = new ModelDuck();
        model.performFly();                          // I can't fly
        model.setFlyBehaviour(new FlyRocketPower());  // change strategy at runtime
        model.performFly();                          // I am flying with a rocket
        model.performQuack();
        model.setQuackBehaviour(new ModelQuack());
        model.performQuack();                        // Quack Model duck
    }
}
```

### Bridge Pattern

The [[bridge pattern]] allows you to **vary both the implementation and the abstraction** by placing both in **separate class hierarchies**. (The lecture groups this under Behavioral; in GoF it is a structural pattern.)

**Implementation Example: TV.** The `TV` implementation hierarchy varies independently from the abstraction (e.g. a remote control) that uses it.

```java
public interface TV {
    void on();
    void off();
    void tune(int chanel);
}

public class LGTV implements TV {
    @Override
    public void on() {
        System.out.println("Switch on LG TV");
    }
    @Override
    public void off() {
        System.out.println("Switch off LG TV");
    }
    @Override
    public void tune(int chanel) {
        System.out.println("Switch on chanel in LG TV is: " + chanel);
    }
}

public class SonyTV implements TV {
    @Override
    public void on() {
        System.out.println("Switch on Sony TV");
    }
    @Override
    public void off() {
        System.out.println("Switch off Sony TV");
    }
    @Override
    public void tune(int chanel) {
        System.out.println("Switch on chanel in Sony TV is: " + chanel);
    }
}
```

### Template Method Pattern

The [[template method pattern]] defines the **steps of an algorithm** and allows subclasses to provide the implementation for one or more steps. The skeleton (the *template method*) is fixed; specific steps are deferred to subclasses without changing the algorithm's structure.

**Implementation Example: Beverage.** `prepareRecepie()` is the template method (fixed steps); `brew()` and `addCondiments()` are abstract steps implemented by `Tea` and `Coffie`.

```java
public abstract class Beverage {
    // The template method — fixed algorithm skeleton (final so subclasses can't change the steps' order)
    final void prepareRecepie() {
        boilWater();
        brew();
        addCondiments();
        pourInCup();
    }

    abstract void brew();           // step deferred to subclasses
    abstract void addCondiments();  // step deferred to subclasses

    void boilWater() {
        System.out.println("Boiling water.");
    }

    void pourInCup() {
        System.out.println("Pour into cup.");
    }
}

public class Tea extends Beverage {
    @Override
    void brew() {
        System.out.println("Steeping the Tea.");
    }
    @Override
    void addCondiments() {
        System.out.println("Adding Lemon.");
    }
}

public class Coffie extends Beverage {
    @Override
    void addCondiments() {
        System.out.println("Add suger and milk.");
    }
    @Override
    void brew() {
        System.out.println("Stripping coffie through filter.");
    }
}
```

---

## 🧠 Flashcards

What is a [[design pattern]]? :: A general repeatable solution to a commonly occurring problem in software design — a description or template for how to solve a problem that can be reused in many situations.

What are the three main categories of design patterns? :: Creational, Structural, and Behavioral patterns.

What is the purpose of Creational patterns? :: They involve object initialization and decouple the client from the objects it needs to instantiate.

What is the purpose of Structural patterns? :: They let you compose classes or objects into larger structures.

What is the purpose of Behavioral patterns? :: They are concerned with how classes and objects interact or distribute responsibility.

What does the [[singleton pattern]] ensure? :: That only one object instance of a class is ever created, with a global access point via getInstance().

What three things does a Singleton need? :: A private constructor (to block extra instances), a private static instance, and a public static getInstance() method (with lazy loading).

Why must a thread-safe Singleton use `synchronized`, and what is the trade-off? :: Without synchronization two threads could each create an instance; adding synchronized to getInstance() prevents this, but synchronization is a bit expensive.

How does the [[factory method pattern]] encapsulate object creation? :: It defines an interface for creating objects but lets subclasses decide which concrete class to instantiate, via a factory method.

What is the difference between a Simple Factory and a Factory Method? :: A Simple Factory does not let you vary the product implementations; a Factory Method creates a framework that lets subclasses decide which product implementation is used.

What does the [[abstract factory pattern]] do? :: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

What are the four roles in the [[command pattern]]? :: Command (with execute()), Receiver (knows how to perform the action), Invoker (holds and triggers the command), and Client (creates ConcreteCommands and sets the Receiver).

How does the Command Pattern map to a restaurant order? :: The Order is the Command, the Chef is the Receiver, the Waiter is the Invoker, and the Customer/Client places the order.

What is the purpose of the [[strategy pattern]]? :: To define a family of interchangeable algorithms (strategies) and change an object's behaviour dynamically at runtime (e.g. Duck.setFlyBehaviour()).

What does the [[bridge pattern]] do? :: It lets you vary both the abstraction and the implementation independently by placing each in its own class hierarchy.

What does the [[template method pattern]] do? :: It defines the fixed skeleton (steps) of an algorithm in a template method and defers specific steps to subclasses (e.g. Beverage.prepareRecepie() with abstract brew() and addCondiments()).

#flashcards
