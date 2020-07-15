/**
 * Blockchain.com Exchange REST API
 * ## Introduction Welcome to Blockchain.com's Exchange API and developer documentation. \\ These documents detail and give examples of various functionality offered by the API such as receiving real time market data, requesting balance information and performing trades. ## To Get Started Create or log into your existing Blockchain.com Exchange account \\ Select API from the drop down menu \\ Fill out form and click “Create New API Key Now” \\ Once generated you can view your keys under API Settings. \\ Please be aware that the API key can only be used once it was verified via email.  The API key must be set via the \\ `X-API-Token`\\ header.  The base URL to be used for all calls is \\ `https://api.blockchain.com/v3/exchange`  Autogenerated clients for this API can be found [here](https://github.com/blockchain/lib-exchange-client). 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DepositAddressCrypto model module.
 * @module com.blockchain.exchange.rest/com.blockchain.exchange.rest.model/DepositAddressCrypto
 * @version 1.0.0
 */
class DepositAddressCrypto {
    /**
     * Constructs a new <code>DepositAddressCrypto</code>.
     * @alias module:com.blockchain.exchange.rest/com.blockchain.exchange.rest.model/DepositAddressCrypto
     * @param type {String} 
     * @param address {String} Address to deposit to. If a tag or memo must be used, it is separated by a colon.
     */
    constructor(type, address) { 
        
        DepositAddressCrypto.initialize(this, type, address);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type, address) { 
        obj['type'] = type;
        obj['address'] = address;
    }

    /**
     * Constructs a <code>DepositAddressCrypto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:com.blockchain.exchange.rest/com.blockchain.exchange.rest.model/DepositAddressCrypto} obj Optional instance to populate.
     * @return {module:com.blockchain.exchange.rest/com.blockchain.exchange.rest.model/DepositAddressCrypto} The populated <code>DepositAddressCrypto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DepositAddressCrypto();

            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {String} type
 */
DepositAddressCrypto.prototype['type'] = undefined;

/**
 * Address to deposit to. If a tag or memo must be used, it is separated by a colon.
 * @member {String} address
 */
DepositAddressCrypto.prototype['address'] = undefined;






export default DepositAddressCrypto;

