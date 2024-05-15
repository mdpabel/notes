---
title: Development Best Practices
description: folder structures, design patterns, coding standards, and other best practices.
date: 05-15-2024
status: published
priority: 1
---

## NodeJS folder structure

```bash
project/
│
├── src/
│   ├── controllers/
│   │   ├── auth.controller.js
│   │   ├── user.controller.js
│   │   └── ...
│   │
│   ├── routes/
│   │   ├── auth.routes.js
│   │   ├── user.routes.js
│   │   └── ...
│   │
│   ├── services/
│   │   ├── auth.service.js
│   │   ├── user.service.js
│   │   └── ...
│   │
│   ├── models/
│   │   ├── auth.model.js
│   │   ├── user.model.js
│   │   └── ...
│   │
│   ├── middleware/
│   │   ├── authentication.js
│   │   └── ...
│   │
│   ├── utils/
│   │   ├── validation.js
│   │   └── ...
│   │
│   ├── config/
│   │   └── database.js
│   │
│   ├── app.js
│   └── server.js
│
└── .env
```

## Git commit message types:

1. build: Changes related to building the project or its dependencies.
2. chore: Regular maintenance tasks, such as updating dependencies or refactoring 3. code without impacting functionality.
3. ci: Changes to the Continuous Integration (CI) configuration or scripts.
4. docs: Documentation-related changes, including adding or updating documentation.
5. feat: New features or functionalities added to the project.
6. fix: Bug fixes or corrections to existing code.
7. perf: Performance improvements or optimizations.
8. refactor: Code refactoring that does not change its external behavior.
9. revert: Reverting a previous commit.
10. style: Changes that do not affect the code's functionality, such as formatting, indentation, or whitespace.
11. test: Adding, updating, or fixing tests.
