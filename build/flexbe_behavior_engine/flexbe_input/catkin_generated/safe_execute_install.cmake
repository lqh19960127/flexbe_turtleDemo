execute_process(COMMAND "/home/linuxlqh/fb_test_2/build/flexbe_behavior_engine/flexbe_input/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/linuxlqh/fb_test_2/build/flexbe_behavior_engine/flexbe_input/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
