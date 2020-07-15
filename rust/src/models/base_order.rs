/*
 * Blockchain.com Exchange REST API
 *
 * ## Introduction Welcome to Blockchain.com's Exchange API and developer documentation. \\ These documents detail and give examples of various functionality offered by the API such as receiving real time market data, requesting balance information and performing trades. ## To Get Started Create or log into your existing Blockchain.com Exchange account \\ Select API from the drop down menu \\ Fill out form and click “Create New API Key Now” \\ Once generated you can view your keys under API Settings. \\ Please be aware that the API key can only be used once it was verified via email.  The API key must be set via the \\ `X-API-Token`\\ header.  The base URL to be used for all calls is \\ `https://api.blockchain.com/v3/exchange`  Autogenerated clients for this API can be found [here](https://github.com/blockchain/lib-exchange-client). 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct BaseOrder {
    /// Reference field provided by client. Cannot exceed 20 characters, only alphanumeric characters are allowed.
    #[serde(rename = "clOrdId")]
    pub cl_ord_id: String,
    #[serde(rename = "ordType")]
    pub ord_type: crate::models::OrdType,
    /// Blockchain symbol identifier
    #[serde(rename = "symbol")]
    pub symbol: String,
    #[serde(rename = "side")]
    pub side: crate::models::Side,
    /// The order size in the terms of the base currency
    #[serde(rename = "orderQty")]
    pub order_qty: f64,
    #[serde(rename = "timeInForce", skip_serializing_if = "Option::is_none")]
    pub time_in_force: Option<crate::models::TimeInForce>,
    /// The limit price for the order
    #[serde(rename = "price", skip_serializing_if = "Option::is_none")]
    pub price: Option<f64>,
    /// expiry date in the format YYYYMMDD
    #[serde(rename = "expireDate", skip_serializing_if = "Option::is_none")]
    pub expire_date: Option<i32>,
    /// The minimum quantity required for an IOC fill
    #[serde(rename = "minQty", skip_serializing_if = "Option::is_none")]
    pub min_qty: Option<f64>,
    /// The limit price for the order
    #[serde(rename = "stopPx", skip_serializing_if = "Option::is_none")]
    pub stop_px: Option<f64>,
}

impl BaseOrder {
    pub fn new(cl_ord_id: String, ord_type: crate::models::OrdType, symbol: String, side: crate::models::Side, order_qty: f64) -> BaseOrder {
        BaseOrder {
            cl_ord_id,
            ord_type,
            symbol,
            side,
            order_qty,
            time_in_force: None,
            price: None,
            expire_date: None,
            min_qty: None,
            stop_px: None,
        }
    }
}


