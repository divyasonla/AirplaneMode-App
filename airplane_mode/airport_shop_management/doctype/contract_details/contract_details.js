// Copyright (c) 2024, divya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contract Details", {
	refresh(frm) {
		check_the_status(frm);
	},
	onload(frm) {
		check_the_status(frm);
	},
	validate(frm) {
		check_the_status(frm);
	}
});

function check_the_status(frm) {
	let today = frappe.datetime.get_today();  
	let expire = frm.doc.contract_end_date;

	if (expire && expire < today) {
		frm.set_value("status", "Expired");
	} else if(expire && expire >= today) {
		frm.set_value("status", "Active");
	}
}
