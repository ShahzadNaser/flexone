// Copyright (c) 2023, GreyCube Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Expence Against Serial Number"] = {
	"filters": [
		{
            fieldname: 'serial_no',
            label: __('Serial No'),
            fieldtype: 'Link',
            options: 'Item',
            get_query: function() {
                return {
                    query: 'erpnext.controllers.queries.item_query'
                };
            }
        }
	]
};
