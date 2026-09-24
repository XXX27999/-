# FARFilter

A struct to serve as a filter for Asset Registry queries. Each component element is processed as an 'OR' operation while all the components are processed together as an 'AND' operation.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| PackageNames | `TArray < FName >` | The filter component for package names |
| PackagePaths | `TArray < FName >` | The filter component for package paths |
| ObjectPaths | `TArray < FName >` | The filter component containing specific object paths |
| FolderPaths | `TArray < FName >` | The filter component containing specific object paths |
| ClassNames | `TArray < FName >` | The filter component for class names. Instances of the specified classes, but not subclasses (by default), will be included. Derived classes will be included only if bRecursiveClasses is true. |
| RecursiveClassesExclusionSet | `TSet < FName >` | Only if bRecursiveClasses is true, the results will exclude classes (and subclasses) in this list |
| bRecursivePaths | `bool` | If true, PackagePath components will be recursive |
| bRecursiveClasses | `bool` | If true, subclasses of ClassNames will also be included and RecursiveClassesExclusionSet will be excluded. |
| bIncludeOnlyOnDiskAssets | `bool` | If true, only on-disk assets will be returned. Be warned that this is rarely what you want and should only be used for performance reasons |
