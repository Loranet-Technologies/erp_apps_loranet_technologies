
__version__ = '0.0.1'

import frappe

@frappe.whitelist(allow_guest=True) 
def get_user_list():
    user = frappe.get_all('User')
    obj = []
    for x in user:
          o = frappe.get_doc('User',x)
          print('\nemail:',x.name)
          # print(o.phone)
          a = {
            'email': x.name,
            'phone': o.phone
          }
          obj.append(a)
    return obj
