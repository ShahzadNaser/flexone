import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_report_data(filters)
    return columns, data

def get_columns():
    columns = [
        {"fieldname": "serial_no", "label": "Serial No", "fieldtype": "Link", "options": "Item:120"},
        {"fieldname": "expense_date", "label": "Date", "fieldtype": "Date:100"},
        {"fieldname": "description", "label": "Description", "fieldtype": "Data:200"},
        {"fieldname": "expense_amount", "label": "Amount", "fieldtype": "Currency:120"},
    ]
    return columns

def get_report_data(filters):
    data = []

    if filters.get("serial_no"):
        expenses = frappe.get_all(
            "Expense",
            filters={"serial_no": filters.get("serial_no")},
            fields=["serial_no", "expense_date", "description", "expense_amount"],
        )

        for expense in expenses:
            data.append({
                "serial_no": expense.serial_no,
                "expense_date": expense.expense_date,
                "description": expense.description,
                "expense_amount": expense.expense_amount
            })

    return data