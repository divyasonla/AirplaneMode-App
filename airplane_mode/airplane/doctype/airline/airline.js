// Copyright (c) 2024, divya and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // if (frm.doc.website) {
        //     frm.add_custom_button('Visit Website', () => {
        //         window.open(frm.doc.website, '_blank');
        //     }).addClass('btn-primary');
        // }
        const website = frm.doc.website;
        frm.add_web_link(website,"Visit Website");
    }
});
