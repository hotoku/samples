cc_library(
    name = "greet",
    srcs = ["greet.cpp"],
    hdrs = ["greet.hpp"]
)
cc_binary(
    name = "hello",
    srcs = [
        "main.cpp"
    ],
    deps = [
        ":greet"
    ]
)
