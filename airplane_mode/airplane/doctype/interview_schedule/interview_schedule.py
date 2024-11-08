# Copyright (c) 2024, divya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class InterviewSchedule(Document):
    def validate(self):
        if self.interview_date and self.interview_date < nowdate():
            frappe.throw("Due Date cannot be in the past")

    def before_submit(self):
        if self.status != 'Hired' :
            frappe.throw('your status is not hired ')
         