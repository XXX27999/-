# FNavigationLinkBase

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LeftProjectHeight | `float` | if greater than 0 nav system will attempt to project navlink's start point on geometry below |
| MaxFallDownLength | `float` | if greater than 0 nav system will attempt to project navlink's end point on geometry below |
| Direction | `TEnumAsByte < ENavLinkDirection :: Type >` |  |
| SnapRadius | `float` |  |
| SnapHeight | `float` |  |
| SupportedAgents | [FNavAgentSelector](./FNavAgentSelector.md) | restrict area only to specified agents |
| bSupportsAgent0 | `uint32` |  |
| bSupportsAgent1 | `uint32` |  |
| bSupportsAgent2 | `uint32` |  |
| bSupportsAgent3 | `uint32` |  |
| bSupportsAgent4 | `uint32` |  |
| bSupportsAgent5 | `uint32` |  |
| bSupportsAgent6 | `uint32` |  |
| bSupportsAgent7 | `uint32` |  |
| bSupportsAgent8 | `uint32` |  |
| bSupportsAgent9 | `uint32` |  |
| bSupportsAgent10 | `uint32` |  |
| bSupportsAgent11 | `uint32` |  |
| bSupportsAgent12 | `uint32` |  |
| bSupportsAgent13 | `uint32` |  |
| bSupportsAgent14 | `uint32` |  |
| bSupportsAgent15 | `uint32` |  |
| bUseSnapHeight | `uint32` |  |
| bSnapToCheapestArea | `uint32` | If set, link will try to snap to cheapest area in given radius |
| bCustomFlag0 | `uint32` | custom flag, check DescribeCustomFlags for details |
| bCustomFlag1 | `uint32` | custom flag, check DescribeCustomFlags for details |
| bCustomFlag2 | `uint32` | custom flag, check DescribeCustomFlags for details |
| bCustomFlag3 | `uint32` | custom flag, check DescribeCustomFlags for details |
| bCustomFlag4 | `uint32` | custom flag, check DescribeCustomFlags for details |
| bCustomFlag5 | `uint32` | custom flag, check DescribeCustomFlags for details |
| bCustomFlag6 | `uint32` | custom flag, check DescribeCustomFlags for details |
| bCustomFlag7 | `uint32` | custom flag, check DescribeCustomFlags for details |
| AreaClass | `TSubclassOf < UNavArea >` | Area type of this link (empty = default) |
| Description | `FString` | this is an editor-only property to put descriptions in navlinks setup, to be able to identify it easier |
