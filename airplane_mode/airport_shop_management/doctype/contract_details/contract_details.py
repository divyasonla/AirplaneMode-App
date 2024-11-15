# Copyright (c) 2024, divya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ContractDetails(Document):
    def before_insert(self):

        self.rent_amount = frappe.db.get_single_value('Rent Setting', 'rent_amount')