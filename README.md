# Python-project-on-Border_Crossing_Data
I use all the concept of DATA SCIENCE TOOLBOX: PYTHON PROGRAMMING
🔍 Data Loading & Inspection
📥 Loaded CSV into a DataFrame using pandas.

🧾 Checked info of the dataset: data types, non-null counts.

📊 Summary statistics using .describe().

👀 Previewed data with .head() and .tail().

❌ Dropped NA values and checked for missing data.

📌 Checked unique values in the 'Border' column.

🧹 Data Cleaning & Transformation
🧼 Filled missing values with "Unknown".

🏷️ Renamed columns: 'Port Name' → 'Port_Name', 'Measure' → 'Entry_Type'.

🔍 Filtered rows:

Only US-Mexico Border crossings.

US-Canada Border crossings with Value > 1000.

📈 Sorting, Aggregation, and Outlier Detection
📆 Sorted data by Date in descending order.

➕ Grouped data by 'Border' and summed 'Value'.

🚨 Detected outliers using IQR method.

🔗 Correlation & Covariance
📈 Computed correlation and covariance for numeric columns.

🧊 Plotted a heatmap to visualize correlations.

📅 Time Series Analysis
🧮 Grouped data by Date and Border to plot total crossings over time.

🗓️ Converted 'Date' column to datetime format.

📆 Created monthly aggregated border crossing totals.

📉 Plotted:

Line chart for crossings over time by border.

Monthly trends using line plots.

🛻 Trucks Analysis
🚚 Filtered data where Measure == 'Trucks'.

🧠 Calculated mean, median, std deviation for trucks.

⚖️ Performed a t-test comparing trucks between US-Canada and US-Mexico borders.

🧪 A/B Testing: January vs April
🧬 Simulated A/B test comparing crossings in Jan-24 vs Apr-24.

✅ Reported t-statistic and p-value.

📌 Concluded whether difference is statistically significant.

