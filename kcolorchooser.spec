#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcolorchooser
Version  : 22.12.3
Release  : 50
URL      : https://download.kde.org/stable/release-service/22.12.3/src/kcolorchooser-22.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.3/src/kcolorchooser-22.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.3/src/kcolorchooser-22.12.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: kcolorchooser-bin = %{version}-%{release}
Requires: kcolorchooser-data = %{version}-%{release}
Requires: kcolorchooser-license = %{version}-%{release}
Requires: kcolorchooser-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the kcolorchooser package.
Group: Binaries
Requires: kcolorchooser-data = %{version}-%{release}
Requires: kcolorchooser-license = %{version}-%{release}

%description bin
bin components for the kcolorchooser package.


%package data
Summary: data components for the kcolorchooser package.
Group: Data

%description data
data components for the kcolorchooser package.


%package license
Summary: license components for the kcolorchooser package.
Group: Default

%description license
license components for the kcolorchooser package.


%package locales
Summary: locales components for the kcolorchooser package.
Group: Default

%description locales
locales components for the kcolorchooser package.


%prep
%setup -q -n kcolorchooser-22.12.3
cd %{_builddir}/kcolorchooser-22.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677793620
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1677793620
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcolorchooser
cp %{_builddir}/kcolorchooser-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kcolorchooser/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kcolorchooser-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kcolorchooser/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
pushd clr-build
%make_install
popd
%find_lang kcolorchooser

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kcolorchooser

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kcolorchooser.desktop
/usr/share/icons/hicolor/16x16/apps/kcolorchooser.png
/usr/share/icons/hicolor/22x22/apps/kcolorchooser.png
/usr/share/metainfo/org.kde.kcolorchooser.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcolorchooser/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/kcolorchooser/29fb05b49e12a380545499938c4879440bd8851e

%files locales -f kcolorchooser.lang
%defattr(-,root,root,-)

