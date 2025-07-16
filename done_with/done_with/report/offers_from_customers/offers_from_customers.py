# Copyright (c) 2025, Light and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_data(filters):
    conditions = ""

    if filters.get("customer_name"):
        conditions += f" AND c.customer_name='{filters.get('customer_name')}'"

    if filters.get("item_name"):
        conditions += f" AND i.item_name = '{filters.get('item_name')}'"

    SQL = f"""
        SELECT
            c.customer_name,
            i.item_name,
            l.price,
            lo.offer_price
        FROM
            `tabItem Sample` AS i
        JOIN
            `tabListing` AS l
            ON i.name = l.item_name
        JOIN
            `tabListing Request` AS lo
            ON lo.parent = l.name
        JOIN
            `tabCustomer` AS c
            ON c.name = lo.full_name
        WHERE
            1=1 {conditions}
        ORDER BY l.item_name
    """

    return frappe.db.sql(SQL, as_list=True)


def get_columns():
	return [
		"Customer Name: Link/Customer: 200",
		"Item: Link/Item Sample: 200",
		"Sale Price: Currency:150",
		"Offer Price: Currency: 150"
	]

	
