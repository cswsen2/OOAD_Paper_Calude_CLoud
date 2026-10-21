---
course: SE2012
lecture_num: 12
topics: [Java, Threads, Concurrency, Synchronization, Daemon Threads]
---

# Threads in Java

## What is a Thread?
A [[thread]] is a path of execution within a program. It allows multiple sequences of operations to execute concurrently within a single program or [[process]]. 

**Examples of applications utilizing threads:**
- **Word Processors**: One thread processes user keystrokes, while another thread performs background spell checking, and another periodically saves the document.
- **Games**: Complex games often have multiple threads—e.g., one for rendering graphics, one for handling user input, one for physics calculations, and one for networking.

### Other Scenarios Threads Can Be Applied
- **Producer-Consumer Problem**: A producer thread generates data and places it into a buffer, while a consumer thread removes data from the buffer.
- **Client-Server Architecture**: A server receives a request from a client. It creates a new thread to service that specific request, allowing the main server thread to resume listening for additional client requests without blocking.

## Multi-threaded Environment
In a multi-threaded environment, multiple threads interact to share resources.
For example, multiple Producer Threads (P1, P2, P3) can put data into a shared **Data Buffer**, and multiple Consumer Threads (C1, C2, C3) can consume data from it. Proper management and synchronization are necessary to ensure data integrity and avoid race conditions.

## Thread vs. Process

| Feature | [[thread]] | [[process]] |
| :--- | :--- | :--- |
| **Creation** | Easier to create (no separate address space required). | Heavier, require more overhead to create. |
| **Weight** | Lightweight (use fewer resources). | Heavyweight. |
| **Independence** | Exist as subsets of a process. | Typically independent. |
| **Memory** | Share the address space of their parent process. | Have separate, isolated address spaces. |
| **Context Switching** | Faster (since address space is shared). | Slower (requires switching memory contexts). |

### Resources Utilized by Threads
**A Thread in execution works with its own:**
- **Thread ID**
- **Registers** (program counter and working register set)
- **Stack** (for procedure call parameters, local variables, etc.)

**A thread shares with other threads in the same process:**
- **Code section**
- **Data section** (static + heap)
- **Permissions**
- **Other resources** (e.g., open files, sockets)

## Thread Life Cycle and States
The lifecycle of a Java thread transitions through various states from its creation to termination.

1. **New**: A thread object is created but `start()` has not been called yet.
2. **Runnable / Ready**: The `start()` method is invoked. The thread is ready to run and waiting for the CPU.
3. **Running**: The thread dispatcher allocates CPU time, and the `run()` method executes.
4. **Blocked / Waiting / Sleeping**: 
   - `sleep()` moves the thread to **Sleeping**.
   - `wait()` moves the thread to **Waiting**.
   - I/O requests move the thread to **Blocked**.
5. **Dead (Terminated)**: The `run()` method completes or the thread is stopped.

## Thread Implementation

There are two primary ways to create a thread in Java:
1. Extending the `Thread` class.
2. Implementing the `Runnable` interface.

### 1. Extends `Thread` Class
```java
public class ThreadImpl extends Thread {

    /**
     * Thread execution scenario implementation
     * @param args
     */
    public static void main(String[] args) {
        ThreadImpl threadImpl = new ThreadImpl();
        threadImpl.start(); // Invokes run() in a new thread
        for (int i = 0; i < 10; i++) {
            System.out.println("Main Thread " + i);
        }
    }

    /**
     * New thread implementation
     */
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println("New Thread " + i);
        }
    }
}
```

### 2. Implements `Runnable` Interface
```java
public class ThreadImpl implements Runnable {

    /**
     * Thread execution scenario implementation
     * @param args
     */
    public static void main(String[] args) {
        // Create Runnable instance and wrap it in a Thread object
        Thread thread = new Thread(new ThreadImpl());
        thread.start();
        for (int i = 0; i < 10; i++) {
            System.out.println("Main Thread " + i);
        }
    }

    /**
     * New thread implementation
     */
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println("New Thread " + i);
        }
    }
}
```

## [[thread synchronization]]
When multiple threads access a shared resource without coordination, unpredictable behavior or data corruption can occur. 

### Why Synchronization is Needed
By default, threads are **not synchronized**.
- When `Thread.sleep()` is called, it keeps the lock with it. It throws an `InterruptedException`.
- If multiple threads try to modify the same object simultaneously, the final state of the object depends on thread scheduling (race condition).

### Synchronized Method
Using the `synchronized` keyword on a method ensures that only one thread can execute it at a time for a given object instance.
```java
class Sample {
    // Synchronized method
    public synchronized void displayOutput(Sample sample) {
        try {
            for (int i = 0; i < 10; i++) {
                Thread.sleep(1000);
                System.out.println(Thread.currentThread().getName());
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

### Synchronized Block
Sometimes, synchronizing an entire method is inefficient. A `synchronized` block allows you to synchronize only a specific section of code by explicitly defining the object lock.
```java
class Sample {
    public void displayOutput(Sample sample) {
        // Synchronized block locking on the 'sample' object
        synchronized (sample) {
            try {
                for (int i = 0; i < 10; i++) {
                    Thread.sleep(1000);
                    System.out.println(Thread.currentThread().getName());
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

**Common Mistake: Locking on newly instantiated objects:**
```java
// Anti-pattern: Each thread gets a separate object to lock on.
// The method is effectively NOT synchronized.
synchronized (new Sample()) { 
    // ...
}
```

### Importance of Synchronization: Singleton Pattern Example
Without synchronization, a multi-threaded environment might create multiple instances of a Singleton class.
```java
public class ThreadSafeSingleton {
    private ThreadSafeSingleton() { }
    
    private static ThreadSafeSingleton instance;
    
    public static ThreadSafeSingleton getInstance() {
        if (instance == null) {
            // Synchronize on the class literal to ensure only one instance is created
            synchronized (ThreadSafeSingleton.class) {
                if (instance == null) {
                    instance = new ThreadSafeSingleton();
                    System.out.println("Thread Safe Instance created " + Thread.currentThread().getName());
                }
            }
        }
        return instance;
    }
}
```

## Thread Control Methods

### Thread `join()` Method
- The `join()` method causes the currently running thread to stop executing and wait until the thread it joins with completes its task (dies).
```java
public class ThreadJoin extends Thread {
    public void run() {
        Thread t = Thread.currentThread();
        System.out.println("Started executing " + t.getName());
        for (int i = 0; i < 10; i++) {
            System.out.println(t.getName() + i);
        }
        System.out.println("Finished executing " + t.getName());
    }

    public static void main(String args[]) throws Exception {
        Thread t = new Thread(new ThreadJoin(), "New Thread ");
        t.start();
        System.out.println("Started executing main thread");
        
        // Main thread waits for the new thread 't' to die before proceeding
        t.join();
        
        for (int i = 0; i < 10; i++) {
            System.out.println(Thread.currentThread().getName() + i);
        }
        System.out.println("Finished executing " + Thread.currentThread().getName());
    }
}
```

### Thread `yield()` Method
- `yield()` is used to give other threads of the **same priority** a chance to execute.
- It causes the currently running thread to temporarily pause and move from the **Running** state back to the **Runnable/Ready** state.

### Thread `wait()`, `notify()`, and `notifyAll()`
These methods provide inter-thread communication.
- `wait()`: Releases the object's lock and changes the thread state from Runnable to **Waiting**. It throws an `InterruptedException`.
- `notify()`: Wakes up a single thread that is waiting on the object's monitor and moves it to the **Ready** state to resume execution.
- `notifyAll()`: Wakes up **all** threads that called `wait()` on the same object.

#### Example: `wait()` and `notify()`
```java
// Thread that waits
public void run() {
    synchronized (object) {
        try {
            System.out.println("Started " + Thread.currentThread().getName() + " wait");
            object.wait(); // Releases lock, goes to waiting state
            System.out.println("Started " + Thread.currentThread().getName() + " notified");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // ...
    }
}

// Thread that notifies
public void run() {
    synchronized (object) {
        System.out.println(Thread.currentThread().getName() + " notify Thread");
        object.notify(); // Or notifyAll() to wake all waiting threads
    }
}
```

## Thread Priority
Threads can be assigned a priority to help the thread scheduler determine the execution order.
- Minimum Priority: `1`
- Normal Priority (Default): `5`
- Maximum Priority: `10`

## [[daemon threads]]
Daemon Threads are "background threads" that provide services to other threads (e.g., the Java Garbage Collection thread).
- The Java Virtual Machine (JVM) will **not exit** if non-daemon threads are still executing.
- The JVM **will exit** if only Daemon threads are left executing.
- Daemon threads die abruptly when the JVM exits; `finally` blocks in daemon threads may not be executed.

**Example:**
```java
public class DeamonThread extends Thread {
    public static void main(String[] args) {
        System.out.println("Entering main Method");
        
        DeamonThread t = new DeamonThread();
        t.setDaemon(true); // Set as daemon before starting
        t.start();
        
        try {
            Thread.sleep(3000);
        } catch (InterruptedException x) { }
        
        System.out.println("Leaving main method");
        // Main thread finishes, JVM exits, Daemon thread dies abruptly
    }
    
    public void run() {
        System.out.println("Entering run method");
        try {
            System.out.println("In run Method: " + Thread.currentThread().getName());
            while (true) {
                try {
                    Thread.sleep(500);
                    System.out.println("In run method: woke up again");
                } catch (InterruptedException x) {
                    x.printStackTrace();
                }
            }
        } finally {
            // May NOT execute when the JVM shuts down
            System.out.println("Leaving run Method");
        }
    }
}
```

## Commonly Used Methods for `Thread` Class

| Method | Description |
| :--- | :--- |
| `public void run()` | Used to perform the action for a thread. |
| `public void start()` | Starts the execution of the thread. JVM calls `run()` method on the thread. |
| `public void sleep(long milliseconds)` | Causes the currently executing thread to sleep (temporarily cease execution) for the specified duration. |
| `public void join()` | Waits for a thread to die. |
| `public void join(long milliseconds)` | Waits for a thread to die for a specified duration. |
| `public int getPriority()` | Returns the priority of the thread. |
| `public int setPriority(int priority)` | Changes the priority of the thread. |
| `public String getName()` | Returns the name of the thread. |
| `public void setName(String name)` | Changes the name of the thread. |
| `public Thread currentThread()` | Returns the reference to the currently executing thread. |
| `public int getId()` | Returns the thread's ID. |

## 🧠 Flashcards

What is a Thread? :: A lightweight path of execution within a program that allows concurrent execution of operations within a process.

List two main differences between a Thread and a Process. :: Threads share the memory/address space of their parent process while processes have independent address spaces; threads are lightweight and context-switch faster than processes.

Why are threads considered lightweight? :: They don't require a separate address space and use far fewer resources than processes.

What does a thread have its own copy of? :: Thread ID, registers (program counter and working register set), and a stack (for call parameters and local variables).

What does a thread share with other threads in its process? :: The code section, data section (static + heap), permissions, and other resources such as open files.

What are the states of a Thread's life cycle? :: New, Runnable (Ready), Running, Blocked/Waiting/Sleeping, and Dead (Terminated).

What are the two primary ways to create a thread in Java? :: By extending the Thread class, or by implementing the Runnable interface.

Why is Thread Synchronization necessary? :: To prevent race conditions and data corruption when multiple threads access and modify shared resources concurrently.

What happens to object locks when Thread.sleep() is called? :: The thread sleeps but retains (keeps) the locks it currently holds; sleep() also throws InterruptedException.

What is the difference between wait() and sleep() regarding object locks? :: wait() releases the object's lock so other threads can acquire it, whereas sleep() retains the lock.

Why does synchronizing on a newly instantiated object fail to synchronize threads? :: Each thread gets a separate object to lock on, so the method is effectively not synchronized.

What does the join() method do? :: It causes the currently running thread to stop and wait until the thread it joins with completes its task (dies).

What does the yield() method do? :: It gives other threads of the same priority a chance to execute, moving the current thread from Running back to Runnable/Ready state.

What does wait() do to a thread's state and lock? :: It releases the object's lock and moves the thread from Runnable to Waiting; it throws InterruptedException.

What is the purpose of notifyAll() compared to notify()? :: notifyAll() wakes up all threads waiting on the same object's monitor, whereas notify() wakes only a single waiting thread.

What are the minimum, normal, and maximum thread priorities? :: 1 (minimum), 5 (normal/default), and 10 (maximum).

What is a Daemon Thread? :: A background thread (like the garbage collector) that services other threads; the JVM exits when only daemon threads remain, and daemon threads die when the JVM exits.

#flashcards
