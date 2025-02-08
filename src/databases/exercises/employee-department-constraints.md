---
template: exercise
title: Dorms Query Exercise in SQLite
---

# Employee - Department Constraints Exercise

## Employee - Department Database

Given the following relations:

![](../slides/employee-department.png)

1. Write down some reasonable constraints given the data shown.

2. Given your constraints, which of the following are permissible?  If an operation is not permissible, why is it not?

- Update `Salary` for `John Smith` to `"100K"`.
- Update `Bdate` for `Jennifer Wallace` to `February 29, 1980`.
- Update `SSN` for `Ahmad Jabbar` to `123456789`.
- Update `Dno` for `Alicia Zelaya` to `2`.
- Insert into `DEPT_LOCATIONS` the tuple `<3, "Marietta">`.
- Update `Super_ssn` for `James Borg` to `8675309`.
- Update `Super_ssn` for `John Smith` to `NULL`.
- Delete the `Research` depatment from the `DEPARTMENT` relation.
