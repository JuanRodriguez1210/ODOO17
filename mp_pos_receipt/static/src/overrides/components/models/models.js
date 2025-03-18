/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";

patch(Order.prototype, {

     /**
     * Add info of partner in case of reprint
     *
     * @override
     */
    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        if (this.get_partner() && !result.headerData.partner) {
            result.partner = this.get_partner();
            result.headerData.partner =  this.get_partner();
        }
        return result;
    },

});