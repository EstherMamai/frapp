// Copyright (c) 2025, Light and contributors
// For license information, please see license.txt

frappe.query_reports["Offers From Customers"] = {
	"filters": [
		{
			"fieldname": "customer_name",
			"label": __("Customer Name"),
			"fieldtype": "Link",
			"options": "Customer",
			"width":100,
			"reqd": 0
		},
		{
			"fieldname": "item_name",
			"label": __("Item Name"),
			"fieldtype": "Link",
			"options": "Item Sample",
			"width":100,
			"reqd": 0
		},
		{
			"fieldname": "price",
			"label": __("Sale Price"),
			"fieldtype": "Currency",
			"width":100,
			"reqd": 0
		},
		{
			"fieldname": "offer_price",
			"label": __("Offer Price"),
			"fieldtype": "Currency",
			"width":100,
			"reqd": 0
		}
	]	
};
