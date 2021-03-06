# -*- encoding: utf-8 -*-
#################################################################################
#
#    Copyright (C) 2010  Renato Lima - Akretion
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU  Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    'name': 'Account Fiscal Position Rule Stock',
    'version': '1.1',
    'category': 'Generic Modules/Accounting',
    'description': """Include a rule to decide the correct fiscal position for Stock""",
    'license': 'AGPL-3',
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': [
                'account', 
                'sale',
                'purchase'
                ],
    'init_xml': [],
    'update_xml': 
                [
                'stock_view.xml',
                'security/account_fiscal_position_rule_security.xml',
                'security/ir.model.access.csv',
                ],
    'demo_xml': [],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
