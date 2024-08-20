from enum import Enum

import polars as pl

DEFAULT_FOCUS_NAMESPACE = "F"


class FocusColumnNames(Enum):
    """
    Focus column names as described in https://focus.finops.org/#specification
    """

    PLACE_HOLDER = "PlaceHolder"

    AVAILABILITY_ZONE = "AvailabilityZone"
    BILLED_COST = "BilledCost"
    BILLING_ACCOUNT_ID = "BillingAccountId"
    BILLING_ACCOUNT_NAME = "BillingAccountName"
    BILLING_CURRENCY = "BillingCurrency"
    BILLING_PERIOD_END = "BillingPeriodEnd"
    BILLING_PERIOD_START = "BillingPeriodStart"
    CHARGE_CATEGORY = "ChargeCategory"
    CHARGE_CLASS = "ChargeClass"
    CHARGE_DESCRIPTION = "ChargeDescription"
    CHARGE_FREQUENCY = "ChargeFrequency"
    CHARGE_PERIOD_END = "ChargePeriodEnd"
    CHARGE_PERIOD_START = "ChargePeriodStart"
    COMMITMENT_DISCOUNT_CATEGORY = "CommitmentDiscountCategory"
    COMMITMENT_DISCOUNT_ID = "CommitmentDiscountId"
    COMMITMENT_DISCOUNT_NAME = "CommitmentDiscountName"
    COMMITMENT_DISCOUNT_STATUS = "CommitmentDiscountStatus"
    COMMITMENT_DISCOUNT_TYPE = "CommitmentDiscountType"
    CONSUMED_QUANTITY = "ConsumedQuantity"
    CONSUMED_UNIT = "ConsumedUnit"
    CONTRACTED_COST = "ContractedCost"
    CONTRACTED_UNIT_PRICE = "ContractedUnitPrice"
    EFFECTIVE_COST = "EffectiveCost"
    INVOICE_ISSUER_NAME = "InvoiceIssuerName"
    LIST_COST = "ListCost"
    LIST_UNIT_PRICE = "ListUnitPrice"
    PRICING_CATEGORY = "PricingCategory"
    PRICING_QUANTITY = "PricingQuantity"
    PRICING_UNIT = "PricingUnit"
    PROVIDER_NAME = "ProviderName"
    PUBLISHER_NAME = "PublisherName"
    REGION = "RegionId"
    REGION_NAME = "RegionName"
    RESOURCE_ID = "ResourceId"
    RESOURCE_NAME = "ResourceName"
    RESOURCE_TYPE = "ResourceType"
    SERVICE_CATEGORY = "ServiceCategory"
    SERVICE_NAME = "ServiceName"
    SKU_ID = "SkuId"
    SKU_PRICE_ID = "SkuPriceId"
    SUB_ACCOUNT_ID = "SubAccountId"
    SUB_ACCOUNT_NAME = "SubAccountName"
    TAGS = "Tags"
    x_CostCategories = "x_CostCategories"
    x_Discount = "x_Discount"
    x_Operation = "x_Operation"
    x_ServiceCode = "x_ServiceCode"
    x_UsageType = "x_UsageType"

FOCUS_DATETIME_ISO_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_dtype_for_focus_column_name(focus_column_name: FocusColumnNames):
    """
    Return the dtype for the focus column name
    """

    # convert loop to match statements
    if focus_column_name == FocusColumnNames.PLACE_HOLDER:
        raise ValueError("PLACE_HOLDER is not a valid focus column name")
    elif (
        focus_column_name == FocusColumnNames.CHARGE_PERIOD_START
        or focus_column_name == FocusColumnNames.CHARGE_PERIOD_END
        or focus_column_name == FocusColumnNames.BILLING_PERIOD_START
        or focus_column_name == FocusColumnNames.BILLING_PERIOD_END
    ):
        return pl.Datetime
    elif (
        focus_column_name == FocusColumnNames.BILLED_COST
        or focus_column_name == FocusColumnNames.EFFECTIVE_COST
        or focus_column_name == FocusColumnNames.LIST_COST
        or focus_column_name == FocusColumnNames.LIST_UNIT_PRICE
        or focus_column_name == FocusColumnNames.PRICING_QUANTITY
        or focus_column_name == FocusColumnNames.CONSUMED_QUANTITY
        or focus_column_name == FocusColumnNames.CONTRACTED_COST
        or focus_column_name == FocusColumnNames.CONTRACTED_UNIT_PRICE
    ):
        return pl.Float64
    else:
        return pl.Utf8
