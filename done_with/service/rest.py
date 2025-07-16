import frappe

# @frappe.whitelist(allow_guest=True)
# def get_users(doc,event):
#     # return frappe.db.get_all("User")

# 	query = """
# 		SELECT * FROM tabuser
# 	"""

# 	users=frappe.db.sql(query, as_dict=True)

# 	print (f"\n\n\n {doc.email} \n\n\n")
		
# 	return users

def get_all_listings(doc):
    # return frappe.db.get_all("Listing", fields=["item_name","price","acquired_on"])
    return frappe.db.count("Listing")