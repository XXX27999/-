# FGameplayTagContainer

A Tag Container holds a collection of FGameplayTags, tags are included explicitly by adding them, and implicitly from adding child tags

  一个容纳GameplayTag的集合，GameplayTag能够通过显式添加或者添加子标签隐式地包含进来

## Fields

| Name | Type | Description |
| --- | --- | --- |
| GameplayTags | `TArray < FGameplayTag >` | Array of gameplay tags<br>	 UGC<br>	  包含GameplayTag的数组 |
| ParentTags | `TArray < FGameplayTag >` | Array of expanded parent tags, in addition to GameplayTags. Used to accelerate parent searches. May contain duplicates in some cases<br>	 UGC<br>	  除 GameplayTags 之外的父级GameplayTag的数组，用于加速父级搜索。 可能包含重复项。 |
