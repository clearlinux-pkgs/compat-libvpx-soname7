#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-libvpx-soname7
Version  : 1.12.0
Release  : 38
URL      : https://github.com/webmproject/libvpx/archive/v1.12.0/libvpx-1.12.0.tar.gz
Source0  : https://github.com/webmproject/libvpx/archive/v1.12.0/libvpx-1.12.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause HPND
Requires: compat-libvpx-soname7-lib = %{version}-%{release}
Requires: compat-libvpx-soname7-license = %{version}-%{release}
BuildRequires : nasm
BuildRequires : yasm
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: build.patch

%description
v1.12.0 Torrent Duck
Welcome to the WebM VP8/VP9 Codec SDK!
COMPILING THE APPLICATIONS/LIBRARIES:
The build system used is similar to autotools. Building generally consists of
"configuring" with your desired build options, then using GNU make to build
the application.

%package lib
Summary: lib components for the compat-libvpx-soname7 package.
Group: Libraries
Requires: compat-libvpx-soname7-license = %{version}-%{release}

%description lib
lib components for the compat-libvpx-soname7 package.


%package license
Summary: license components for the compat-libvpx-soname7 package.
Group: Default

%description license
license components for the compat-libvpx-soname7 package.


%prep
%setup -q -n libvpx-1.12.0
cd %{_builddir}/libvpx-1.12.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676068593
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static || : ; CC=gcc CXX=g++ AR=ar STRIP=strip NM=nm ./configure --prefix=/usr --libdir=/usr/lib64 --target=x86_64-linux-gnu --disable-static --enable-libs --enable-vp8 --enable-vp9 --enable-runtime-cpu-detect --enable-shared --enable-webm-io --enable-experimental
make  %{?_smp_mflags}  V=1 AS_FLAGS="-a AMD64"

%install
export SOURCE_DATE_EPOCH=1676068593
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-libvpx-soname7
cp %{_builddir}/libvpx-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/compat-libvpx-soname7/4dbe7c1f3a1833a88333a7c282119323e9ef44fa || :
cp %{_builddir}/libvpx-%{version}/third_party/googletest/src/LICENSE %{buildroot}/usr/share/package-licenses/compat-libvpx-soname7/5a2314153eadadc69258a9429104cd11804ea304 || :
cp %{_builddir}/libvpx-%{version}/third_party/libwebm/LICENSE.TXT %{buildroot}/usr/share/package-licenses/compat-libvpx-soname7/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9 || :
cp %{_builddir}/libvpx-%{version}/third_party/libyuv/LICENSE %{buildroot}/usr/share/package-licenses/compat-libvpx-soname7/f71908f9aaa4aee0f15f9983b6cf83791d18cfd7 || :
cp %{_builddir}/libvpx-%{version}/third_party/x86inc/LICENSE %{buildroot}/usr/share/package-licenses/compat-libvpx-soname7/697c7d5a9839cf4160acd85431b0c58be874dba8 || :
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/vpxdec
rm -f %{buildroot}*/usr/bin/vpxenc
rm -f %{buildroot}*/usr/include/vpx/vp8.h
rm -f %{buildroot}*/usr/include/vpx/vp8cx.h
rm -f %{buildroot}*/usr/include/vpx/vp8dx.h
rm -f %{buildroot}*/usr/include/vpx/vpx_codec.h
rm -f %{buildroot}*/usr/include/vpx/vpx_decoder.h
rm -f %{buildroot}*/usr/include/vpx/vpx_encoder.h
rm -f %{buildroot}*/usr/include/vpx/vpx_ext_ratectrl.h
rm -f %{buildroot}*/usr/include/vpx/vpx_frame_buffer.h
rm -f %{buildroot}*/usr/include/vpx/vpx_image.h
rm -f %{buildroot}*/usr/include/vpx/vpx_integer.h
rm -f %{buildroot}*/usr/lib64/libvpx.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/vpx.pc

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvpx.so.7
/usr/lib64/libvpx.so.7.1
/usr/lib64/libvpx.so.7.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-libvpx-soname7/4dbe7c1f3a1833a88333a7c282119323e9ef44fa
/usr/share/package-licenses/compat-libvpx-soname7/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9
/usr/share/package-licenses/compat-libvpx-soname7/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/compat-libvpx-soname7/697c7d5a9839cf4160acd85431b0c58be874dba8
/usr/share/package-licenses/compat-libvpx-soname7/f71908f9aaa4aee0f15f9983b6cf83791d18cfd7
