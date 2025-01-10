# Databricks notebook source
# MAGIC %md
# MAGIC ## To list all the existing mount

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

# MAGIC %md
# MAGIC ## To list all the secret scopes

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Add the external mount locations

# COMMAND ----------

storage_account_name = "azdeprojectadls"
storage_access_key = dbutils.secrets.get(scope="secret-access-key", key="storage-access-key")
mountPoints = ['gold', 'silver', 'bronze', 'landing','configs']
for mountPoint in mountPoints:
    if not any(mount.mountPoint == f"/mnt/{mountPoint}" for mount in dbutils.fs.mounts()):
        try:
            dbutils.fs.mount(
                source="wasbs://{}@{}.blob.core.windows.net/".format(mountPoint, storage_account_name),
                mount_point="/mnt/{}".format(mountPoint),
                extra_configs={'fs.azure.account.key.' + storage_account_name +'.blob.core.windows.net': storage_access_key})
            print(f"{mountPoint} mount successful")
        except Exception as e:
            print("mount exception", e)

# COMMAND ----------

dbutils.fs.mounts()
