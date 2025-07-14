// Copyright (c) 2025, Light and contributors
// For license information, please see license.txt

frappe.ui.form.on("Listing", {
 	refresh(frm) {
        frm.add_custom_button(__('Sum Interests'), function() {
            frappe.call({
                method: 'done_with.done_with.doctype.listing.listing.get_sum',
                args: {
                    'price': frm.doc.price
            },
            callback: function(r) {
                console.log(r.message) 
            }
        });

        },__("Actions"));

    //     frm.add_custom_button(__('Something Else'), function() {
    //         frappe.msgprint("Something Else");
    //    },__("Actions"));
 	},
    validate: function(frm){
        let offers=frm.doc.shown_interests;

        let total_offers_value=0;

        offers.forEach(row => {
            total_offers_value += row.offer_price
        })
        
        frm.set_value("totals",total_offers_value);
        frm.refresh;
    }
});