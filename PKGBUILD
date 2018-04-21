# Script generated with Bloom
pkgdesc="ROS - The ros_type_introspection package allows the user to parse and deserialize ROS messages which type is unknown at compilation time."
url='http://www.ros.org/wiki/ros_type_introspection'

pkgname='ros-lunar-ros-type-introspection'
pkgver='1.0.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gtest'
'ros-lunar-abseil-cpp'
'ros-lunar-catkin'
'ros-lunar-geometry-msgs'
'ros-lunar-rosbag'
'ros-lunar-rosbag-storage'
'ros-lunar-roscpp'
'ros-lunar-roscpp-serialization'
'ros-lunar-rostime'
'ros-lunar-sensor-msgs'
'ros-lunar-tf2'
'ros-lunar-topic-tools'
)

depends=('ros-lunar-abseil-cpp'
'ros-lunar-geometry-msgs'
'ros-lunar-rosbag'
'ros-lunar-rosbag-storage'
'ros-lunar-roscpp'
'ros-lunar-roscpp-serialization'
'ros-lunar-rostime'
'ros-lunar-sensor-msgs'
'ros-lunar-topic-tools'
)

conflicts=()
replaces=()

_dir=ros_type_introspection
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros_type_introspection $srcdir/ros_type_introspection
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

