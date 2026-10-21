---
course: SE2012
lecture_num: 10
aliases: [Errors and Exceptions, Exception Handling, exception]
topics: [Java, Compile-time errors, Run-time errors, Exceptions, Checked Exceptions, Unchecked Exceptions, try-catch, finally, throws, Custom Exceptions]
---

# Errors and Exceptions in Java

## Overview
An [[exception]] is an *abnormal event* that arises during the execution (run time) of a program and disrupts the normal flow of the program.

> [!NOTE] Why this matters
> Rarely does a program run successfully at its very first attempt. A mistake might lead to an **error** causing the program to produce unexpected results, terminate abruptly, or even crash the system. It is therefore important to **detect and manage** all possible error conditions so the program does not terminate or crash during execution.

### Types of Errors
The lecture broadly classifies errors into **two categories**:
1. **[[Compile-time error|Compile-time errors]]**
2. **[[Run-time error|Run-time errors]]**

---

## Compile-Time Errors
All **syntax errors** are detected and displayed by the Java compiler — hence they are known as **compile-time errors**. Whenever the compiler displays an error, it will **not create the `.class` file**. All such errors must be fixed before the program can be successfully compiled and run.

```java
/* This program contains an error */
public class Error1 {
    public static void main(String args[]) {
        System.out.println("Hello Java!")   // Missing ;
    }
}
```

The Java compiler reports where the error is. For the missing semicolon above, it displays:
```
Error1.java:5: ';' expected
        System.out.println("Hello Java! ")
                                          ^
1 error
```

### Common Compile-Time Errors
Most compile-time errors are due to typing mistakes. The most common problems are:
- Missing **semicolons**
- Missing (or mismatch of) **brackets** in classes and methods
- **Misspelling** of identifiers and keywords; missing double quotes in strings
- Use of **undeclared variables**
- **Incompatible types** in assignments / initializations
- **Bad references** to objects
- Use of `=` in place of the `==` operator

> [!WARNING] Directory / Path errors
> Other errors relate to directory paths. An error such as `javac: command not found` means the **path is not set correctly**. Ensure the path includes the directory where the Java executables are stored.

---

## Run-Time Errors
Sometimes a program **compiles successfully** (creating the `.class` file) but does **not run properly**. Such programs may produce wrong results due to wrong logic, or terminate due to errors such as stack overflow.

### Most Common Run-Time Errors
- Dividing an integer by **zero**
- Accessing an element that is **out of the bounds** of an array
- Trying to store a value into an array of an **incompatible** class or type
- Trying to **cast** an instance of a class to one of its subclasses
- Passing a **parameter** that is not in a valid range or value for a method
- Trying to illegally **change the state of a [[thread]]**
- Attempting to use a **negative size** for an array
- Using a **null object reference** as a legitimate object reference to access a method or variable
- Converting an **invalid string** to a number
- Accessing a **character** that is out of bounds of a string

```java
class Error2 {
    public static void main(String args[]) {
        int a = 10;
        int b = 5;
        int c = 5;
        int x = a / (b - c);          // Division by zero
        System.out.println("x = " + x);
        int y = a / (b + c);
        System.out.println("y = " + y);
    }
}
```

The program is syntactically correct, so it compiles. However, while executing it displays the following message and stops **without executing further statements**:
```
java.lang.ArithmeticException: / by zero
        at Error2.main(Error2.java:8)
```
When the Java run-time tries to execute a division by zero, it generates an error condition that causes the program to stop after displaying an appropriate message.

> [!QUESTION] Coding Exercise
> Create a simple Java program that generates a run-time exception for **converting an invalid string to an Integer**. (Hint: use `Integer.parseInt(String s)`.)
> ```java
> public class EX1 {
>     public static void main(String[] args) {
>         String number = "123a";
>         int value = Integer.parseInt(number);   // throws NumberFormatException at runtime
>     }
> }
> ```

---

## Why Exceptions?
Exceptions, as a mechanism, provide several advantages over ad-hoc error checking:
- **Allow separation of error-handling code from "regular" code** — mixing error-handling with regular code makes it hard to read.
- **Easily propagating errors up the call stack** — explicit (manual) propagation of errors can be very clunky.
- **Allow grouping and differentiating error types.**

---

## The Exception Mechanism

When a runtime error occurs within a method, the method creates an object (the **exception object**) and hands it off to the runtime system.
- This object contains information about the error, including its type and the state of the program when the error occurred.
- Creating an exception object and handing it to the runtime system is called **throwing** an exception.
- That method may choose to handle the exception itself or pass it on. At some point, the exception must be **caught** and processed.

> [!NOTE] Origin of Exceptions
> Exceptions can be generated automatically by the Java run-time system, or they can be manually generated by your code using the `throw` keyword.

### Uncaught Exceptions
If an exception is not caught anywhere in your program, it will eventually reach the default exception handler provided by the Java run-time system.
- The default handler displays a string describing the exception.
- It prints the **[[stack trace]]** (the sequence of method calls that led to the error).
- It **terminates the program**.

---

## Three Kinds of Exceptions

Java classifies all abnormal events into three categories, rooted in the `Throwable` hierarchy:

### 1. `Error` (Unchecked)
- **Nature**: External to the application (e.g., `OutOfMemoryError`, hardware failure).
- **Recovery**: Usually, programs cannot recover from them.
- **Requirement**: Not subject to the "catch or specify" requirement.

### 2. `RuntimeException` (Unchecked)
- **Nature**: Internal to the application (e.g., divide by zero, null pointer access).
- **Recovery**: Usually not anticipated to recover from them; they represent bugs that should be fixed.
- **Requirement**: Not subject to the "catch or specify" requirement.

### 3. `Exception` (Checked)
- **Nature**: Internal to the application but outside the direct control of the code (e.g., `FileNotFoundException`).
- **Recovery**: Anticipated to recover from.
- **Requirement**: **Subject to the "catch or specify" requirement**. The compiler enforces that these exceptions must either be caught in a `try-catch` block or declared in a `throws` clause.

---

## Hierarchy of Java Exception Classes
All errors and exceptions descend from `Throwable`:

```
                Throwable
                /        \
            Error        Exception
         (unchecked)    /         \
              RuntimeException   (other checked
               (unchecked)        exceptions, e.g.
              /     |     \       IOException, SQLException)
   Arithmetic  NullPointer  ArrayIndexOutOfBounds ...
```

### Error Class
- An `Error` **is a** subclass of `Throwable` that indicates **serious problems**.
- Errors represent **critical, irrecoverable** problems once they occur (the system is not expected to recover).
- Errors can be generated from a mistake in program **logic or design**.
- **Most applications should not try to handle** them.
- They are **unchecked** — not subject to "throw or specify".
- e.g. `OutOfMemoryError`, `VirtualMachineError`, `AssertionError`.

### Exception Class
- Represents the exceptional conditions that a user may **throw and/or catch (handle)**.
- When an exceptional condition arises, an object representing that exception is created and thrown in the method that caused the error.
- That method may handle the exception itself or pass it on; at some point the exception is caught and processed.
- Exceptions can be generated by the Java run-time system, or **manually generated** by your code.

### Checked vs Unchecked Exceptions
| | Checked Exceptions | Unchecked Exceptions |
|---|---|---|
| **Definition** | All exceptions that require being caught and handled **at compile time**. | Usually caused by incorrect program code or logic (e.g. invalid parameters passed to a method). |
| **Class rule** | Classes that extend `Throwable` **except** `RuntimeException` and `Error`. | Classes that extend `RuntimeException`. |
| **When checked** | At **compile time** (enforced by compiler). | At **runtime**. |
| **Examples** | `IOException`, `SQLException` | `ArithmeticException`, `ArrayIndexOutOfBoundsException` |

> [!IMPORTANT] Catch or Specify Requirement
> Code containing **checked exceptions** must honour the **Catch or Specify Requirement** — code that might throw such exceptions must be enclosed by **either**:
> - A `try` statement that **catches** the exception (providing a handler), **or**
> - A method that **specifies** it can throw the exception via a `throws` clause that lists the exception.

### Two Ways to Handle Exceptions
1. **Throw out and ignore** — when an exception occurs inside a method, simply throw it and let the caller handle it; the method *specifies* that it throws the exception (`throws`).
2. **Catch and handle** — if a code segment generates an exception, place it inside a `try` block and explicitly handle the exception inside a `catch` block.

---

## Exception Handling with try-catch

The fundamental workflow of exception handling is:
1. **Find the problem** (Hit the exception).
2. **Inform that an error has occurred** (Throw the exception).
3. **Receive the error information** (Catch the exception).
4. **Take corrective actions** (Handle the exception).

This provides two massive benefits:
- It allows you to fix the error gracefully.
- It **prevents the program from automatically terminating**.

To guard against and handle a run-time error, simply enclose the code you want to monitor inside a `try` block, and immediately follow it with a `catch` clause that specifies the exception type you wish to catch:
```java
try {
    statement;                  // generates an exception
} catch (Exception-type e) {
    statement;                  // processes the exception
}
```

### Basic try-catch Block
```java
class Exc2 {
    public static void main(String args[]) {
        int d, a;
        try { // monitor a block of code.
            d = 0;
            a = 42 / d;
            System.out.println("This will not be printed.");
        } catch (ArithmeticException e) { // catch divide-by-zero error
            System.out.println("Exception: " + e);
            System.out.println("Division by zero.");
        }
    }
}
```

> [!NOTE] How control flows
> The call to `println()` inside the `try` block is **never executed**. Once an exception is thrown, program control transfers out of the `try` block into the `catch` block. Put differently, `catch` is not "called," so execution never "returns" to the `try` block from a `catch`. Once the `catch` statement has executed, program control continues with the next line following the entire `try`/`catch` mechanism.

### Multiple Catch Clauses
More than one exception could be raised by a single piece of code. You can specify two or more `catch` clauses.
- Each `catch` statement is inspected in order.
- The **first one** whose type matches the exception is executed.
- After one executes, the others are bypassed.

```java
class MultipleCatches {
    public static void main(String args[]) {
        try {
            int a = args.length;
            System.out.println("a = " + a);
            int b = 42 / a;
            int c[] = {1}; 
            c[42] = 99;
        } catch (ArithmeticException e) {
            System.out.println("Divide by 0: " + e);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index OOB: " + e);
        }
        System.out.println("After try/catch blocks.");
    }
}
```

### Java SE 7 Multi-Catch
In Java 7 and later, a single catch block can handle more than one type of exception using a vertical bar (`|`). This reduces code duplication.
```java
try {
    // some code
} catch (IOException | SQLException ex) {
    System.out.println(ex);
}
```
> [!IMPORTANT]
> If a catch block handles more than one exception type, the catch parameter is implicitly `final` and cannot be reassigned within the block.

---

## Nested try Statements

When a `try-catch` block is present inside another `try` block, it is called a [[nested try-catch]].
- If a nested `try` block does not have a handler for a particular exception, the system inspects the catch blocks of its **parent** `try` block.
- If neither handles it, the system default handler takes over.

```java
public class NestingDemo {
    public static void main(String[] args) {
        try { // Main try-block
            try { // try-block2
                try { // try-block3
                    int arr[] = {1, 2, 3, 4};
                    System.out.println(arr[10]);
                } catch (ArithmeticException e) {
                    System.out.print("Arithmetic Exception");
                    System.out.println(" handled in try-block3");
                }
            } catch (ArithmeticException e) {
                System.out.print("Arithmetic Exception");
                System.out.println(" handled in try-block2");
            }
        } catch (ArithmeticException e3) {
            System.out.print("Arithmetic Exception");
            System.out.println(" handled in main try-block");
        } catch (ArrayIndexOutOfBoundsException e4) {
            System.out.print("ArrayIndexOutOfBoundsException");
            System.out.println(" handled in main try-block");
        } catch (Exception e5) {
            System.out.print("Exception");
            System.out.println(" handled in main try-block");
        }
    }
}
```

---

## The `finally` Block

The [[finally block]] is used to execute code that must run **regardless of whether an exception is thrown or caught**.
- It is added immediately after the `try` block or after the last `catch` block.
- It is typically used for **house-keeping operations**, such as closing files, closing database connections, or releasing system resources.

```java
public class EX1 {
    public static void main(String[] args) {
        try {
            String number = "123a";
            int value = Integer.parseInt(number);
        } catch (NumberFormatException ex) {
            System.out.println("Wrong number format");
        } finally {
            System.out.println("End of operation");
        }
    }
}
```

---

## The `throws` Keyword

If a method is capable of causing an exception that it does not handle itself, it must specify this behavior so callers can guard against it.
- Used for handling **Checked Exceptions** (the "specify" part of the catch-or-specify requirement).
- You can declare multiple exceptions in one go separated by commas.

```java
import java.io.*;
class Error03 {
    // Specifies that this method may throw an IOException
    public static void main(String[] a) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String text = ""; 
        System.out.print("Enter an integer value : "); 
        text = in.readLine(); 
        int num = Integer.parseInt(text); 
        System.out.println("You inserted " + num);
    }
}
```

### Delegation and Handling Example
```java
public class MathOp {
    public int add(int a, int b) { 
        return a + b;
    }
    // Delegate the exception handling to the caller
    public double divide(int a, int b) throws ArithmeticException {
        return a / b;
    }
}

public class EX2 {
    public static void main(String[] args) {
        MathOp math = new MathOp();
        math.add(2, 0);
        
        try {
            // Caller handles the exception
            math.divide(2, 0);
        } catch (ArithmeticException ex) {
            System.out.println("Error: division by zero");
        }
    }
}
```

---

## Creating Custom Exceptions

To define your own exception, create a subclass of `Exception` (which is a subclass of `Throwable`).
- The `Exception` class does not define any methods of its own; it inherits them from `Throwable`.
- It defines four constructors, primarily: `Exception()` and `Exception(String msg)`.

```java
class MyException extends Exception { 
    MyException(String message) {
        super(message);
    }
} 

class TestMyException {
    public static void main(String args[]) { 
        int x = 5, y = 1000;
        try {
            float z = (float) x / (float) y;
            if (z < 0.01) {
                // Manually throwing the custom exception
                throw new MyException("Number is too small");
            }
        } catch (MyException e) {
            System.out.println("Caught my exception");
            System.out.println(e.getMessage());
        } finally {
            System.out.println("I am always here");
        }
    }
}
```

---

## Commonly Used Exceptions Reference

| Exception | Meaning |
|---|---|
| `ArithmeticException` | Arithmetic error, such as divide-by-zero. |
| `ArrayIndexOutOfBoundsException` | Array index is out-of-bounds. |
| `ArrayStoreException` | Assignment to an array element of an incompatible type. |
| `ClassCastException` | Invalid cast. |
| `EnumConstantNotPresentException` | An attempt is made to use an undefined enumeration value. |
| `IllegalArgumentException` | Illegal argument used to invoke a method. |
| `IllegalMonitorStateException` | Illegal monitor operation, such as waiting on an unlocked thread. |
| `IllegalStateException` | Environment or application is in incorrect state. |
| `IllegalThreadStateException` | Requested operation not compatible with current thread state. |
| `IndexOutOfBoundsException` | Some type of index is out-of-bounds. |
| `NegativeArraySizeException` | Array created with a negative size. |
| `NullPointerException` | Invalid use of a null reference. |
| `NumberFormatException` | Invalid conversion of a string to a numeric format. |
| `SecurityException` | Attempt to violate security. |
| `StringIndexOutOfBounds` | Attempt to index outside the bounds of a string. |
| `TypeNotPresentException` | Type not found. |

---

## 🧠 Flashcards

What are the two broad categories of errors per the lecture? :: Compile-time errors and Run-time errors.

What is a compile-time error? :: A syntax error detected and displayed by the Java compiler; when it occurs the compiler does not create the .class file.

Name four common compile-time errors. :: Missing semicolons, mismatched brackets, misspelled identifiers/keywords (or missing string quotes), and use of undeclared variables.

What does the error `javac: command not found` indicate? :: The path is not set correctly — it must include the directory where the Java executables are stored.

What is a run-time error? :: An error in a program that compiled successfully but fails while running (e.g. divide-by-zero, array out-of-bounds, null reference, stack overflow).

What exception is thrown when an integer is divided by zero? :: java.lang.ArithmeticException (/ by zero).

Why use exceptions instead of ad-hoc error checking? :: They separate error-handling code from regular code, allow errors to propagate up the call stack easily, and allow grouping/differentiating error types.

What is an Exception in Java? :: An abnormal event that arises during runtime and disrupts the normal flow of the program.

What does "throwing" an exception mean? :: A method creates an exception object containing the error type and program state, and hands it off to the Java runtime system.

What happens if an exception is completely uncaught? :: The default Java runtime handler catches it, prints the stack trace and an error description, and then terminates the program.

What are the three kinds of exceptions in Java's hierarchy? :: Error (unchecked), RuntimeException (unchecked), and Exception (checked).

Which Throwable subclasses are unchecked? :: Error and RuntimeException (and their subclasses).

By the class rule, which exceptions are checked? :: Classes that extend Throwable except RuntimeException and Error (e.g. IOException, SQLException).

When are checked vs unchecked exceptions verified? :: Checked exceptions are checked at compile time; unchecked exceptions are checked at runtime.

What is the Catch or Specify Requirement? :: Code that might throw a checked exception must either catch it in a try statement or specify it in the method's throws clause.

What are the two ways to handle an exception? :: Throw out and ignore (specify with throws), or catch and handle (try-catch).

What happens if multiple `catch` blocks match an exception? :: Only the first matching catch block in order is executed; the rest are bypassed.

What is the syntax for catching multiple exceptions in a single block (Java SE 7+)? :: Use a vertical bar: catch (IOException | SQLException ex).

If you use multi-catch (e.g. `catch (A | B e)`), what implicit modifier applies to `e`? :: It is implicitly final and cannot be reassigned.

In a nested `try-catch`, what happens if the inner block has no matching `catch`? :: The catch blocks of the parent try block are inspected for a match.

What is the primary purpose of the `finally` block? :: To execute house-keeping code (like closing files or releasing resources) regardless of whether an exception was thrown or caught.

What is the `throws` keyword used for? :: To specify that a method may throw a checked exception, delegating handling to the caller (the "specify" part of catch-or-specify).

How do you create a custom exception in Java? :: Create a subclass of Exception (a subclass of Throwable), typically with a constructor that calls super(message).

What keyword manually throws an exception, and what is the syntax? :: throw — e.g. `throw new MyException("message");`.

What causes an `ArrayStoreException`? :: Attempting to assign an element of an incompatible type into an array.

What causes an `IllegalMonitorStateException`? :: An illegal monitor operation, such as waiting on a thread that is not locked.

#flashcards
