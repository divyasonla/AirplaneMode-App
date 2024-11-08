# Copyright (c) 2024, divya and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    # columns[],data[]
    # return columns,data
    columns = [{
        "fieldname": "airline",
        "label": "Airline",
        "fieldtype": "Link",
        "options": "Airline"
    }, {
        "fieldname": "revenue",
        "label": "Revenue",
        "fieldtype": "Currency"
    }]
    
    airlines = frappe.get_all("Airline", fields=["name"])
    data = []
    
    for airline in airlines:
        tickets = frappe.get_all(
            'Airplane Ticket',
            filters={'flight': ['like', f"{airline['name']}-%"]},
            fields=['total_amount']
        )
        
        revenue = sum(ticket['total_amount'] for ticket in tickets)

        data.append({
            "airline": airline['name'],
            "revenue": revenue
        })
        data.sort(key=lambda x: x['revenue'], reverse=True)
    chart = {
        "data": {
            "labels": [entry['airline'] for entry in data],
            "datasets": [{
                "values": [entry['revenue'] for entry in data]
            }],
        },
        "type": "donut",
        "colors": ['#7cd6fd', '#743ee2']
    }
    
    total_revenue = sum(d['revenue'] for d in data)

    report_summary = [{
        "value": total_revenue,
        "indicator": "Green" if total_revenue > 0 else "Red",
        "label": "Total Revenue",
        "datatype": "Currency",
        "currency": "INR"
    }]

    return columns, data,total_revenue ,chart,report_summary
    
