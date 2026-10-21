---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: "Lab 03"
aliases: [Use Case Diagrams, use case diagrams]
topics:
  - use case diagrams
  - actors
  - use case scenarios
  - include and extend
---

# Use Case Diagrams

> **Source**: SE2012 OOAD — Lab 03: Use Case Diagrams (case studies practised with draw.io / Visual Paradigm). Use-case *notation* and actor concepts are introduced in [[Requirements_Engineering]] (Lecture 02).

[[use case diagram|Use case diagrams]] are used to identify the primary elements and processes that form a system. They identify the system's [[actor|actors]], the [[use case|use cases]] (functions or processes), and the relationships among them.

This note covers practical case studies and scenarios for drawing Use Case Diagrams.

---

## Case Study 1: Flamingo Musical System

**Background:** "Flamingo" is a music and video store. The Sri Lanka Media Association (SLMA) is launching its digital version.

### Requirements & Scenarios

- **Visitor (Unregistered User):** Can watch the public gallery and search for videos. Short clips of trending music videos are available. To watch full trending videos, the visitor must purchase them, which requires creating a **Fan account**.
- **Contributor:** Anyone interested in uploading their own audio or video must create a **Contributor account**. 
- **Registration Process:** First, enter personal details, agree with terms and conditions, and then choose a payment plan for the year.
- **Watching Content (Fan / User):** Once registered, a user can watch trending music videos by buying content from the pool.
- **Discounts & Payments:** If there are seasonal discounts, the discount is generated during purchasing. Payments can be done via PayPal, Master/VISA, or American Express.
- **FAQ & Feedback:** Users can access the FAQ, post issues, and provide ratings/feedback on videos.
- **Admin:** Responsible for answering questions, managing the FAQ, and handling feedback and ratings.
- **Contributor Privileges:** For every multiple of 100 videos uploaded, their level is uplifted. Depending on the level, a special contributor discount is calculated when buying videos.
- **Reports:** The system generates weekly reports for Fans and Contributors upon request.

> [!NOTE] Practical Application
> This scenario demonstrates the use of **includes** (like processing payments when purchasing) and **extends** (like calculating seasonal or contributor discounts). It also highlights how different actors (Visitor, Fan, Contributor, Admin) interact with overlapping vs exclusive system boundaries.

---

## Case Study 2: TasteBuds Catering System (TBCS)

**Background:** "TasteBuds (TB)" is a restaurant needing a system to track customers and orders.

### Requirements & Scenarios

- **Customer:** Can place orders through TBCS. Registered customers receive a discount based on the number of monthly orders. Orders are given a queue number, and the current serving number is displayed on the main page.
- **Head Chef (HC):** Receives the order numbers and details. Based on details, the HC prepares the order as "normal" or "priority", assigns chef(s), and estimates the time taken.
- **Delivery Manager:** Assigns delivery staff considering the order category (e.g., priority orders get a vehicle/driver within 10 minutes; normal orders depend on availability).
- **Delivery Driver:** Must have a valid driving license (stored in TBCS for security). Checks out the delivery using TBCS on a mobile phone with the order number and license number.
- **Post-Delivery (Customer):** Customer marks the order as delivered in the TBCS, and can optionally provide ratings, comments, or suggestions.

---

## Case Study 3: Cool Cuts Saloon (Hairdresser System)

**Background:** A hairdresser appointment and payment management system.

### Requirements & Scenarios

- **Making Appointments:** Customers (e.g., Jacky, Ravi, Amanda) ring for an appointment. The Receptionist or Manager checks schedules and books slots for specific hairdressers.
- **System Access:** 
  - **Manager (Michael):** Has full access. Enters employee details (e.g., adding a new cutter and their days off). 
  - **Receptionist (Mandy):** Mainly responsible for taking payments. Also handles inventory in the manager's absence.
- **Payments:** After a haircut, the Receptionist calculates the amount, accepts payment, and registers it on the system.
- **Inventory Management:** When new stock arrives, the Receptionist updates prices and stock levels.
- **Product Sales:** Customers can buy products (shampoo, conditioner). The Receptionist enters the product code (system validates and looks up price). The Receptionist can cancel items before finalizing. Finally, the total is calculated, payment is made, and an invoice is printed.

---

## Use Case Scenarios

A **Use Case Scenario** is a text description of a single path through a [[use case]]. It describes the step-by-step interaction between the [[actor]] and the system.

**Examples of common scenarios to write:**
- "Login" function
- "Search a book" function
- "Reserve a book" function

> [!TIP] Writing Scenarios
> Use Case Scenarios are highly effective for mapping out exactly how edge cases (like invalid product codes or unavailable stock) are handled step-by-step.

---

## 🧠 Flashcards

What are the primary elements identified by a [[use case diagram]]? :: The system's actors, the use cases (functions/processes), and the relationships among them.

What is a use case scenario? :: A step-by-step text description of a single path through a use case, detailing the interaction between the actor and the system.

In a use case diagram, what does an [[actor]] represent? :: A user or another system that interacts with the system being modeled.

How does an "include" relationship function in a use case diagram? :: It shows that a use case always includes the functionality of another use case (e.g. Purchasing a video always includes Processing Payment).

How does an "extend" relationship function in a use case diagram? :: It shows that a use case may optionally extend another use case's behaviour under certain conditions (e.g. Calculating a seasonal discount extends the Purchasing process).

#flashcards
