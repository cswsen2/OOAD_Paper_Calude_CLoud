---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 05b
topics:
  - function overloading
  - constructors
  - default constructor
  - overloaded constructor
  - object initialization
---

# Function Overloading and Constructors

> **Source**: SE2012 OOAD — Lecture 05b | Prof. Nuwan Kodagoda & Mr. Jeewaka Perera
> **Note**: This lecture demonstrates the concepts in **C++** (the code uses `cout`, `char[]`, `strcpy`). The same ideas — [[function overloading]] and [[constructor|constructors]] — apply to [[Java]].

## Overview

This lecture extends the basic [[class]] structure with two mechanisms:
1. **[[function overloading]]** — multiple methods with the same name but different parameters.
2. **[[constructor|constructors]]** — special methods that automatically initialize an [[object]] the moment it is created, solving the *garbage value* problem.

## Function Overloading

In C++ you can have **multiple functions with the same name** but **different types of parameters** — this is **[[function overloading]]**.

> [!IMPORTANT] Rules of overloading
> - The **parameters of each function must be different**.
> - The **return type and the function name must remain the same**.

### Example — overloading `print()` (Slide 3)

```cpp
// Prototype functions
void print();
void print(char msg[]);
void print(char msg[], int no);

// Prototype function implementation
void print() {
    cout << "Hello " << endl;
}
void print(char msg[]) {
    cout << "Hello " << msg << endl;
}
void print(char msg[], int no) {
    cout << msg << " : " << no << endl;
}

int main() {
    print();
    print("SLIIT");
    print("Age ", 19);
    return 0;
}
```

**Output:**
```
Hello
Hello SLIIT
Age  : 19
```

## The Employee Class (from Lab 6)

The `Employee` class has five private attributes; only **public functions** can touch them ([[encapsulation]]):

```cpp
class Employee {
    private:
        int empno;
        char name[20];
        double basicSal;
        double allowance;
        double salary;
    public:
        void assignDetails(int pempno, char pname[], double pbasicSal);
        void setAllowance(double pallowance);
        void calcSalary();
        void printPaySlip();
};
```

> [!QUESTION] The garbage-value problem (Slide 5)
> If we create an object and print before setting all attributes, uninitialised attributes hold **garbage values**:
> ```cpp
> int main() {
>     Employee emp;
>     emp.assignDetails(0, "", 0);
>     emp.printPaySlip();
>     return 0;
> }
> ```
> Output shows a garbage `Allowance : 6.9528e-310` — because `assignDetails()` does **not** handle the allowance.

### Using an overloaded `assignDetails()` to initialize (Slide 7)

We can add a **no-argument overload** of `assignDetails()` that sets everything to 0:

```cpp
class Employee {
    private:
        int empno;
        char name[20];
        double basicSal;
        double allowance;
        double salary;
    public:
        void assignDetails();                                       // overloaded: initialize to 0
        void assignDetails(int pempno, char pname[], double pbasicSal);
        void setAllowance(double pallowance);
        void calcSalary();
        void printPaySlip();
};

int main() {
    Employee emp;
    emp.assignDetails();      // the no-arg overload
    emp.printPaySlip();
    return 0;
}
```

This works (all values print as 0) — *"but what if we want to do this **automatically** when an object is created?"* → **constructors**.

## Constructors

> [!NOTE] Initialize vs. assign (Slide 8)
> **Initialize** means setting values to attributes *at the beginning* (usually when they are declared). Although `assignDetails()` is a method on the class, it does **not** initialize automatically — when called it *assigns/overwrites* the garbage values already in the attributes. A special kind of method called a **[[constructor]]** can initialize attributes automatically.

> [!IMPORTANT] Properties of a constructor (Slide 10)
> - Used to **initialize the object when it is declared**.
> - **Does not return a value, and has no return type** (not even `void`).
> - Has the **same name as the class**.
> - There can be **default constructors** or **constructors with parameters**.
> - When an object is declared, the **appropriate constructor is executed** automatically.

| Type | Purpose |
| ---- | ------- |
| **[[default constructor\|Default constructor]]** | initialize attributes to default values |
| **[[overloaded constructor\|Overloaded constructor]]** (constructor with parameters) | assign values sent by the main program as arguments |

### Employee with both constructors (Slide 9)

```cpp
class Employee {
    private:
        int empno;
        char name[20];
        double basicSal;
        double allowance;
        double salary;
    public:
        Employee();
        Employee(int pempno, char pname[], double pbasicSal);
        void setAllowance(double pallowance);
        void calcSalary();
        void printPaySlip();
};

// default constructor
Employee::Employee() {
    empno = 0;
    strcpy(name, "");
    basicSal = 0;
    allowance = 0;
}

// Constructor with parameters
Employee::Employee(int pempno, char pname[], double pbasicSal) {
    empno = pempno;
    strcpy(name, pname);
    basicSal = pbasicSal;
}
```

> *Constructors don't have a return type. They have the same name as the class. `Employee()` is the **default constructor** and `Employee(int pempno, char ..)` is the **overloaded constructor**.*

### Using the Default Constructor (Slide 12)

```cpp
int main() {
    Employee emp;            // default constructor runs automatically
    emp.printPaySlip();
    return 0;
}
```
**Output:** EmpNo 0, Name (empty), Basic Salary 0, Allowance 0, Net Salary 0.

### Using the Overloaded Constructor (Slide 13)

```cpp
int main() {
    Employee emp(100, "Niranjan", 5000);   // overloaded constructor runs automatically
    emp.printPaySlip();
    return 0;
}
```
**Output:** EmpNo 100, Name Niranjan, Basic Salary 5000, Allowance 0, Net Salary 0.

## Exercises

> [!QUESTION] Exercise 1 — Write the constructors for a Rectangle class

**Solution (Slide 15):**

```cpp
class Rectangle {
    private:
        int width;
        int length;
    public:
        Rectangle();
        Rectangle(int l, int w);
        void setWidth(int w);
        int getWidth();
        void setLength(int l);
        int getLength();
        int calcArea();
};

// default Constructor
Rectangle::Rectangle() {
    length = 0;
    width = 0;
}

// Constructor with parameters
Rectangle::Rectangle(int l, int w) {
    length = l;
    width = w;
}
```

> [!QUESTION] Exercise 2 — Create two objects using the two constructors

**Solution (Slide 17):**

```cpp
int main() {
    Rectangle rec1;
    Rectangle rec2(10, 5);

    cout << "Rectangle 1 = length - " << rec1.getLength()
         << ", width - " << rec1.getWidth() << endl;
    cout << "Rectangle 2 = length - " << rec2.getLength()
         << ", width - " << rec2.getWidth() << endl;
    return 0;
}
```
**Output:**
```
Rectangle 1 = length - 0, width - 0
Rectangle 2 = length - 10, width - 5
```

## Constructor vs. Regular Method

| Feature | Constructor | Regular Method |
| ------- | ----------- | -------------- |
| **Name** | Same as the class name | Any valid identifier |
| **Return type** | None (not even `void`) | Has a return type |
| **Called when** | Automatically at object creation | Explicitly by the programmer |
| **Purpose** | Initialize the object | Perform an operation |
| **Overloading** | Yes (default + parameterized) | Yes |

## Related Concepts

- [[encapsulation]] — constructors keep initialization logic *inside* the class.
- [[information hiding]] — a constructor guarantees a valid initial state behind a clean interface.
- [[function overloading]] — constructors are themselves overloaded (default + parameterized).
- [[class]] and [[object]] — see [[OOP_Fundamentals]] for the foundational model.
- [[access modifiers]] — constructors are typically `public`.

## 📅 Tasks

- [ ] Implement the Rectangle class with default and overloaded constructors [due:: 2026-07-05] #p1
- [ ] Add default and parameterized constructors to the Lab 6 Employee class [due:: 2026-07-05] #p1
- [ ] Practice creating two objects using different constructors from the same class [due:: 2026-07-07] #p2

## 🧠 Flashcards

What is function overloading? :: Having multiple functions with the same name but different parameter types in the same scope; the return type and name stay the same, only the parameters differ.

What are the rules for function overloading? :: The parameters of each function must be different; the return type and function name must remain the same.

In the print() overloading example, what does print("Age ", 19) output? :: "Age  : 19" — it calls the print(char msg[], int no) overload.

Why does the Employee object print a garbage allowance value? :: Because assignDetails(int, char[], double) does not set the allowance attribute, so it keeps its uninitialised garbage value.

What is the difference between initialize and assign? :: Initialize means setting values at the beginning (when declared); assign overwrites whatever (possibly garbage) values are already there. Constructors initialize; assignDetails() assigns.

What is a [[constructor]]? :: A special method that automatically initializes an object when it is declared; it has the same name as the class and no return type (not even void).

Does a constructor have a return type? :: No — not even void. This distinguishes it from a regular method.

When is a constructor executed? :: Automatically when an object is declared/created; the appropriate constructor (default or overloaded) is chosen based on the arguments.

What is a [[default constructor]]? :: A constructor with no parameters that initializes attributes to default values (e.g. Employee() setting everything to 0).

What is an [[overloaded constructor]]? :: A constructor that takes parameters and assigns the values passed from the main program (e.g. Employee(100, "Niranjan", 5000)).

Can a class have both a default and an overloaded constructor? :: Yes — constructors can be overloaded, and the correct one runs based on the arguments used when creating the object.

In the Rectangle solution, what does `Rectangle rec2(10, 5)` produce? :: A rectangle with length 10 and width 5 (the overloaded constructor sets length = l, width = w).

How do constructors support encapsulation? :: They keep initialization logic inside the class and guarantee the object never exists in an invalid (garbage) state, hiding the initialization details behind a clean interface.

#flashcards
