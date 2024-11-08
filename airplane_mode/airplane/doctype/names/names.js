// Copyright (c) 2024, divya and contributors
// For license information, please see license.txt

frappe.ui.form.on("names", {
    refresh(frm) {
        frappe.confirm('Are you sure you want to proceed?',
            () => {
                frappe.msgprint('You selected Yes! Proceeding with action.');
            }, 
            () => {
                frappe.msgprint('You selected No! Action canceled.');
            }
        );
    }
});
