# Restore a lakehouse/warehouse table to a previous version

MS Fabric lakehouse and warehouse leverage the [Delta format](https://docs.delta.io/latest/delta-intro.html) and Delta format allow [Time travel](https://delta.io/blog/2023-02-01-delta-lake-time-travel/) which allows querying a table as it was in a specific poin in time. 
This depends on the Data retention for the lakehouse/Warehouse
1. A Lakehouse allows infinite versions of the same tables because there's no default data retention
2. A Warehouse allows up to 30 calendar days data retention. It means that an user can time travel back to 30 days in the past.

Due to data inconsistency, bug in the data process, user error etc, it might be necessary to restore the table as it was before the issue; with a Lakehouse the user can restore the table as it was before the issue happened easally using a notebook.
With a warehouse this can be done using the T-SQL code and some intermediate step.

[Here how to restore a table in a lakehouse](scripts/RestoreTable_Lakehouse.ipynb) </br>
[Here how to restore a table in a warehouse](scripts/RestoreTable_Warehouse.sql)


   


