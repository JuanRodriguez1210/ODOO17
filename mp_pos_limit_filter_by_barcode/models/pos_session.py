from odoo import models, fields, api


class pos_session(models.Model):
     _inherit = 'pos.session'



     def _get_pos_ui_pos_config(self, params):
          res = super(pos_session,self)._get_pos_ui_pos_config(params)
          config_pos = res
          list_fields_to_filter = []
          for field in res['field_to_filter']:
              list_item = self.env['field.to.filter.pos'].search([('id','=',field)]).code
              list_fields_to_filter.append(list_item)
          res['fields_to_filter_pos'] = list_fields_to_filter
          return res