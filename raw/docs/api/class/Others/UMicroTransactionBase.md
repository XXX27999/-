# UMicroTransactionBase

## Parents

- [UPlatformInterfaceBase](./UPlatformInterfaceBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AvailableProducts | `TArray < struct FPurchaseInfo >` | The list of products available to purchase, filled out by the time a MTD_PurchaseQueryComplete is fired |
| LastError | `FString` | In case of errors, this will describe the most recent error |
| LastErrorSolution | `FString` | In case of errors, this will describe possible solutions (if there are any) |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
