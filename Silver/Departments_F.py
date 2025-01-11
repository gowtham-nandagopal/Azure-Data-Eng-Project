# Databricks notebook source
from pyspark.sql import SparkSession, functions as f

#Reading Hospital A departments data 
df_hosa=spark.read.parquet("/mnt/bronze/hosa/departments")

#Reading Hospital B departments data 
df_hosb=spark.read.parquet("/mnt/bronze/hosb/departments")

#union two departments dataframes
df_merged = df_hosa.unionByName(df_hosb)

# Create the dept_id column and rename deptid to src_dept_id
df_merged = df_merged.withColumn("SRC_Dept_id", f.col("deptid")) \
                     .withColumn("Dept_id", f.concat(f.col("deptid"),f.lit('-'), f.col("datasource"))) \
                     .drop("deptid")

df_merged.createOrReplaceTempView("departments")


# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS departments (
# MAGIC Dept_Id string,
# MAGIC SRC_Dept_Id string,
# MAGIC Name string,
# MAGIC datasource string,
# MAGIC is_quarantined boolean
# MAGIC )
# MAGIC USING DELTA
# MAGIC LOCATION '/mnt/silver/departments';

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate table hive_metastore.default.departments

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into hive_metastore.default.departments
# MAGIC SELECT 
# MAGIC Dept_Id,
# MAGIC SRC_Dept_Id,
# MAGIC Name,
# MAGIC Datasource,
# MAGIC     CASE 
# MAGIC         WHEN SRC_Dept_Id IS NULL OR Name IS NULL THEN TRUE
# MAGIC         ELSE FALSE
# MAGIC     END AS is_quarantined
# MAGIC FROM departments

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from hive_metastore.default.departments
