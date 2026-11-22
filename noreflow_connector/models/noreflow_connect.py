from urllib.parse import urlencode, urlsplit

from odoo import api, fields, models

NOREFLOW_APP = "https://noreflow.net"


class NoreflowConnect(models.TransientModel):
    """Opens Noreflow with this Odoo's address and database filled in.

    Nothing is sent to Noreflow from Odoo: the administrator signs in to Noreflow and pastes an API key they create in
    Odoo (My Profile > Account Security > New API Key). Noreflow then writes its sales to this Odoo as customer
    invoices and registers the payments.
    """

    _name = "noreflow.connect"
    _description = "Connect to Noreflow"

    odoo_url = fields.Char(string="Odoo address", readonly=True, default=lambda self: self._default_odoo_url())
    database = fields.Char(string="Database", readonly=True, default=lambda self: self.env.cr.dbname)

    @api.model
    def _default_odoo_url(self):
        base = self.get_base_url() or ""
        parts = urlsplit(base)
        return parts.netloc or base

    def action_open_noreflow(self):
        self.ensure_one()
        query = urlencode({"odoo_url": self.odoo_url or "", "odoo_db": self.database or ""})
        return {
            "type": "ir.actions.act_url",
            "url": f"{NOREFLOW_APP}/reports?{query}",
            "target": "new",
        }

    def action_open_api_keys(self):
        """The current user's preferences, where Odoo creates API keys (Account Security tab)."""
        return self.env.user.action_get()
