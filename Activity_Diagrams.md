---
course: SE2012
lecture_num: 9
aliases: [Activity Diagrams, activity diagrams]
topics: [UML, Activity Diagrams, Workflow, Swimlanes, Action Nodes, Control Nodes]
---

# Activity Diagrams

## Overview
An [[activity diagram]] models the **activities of a system**, the **dependencies between activities**, and represents **[[workflow|workflows]]**. It shows the flow of control from activity to activity.

> [!OUTSIDE] This framing was not present in the original lecture material.
> Activity diagrams are commonly described as a variation of the [[state diagram]] for the dynamic aspects of a system: where state diagrams model the states of a single object, activity diagrams model the computational and organizational processes (the workflow).

## When to Use Activity Diagrams

- Modeling **business processes**.
- Analyzing system functionality to **identify the use cases**.
- Analyzing **individual use cases** in detail.
- Clarifying **concurrency** issues.

---

## Elements of an Activity Diagram

### 1. Action Nodes
An [[action node]] represents a single step within an activity. It is the fundamental unit of executable functionality.
- **Simple Action**: A single step.
- **Call Action**: An action that invokes another activity or behavior.
> **Notation**: Actions are represented by **rounded rectangles**.

### 2. Transitions (Control Flow)
Activity/Action nodes are connected by [[Transitions]].
- Also known as a **control flow**, **directed flow**, or **edge**.
- When the execution of a node completes, execution proceeds to the node found on the output flow.
> **Notation**: Represented by a **solid directed arrow**.

### 3. Control Nodes
[[control node|Control nodes]] manage the flow of execution through the activity. They include starting points, ending points, and decision mechanisms.

#### Initial & Final Nodes
- **Initial/Start Node**: Represents the beginning of a diagram.
  > **Notation**: A **solid filled circle**.
- **Final/End Node**: Represents the end of the diagram. When the flow reaches this node, the activity terminates.
  > **Notation**: A **solid filled circle within an outer hollow circle** (a bullseye).

> [!OUTSIDE] This extra detail was not present in the original lecture material.
> Standard UML also defines a **Flow Final Node** (a circle with an 'X') that destroys only the token arriving at it without affecting other concurrent flows. The lecture covered only the **Initial (start)** and **Final (end)** nodes.

#### Decision & Merge Nodes
- **Decision/Branch Node**: Used when a flow of control needs to be split based on a condition. 
  - Each branch must have a **[[guard condition]]** (e.g., `[Guard Expression]`).
  - The flow of control flows down the **single** path where the branch condition evaluates to true.
  - There is **no limit** on the number of branches a decision point may have.
  > **Notation**: A **diamond** with one incoming flow and multiple outgoing flows.
- **Merge Node**: Used to bring together multiple alternate flows that were split by a [[decision node]]. It does *not* synchronize the flows; whichever flow arrives first simply passes through.
  > **Notation**: A **diamond** with multiple incoming flows and one outgoing flow.

#### Fork & Join Nodes
- **Fork Node**: Used to split a single flow into multiple **concurrent (parallel)** flows.
  - Unlike a branch point, the control flows down **all** forked paths simultaneously.
  > **Notation**: A **thick solid line (bar)** with one incoming flow and multiple outgoing flows.
- **Join Node**: Used to synchronize multiple concurrent flows back into a single flow.
  - The execution waits until **all** incoming flows have arrived before proceeding to the single outgoing flow.
  > **Notation**: A **thick solid line (bar)** with multiple incoming flows and one outgoing flow.

> [!WARNING] Common Mistakes with Nodes
> - **Incorrect use of forks/joins vs. branch/merges**: A fork means the flow goes down *both* paths concurrently. A merge point indicates the merging of divergent paths, not concurrent flows. Do not mix a Fork with a Merge diamond.
> - **Missing Guard Conditions**: All loops and decision branches must have explicit guard conditions (e.g., `[yes]`, `[no]`).

---

## Advanced Structures

### Iteration (Loops)
An asterisk (`*`) inside an action state indicates that it may need to be performed more than once. This notation shows iteration without the unnecessary details of a loop construct. The next action state does not occur until the loop is finished.
> [!IMPORTANT]
> The use of an asterisk will not clearly highlight loop termination conditions. Therefore, using a **Decision Node** with explicit guard conditions to represent an iteration/loop is the ideal and preferred approach.

### Partitioning & Swimlanes
An [[activity partition]] is an activity group for actions that have some common characteristic. Partitions often correspond to organizational units or business actors in a business model.
- **SwimLanes**: Activity partitions are usually drawn as [[swimlane|SwimLanes]].
  - Notation: Two, usually parallel lines (either horizontal or vertical) with a name labeling the partition in a box at one end.
- **Sub-Partitioning**: You can nest partitions inside other partitions (e.g., An "Order Department" swimlane nested inside a broader "Company" class swimlane).

---

## Pedagogical Scenarios & Case Studies

### Case Study 1: Library Membership
> [!NOTE] Scenario: Becoming a Library Member
> To become a library member, a student must keep a refundable security deposit of Rs.3000/=. Few registration forms should be filled in order to handle membership. Upon registration, a member will be given a membership ID and a password.

### Case Study 2: Borrowing Books
> [!NOTE] Scenario: Borrow Books Activity
> To borrow books, one must become a member. Members have access to core textbooks, reference books, general reading materials, CDs, and DVDs. If a member student needs to borrow more than one book at a time, he/she can do so after depositing an additional refundable deposit of Rs. 3000/-.

### Case Study 3: University Enrollment
> [!NOTE] Scenario: Enrolling in University
> 1. Candidates who wish to register for university have to fill out enrolment forms and submit them promptly.
> 2. The forms which are incorrectly filled will be rejected.
> 3. The candidates who submitted properly filled forms are enrolled.
> 4. The enrolled candidates then have to register for a seminar and make payments for initial tuitions.
> 5. Meanwhile, they have to attend a university overview presentation as a start.
> 6. Then only students can start classes.
> *(This scenario emphasizes the use of **Forks and Joins** for concurrent activities: making payments while attending the presentation).*

### Case Study 4: Developing a Software System (No Swimlanes vs. Swimlanes)
> [!NOTE] Scenario: Software Development Lifecycle
> 1. Project Manager (PM) first gathers the requirements.
> 2. UI Engineer (UIE) develops the prototype.
> 3. PM shows the prototype to the client.
> 4. Till the client is satisfied, UIE modifies the prototype (Loop).
> 5. Once the client is satisfied, they sign off on the prototype.
> 6. UIE develops the UI screens while the Software Engineer (SE) develops the system (Parallel Fork).
> 7. Once both are done, the SE integrates the system (Parallel Join).
> 8. PM delivers the system to the client.
> 9. Client signs off on the delivery.
> *(When modeled with **Swimlanes**, this activity is divided into four vertical partitions: PM, UIE, Client, and SE, bringing extreme clarity to who is responsible for which action).*

### Case Study 5: Order Processing System
> [!NOTE] Scenario: Fulfilling Orders
> 1. Once the order is received by the customer service department, several other departments operate on various activities.
> 2. The fulfillment department fills the order and delivers it.
> 3. Meanwhile, as soon as the order is received, customer service works on sending an invoice.
> 4. The finance department handles payments. The shop operates on credit, so receiving payments is not mandatory prior to delivery.
> 5. Customer service can close the order only after completing all the above activities.

---

## How to Create an Activity Diagram

When starting from a scenario description, follow these steps:
1. Identify activities (steps) of a process.
2. Identify who/what performs the activities (process steps).
3. Draw swim lanes.
4. Identify decision points (if-then).
5. Determine if a step is in a loop (For each..., or if-then loop).
6. Determine if a step is parallel with some other step.
7. Identify the order of activities and decision points.
8. Draw the start point of the process in the swimlane of the first activity.
9. Draw the oval (rounded rectangle) of the first activity.
10. Draw an arrow to the location of the second step.
11. Draw subsequent steps, while inserting decision/synchronization/loop bars where appropriate.
12. Draw the end point after the last step.

### Tabular Organization Example
You can tabulate the data extracted from a scenario to make drawing the diagram easier. Here is an example matrix for generating a quote:

| Step ID | Process Activity or Decision | Who/What Performs | Parallel Activity | Loop | Preceding Step |
|---|---|---|---|---|---|
| 1 | Request quote | Customer | No | No | - |
| 2 | Develop requirement notes | Salesperson | No | Yes | 1 |
| 3 | Decision: Help? | Salesperson | - | Yes | 2 |
| 4 | Salesperson enters data | Salesperson | No | Yes | 3 |
| 5 | Check requirements | Technical Expert | No | Yes | 3 |
| 6 | Tech. expert enters data | Technical Expert | No | Yes | 5 |
| 7 | Calculate quote | System | No | Yes | 4, 6 |
| 8 | Review quote | Customer | No | Yes | 7 |
| 9 | Decision: Changes? | Customer | No | Yes | 8 |
| 10 | Accept quote as order | Customer | No | No | 9 |

---

## 🧠 Flashcards

What is an Activity Diagram used for? :: It is a UML diagram used to model the workflow, computational processes, and dynamic aspects of a system.
What shape represents an Action Node in an activity diagram? :: A rounded rectangle.
What shape represents the Initial/Start node? :: A solid filled circle.
What is the difference between an Activity Final Node and a Flow Final Node? :: An Activity Final Node (bullseye) terminates the entire activity, whereas a Flow Final Node (circle with an X) only destroys the token that arrives at it without affecting concurrent flows.
What shape is used for a Decision/Branch point? :: A diamond.
What must each branch of a Decision node possess? :: A guard condition (e.g., [yes] or [no]).
What is the difference between a Branch and a Fork? :: A branch sends the flow down a single path based on a condition. A fork splits the flow into multiple concurrent (parallel) paths simultaneously.
What is the difference between a Merge and a Join? :: A merge brings alternative paths back together without synchronizing. A join synchronizes multiple concurrent flows, waiting for all of them to arrive before proceeding.
What notation is used to represent a Fork or Join? :: A thick solid line (a bar).
Why is using an asterisk (*) to represent iteration considered non-ideal? :: Because it does not clearly highlight the loop termination conditions. Using a Decision Node with guard conditions is preferred.
What is a Swimlane (Activity Partition) used for? :: To group actions that share a common characteristic, typically representing organizational units or business actors responsible for those actions.
#flashcards
