# Copyright (c) 2024, divya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ContractDetails(Document):
    def before_insert(self):
      
        # if self.shop_setting:
        #     # Fetch the rent_amount from the Shop Setting DocType
        #     rent_amount = frappe.db.get_value("Shop Setting", self.shop_setting, "rent_amount")
        #     if rent_amount:
        #         self.rent_amount = rent_amount
        if not self.rent_amount:
            self.rent_amount = frappe.db.get_single_value('Shop Settings', 'rent_amount')