# import frappe
import frappe
settings = frappe.get_doc("Rent Setting")
if settings.rent_reminders:
    unpaid_contracts = frappe.get_all(
        "Contract Details",
        filters={"status": "Unpaid"},
        fields=["tenant_name", "name","tenant_email","rent_amount"]
    )

    if unpaid_contracts:
        for contract in unpaid_contracts:
            if contract.tenant_email:
                try:
                    frappe.sendmail(
                        recipients=contract.tenant_email,
                        subject="Rent Payment Reminder",
                        content=f"Dear {contract.tenant_name},\n\nThis is a reminder to pay your rent of {contract.rent_amount}. Please make the payment at the earliest.",
                        cc="divyasonla143@gmail.com", 
                        now=True
                    )
                    frappe.log(f"Reminder sent to {contract.tenant_email} for Contract Details {contract.name}.")
                except Exception as ex:
                    frappe.log_error(message=str(ex), title="Rent Reminder Email Sending Error")
            else:
                frappe.log_error(f"No email found for Lease Contract {contract.name}", title="Missing Tenant Email")
    else:
        frappe.log("No unpaid contracts found for rent reminders.")
else:
    frappe.log("Rent reminders are disabled in Rent Settings.")