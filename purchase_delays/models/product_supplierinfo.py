# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, fields, models


class ProductSupplierinfo(models.Model):

    _inherit = "product.supplierinfo"

    delay = fields.Integer(
        string="Lead Time",
        compute="_compute_delay",
        inverse="_inverse_delay",
        readonly=True,
    )
    supplier_delay = fields.Integer(
        string="Supplier Lead Time", default=1, required=True
    )
    transport_delay = fields.Integer(
        string="Transport Lead Time", default=0, required=True
    )

    @api.depends("supplier_delay", "transport_delay")
    def _compute_delay(self):
        for record in self:
            record.delay = record.supplier_delay + record.transport_delay

    def _inverse_delay(self):
        for record in self:
            delay = record.delay
            record.write({"supplier_delay": delay, "transport_delay": 0})
