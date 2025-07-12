# Chipotle Data Analysis - Ex2: Getting and Knowing Your Data
import pandas as pd

# Step 2: Import the dataset from this address
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

# Step 3: Assign it to a variable called chipo
chipo = pd.read_csv(url, sep='\t')

# Step 4: See the first 10 entries
print("Step 4: First 10 entries\n", chipo.head(10))

# Step 5: What is the number of observations in the dataset?
# Solution 1
print("\nStep 5 - Solution 1: Number of observations:", chipo.shape[0])
# Solution 2
print("Step 5 - Solution 2: Number of observations:", len(chipo))

# Step 6: What is the number of columns in the dataset?
print("\nStep 6: Number of columns:", chipo.shape[1])

# Step 7: Print the name of all the columns.
print("\nStep 7: Column names:\n", chipo.columns.tolist())

# Step 8: How is the dataset indexed?
print("\nStep 8: Index info:\n", chipo.index)

# Step 9: Which was the most-ordered item?
most_ordered_item = chipo.groupby('item_name').sum().sort_values('quantity', ascending=False).head(1)
print("\nStep 9: Most ordered item:\n", most_ordered_item)

# Step 10: For the most-ordered item, how many items were ordered?
print("\nStep 10: Number of most-ordered items:", most_ordered_item['quantity'].values[0])

# Step 11: Most ordered item in the choice_description column
most_choice = chipo['choice_description'].value_counts().head(1)
print("\nStep 11: Most ordered choice_description:\n", most_choice)

# Step 12: Total number of items ordered
total_items_ordered = chipo['quantity'].sum()
print("\nStep 12: Total items ordered:", total_items_ordered)

# Step 13: Turn the item price into a float
# Step 13a: Check the item price type
print("\nStep 13a: Item price type before:", chipo['item_price'].dtype)

# Step 13b: Convert to float
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x.replace('$','')))

# Step 13c: Check new type
print("Step 13c: Item price type after:", chipo['item_price'].dtype)

# Step 14: Revenue = sum of (quantity * item_price)
revenue = (chipo['quantity'] * chipo['item_price']).sum()
print("\nStep 14: Total revenue: $%.2f" % revenue)

# Step 15: How many orders were made in the period?
total_orders = chipo['order_id'].nunique()
print("\nStep 15: Total orders:", total_orders)

# Step 16: Average revenue per order
# Solution 1:
avg_rev = revenue / total_orders
print("\nStep 16 - Solution 1: Average revenue per order: $%.2f" % avg_rev)

# Solution 2:
order_totals = chipo.groupby('order_id').apply(lambda x: (x['quantity'] * x['item_price']).sum())
print("Step 16 - Solution 2: Average revenue per order: $%.2f" % order_totals.mean())

# Step 17: How many different items are sold?
diff_items = chipo['item_name'].nunique()
print("\nStep 17: Number of different items sold:", diff_items)
