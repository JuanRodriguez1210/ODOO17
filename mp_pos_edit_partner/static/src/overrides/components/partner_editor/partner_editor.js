/** @odoo-module */

import { PartnerDetailsEdit } from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import { patch } from "@web/core/utils/patch";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";


patch(PartnerDetailsEdit.prototype, {
    setup(){
        super.setup(...arguments);

        },

    //Valida campos obligatorios (vat,mobile)
     saveChanges() {
        const processedChanges = {};
        for (const [key, value] of Object.entries(this.changes)) {
            if (this.intFields.includes(key)) {
                processedChanges[key] = parseInt(value) || false;
            } else {
                processedChanges[key] = value;
            }
        }
         if ((!this.props.partner.vat && !processedChanges.vat) || processedChanges.vat === "") {
            return this.popup.add(ErrorPopup, {
                title: ("El Numero de identificación es obligatorio"),
            });
        }

         if ((!this.props.partner.email && !processedChanges.email) || processedChanges.email === "") {
            return this.popup.add(ErrorPopup, {
                title: ("El correo electrónico es obligatorio"),
            });
        }
         super.saveChanges(...arguments);

     },
});