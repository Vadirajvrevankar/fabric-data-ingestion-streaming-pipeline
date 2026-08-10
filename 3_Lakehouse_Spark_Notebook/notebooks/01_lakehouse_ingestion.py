# Read CSV into DataFrame

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("Files/sample_data.csv")

display(df)


# Write raw data as Parquet

df.write \
    .mode("overwrite") \
    .parquet("Files/raw/orders")


# Write data as managed Delta table

df.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("orders_delta")


# Verify Delta table

display(spark.table("orders_delta"))


# Run child notebook

mssparkutils.notebook.run("NB_Child_Notebook", 60)