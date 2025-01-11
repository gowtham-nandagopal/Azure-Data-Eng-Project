# **Azure Data Engineering Project: Healthcare Revenue Cycle Management (RCM)**

## **Domain: Healthcare Revenue Cycle Management (RCM)**

Revenue Cycle Management (RCM) is a critical process used to manage the financial aspects of a hospital, from the time a patient schedules an appointment to the time the healthcare provider (hospital) receives payment.

### **Key Aspects of RCM**

Accounts Receivable (AR): Represents revenue that has been billed but not yet collected. It includes amounts due from patients and insurance companies.

Accounts Payable (AP): Covers the hospital's financial obligations, such as salaries for employees and doctors, and payments for medical equipment.

### **Project Datasets**

**1. **EMR Data (Electronic Medical Record)****

Stored in Azure SQL Databases, split across two different accounts for two hospitals (e.g., Apollo and Manipal Hospital).

Includes:

- Patient information

- Doctor information

- Transaction records

- Department details

- Encounters: When a patient visits a hospital for the first time, an encounter is created (e.g., Encounter 1), with multiple transactions associated with it.

**2. **Claims Data****

- Provided by insurance companies.

- Stored in Azure Blob Storage within a container named Landing.

- Format: Flat files (CSV).

**3. **NPI Data (National Provider Identifier)****

- Unique 10-digit numerical identifier for individual providers (e.g., doctors).

- Retrieved via a public API.

**4. **ICD Codes (International Classification of Diseases)****

- Standardized codes used by healthcare providers to map diagnoses to descriptions.

- Retrieved via an API.

**5. **CPT Codes (Current Procedural Terminology)****

- Standardized codes that identify medical procedures and services.

- Stored in a Data Lake container named Landing.

### **Architecture: Medallion Architecture**

This project implements a Medallion Architecture with three layers: Bronze, Silver, and Gold.

**1. **Bronze Layer:****

- Stores raw data in Parquet format.

- Serves as the source of truth.

**2. **Silver Layer:****

- Data is cleansed, validated, and transformed.

- Data quality checks are performed.

- Slowly Changing Dimensions Type 2 (SCD2) is implemented for dimension tables such as Patients, Providers, Claims, NPI, CPT, and ICD datasets.

- Stored as Delta tables.

**3. **Gold Layer:****

- Contains aggregated and processed data optimized for analytics.

- Stored as Delta tables.

- Process Flow

### **Data Ingestion:**

- EMR data is ingested from Azure SQL Databases.

- Claims and CPT data is ingested from Azure Blob Storage.

- NPI and ICD data is fetched via API.

### **Automation:**

- The end-to-end pipeline is implemented in Azure Data Factory (ADF).

- Automates data ingestion, transformation, and movement between layers.

### **Tools and Technologies Used**

- Azure SQL Database: For EMR data storage.

- Azure Blob Storage: For Claims data ingestion.

- Azure Data Factory (ADF): For pipeline orchestration and automation.

- Azure Data Lake Storage: For data storage in Bronze, Silver, and Gold layers.

- Delta Lake: For efficient storage and handling of Silver and Gold layers.

- Parquet Format: For raw data storage in the Bronze layer.

- APIs: For fetching NPI and ICD codes.

**Credits**

- Sumit Mittal

- [Watch the YouTube Video](https://www.youtube.com/watch?v=d3Vw3VtKDnc)

