---
title: Database Management System (DBMS)
description: Everything about database management systems
date: 04-07-2024
isPublished: false
priority: 1
---

## ER Diagram:

ER diagrams, or Entity-Relationship diagrams, are visual representations used to design databases. They help us understand how different entities in a system relate to each other.

### Entities:

Entities are objects or things we want to store information about. For example, in a school database, entities could be students, teachers, courses, etc. Each entity is represented by a rectangle in the diagram.

### Attributes:

Attributes are the properties of entities. A student entity might have attributes like student ID, name, age, etc. These are represented inside the rectangles for each entity.

1. Simple Attribute: cannot be divided into smaller parts. For example, a student's name or age.
2. Composite Attribute: can be divided into smaller sub-parts. For example, a student's address might have sub-parts such as street, city, state, and zip code.
3. Derived Attribute: whose value can be derived or calculated from other attributes. For example, a student's age can be derived from their date of birth
4. Multi-valued Attribute: can have multiple values. For example, a student may have multiple phone numbers associated with them.
5. Key Attribute: uniquely identifies each entity.For example, a student's ID.
6. Composite Key: combination of two or more attributes that uniquely identify.For example, a combination of a student's name and date of birth.
7. Foreign Key: an attribute or a set of attributes in one relation that refers to the primary key in another relation. For example, in a database linking students to courses, the student ID in the course enrollment table would be a foreign key referencing the student table.

### Relationships:

Relationships show how entities are connected or linked to each other. For example, in a school database, a student entity might be related to a course entity through an "enrolled in" relationship. Relationships are represented by lines connecting the related entities.

1. One to One
2. One to Many / Many to One
3. Many to Many

### Cardinality:

Cardinality represents the number of occurrences of one entity that are associated with the number of occurrences of another entity through a relationship. Cardinality is usually represented by symbols like "1" for one occurrence or "N" for many occurrences.
