# FCompositeSection

Section data for each track. Reference of data will be stored in the child class for the way they want
  AnimComposite vs AnimMontage have different requirement for the actual data reference
  This only contains composite section information. (vertical sequences)

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SectionName | `FName` | Section Name |
| StartTime_DEPRECATED | `float` | Start Time |
| NextSectionName | `FName` | Should this animation loop. |
| MetaData | `TArray < UAnimMetaData * >` | Meta data that can be saved with the asset<br><br>	  You can query by GetMetaData function |
