---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 12
topics:
  - command pattern
  - behavioral patterns
  - encapsulating invocation
  - undo
  - macro command
  - null object
  - queuing and logging requests
aliases:
  - command pattern
  - Command Pattern
  - Command
  - encapsulating invocation
---

# Command Pattern

> **Source**: SE2012 OOAD — *Head First Design Patterns*, Chapter 6: *Encapsulating Invocation* (used as the lecture deck).

In this chapter we take **[[encapsulation]] to a whole new level: we encapsulate method invocation**. By encapsulating method invocation, we can crystallize pieces of computation so that the object **invoking** the computation doesn't need to know **how** to do things — it just uses our crystallized method to get it done. We can also do wickedly smart things with these encapsulated invocations, like **save them away for logging** or **reuse them to implement undo**.

> [!NOTE] Official definition
> **The Command Pattern encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations.**

A command object encapsulates a request by **binding together a set of actions on a specific receiver**. It packages the actions and the receiver into an object exposing just **one method, `execute()`**. When called, `execute()` causes the actions to be invoked on the receiver. From the outside, **no other object knows what actions get performed on what receiver** — they just know that calling `execute()` services their request.

---

## The Problem: Home Automation or Bust, Inc.

> [!QUESTION] Designing a remote control API
> A home-automation company sends a set of **vendor classes** to control from a remote. Instead of the uniform `on()`/`off()` you'd expect, the classes have **diverse** methods: `dim()`, `setTemperature()`, `setVolume()`, `setInputChannel()`, `waterOn()`... and **more vendor classes are expected in the future**. How do you design a remote whose seven slots can control *any* of these devices?

The team's reasoning (Cubicle Conversation):
- **Mary:** This is about a **separation of concerns** — the remote should know how to interpret **button presses** and make requests, but it **shouldn't know** how to turn on a hot tub.
- **The bad design to avoid:** a remote made of `if` statements like `if (slot1 == Light) light.on(); else if (slot1 == Hottub) hottub.jetsOn();`. Every new vendor class would force us to **reopen and modify** the code — bugs and busywork.
- **Joe:** The **Command Pattern** lets you **decouple the requester of an action from the object that performs it**. The *requester* is the remote control; the *performer* is a vendor object. You introduce **command objects**: each encapsulates a request to do something (turn on a light) on a specific object (the living-room light). Store one command per button; when the button is pressed, ask the command object to do the work. **The remote has no idea what the work is** — it just holds a command object that knows how to talk to the right object.

---

## The Diner Analogy — meeting the players

> [!QUESTION] The Objectville Diner
> The Command Pattern is easier to grasp through the diner. Study the interactions between the **Customer**, the **Waitress**, the **Order Slip**, and the **Short-Order Cook**.
>
> - **An Order Slip encapsulates a request to prepare a meal.** It can be passed around (Waitress → order counter → next Waitress). Its interface has **one method, `orderUp()`**, that encapsulates the actions needed to prepare the meal, plus a **reference to the object that prepares it** (the Cook). The Waitress doesn't need to know what's on the order or who cooks it — she just passes the slip and calls *"Order up!"*
> - **The Waitress's job** is to take Order Slips and invoke `orderUp()` on them. Her `takeOrder()` gets **parameterized** with different Order Slips all day; she just knows every slip supports `orderUp()`.
> - **The Short-Order Cook** has the knowledge to actually prepare the meal. Once `orderUp()` is invoked, the Cook implements all the methods needed to create meals.
> - **The Waitress and Cook are totally decoupled** — they communicate only through the Order Slip.

### Who does what? (Diner → Command Pattern mapping)

| Diner role / method | Command Pattern role / method |
| --- | --- |
| Customer | **Client** |
| Waitress | **Invoker** |
| `takeOrder()` | `setCommand()` |
| Order (Order Slip) | **Command** |
| `orderUp()` | `execute()` |
| Short-Order Cook | **Receiver** |

### Loading the Invoker (the sequence)

1. The **client** creates a **command object**.
2. The client calls **`setCommand()`** to store the command object in the **invoker**.
3. Later, the client asks the **invoker to execute** the command. Once loaded, the command may be **used and discarded**, or it may **remain and be used many times**.

---

## Building the First Command Object (the Simple Remote)

All command objects implement the **same interface**, which consists of one method. In the diner we called it `orderUp()`; we typically just call it **`execute()`**.

```java
public interface Command {
    public void execute();
}
```

The vendor `Light` class has `on()` and `off()` methods. Here is a command that turns a light on — it stores a reference to the **receiver** (the `Light`) and calls the right action in `execute()`:

```java
public class Light {
    public Light() {}

    public void on() {
        System.out.println("Light is on");
    }

    public void off() {
        System.out.println("Light is off");
    }
}
```

```java
public class LightOnCommand implements Command {
    Light light;                                  // the receiver

    public LightOnCommand(Light light) {          // receiver passed in via constructor
        this.light = light;
    }

    public void execute() {                       // execute() invokes the action on the receiver
        light.on();
    }
}
```

A remote with **one button** and a single slot to hold a device to control:

```java
public class SimpleRemoteControl {
    Command slot;                                 // holds one command

    public SimpleRemoteControl() {}

    public void setCommand(Command command) {     // set the command this slot will run
        slot = command;
    }

    public void buttonWasPressed() {              // press the button → execute the command
        slot.execute();
    }
}
```

A simple test that loads two different commands into the same slot:

```java
public class RemoteControlTest {
    public static void main(String[] args) {
        SimpleRemoteControl remote = new SimpleRemoteControl();   // the Invoker
        Light light = new Light();                                // a Receiver
        GarageDoor garageDoor = new GarageDoor();                 // another Receiver
        LightOnCommand lightOn = new LightOnCommand(light);       // a Command
        GarageDoorOpenCommand garageOpen =
                new GarageDoorOpenCommand(garageDoor);            // another Command

        remote.setCommand(lightOn);                               // load + run the light command
        remote.buttonWasPressed();
        remote.setCommand(garageOpen);                            // load + run the garage command
        remote.buttonWasPressed();
    }
}
```

> [!NOTE] Sharpen Your Pencil — the GarageDoorOpenCommand (solution)
> The `GarageDoor` class has an `up()` method that prints `"Garage Door is Open"`. The command binds the garage door receiver to its `up()` action:
>
> ```java
> public class GarageDoorOpenCommand implements Command {
>     GarageDoor garageDoor;
>
>     public GarageDoorOpenCommand(GarageDoor garageDoor) {
>         this.garageDoor = garageDoor;
>     }
>
>     public void execute() {
>         garageDoor.up();
>     }
> }
> ```
>
> Output of the test (light on, then garage door opened):
> ```
> Light is on
> Garage Door is Open
> ```

---

## The Command Pattern's Four Roles

| Role | Responsibility |
| --- | --- |
| **Client** | Creates a ConcreteCommand and sets its Receiver. |
| **Command** | Declares the interface with the single `execute()` method (and optionally `undo()`). |
| **ConcreteCommand** | Defines a binding between an **action** and a **Receiver**; `execute()` calls the receiver's method(s). |
| **Invoker** | Holds a command and asks it to carry out a request by calling `execute()`. |
| **Receiver** | Knows how to perform the work to satisfy the request. |

> [!NOTE] Brain Power — how does Command support decoupling?
> The Command object sits **between** the invoker and the receiver. The invoker only knows the `Command` interface (`execute()`); it never references the receiver directly. The receiver only knows how to do its job. The ConcreteCommand wires them together at creation time, so neither the invoker nor the receiver needs to know about the other.

---

## Building the Full Remote (seven slots, on & off)

The full remote control is our **invoker**: it has **seven slots**, each with an **on** and **off** button. When a button is pressed, `execute()` is called on the corresponding command, invoking actions on the receiver (lights, ceiling fans, stereos).

```java
public class Light {
    String location = "";

    public Light(String location) {
        this.location = location;
    }

    public void on() {
        System.out.println(location + " light is on");
    }

    public void off() {
        System.out.println(location + " light is off");
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

A more challenging receiver — the **Stereo** — and a command that turns it on with a CD at volume 11 (the on command does **three** actions in `execute()`):

```java
public class Stereo {
    String location;

    public Stereo(String location) {
        this.location = location;
    }

    public void on() {
        System.out.println(location + " stereo is on");
    }

    public void off() {
        System.out.println(location + " stereo is off");
    }

    public void setCD() {
        System.out.println(location + " stereo is set for CD input");
    }

    public void setDVD() {
        System.out.println(location + " stereo is set for DVD input");
    }

    public void setRadio() {
        System.out.println(location + " stereo is set for Radio");
    }

    public void setVolume(int volume) {
        // code to set the volume; valid range is 1-11
        System.out.println(location + " stereo volume set to " + volume);
    }
}
```

```java
public class StereoOnWithCDCommand implements Command {
    Stereo stereo;

    public StereoOnWithCDCommand(Stereo stereo) {
        this.stereo = stereo;
    }

    public void execute() {
        stereo.on();
        stereo.setCD();
        stereo.setVolume(11);
    }
}

public class StereoOffCommand implements Command {
    Stereo stereo;

    public StereoOffCommand(Stereo stereo) {
        this.stereo = stereo;
    }

    public void execute() {
        stereo.off();
    }
}
```

### The NoCommand "null object"

> [!IMPORTANT] Pattern Honorable Mention — the Null Object
> Without a default command, `onButtonWasPushed()` would need a null check **every** time it referenced a slot:
> ```java
> public void onButtonWasPushed(int slot) {
>     if (onCommands[slot] != null) {
>         onCommands[slot].execute();
>     }
> }
> ```
> Instead, we implement a command that **does nothing** and assign it to every slot by default. A **null object** is useful when you don't have a meaningful object to return, yet you want to **remove the responsibility for handling `null` from the client**. You'll see Null Objects used with many design patterns — sometimes "Null Object" is itself listed as a pattern.

```java
public class NoCommand implements Command {
    public void execute() { }
}
```

The full remote control with seven slots, each pre-loaded with a `NoCommand`:

```java
public class RemoteControl {
    Command[] onCommands;
    Command[] offCommands;

    public RemoteControl() {
        onCommands = new Command[7];
        offCommands = new Command[7];

        Command noCommand = new NoCommand();          // default for every slot
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
        onCommands[slot].execute();                   // no null check needed thanks to NoCommand
    }

    public void offButtonWasPushed(int slot) {
        offCommands[slot].execute();
    }

    public String toString() {
        StringBuffer stringBuff = new StringBuffer();
        stringBuff.append("\n------ Remote Control -------\n");
        for (int i = 0; i < onCommands.length; i++) {
            stringBuff.append("[slot " + i + "] " + onCommands[i].getClass().getName()
                + "    " + offCommands[i].getClass().getName() + "\n");
        }
        return stringBuff.toString();
    }
}
```

The client (`RemoteLoader`) creates every receiver and command, loads the slots, then pushes buttons:

```java
public class RemoteLoader {
    public static void main(String[] args) {
        RemoteControl remoteControl = new RemoteControl();

        Light livingRoomLight = new Light("Living Room");
        Light kitchenLight = new Light("Kitchen");
        CeilingFan ceilingFan = new CeilingFan("Living Room");
        GarageDoor garageDoor = new GarageDoor("");
        Stereo stereo = new Stereo("Living Room");

        LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);
        LightOnCommand kitchenLightOn = new LightOnCommand(kitchenLight);
        LightOffCommand kitchenLightOff = new LightOffCommand(kitchenLight);

        CeilingFanOnCommand ceilingFanOn = new CeilingFanOnCommand(ceilingFan);
        CeilingFanOffCommand ceilingFanOff = new CeilingFanOffCommand(ceilingFan);

        GarageDoorUpCommand garageDoorUp = new GarageDoorUpCommand(garageDoor);
        GarageDoorDownCommand garageDoorDown = new GarageDoorDownCommand(garageDoor);

        StereoOnWithCDCommand stereoOnWithCD = new StereoOnWithCDCommand(stereo);
        StereoOffCommand stereoOff = new StereoOffCommand(stereo);

        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff);
        remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff);
        remoteControl.setCommand(2, ceilingFanOn, ceilingFanOff);
        remoteControl.setCommand(3, stereoOnWithCD, stereoOff);

        System.out.println(remoteControl);

        remoteControl.onButtonWasPushed(0);
        remoteControl.offButtonWasPushed(0);
        remoteControl.onButtonWasPushed(1);
        remoteControl.offButtonWasPushed(1);
        remoteControl.onButtonWasPushed(2);
        remoteControl.offButtonWasPushed(2);
        remoteControl.onButtonWasPushed(3);
        remoteControl.offButtonWasPushed(3);
    }
}
```

> [!NOTE] How does the remote tell the living-room light from the kitchen light?
> **It doesn't!** The remote only knows how to call `execute()` on the corresponding command. When we **create** the commands, we bind one `LightOnCommand` to the living-room light object and another to the kitchen light object. The **receiver is bound into the command it's encapsulated in**, so by the time the button is pressed, the right thing just happens.

---

## Adding Undo

When commands support undo, they get an **`undo()`** method that **mirrors `execute()`** — whatever `execute()` last did, `undo()` reverses. First, add `undo()` to the interface:

```java
public interface Command {
    public void execute();
    public void undo();
}
```

For the `LightOnCommand`, `execute()` last called `on()`, so `undo()` must call `off()` (and vice-versa for `LightOffCommand`):

```java
public class LightOnCommand implements Command {
    Light light;

    public LightOnCommand(Light light) {
        this.light = light;
    }

    public void execute() {
        light.on();
    }

    public void undo() {
        light.off();
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

    public void undo() {
        light.on();
    }
}
```

The remote tracks the **last command invoked** and reverses it when the undo button is pressed:

```java
public class RemoteControlWithUndo {
    Command[] onCommands;
    Command[] offCommands;
    Command undoCommand;                              // tracks the last command

    public RemoteControlWithUndo() {
        onCommands = new Command[7];
        offCommands = new Command[7];

        Command noCommand = new NoCommand();
        for (int i = 0; i < 7; i++) {
            onCommands[i] = noCommand;
            offCommands[i] = noCommand;
        }
        undoCommand = noCommand;                      // undo also defaults to NoCommand
    }

    public void setCommand(int slot, Command onCommand, Command offCommand) {
        onCommands[slot] = onCommand;
        offCommands[slot] = offCommand;
    }

    public void onButtonWasPushed(int slot) {
        onCommands[slot].execute();
        undoCommand = onCommands[slot];               // remember it for undo
    }

    public void offButtonWasPushed(int slot) {
        offCommands[slot].execute();
        undoCommand = offCommands[slot];
    }

    public void undoButtonWasPushed() {
        undoCommand.undo();                           // reverse the last action
    }

    public String toString() {
        StringBuffer stringBuff = new StringBuffer();
        stringBuff.append("\n------ Remote Control -------\n");
        for (int i = 0; i < onCommands.length; i++) {
            stringBuff.append("[slot " + i + "] " + onCommands[i].getClass().getName()
                + "    " + offCommands[i].getClass().getName() + "\n");
        }
        stringBuff.append("[undo] " + undoCommand.getClass().getName() + "\n");
        return stringBuff.toString();
    }
}
```

### Using state to implement Undo — the Ceiling Fan

> [!IMPORTANT] Undo usually needs state
> The light undo was easy. Usually we must **manage some state** to implement undo. The `CeilingFan` supports several **speeds** plus off, so its commands must **remember the previous speed** and restore it on `undo()`.

```java
public class CeilingFan {
    public static final int HIGH = 3;
    public static final int MEDIUM = 2;
    public static final int LOW = 1;
    public static final int OFF = 0;
    String location;
    int speed;

    public CeilingFan(String location) {
        this.location = location;
        speed = OFF;
    }

    public void high() {
        speed = HIGH;
        System.out.println(location + " ceiling fan is on high");
    }

    public void medium() {
        speed = MEDIUM;
        System.out.println(location + " ceiling fan is on medium");
    }

    public void low() {
        speed = LOW;
        System.out.println(location + " ceiling fan is on low");
    }

    public void off() {
        speed = OFF;
        System.out.println(location + " ceiling fan is off");
    }

    public int getSpeed() {
        return speed;
    }
}
```

```java
public class CeilingFanHighCommand implements Command {
    CeilingFan ceilingFan;
    int prevSpeed;                                    // saved state for undo

    public CeilingFanHighCommand(CeilingFan ceilingFan) {
        this.ceilingFan = ceilingFan;
    }

    public void execute() {
        prevSpeed = ceilingFan.getSpeed();            // remember current speed before changing
        ceilingFan.high();
    }

    public void undo() {
        if (prevSpeed == CeilingFan.HIGH) {
            ceilingFan.high();
        } else if (prevSpeed == CeilingFan.MEDIUM) {
            ceilingFan.medium();
        } else if (prevSpeed == CeilingFan.LOW) {
            ceilingFan.low();
        } else if (prevSpeed == CeilingFan.OFF) {
            ceilingFan.off();
        }
    }
}
```

The `CeilingFanMediumCommand`, `CeilingFanLowCommand`, and `CeilingFanOffCommand` follow the **same pattern** — save `prevSpeed` in `execute()`, restore it in `undo()`:

```java
public class CeilingFanMediumCommand implements Command {
    CeilingFan ceilingFan;
    int prevSpeed;

    public CeilingFanMediumCommand(CeilingFan ceilingFan) {
        this.ceilingFan = ceilingFan;
    }

    public void execute() {
        prevSpeed = ceilingFan.getSpeed();
        ceilingFan.medium();
    }

    public void undo() {
        if (prevSpeed == CeilingFan.HIGH) {
            ceilingFan.high();
        } else if (prevSpeed == CeilingFan.MEDIUM) {
            ceilingFan.medium();
        } else if (prevSpeed == CeilingFan.LOW) {
            ceilingFan.low();
        } else if (prevSpeed == CeilingFan.OFF) {
            ceilingFan.off();
        }
    }
}
```

---

## The Meta Command Pattern: Macro Commands (Party Mode)

> [!QUESTION] Every remote needs a Party Mode!
> What's the point of a remote if you can't push **one button** and have the lights dimmed, the stereo and TV turned on, and the hot tub fired up? A **MacroCommand** holds an array of commands and runs them all from one `execute()`.

```java
public class MacroCommand implements Command {
    Command[] commands;

    public MacroCommand(Command[] commands) {
        this.commands = commands;
    }

    public void execute() {
        for (int i = 0; i < commands.length; i++) {
            commands[i].execute();
        }
    }

    public void undo() {                              // undo in REVERSE order
        for (int i = commands.length - 1; i >= 0; i--) {
            commands[i].undo();
        }
    }
}
```

Using the macro command — create the on/off command sets, build two arrays, wrap them in MacroCommands, and assign to a slot:

```java
public class RemoteLoader {
    public static void main(String[] args) {
        RemoteControlWithUndo remoteControl = new RemoteControlWithUndo();

        Light light = new Light("Living Room");
        TV tv = new TV("Living Room");
        Stereo stereo = new Stereo("Living Room");
        Hottub hottub = new Hottub();

        LightOnCommand lightOn = new LightOnCommand(light);
        StereoOnCommand stereoOn = new StereoOnCommand(stereo);
        TVOnCommand tvOn = new TVOnCommand(tv);
        HottubOnCommand hottubOn = new HottubOnCommand(hottub);

        LightOffCommand lightOff = new LightOffCommand(light);
        StereoOffCommand stereoOff = new StereoOffCommand(stereo);
        TVOffCommand tvOff = new TVOffCommand(tv);
        HottubOffCommand hottubOff = new HottubOffCommand(hottub);

        Command[] partyOn = { lightOn, stereoOn, tvOn, hottubOn };
        Command[] partyOff = { lightOff, stereoOff, tvOff, hottubOff };

        MacroCommand partyOnMacro = new MacroCommand(partyOn);
        MacroCommand partyOffMacro = new MacroCommand(partyOff);

        remoteControl.setCommand(0, partyOnMacro, partyOffMacro);

        System.out.println(remoteControl);
        System.out.println("--- Pushing Macro On ---");
        remoteControl.onButtonWasPushed(0);
        System.out.println("--- Pushing Macro Off ---");
        remoteControl.offButtonWasPushed(0);
    }
}
```

> [!QUESTION] Why MacroCommand instead of a hardcoded PartyCommand?
> You *could* make a `PartyCommand` whose `execute()` calls the other commands — but that **hardcodes** party mode. With `MacroCommand` you decide **dynamically** which commands go into the macro, giving more flexibility, a more elegant solution, and **less new code**.

---

## Using Lambda Expressions (Serious Coding)

> [!TIP] Lambdas as commands
> You can use Java's **lambda expressions** to skip creating all those concrete command classes. Instead of instantiating a ConcreteCommand, use a **function object** in its place — and then **delete** all the concrete command classes. Doing this for every command can reduce the remote-control app from **22 classes to 9**.
>
> ```java
> Light livingRoomLight = new Light("Living Room");
>
> // Instead of: remoteControl.setCommand(0,
> //                 new LightOnCommand(livingRoomLight),
> //                 new LightOffCommand(livingRoomLight));
> remoteControl.setCommand(0,
>     () -> livingRoomLight.on(),
>     () -> livingRoomLight.off());
> ```
>
> **Restriction:** this only works if your `Command` interface has **one abstract method** (it's a *functional interface*). As soon as you add a **second** abstract method, the lambda shorthand no longer works.

---

## More Uses of the Command Pattern

> [!NOTE] Queuing requests
> Commands let us package a piece of computation (a receiver + actions) and pass it around as a **first-class object**. The computation may be invoked **long after** the command is created — even by a **different [[Threads|thread]]**. This applies to **schedulers, thread pools, and job queues**.
>
> **Job queue:** add commands on one end; a group of threads on the other end repeatedly **remove a command, call `execute()`, wait for it to finish, discard it, and retrieve the next**. The queue is **totally decoupled** from the computation — one minute a thread runs a financial computation, the next it retrieves something from the network. The queue doesn't care; as long as the objects implement the Command interface, `execute()` will run when a thread is free.

> [!NOTE] Logging requests
> Some applications must **log all actions** and be able to **recover after a crash** by reinvoking them. The Command Pattern supports this by adding two methods: **`store()`** and **`load()`** (in Java, via object serialization). As we execute commands, we **store a history** of them on disk; after a crash, we **reload** the command objects and invoke their `execute()` methods **in batch and in order**.
>
> This is useful for applications that invoke actions on **large data structures** that can't be quickly saved on every change — e.g., a **spreadsheet** application logs the actions rather than rewriting the whole spreadsheet each time. In advanced applications these techniques extend to **transactional** sets of operations, so that **all** operations complete or **none** do.

> [!NOTE] Command Pattern in the real world — Swing ActionListener
> Java's Swing `ActionListener` is **both** an Observer interface **and** a Command interface — two patterns in one example. In the "should I do it?" button example, `AngelListener` and `DevilListener` are concrete commands whose `actionPerformed()` plays the role of `execute()`:
>
> ```java
> public class SwingObserverExample {
>     JFrame frame;
>
>     public static void main(String[] args) {
>         SwingObserverExample example = new SwingObserverExample();
>         example.go();
>     }
>
>     public void go() {
>         frame = new JFrame();
>         JButton button = new JButton("Should I do it?");
>         button.addActionListener(new AngelListener());
>         button.addActionListener(new DevilListener());
>         // set frame properties here
>     }
>
>     class AngelListener implements ActionListener {
>         public void actionPerformed(ActionEvent event) {
>             System.out.println("Don't do it, you might regret it!");
>         }
>     }
>
>     class DevilListener implements ActionListener {
>         public void actionPerformed(ActionEvent event) {
>             System.out.println("Come on, do it!");
>         }
>     }
> }
> ```

> [!QUESTION] Do I always need a receiver?
> In general we strive for **"dumb"** command objects that just invoke an action on a receiver. But there are many **"smart"** command objects that implement most or all of the logic themselves. You can do this — just know you'll **lose the decoupling** between invoker and receiver, and you won't be able to **parameterize commands with receivers**.

> [!QUESTION] How do I implement a *history* of undo (multiple undos)?
> Instead of keeping a reference to just the last command, keep a **stack** of previous commands. On each undo, the invoker **pops** the top command off the stack and calls its `undo()`.

---

## Key Points (Bullet Points)

- The Command Pattern **decouples** an object making a request from the one that knows how to perform it.
- A **Command object** is at the center of this decoupling and **encapsulates a receiver with an action** (or set of actions).
- An **invoker** makes a request of a Command object by calling its **`execute()`** method, which invokes those actions on the **receiver**.
- Invokers can be **parameterized** with Commands, even **dynamically at runtime**.
- Commands may support **undo** by implementing an `undo()` method that restores the object to its state before `execute()` was last called.
- **MacroCommands** are a simple extension allowing **multiple commands** to be invoked; they can also support `undo()`.
- In practice it's not uncommon for **"smart" Command objects** to implement the request themselves rather than delegating to a receiver.
- Commands may also be used to implement **logging** and **transactional** systems.

> Command is a **behavioral** [[design pattern]]. It builds directly on [[encapsulation]] and [[polymorphism]] (the invoker depends only on the `Command` [[interface]]), uses a **[[null object pattern]]** for empty slots, and its queuing/logging uses feed straight into [[Threads]]. Compare its intent with the creational **[[factory method pattern]]** (see **[[Factory Pattern]]**) and the **[[singleton pattern]]** (see **[[Singleton Pattern]]**). The overview lives in **[[Design Patterns]]**.

---

## 🧠 Flashcards

What does the [[command pattern]] encapsulate? :: A request as an object — binding a set of actions on a specific receiver behind a single execute() method — letting you parameterize objects with requests, queue/log them, and support undo.

What is the single method on the Command interface? :: execute() (originally called orderUp() in the diner analogy).

What are the four/five roles in the Command Pattern? :: Client (creates the command and sets its receiver), Command (the execute() interface), ConcreteCommand (binds an action to a receiver), Invoker (holds the command and calls execute()), and Receiver (knows how to do the work).

How does the diner analogy map to the Command Pattern? :: Customer = Client, Waitress = Invoker, takeOrder() = setCommand(), Order Slip = Command, orderUp() = execute(), Short-Order Cook = Receiver.

What are the three steps of "loading the invoker"? :: (1) The client creates a command object, (2) calls setCommand() to store it in the invoker, (3) later asks the invoker to execute the command.

How does a ConcreteCommand know which receiver to act on? :: The receiver is passed into the command's constructor and stored, so the receiver is bound into the command it is encapsulated in.

What is the NoCommand object and why is it used? :: A null object — a command whose execute() does nothing — assigned to every slot by default so the invoker never has to null-check before calling execute().

What is a null object? :: An object that does nothing meaningful, used when you have no meaningful object to return but want to remove the burden of handling null from the client.

How is undo implemented in a command? :: Add an undo() method that mirrors execute() and reverses its last action (e.g. LightOnCommand.execute() calls on(), so undo() calls off()).

Why does the CeilingFan command need a prevSpeed field? :: Undo requires state — execute() saves the fan's current speed into prevSpeed before changing it, and undo() restores that previous speed.

What is a MacroCommand? :: A command holding an array of commands; its execute() runs them all in order, and its undo() runs them all in reverse order — enabling things like "party mode".

Why prefer a MacroCommand over a hardcoded PartyCommand? :: MacroCommand lets you decide dynamically which commands to include, giving more flexibility and less new code than hardcoding the calls in one command's execute().

What restriction lets you replace a ConcreteCommand with a lambda? :: The Command interface must have exactly one abstract method (a functional interface); adding a second abstract method breaks the lambda shorthand.

How does the Command Pattern enable job queues? :: Commands are first-class objects added to a queue; worker threads remove a command, call execute(), wait, discard it, and fetch the next — fully decoupling the queue from the computation.

Which two methods support logging/recovery with Command, and how? :: store() and load() (via serialization) — actions are stored to disk as they execute, and on a crash the commands are reloaded and their execute() methods reinvoked in order.

In what way is Swing's ActionListener related to Command? :: ActionListener is both an Observer and a Command interface — its actionPerformed() acts as execute(), making listener classes concrete commands.

What is the trade-off of a "smart" command that does the work itself instead of delegating to a receiver? :: You lose the decoupling between invoker and receiver and can no longer parameterize commands with different receivers.

#flashcards
