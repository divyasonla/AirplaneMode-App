// Copyright (c) 2024, divya and contributors
// For license information, please see license.txt
frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        frm.add_custom_button("Assign Seat", () => {
            frappe.prompt([
                {
                    label: 'Seat',
                    fieldname: 'seat',
                    fieldtype: 'Data'
                }
            ],
            (values) => {
                frm.set_value('seat', values.seat);
            },
            'Assign Seat',  
            'Assign'  
            );
        }, "Action");
    },
});
//     before_save: async function(frm) {
//         try {
//             let airplane = await frappe.db.get_value('Airplane', {'name': frm.doc.airplane}, 'capacity');
            
//             if (!airplane.message || !airplane.message.capacity) {
//                 frappe.throw('Airplane capacity could not be found. Please check the airplane details.');
//                 return;
//             }

//             let capacity = airplane.message.capacity;

//             let ticket_count = await frappe.db.count('Airplane Ticket', {
//                 filters: {
//                     'airplane': frm.doc.airplane
//                 }
//             });

//             if (ticket_count >= capacity) {
//                 frappe.throw(`Naya ticket create nahi kar sakte. Airplane ki maximum capacity ${capacity} seats ki hai, jo reach ho chuki hai.`);
//             }
//         } catch (error) {
//             console.error(error);
//             frappe.msgprint('An unexpected error occurred. Please try again.');
//         }
//     }
// });
