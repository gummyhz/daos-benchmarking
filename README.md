# daos-benchmarking
Notes doc: https://docs.google.com/document/d/1mf2JfuIG7SXV3KOU3kDi35w4nssFurwodq81qu-ZrRA/edit?usp=sharing 
- installation details, test completion status, testing plans, and general notes are in this document

## fio
`fio_scripts`: scripts used to run subsets of fio test cases (split into different scripts to minimize errors/time editing code when running) \
`fio_results`: results from fio test cases, formatted as: `fio_[I/O Pattern]_[Block Size]_[Number of Jobs]_[IO Depth]`
- `fio_results_st` and `fio_results_st-buf` repeat tests already run, with and without a buffer (-buf / not), but requesting fio report read and write latency separately instead of as a pre-calculated 'mixed' value

## io500
`io500_scripts`: the script used to run io500 \
`io500_results`: the results from io500 runs on 1, 2, 4, 8, and 16 nodes, formatted as: `io500_[API Used]_[Number of Nodes]-n_[Job ID]`

## ior
`ior_scripts`: the scripts used to run non-io500 ior tests \
`ior_results`: the our non-io500 ior tests

## mdtest
`mdtest_scripts`: the scripts used to run non-io500 mdtest tests \
`mdtest_results`: the our non-io500 mdtest tests
  - branch tests complete, depth tests with unique `-u` setting complete except for depth 8, non-unique depths running
