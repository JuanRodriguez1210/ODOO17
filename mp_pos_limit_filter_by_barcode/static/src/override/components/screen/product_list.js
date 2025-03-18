/** @odoo-module */
import { ProductsWidget } from "@point_of_sale/app/screens/product_screen/product_list/product_list";
import { patch } from "@web/core/utils/patch";

patch(ProductsWidget.prototype, {
    setup() {
        super.setup();
    },
    //cargar productos en buscar más
    async loadProductFromDB() {
        const { searchProductWord } = this.pos;
        if (!searchProductWord) {
            return;
        }

        try {
            var domain = ["&",
                        ["available_in_pos", "=", true]]
            var fields_to_filter = this.pos.config.fields_to_filter_pos
            var barcode = fields_to_filter.includes('barcode');
            var name = fields_to_filter.includes('name');
            var reference = fields_to_filter.includes('reference');
            if(fields_to_filter.length == 0 || fields_to_filter.length == 3)
            {
                domain.push("|")
                domain.push("|")
            }
            if(fields_to_filter.length == 2 )
            {
                domain.push("|")
            }
            if (barcode ||  fields_to_filter.length == 0)
            {
                domain.push(["barcode", "ilike", searchProductWord])

            }
             if (name || fields_to_filter.length == 0)
            {
                domain.push(["name", "ilike", searchProductWord])
            }
             if (reference ||  fields_to_filter.length == 0)
            {
                domain.push(["default_code", "ilike", searchProductWord])
            }

            const limit = 30;
            const ProductIds = await this.orm.call(
                "product.product",
                "search",
                [
                    domain,
                ],
                {
                    offset: this.state.currentOffset,
                    limit: limit,
                }
            );
            if (ProductIds.length) {
                await this.pos._addProducts(ProductIds, false);
            }
            this.updateProductList();
            return ProductIds;
        } catch (error) {
            if (error instanceof ConnectionLostError || error instanceof ConnectionAbortedError) {
                return this.popup.add(OfflineErrorPopup, {
                    title: _t("Network Error"),
                    body: _t(
                        "Product is not loaded. Tried loading the product from the server but there is a network error."
                    ),
                });
            } else {
                throw error;
            }
        }
    }

});