# TagLogFormatPrint

输出格式化的日志（注意：format 使用 <Tag/> XML占位符格式，不是 %s/%d）

有三种使用方式：
  格式1（纯字符串，无额外参数）：TagLogFormatPrint(log)
    示例：TagLogFormatPrint("something happened")

  格式2（带Tag占位符的格式化字符串 + 参数，使用默认Category "LogTagLog"、默认Verbosity Log）：
    TagLogFormatPrint(format, ...)
    示例：TagLogFormatPrint("player=<Any/> score=<Any/>", playerName, score)

  格式3（指定已注册的LogCategory + ELogVerbosity + 带Tag占位符的格式化字符串 + 参数）：
    TagLogFormatPrint(category, verbosity, format, ...)
    示例：TagLogFormatPrint("LogPESkill", ELogVerbosity.Log, "<Character/>: damage=<Any/>", character, damage)

占位符类型：<Any/> <Character/> <Buff/> 等，按顺序对应后续参数
注意：format 中必须包含 <XXX/> 占位符才能传递额外参数，否则会被拒绝输出！
      错误用法：TagLogFormatPrint("type=%s", val)  -- 不支持 %s 格式！

生效范围：服务器&客户端

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| ... | `any` | 输入参数 格式1 string log；格式2 string format, vararg params；格式3 string category, ELogVerbosity verbosity, string format, vararg params |

## Return

_None_
