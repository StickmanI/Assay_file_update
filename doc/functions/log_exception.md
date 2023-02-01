# General
- executes operation with arguments and sends error messages to log


# Arguments
- log: `Log`
  - receives log messages from operation
- operation: `Callable`
  - operation to be performed
  - raised errors will be send to log
- args: `Any`
  - arguments passed to operation



# Return
- returns `None`
