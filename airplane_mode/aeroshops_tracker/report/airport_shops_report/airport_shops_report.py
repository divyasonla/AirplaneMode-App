# Copyright (c) 2024, divya and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    # Fetch the shop data grouped by airport
    shops = frappe.db.sql("""
        SELECT airport, COUNT(*) as number_of_shops, SUM(CASE WHEN status = 'Available' THEN 1 ELSE 0 END) as available_shops
        FROM `tabShop`
        GROUP BY airport
    """, as_dict=True)

    return shops