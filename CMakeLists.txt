cmake_minimum_required(VERSION 3.10)

# set the project name
project(MarsLander CXX)

# add the executable
add_executable(spring spring.cpp)
add_executable(simulation lander_graphics.cpp lander.h lander.cpp)

# add dependencies
find_package(OpenGL REQUIRED)
find_package(GLUT REQUIRED)
include_directories( ${OPENGL_INCLUDE_DIRS}  ${GLUT_INCLUDE_DIRS} )

target_link_libraries(simulation ${OPENGL_LIBRARIES} ${GLUT_LIBRARY} ${lander})