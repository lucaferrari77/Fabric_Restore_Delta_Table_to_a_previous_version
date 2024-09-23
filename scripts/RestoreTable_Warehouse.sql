/**********************************************************************************************************************
This script restore a warehouse table to a specific point in time.
A. Use this approach carefully, this might affect data consistency across multiple tables in the warehouse
B. This affect time travel, sp_rename affect history and users cannot longer browse it

Restore table is not supported, here the steps:
1. Identify the proper TIMESTAMP you want to restore
2. Dump the data in a new table using "CREATE TABLE tablename AS CLONE OF oldtable AT 'yyyy-mm-dd hh:mm:ss'"
3. If you need time travel:
    3a. Identify the Views, Fns, Sps that are referencing the old table
    4b. Change this reference and point the new table
4. If you no longer need time travel
    4a. Rename the old table (THIS AFFECT TIME TRAVEL)
    4b. Rename the clone using its original name

**********************************************************************************************************************/

--Checking the table to identify the proper timestamp
SELECT * FROM tablename OPTION(FOR TIMESTAMP AS OF 'yyyy-mm-dd hh:mm:ss');
--Once the timestamp has been identified
CREATE TABLE table1clone AS CLONE OF mytable1 AT 'yyyy-mm-dd hh:mm:ss';

/**********************************************************************************************************************
Rename the original table: THIS AFFECT TIME TRAVEL. 
**********************************************************************************************************************/
--TIME TRAVEL DISRUPTION
EXECUTE sp_rename 'originaltable_oldname','originaltable_newname';
--TIME TRAVEL DISRUPTION
EXECUTE sp_rename 'clonetable_oldname','clonetable_newname';

/**********************************************************************************************************************
To avoid time travel to be affected by the operation, ensure all the objects/queries etc that are referencing 
the original table are now referencing the cloned one.
**********************************************************************************************************************/
--Stored procedures and Functions
SELECT * FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_DEFINITION LIKE '%originaltable%';

--Views
SELECT * FROM INFORMATION_SCHEMA.VIEW_TABLE_USAGE WHERE SCHEMA_NAME = 'originaltableschemaname' AND TABLE_NAME = 'originaltable';



