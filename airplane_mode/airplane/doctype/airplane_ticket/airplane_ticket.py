# Copyright (c) 2024, divya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
    def validate(self):
        self.total_price = 0
        self.seen_on = set()
        
        for i in self.add_ons:
            if i.item in self.seen_on:
                
                frappe.throw(f"This {i.item} hello already exists!")  
            self.seen_on.add(i.item)
            self.total_price += i.amount 
        
        self.total_amount = self.total_price + self.flight_price


    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Your ticket status is not 'Boarded', so you can't submit your ticket!")
            
    
    def before_insert(self):
        random_integer = random.randint(1, 100)
        random_alphabet = random.choice(["A", "B", "C", "D", "E"])
        
        self.seat = f"{random_integer}{random_alphabet}"
   
    def on_update(self):
        self.capacity()


    def capacity(self):
        if self.flight:
            ticket_count = frappe.db.count("Airplane Ticket", 
                                       filters={"flight": self.flight, 
                                                "name": ("!=", self.name) if self.name else None})

            flight = frappe.get_doc("Airplane Flight", self.flight)
        if flight:
            airplane = frappe.get_doc("Airplane", flight.airplane)
            if ticket_count >= airplane.capacity:
                frappe.throw("Number of tickets exceeds or equals airplane capacity. Cannot create Airplane Ticket.")
        
