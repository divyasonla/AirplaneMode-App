# Copyright (c) 2024, divya and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

# import frappe
# from frappe import _

# def execute(filters=None):
#     columns = [
#         {"fieldname": "airport", "label": _("Airport"), "fieldtype": "Data", "width": 150},
#         {"fieldname": "available_shops", "label": _("Available Shops"), "fieldtype": "Int", "width": 120},
#         {"fieldname": "occupied_shops", "label": _("Occupied Shops"), "fieldtype": "Int", "width": 120},
#     ]
    
#     data = []
#     airports = frappe.get_all("Shop", fields=["airport"], distinct=True)
    
#     for airport in airports:
#         available_count = frappe.db.count("Shop", {
#             "airport": airport["airport"],
#             "status": "Available"
#         })
#         occupied_count = frappe.db.count("Shop", {
#             "airport": airport["airport"],
#             "status": "Occupied"
#         })
#         data.append({
#             "airport": airport["airport"],
#             "available_shops": available_count,
#             "occupied_shops": occupied_count
#         })
    
#     return columns, data

import frappe
from frappe import _

def execute(filters=None):

    columns = [
        {"fieldname": "airport", "label": _("Airport"), "fieldtype": "Data", "width": 200},
        {"fieldname": "total_shops", "label": _("Total Shops"), "fieldtype": "Int", "width": 150},
        {"fieldname": "available_shops", "label": _("Available Shops"), "fieldtype": "Int", "width": 150},
        {"fieldname": "occupied_shops", "label": _("Occupied Shops"), "fieldtype": "Int", "width": 150},
    ]
    
    data = []
    total_available_shops = 0
    total_occupied_shops = 0
    total_shops = 0
    airports = frappe.get_all("Shop", fields=["airport"], distinct=True)
    
    for airport in airports:
        total_count = frappe.db.count("Shop", {
            "airport": airport["airport"]
        })
        
        available_count = frappe.db.count("Shop", {
            "airport": airport["airport"],
            "status": "Available"
        })
        
        occupied_count = frappe.db.count("Shop", {
            "airport": airport["airport"],
            "status": "Occupied"
        })
        total_available_shops += available_count
        total_occupied_shops += occupied_count
        total_shops += available_count + occupied_count
        
        data.append({
            "airport": airport["airport"],
            "total_shops": total_count,
            "available_shops": available_count,
            "occupied_shops": occupied_count
        })
    
    chart = {
        "data": {
            "labels": [d["airport"] for d in data],
            "datasets": [
                {"name": _("Available Shops"), "values": [d["available_shops"] for d in data]},
                {"name": _("Occupied Shops"), "values": [d["occupied_shops"] for d in data]}
            ]
        },
        "type": "bar",
        "colors": ["#34c38f", "#f46a6a"],
        "fieldtype": "Int"
    }
    report_summary = [
        {
            "value": total_shops,
            "indicator": "Green" if total_shops > 0 else "Red",
            "label": _("Total Shops"),
            "datatype": "Int"
        },
        {
            "value": total_available_shops,
            "indicator": "Green" if total_available_shops > 0 else "Red",
            "label": _("Available Shops"),
            "datatype": "Int"
        },
        {
            "value": total_occupied_shops,
            "indicator": "Red" if total_occupied_shops > 0 else "Green",
            "label": _("Occupied Shops"),
            "datatype": "Int"
        }
    ]
    
    return columns, data, None, chart,report_summary