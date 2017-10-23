from openerp.osv import osv,fields
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from odoo import models, fields, api


class res_users(osv.osv):
    
    _inherit = 'res.users'

    # _columns = {
    #     'calendear_localisation' : fields.selection([('ar','Arabic'),('fa','Farsi')],'Localisation'),
    # }
    calendear_localisation = fields.Selection([('ar','Arabic'),('fa','Farsi')],default='ar') 

    def get_calendear_localisation(self, cr, uid, fields=False, context=None):        
        user_brow_obj = self.pool.get('res.users').browse(cr,uid,uid,context=context)
        res_lang_obj = self.pool.get('res.lang')
        lang_ids = res_lang_obj.search(cr,uid,[('code','=',user_brow_obj.lang)])
        date_format = '%m/%d/%Y'
        if lang_ids:
             date_format = res_lang_obj.browse(cr,uid,lang_ids[0],context).date_format        
        return {
            'lang':self.browse(cr,uid,uid,context).calendear_localisation or '',
            'date_format': date_format
        }
    
    