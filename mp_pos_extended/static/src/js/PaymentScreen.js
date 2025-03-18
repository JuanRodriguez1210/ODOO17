/** @odoo-module **/

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

patch(PaymentScreen.prototype, {
    async _isOrderValid(isForceValidate) {
        const result = await super._isOrderValid(...arguments);
        var amount_pos = 0
        const order = this.currentOrder;
        const mainPayment = order.get_paymentlines()[0];
        const mainPayment2 = order.get_paymentlines();

        const remainingLines = this.getRemainingOnlinePaymentLines();
        let remainingAmount = 0;
        let amount = 0;
        for (const line of remainingLines) {
            amount = line.get_amount();
            console.log(amount)
            remainingAmount += amount;
        }

        console.log(amount)
        if (
            mainPayment.amount >= order.pos.config.value_limit_uvt_ticket && !order.is_to_invoice()
        ) {
            console.log("Hay error")
            const result =  this.popup.add(ErrorPopup, {
                title: ('Error al validar Total de UVT'),
                body: ('El valor supera el limite de UVT permitidos para la venta de tipo Ticket'),
            });
            
            return false;
            }

        return result;
    },
});

