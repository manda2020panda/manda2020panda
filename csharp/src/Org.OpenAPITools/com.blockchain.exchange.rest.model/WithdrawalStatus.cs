/* 
 * Blockchain.com Exchange REST API
 *
 * ## Introduction Welcome to Blockchain.com's Exchange API and developer documentation. \\ These documents detail and give examples of various functionality offered by the API such as receiving real time market data, requesting balance information and performing trades. ## To Get Started Create or log into your existing Blockchain.com Exchange account \\ Select API from the drop down menu \\ Fill out form and click “Create New API Key Now” \\ Once generated you can view your keys under API Settings. \\ Please be aware that the API key can only be used once it was verified via email.  The API key must be set via the \\ `X-API-Token`\\ header.  The base URL to be used for all calls is \\ `https://api.blockchain.com/v3/exchange`  Autogenerated clients for this API can be found [here](https://github.com/blockchain/lib-exchange-client). 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.com.blockchain.exchange.rest.model
{
    /// <summary>
    /// Defines WithdrawalStatus
    /// </summary>
    
    [JsonConverter(typeof(StringEnumConverter))]
    
    public enum WithdrawalStatus
    {
        /// <summary>
        /// Enum REJECTED for value: REJECTED
        /// </summary>
        [EnumMember(Value = "REJECTED")]
        REJECTED = 1,

        /// <summary>
        /// Enum PENDING for value: PENDING
        /// </summary>
        [EnumMember(Value = "PENDING")]
        PENDING = 2,

        /// <summary>
        /// Enum REFUNDED for value: REFUNDED
        /// </summary>
        [EnumMember(Value = "REFUNDED")]
        REFUNDED = 3,

        /// <summary>
        /// Enum FAILED for value: FAILED
        /// </summary>
        [EnumMember(Value = "FAILED")]
        FAILED = 4,

        /// <summary>
        /// Enum COMPLETED for value: COMPLETED
        /// </summary>
        [EnumMember(Value = "COMPLETED")]
        COMPLETED = 5

    }

}
