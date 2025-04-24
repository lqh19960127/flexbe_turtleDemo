execute_process(COMMAND "/home/linuxlqh/fb_test_2/build/demo2_test_behaviors/demo2_test_flexbe_behaviors/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/linuxlqh/fb_test_2/build/demo2_test_behaviors/demo2_test_flexbe_behaviors/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
