frappe.ui.form.on('*', {
    refresh: function(frm) {
        frm.add_custom_button(__('Delete'), function() {
            frappe.confirm('Are you sure you want to delete this document?',
                function() {
                    frm.delete_doc();
                }, 
                function() {
                    frappe.msgprint('Deletion cancelled.');
                }
            );
        });
    }
});
