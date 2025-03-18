/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { PosDB } from "@point_of_sale/app/store/db";
patch(PosDB.prototype, {

     constructor(options) {
       super.constructor(options);
    },
    //Agrega los campos para filtro de los productos, según lo seleccionado en el campo de configuración del pos
    // Si no tiene nada, agrega todos.
   _product_search_string(product) {
        var str = "";
        var barcode = product.pos.config.fields_to_filter_pos.includes('barcode');
        if (product.barcode && (barcode ||  product.pos.config.fields_to_filter_pos.length == 0)) {
            str += "|" + product.barcode;
        }
        var name = product.pos.config.fields_to_filter_pos.includes('name');
        if (name || product.pos.config.fields_to_filter_pos.length == 0) {
            str += "|" + product.display_name;
        }
        var reference = product.pos.config.fields_to_filter_pos.includes('reference');
        if (reference || product.pos.config.fields_to_filter_pos.length == 0){
             if (product.default_code) {
            str += "|" + product.default_code;
        }
        }
        str = product.id + ":" + str.replace(/[\n:]/g, "") + "\n";
        return str;
    }
});