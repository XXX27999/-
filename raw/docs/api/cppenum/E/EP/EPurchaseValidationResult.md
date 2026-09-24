# EPurchaseValidationResult

## Values

| Name | Value | Description |
| --- | --- | --- |
| Valid | 0 | 合规 |
| InvalidPrice | 1 | 传入购买价格不对 |
| NotSelling | 2 | 商品未在售卖状态 |
| ReachLimit | 3 | 商品购买次数达到限购上限 |
| NoPrivilege | 4 | 没有购买商品的绿洲特权 |
| InvalidCurrencyType | 5 | ServerBuyProduct传入的商品为绿洲币商品 |
| Canceled | 6 | 取消购买 |
| Other | 100 | 其他错误 |
