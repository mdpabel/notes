---
title: Database Transactions and Concurrency
description: Database Transactions, Concurrency, and Isolation Levels.
date: 03-28-2024
---

A transaction is a sinlge unit of work that execute one or more SQL statements. It represents a single unit of work that should be executed as a whole, either entirely successful or entirely unsuccessful.

```sql
START TRANSACTION;

INSERT INTO orders (customer_id, order_date, status)
VALUES (1, '2024-04-01', 1);

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (LAST_INSERT_ID(), 1, 1, 1);

COMMIT;
```

In the provided example, a transaction starts with START TRANSACTION, executes SQL statements to insert data into tables, and then commits the transaction with COMMIT. If any error occurs during the transaction, it can be rolled back using ROLLBACK.

## ACID Properties:

1. Atomicity: Transactions should be like a single, unbreakable action. Everything inside a transaction should succeed or fail together, so we don't end up with partial changes that mess things up.

2. Consistency: Transactions keep the database in a good, consistent state. For example, if we add an order, we also need to add the items for that order to keep things sensible.

3. Isolation: Transactions should happen in their own little world, so they don't mess each other up. Each transaction should wait its turn to make changes and not interfere with others.

4. Durability: Once a transaction is done, its changes should stick around even if something bad happens like a power outage or a system crash.

## Concurrency Problems:

1. Lost Updates: If two actions try to update the same thing at the same time, one might overwrite the other and cause confusion.

#### Imagine two people are updating the same data at the same time. Let's say we have a customers table:

Person A and Person B both try to update the points of customer with ID 1:

```sql
-- Person A
START TRANSACTION;
UPDATE customers
SET points = points + 10
WHERE customer_id = 1;
COMMIT;

-- Person B
START TRANSACTION;
UPDATE customers
SET points = points + 20
WHERE customer_id = 1;
COMMIT;
```

In this scenario, if Person B's transaction commits after Person A's, Person B's changes will override Person A's changes, resulting in a lost update.

2. Dirty Reads: Imagine if one action reads data that's in the middle of being changed by another action. It might get incorrect or messy information.

#### Let's say we have a products table:

Person A is updating the price of a product, and Person B is trying to read the price while Person A's transaction is still ongoing:

```sql
-- Person A
START TRANSACTION;
UPDATE products
SET price = 15.99
WHERE product_id = 1;

-- Person B
SELECT price
FROM products
WHERE product_id = 1;
COMMIT;
```

In this case, Person B might see the updated price even though Person A's transaction hasn't finished yet, resulting in a dirty read.

3. Non-Repeatable Reads: If an action reads the same data multiple times, but it changes between reads because of other actions, that's a non-repeatable read.

Continuing from the previous example, let's say Person B tries to read the price of the same product again:

```sql
-- Person B (again)
START TRANSACTION;
SELECT price
FROM products
WHERE product_id = 1;
COMMIT;
```

If Person A commits the transaction and updates the price to 15.99 before Person B's second read, Person B will see different prices in the two reads, causing a non-repeatable read.

4. Phantom Reads: This is like reading a book where pages magically appear or disappear as you flip through. If one action sees a set of data, and then another action changes the data so the first action sees something different, that's a phantom read.

Suppose we have an orders table:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    total_amount DECIMAL(10, 2),
    order_date DATE
);
```

Person A is counting the total number of orders, and Person B is inserting a new order:

```sql
-- Person A
START TRANSACTION;
SELECT COUNT(*)
FROM orders;
COMMIT;

-- Person B
START TRANSACTION;
INSERT INTO orders (order_id, customer_id, total_amount, order_date)
VALUES (1001, 1, 50.00, '2024-04-01');
COMMIT;
```

In this scenario, if Person A's transaction finishes before Person B's insertion, Person A might count fewer orders than there actually are, resulting in a phantom read.

## Transaction Isolation Levels:

1. READ UNCOMMITTED: This is the lowest isolation level where transactions can see uncommitted changes made by other transactions, leading to dirty reads.

```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
```

2. READ COMMITTED: This isolation level ensures that transactions only see committed changes made by other transactions, preventing dirty reads. However, it may still result in non-repeatable reads. Example:

```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
```

3. READ COMMITTED: This isolation level ensures that transactions only see committed changes made by other transactions, preventing dirty reads. However, it may still result in non-repeatable reads. Example:

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

4. SERIALIZABLE: This is the highest isolation level that ensures complete isolation between transactions, preventing all concurrency problems (lost updates, dirty reads, non-repeatable reads, and phantom reads). Example:

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

Deadlocks:

- A deadlock occurs when two or more transactions are waiting for each other to release locks on resources that they need. This results in a standstill where none of the transactions can proceed.
- Deadlocks can be detected and resolved by the database management system, typically by aborting one of the transactions involved in the deadlock.

## Transactions — MongoDB

In MongoDB, transactions provide ACID properties (Atomicity, Consistency, Isolation, Durability) for operations that modify multiple documents or collections.

```js
const { MongoClient } = require('mongodb');

async function runTransaction() {
  const uri = 'mongodb://localhost:27017';
  const client = new MongoClient(uri);

  try {
    await client.connect();

    // Start a session
    const session = client.startSession();

    // Begin a transaction
    session.startTransaction();

    const ordersCollection = client.db('mydatabase').collection('orders');
    const inventoryCollection = client.db('mydatabase').collection('inventory');

    // Perform operations within the transaction
    await ordersCollection.insertOne({
      order_id: 1,
      customer_id: 123,
      total_amount: 100,
    });
    await inventoryCollection.updateOne(
      { product_id: 1 },
      { $inc: { quantity: -1 } },
    );

    // Commit the transaction
    await session.commitTransaction();
    console.log('Transaction committed successfully');
  } catch (error) {
    // If any error occurs, abort the transaction
    await session.abortTransaction();
    console.error('Transaction aborted due to error:', error);
  } finally {
    // End the session
    session.endSession();
    await client.close();
  }
}

runTransaction();
```

## Transactions — Redis

Redis, being an in-memory data store, does not natively support transactions in the same way as traditional relational databases. However, Redis provides a form of atomicity for multiple commands through its MULTI/EXEC transaction mechanism.

```shell
MULTI
SET key1 value1
SET key2 value2
GET key3
EXEC
```
