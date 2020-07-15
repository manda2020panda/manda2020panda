<?php
/**
 * TimeInForce
 *
 * PHP version 5
 *
 * @category Class
 * @package  com.blockchain.exchange.rest
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */

/**
 * Blockchain.com Exchange REST API
 *
 * ## Introduction Welcome to Blockchain.com's Exchange API and developer documentation. \\ These documents detail and give examples of various functionality offered by the API such as receiving real time market data, requesting balance information and performing trades. ## To Get Started Create or log into your existing Blockchain.com Exchange account \\ Select API from the drop down menu \\ Fill out form and click “Create New API Key Now” \\ Once generated you can view your keys under API Settings. \\ Please be aware that the API key can only be used once it was verified via email.  The API key must be set via the \\ `X-API-Token`\\ header.  The base URL to be used for all calls is \\ `https://api.blockchain.com/v3/exchange`  Autogenerated clients for this API can be found [here](https://github.com/blockchain/lib-exchange-client).
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 * Generated by: https://openapi-generator.tech
 * OpenAPI Generator version: 4.3.1
 */

/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

namespace com.blockchain.exchange.rest\com.blockchain.exchange.rest.model;
use \com.blockchain.exchange.rest\ObjectSerializer;

/**
 * TimeInForce Class Doc Comment
 *
 * @category Class
 * @description \&quot;GTC\&quot; for Good Till Cancel, \&quot;IOC\&quot; for Immediate or Cancel, \&quot;FOK\&quot; for Fill or Kill, \&quot;GTD\&quot; Good Till Date
 * @package  com.blockchain.exchange.rest
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */
class TimeInForce
{
    /**
     * Possible values of this enum
     */
    const GTC = 'GTC';
    const IOC = 'IOC';
    const FOK = 'FOK';
    const GTD = 'GTD';
    
    /**
     * Gets allowable values of the enum
     * @return string[]
     */
    public static function getAllowableEnumValues()
    {
        return [
            self::GTC,
            self::IOC,
            self::FOK,
            self::GTD,
        ];
    }
}


