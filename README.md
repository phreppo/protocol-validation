# Protocol Validation

Formal specfication in the mCRL2 language of one hospital mechanic bed. Many _liveness_  and _safety_ properties are checked on the system. They can be found in the [properties](https://github.com/parof/protocol-validation/tree/master/specification/properties) directory. The system is also _deadlock free_.

## Compiling

To compile the project the [mCRL2](https://www.mcrl2.org/web/user_manual/index.html) toolkit is needed.

```
make        # run specs
make run    # run symulation
```