// Copyright (c) 2024, divya and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Interview Schedule", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Interview Schedule', {
    validate: function(frm) {
        let today = frappe.datetime.get_today();
        if (frm.doc.interview_date && frm.doc.interview_date < today) {
            frappe.msgprint(__('Due Date cannot be in the past'));
            frappe.validated = false;  
        }
    },
    refresh:function(frm){
            frm.add_custom_button("Hired",()=>{
               
                frm.set_value("status","Hired")
                frm.save()
            })
            frm.add_custom_button("Rejected",()=>{
                frm.set_value("status","Rejected")
                frm.save()
            })
        
},
onload:function(frm){
    frappe.msgprint({
        title: `Welcome ${frm.doc.candidate_name}`,
        message: `your Interview Schedule on ${frm.doc.interview_date}`,
        indicator: 'green'
    });
    
},

});

