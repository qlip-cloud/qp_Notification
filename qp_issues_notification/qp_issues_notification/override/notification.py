import frappe
from frappe.email.doctype.notification.notification import Notification

class CustomNotification(Notification):
    def get_list_of_recipients(self, doc, context):
        print("Esta pasando por la herencia!!!!!!!!!!!!")

        if doc.customer:  # Verificar si hay un cliente seleccionado
            band_name = self.get_band(doc)
            receiver_list = self.get_email(band_name)
        else:
            print("No se seleccionó un cliente, no se enviará ninguna notificación")

            # Si no se seleccionó un cliente, simplemente devuelve una lista vacía de destinatarios.
            receiver_list = []

        return receiver_list, [], []

    def get_band(self, doc):
        print("Se ejecuta la lógica de buscar los destinatarios según banda", doc.customer)

        # TODO: Programar la lógica solicitada

        banda = ""

        if doc.customer:
            banda = frappe.db.get_value('Customer', doc.customer, 'qp_noti_band')

            print("Esta es la banda que vamos a usar para buscar los contactos --->", banda)

        return banda

    def get_email(self, band_name):
        print("Se ejecuta la lógica de buscar los emails de los destinatarios", band_name)

        # TODO: Programar la lógica solicitada

        emails = frappe.db.get_list('Contact', filters={'qp_noti_band': band_name}, fields=['email_id'], order_by='email_id')

        email_list = [email['email_id'] for email in emails]

        print("Estos son los emails a los cuales se les enviará la notificación --->", email_list)

        return email_list


    
    
        

