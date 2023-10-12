import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_report_data(filters)
    return columns, data

def get_columns():
    columns = [
        {"fieldname": "item_name", "label": "Item Name", "fieldtype": "Data", "width":"250"},
        {"fieldname": "serial_no", "label": "Serial No", "fieldtype": "Data", "width":"250"},
        {"fieldname": "item_type", "label": "Item Type", "fieldtype": "Data", "width":"250"},
        {"fieldname": "expense_amount", "label": "Amount", "fieldtype": "Currency", "width":"250"},
    ]
    return columns

def get_report_data(filters):
    data = []
    
  
    base_query = """
        SELECT
            serial.name AS serial_name,
            serial.item_code AS item_code,
            serial.item_type_cf AS item_type,
            COALESCE(SUM(expense.total_amount), 0) AS total_expense
        FROM
            `tabSerial No` AS serial
        LEFT JOIN
            `tabExpense Entry` AS expense
        ON
            serial.name = expense.expense_against_serial_no_cf
    """
    
    # Define the filter conditions based on user input
    conditions = []
    if filters.get("item"):
        conditions.append(f"serial.item_code = '{filters.get('item')}'")
    if filters.get("serial_no"):
        conditions.append(f"serial.name = '{filters.get('serial_no')}'")
    
    # Apply filter conditions to the SQL query
    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)
    
    # Group by "Serial No" and calculate the total expense
    base_query += " GROUP BY serial.name"
    
    # Execute the SQL query
    results = frappe.db.sql(base_query, as_dict=True)

    # Populate the data based on the query results
    for row in results:
        data.append({
            "item_name": row.item_code,
            "serial_no": row.serial_name,
            "item_type": row.item_type,
            "expense_amount": row.total_expense
        })

    return data
