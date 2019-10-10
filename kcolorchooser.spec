#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcolorchooser
Version  : 19.08.2
Release  : 13
URL      : https://download.kde.org/stable/applications/19.08.2/src/kcolorchooser-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/kcolorchooser-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/kcolorchooser-19.08.2.tar.xz.sig
Summary  : Color Chooser
Group    : Development/Tools
License  : MIT
Requires: kcolorchooser-bin = %{version}-%{release}
Requires: kcolorchooser-data = %{version}-%{release}
Requires: kcolorchooser-license = %{version}-%{release}
Requires: kcolorchooser-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

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
%setup -q -n kcolorchooser-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570739365
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570739365
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcolorchooser
cp COPYING %{buildroot}/usr/share/package-licenses/kcolorchooser/COPYING
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
/usr/share/package-licenses/kcolorchooser/COPYING

%files locales -f kcolorchooser.lang
%defattr(-,root,root,-)

