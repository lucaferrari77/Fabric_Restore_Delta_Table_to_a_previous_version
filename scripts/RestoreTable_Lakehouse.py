#!/usr/bin/env python
# coding: utf-8

# ## restorelakehousetable
# 
# New notebook

# **This is an example on how you can restore a table in a MS Fabric Lakehouse**
# 
# Here some basic concept:</br>
# [Time Travel](https://learn.microsoft.com/en-us/azure/databricks/delta/history) </br>
# [Lakehouse and Delta Lake tables](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-and-delta-tables)</br>
# [Describe History](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/delta-describe-history)</br>
# [Restore Table](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/delta-restore)
# 
# 
# 

# **Configure the environment**
# 
# Specify the name of the lakehouse and its workspace id (you can get it from the url in the Fabric Web UI)

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%configure
# {
#     "defaultLakehouse": {  
#         "name": "",
#         "workspaceId": ""
#     }
# }


# **Getting the history of the table**
# 
# This will show the history of the table
# 
# *Parameter* 
# 
# tablename = the name of the table you want to investigate
# 
# 

# In[ ]:


tablename = 'mytable1'
query = f'''DESCRIBE HISTORY {tablename}'''

df = spark.sql(query)
display(df)


# **Investigating the table**
# 
# With this query you can verify its data, as it was in a specific version back in the past.
# 
# Parameter
# 
# version = the version number from the above step

# In[ ]:


version = '4'
query = f'''SELECT * FROM {tablename} VERSION AS OF {version} LIMIT 10'''

df = spark.sql(query)
display(df)


# **Restoring the table**
# 
# Restoring the table as it was in a specific version in the past

# In[ ]:


query = f'''RESTORE TABLE {tablename} VERSION AS OF {version}'''

spark.sql(query)


# **Checking the outcome**
# 
# Data should have been restore as the were in a specific version.
# its latest version should have RESTORE as "operation"

# In[ ]:


tablename = 'mytable1'
query = f'''DESCRIBE HISTORY {tablename}'''

df = spark.sql(query)
display(df)

