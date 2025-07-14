# Copyright (c) 2025, Light and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ListingRequest(Document):
	def before_save(self):
		self.sample=self.listing
