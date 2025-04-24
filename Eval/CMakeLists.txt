find_package(REQUIRED)
set(CMAKE_CXX_FLAGS "-march=native -O3")
add_executable(microtest microtest.cpp)
target_link_libraries(microtest Ppsat pthread emp-tool gmp ssl crypto)
