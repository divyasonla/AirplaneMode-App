import frappe
from frappe.utils import getdate, nowdate

def send_rent_reminders():
    shops = frappe.get_all("Shop", filters={"status": "Occupied"})
    settings = frappe.get_single("Shop Settings")

    if settings.enable_rent_reminders:
        for shop in shops:
            tenant_email = frappe.db.get_value("Tenant", shop.tenant, "email")  # Assuming you have a Tenant DocType
            rent_due_date = getdate(shop.due_date)  # Assuming you store due date in Shop DocType
            if rent_due_date <= nowdate():
                frappe.sendmail(recipients=tenant_email, subject="Rent Reminder", message="Your rent is due!")
