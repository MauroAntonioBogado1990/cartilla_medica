# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ExeReporte(models.Model):
    _inherit = 'res.partner'