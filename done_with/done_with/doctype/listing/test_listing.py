# Copyright (c) 2025, Light and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestListing(FrappeTestCase):
	def test_listing_document(self):
		test_listing=frappe.get_doc({
			"doctype": "Listing",
			"item_name": "Sweater",
			"price": "20",
			"acquired_on": "2022-01-11"
		}).insert()

		self.assertIsNotNone(test_listing.description)