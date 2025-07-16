# Copyright (c) 2025, Light and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Listing(WebsiteGenerator):
	def before_save(self):
		self.route=self.name
		if self.description == None:
			self.description=self.item_name

# @frappe.whitelist(allow_guest=True)
# def get_sum(price, full_name):

# 	print (f"\n\n\n{price}\n\n\n")
# 	print (f"\n\n\n{full_name}\n\n\n")
	
# 	new_price=float(price)*1.12

# 	return new_price