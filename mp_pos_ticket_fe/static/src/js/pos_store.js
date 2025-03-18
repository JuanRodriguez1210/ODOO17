/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import {  qrCodeSrc } from "@point_of_sale/utils";
/* import { Order } from "@point_of_sale/app/store/models"; */
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    // @Override
    async _flush_orders(orders, options) {
        var self = this;
        var result = await super._flush_orders(...arguments);
        if (Array.isArray(result)) {
            for (let order of result) { // Cambiado de forEach a for...of
                let invoice_info = await this.get_order().get_invoice(order.account_move); // Ahora puedes usar await correctamente
                if(invoice_info)
                    {
                        this.get_order().invoice_number = invoice_info['invoice_number'];
                        this.get_order().invoice_info = invoice_info;
                        this.get_order().Qr_code = qrCodeSrc(invoice_info['qr']);
                        
                    }                
            }
        }
        return result
    },

    //agrega información adicional a los datos del encabezado
    getReceiptHeaderData(order) {
        const result = super.getReceiptHeaderData(...arguments);        
        if (order) {
            result.name = order.name;
            result.date = order.receiptDate;
            result.cashier = order.cashier;           
        }
        return result;
    },
});
