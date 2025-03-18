/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";

patch(Order.prototype, {
    // @override
    // Agrega la info de facturas en las ordenes ya pgadas, al prinicipio demora un poco en imprimir el primer ticket, pero luego todo  va bien.
    setup() {
        super.setup(...arguments);
        this.get_invoice(this.account_move);        
    },

     /**
     * Add info of fe
     *
     * @override
     */
    export_for_printing() {
        const result = super.export_for_printing(...arguments);        
        if(this.invoice_info){
            result['headerData']['invoice_info'] = this.invoice_info;
            result['invoice_info'] = this.invoice_info;
            if (this.invoice_info['qr']){
                result['Qr_code_fe'] = "data:image/png;base64," +  this.invoice_info['qr'];    
            }
            
        }
        result['trackingNumber'] = this.trackingNumber;
        result['bigTrackingNumber'] = false;
        
        return result;
    },

    //consulta información de la factura relacionada con la orden    
    async get_invoice(account_move_id)
    {
        var self = this;
        if (self.account_move || account_move_id){
            let invoice = await  self.pos.orm.call ('pos.order','get_invoice_info', [self.id, account_move_id]);
            if(invoice)
            {
                this.invoice_info = invoice;
            }
          }            

    }
});