// Copyright (c) 2023, GreyCube Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Expense Against Serial Number"] = {
	"filters": [
        {
            fieldname: 'item',
            label: __('Item'),
            fieldtype: 'Link',
            options: 'Item',
            
        },
        {
            fieldname: 'serial_no',
            label: __('Serial No'),
            fieldtype: 'Link',
            options: 'Serial No'
        }
	]
};
