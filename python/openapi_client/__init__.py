# coding: utf-8

# flake8: noqa

"""
    Blockchain.com Exchange REST API

    ## Introduction Welcome to Blockchain.com's Exchange API and developer documentation. \\ These documents detail and give examples of various functionality offered by the API such as receiving real time market data, requesting balance information and performing trades. ## To Get Started Create or log into your existing Blockchain.com Exchange account \\ Select API from the drop down menu \\ Fill out form and click “Create New API Key Now” \\ Once generated you can view your keys under API Settings. \\ Please be aware that the API key can only be used once it was verified via email.  The API key must be set via the \\ `X-API-Token`\\ header.  The base URL to be used for all calls is \\ `https://api.blockchain.com/v3/exchange`  Autogenerated clients for this API can be found [here](https://github.com/blockchain/lib-exchange-client).   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from com.blockchain.exchange.rest.api.payments_api import PaymentsApi
from com.blockchain.exchange.rest.api.trading_api import TradingApi
from com.blockchain.exchange.rest.api.unauthenticated_api import UnauthenticatedApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.com.blockchain.exchange.rest.model.balance import Balance
from openapi_client.com.blockchain.exchange.rest.model.balance_map import BalanceMap
from openapi_client.com.blockchain.exchange.rest.model.base_order import BaseOrder
from openapi_client.com.blockchain.exchange.rest.model.cancel_order_request import CancelOrderRequest
from openapi_client.com.blockchain.exchange.rest.model.create_withdrawal_request import CreateWithdrawalRequest
from openapi_client.com.blockchain.exchange.rest.model.deposit_address_crypto import DepositAddressCrypto
from openapi_client.com.blockchain.exchange.rest.model.deposit_info import DepositInfo
from openapi_client.com.blockchain.exchange.rest.model.fees import Fees
from openapi_client.com.blockchain.exchange.rest.model.ord_type import OrdType
from openapi_client.com.blockchain.exchange.rest.model.order_book import OrderBook
from openapi_client.com.blockchain.exchange.rest.model.order_book_entry import OrderBookEntry
from openapi_client.com.blockchain.exchange.rest.model.order_status import OrderStatus
from openapi_client.com.blockchain.exchange.rest.model.order_summary import OrderSummary
from openapi_client.com.blockchain.exchange.rest.model.price_event import PriceEvent
from openapi_client.com.blockchain.exchange.rest.model.price_event_list import PriceEventList
from openapi_client.com.blockchain.exchange.rest.model.side import Side
from openapi_client.com.blockchain.exchange.rest.model.symbol_status import SymbolStatus
from openapi_client.com.blockchain.exchange.rest.model.time_in_force import TimeInForce
from openapi_client.com.blockchain.exchange.rest.model.time_in_force_stop import TimeInForceStop
from openapi_client.com.blockchain.exchange.rest.model.unauthorized_error import UnauthorizedError
from openapi_client.com.blockchain.exchange.rest.model.whitelist_entry import WhitelistEntry
from openapi_client.com.blockchain.exchange.rest.model.withdrawal_info import WithdrawalInfo
from openapi_client.com.blockchain.exchange.rest.model.withdrawal_status import WithdrawalStatus

