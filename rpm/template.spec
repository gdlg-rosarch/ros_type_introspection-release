Name:           ros-lunar-ros-type-introspection
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS ros_type_introspection package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_type_introspection
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-abseil-cpp
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-rosbag
Requires:       ros-lunar-rosbag-storage
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-roscpp-serialization
Requires:       ros-lunar-rostime
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-topic-tools
BuildRequires:  gtest-devel
BuildRequires:  ros-lunar-abseil-cpp
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-rosbag
BuildRequires:  ros-lunar-rosbag-storage
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-roscpp-serialization
BuildRequires:  ros-lunar-rostime
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-tf2
BuildRequires:  ros-lunar-topic-tools

%description
The ros_type_introspection package allows the user to parse and deserialize ROS
messages which type is unknown at compilation time.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Oct 12 2017 Davide Faconti <faconti@icarustechnology.com> - 1.0.0-0
- Autogenerated by Bloom

* Wed Aug 30 2017 Davide Faconti <faconti@icarustechnology.com> - 0.9.0-0
- Autogenerated by Bloom

* Tue Aug 29 2017 Davide Faconti <faconti@icarustechnology.com> - 0.7.1-0
- Autogenerated by Bloom

* Mon Jun 26 2017 Davide Faconti <faconti@icarustechnology.com> - 0.6.3-0
- Autogenerated by Bloom

* Fri Jun 23 2017 Davide Faconti <faconti@icarustechnology.com> - 0.6.2-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Davide Faconti <faconti@icarustechnology.com> - 0.6.0-0
- Autogenerated by Bloom

